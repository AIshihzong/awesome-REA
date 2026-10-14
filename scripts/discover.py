"""Find recently created GitHub repos that mention REA and aren't listed yet.

Writes a Markdown candidate list to the path given as the first argument.
Only uses the standard library. Set GITHUB_TOKEN to raise the rate limit.
Candidates are never added to the README; a maintainer reviews them.
"""

import datetime
import json
import os
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
LISTED_FILES = ["README.md", "README.zh-CN.md", "docs"]

QUERIES = [
    '"reverse engineer anything" in:readme,description',
    'morluto/rea in:readme',
    'topic:reverse-engineer-anything',
    '"REA" "reverse engineering" MCP in:readme',
]

LOOKBACK_DAYS = 14
PER_PAGE = 30


def listed_repos() -> set[str]:
    """Collect every owner/repo link already present in the docs (lowercased)."""
    text = ""
    for name in LISTED_FILES:
        path = ROOT / name
        files = path.rglob("*.md") if path.is_dir() else [path]
        for f in files:
            text += f.read_text(encoding="utf-8").lower()
    return set(re.findall(r"github\.com/([\w.-]+/[\w.-]+)", text))


def search(query: str, since: str) -> list[dict]:
    q = f"{query} created:>={since}"
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(
        {"q": q, "sort": "updated", "order": "desc", "per_page": PER_PAGE}
    )
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-rea-discover"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp).get("items", [])


def main() -> int:
    out_path = pathlib.Path(sys.argv[1])
    since = (datetime.date.today() - datetime.timedelta(days=LOOKBACK_DAYS)).isoformat()
    known = listed_repos()

    seen: dict[str, dict] = {}
    failures = []
    for query in QUERIES:
        try:
            items = search(query, since)
        except Exception as exc:  # network or rate limit: report and keep going
            failures.append(f"{query}: {exc}")
            continue
        for item in items:
            name = item["full_name"].lower()
            if name in known or name in seen:
                continue
            seen[name] = item

    lines = [
        f"# Daily discovery: {datetime.date.today().isoformat()}",
        "",
        f"New repos created since {since} that mention REA and are not listed yet. "
        "Each one needs a check (see [Did it really use REA?](docs/is-it-rea.md)) before it goes in the list.",
        "",
    ]
    if seen:
        lines += ["| Repo | Created | Stars | Description |", "|---|---|---|---|"]
        for item in sorted(seen.values(), key=lambda i: i["created_at"], reverse=True):
            desc = (item.get("description") or "").replace("|", "\\|").replace("\n", " ")
            lines.append(
                f"| [{item['full_name']}]({item['html_url']}) | {item['created_at'][:10]} "
                f"| {item['stargazers_count']} | {desc} |"
            )
    else:
        lines.append("No new candidates today.")
    if failures:
        lines += ["", "Searches that failed:"] + [f"- {f}" for f in failures]

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(seen)} candidates, {len(failures)} failed searches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
