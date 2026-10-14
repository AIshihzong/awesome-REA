# Awesome REA [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**English** | [简体中文](README_zh.md)

> **Take any software apart, understand it, and rebuild it with AI agents.** A curated list of open-source projects, real cases, tools, tutorials and discussions on AI-driven reverse engineering and rebuilding. Every entry is checked against its source by hand.

**What is REA?** "REA (Reverse Engineer Anything)" started as the name of the open-source tool [morluto/rea](https://github.com/morluto/rea). After it hit #1 on GitHub Trending in October 2026 and passed 100k stars within days, the name came to stand for a whole way of working: **no source code, yet an AI agent works out how a piece of software works, and you rebuild it with your own code.** This list uses that broader meaning, and tags each entry by how it relates to the REA tool:

| Tag | Meaning |
|:---:|---|
| 🔧 | The project README or the author's post says it used [morluto/rea](https://github.com/morluto/rea) |
| 🤖 | Reverse engineered with AI help, but REA is not mentioned |
| 🧪 | AI-assisted clean-room reimplementation, based mainly on public information and observed behavior rather than binary analysis |

> ⚠️ Reverse engineering is governed by local law, software licenses and terms of service. This list only collects public information for learning, research, interoperability and software preservation. Make sure you are allowed to analyze the target software before you start. See [Legal and controversy](#legal-and-controversy).

## Start here

- 🔧 [DX-Ball: 63 bytes, byte-for-byte identical](https://rea.tools/showcase/dx-ball/) - Traced one sound call to the stereo-pan function of a 1996 game. The rebuilt C passes 3,205 test cases against the original x86 code and compiles to exactly the same bytes.
- 🔧 [One person and an agent rebuild the Touhou Project games](https://rea.tools/blog/touhou-reconstruction) - [N0zoM1z0](https://github.com/N0zoM1z0?tab=repositories) reconstructed th04, th08, th10 and more, and compiled th08 to WebAssembly so it [runs in the browser](https://github.com/N0zoM1z0/th08-web).
- 🧪 [storytold/photocraft](https://github.com/storytold/photocraft) - A Photoshop-style image editor rewritten in pure Rust that passed 50k stars in one to two weeks. The same family covers Word, Excel and Illustrator-style apps.
- 🔧 [Baoyu: reverse engineering the Claude Slides editor](https://x.com/dotey/status/2109151666020794711) - 🇨🇳 Recovered an almost complete slide editor from minified web scripts, then had Claude Code rewrite it into a clean codebase. Step-by-step notes included.
- 🔧 [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) - Tears down Wispr Flow's dictation pipeline, labels every finding as confirmed, inferred or unknown, then rebuilds a minimal local version in 64 lines.
- 🔧 [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) - A C++20 clean-room reimplementation of the Battlefield 2 engine, shipped with its REA investigation tooling.
- 🤖 [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) - The author says it took about 45 minutes to reverse engineer the first-gen Apple TV remote and make it work on Linux over Bluetooth.

## Find by software

Looking for an open-source rebuild or reconstruction of a specific program? Start with this table. Star counts are live from shields.io.

| Software rebuilt or reconstructed | Open-source project | Tag | Stars |
|---|---|:---:|---|
| Photoshop | [storytold/photocraft](https://github.com/storytold/photocraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/photocraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/photocraft) |
| Microsoft Word | [storytold/wordcraft](https://github.com/storytold/wordcraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/wordcraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/wordcraft) |
| Excel | [storytold/gridcraft](https://github.com/storytold/gridcraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/gridcraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/gridcraft) |
| Illustrator | [storytold/vectorcraft](https://github.com/storytold/vectorcraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/vectorcraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/vectorcraft) |
| Roblox engine | [AsyncFinn/rook](https://github.com/AsyncFinn/rook) | 🧪 | [![](https://img.shields.io/github/stars/AsyncFinn/rook?style=flat-square&label=%E2%98%85)](https://github.com/AsyncFinn/rook) |
| Heroes of Might and Magic IV engine | [tallowmere/free-heroes4](https://github.com/tallowmere/free-heroes4) | 🧪 | [![](https://img.shields.io/github/stars/tallowmere/free-heroes4?style=flat-square&label=%E2%98%85)](https://github.com/tallowmere/free-heroes4) |
| Battlefield 2 (Refractor 2 engine) | [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) | 🔧 | [![](https://img.shields.io/github/stars/Moxnatiy/OpenBattlefield2?style=flat-square&label=%E2%98%85)](https://github.com/Moxnatiy/OpenBattlefield2) |
| GunZ: The Duel | [OpenRsG/GunZRs](https://github.com/OpenRsG/GunZRs) | 🔧 | [![](https://img.shields.io/github/stars/OpenRsG/GunZRs?style=flat-square&label=%E2%98%85)](https://github.com/OpenRsG/GunZRs) |
| DX-Ball 1.07 | [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) | 🔧 | [![](https://img.shields.io/github/stars/N0zoM1z0/dx-ball?style=flat-square&label=%E2%98%85)](https://github.com/N0zoM1z0/dx-ball) |
| Touhou Project (PC-98 / Windows games) | [N0zoM1z0/th04](https://github.com/N0zoM1z0/th04) | 🔧 | [![](https://img.shields.io/github/stars/N0zoM1z0/th04?style=flat-square&label=%E2%98%85)](https://github.com/N0zoM1z0/th04) |
| Ski or Die (snowball fight) | [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | 🔧 | [![](https://img.shields.io/github/stars/tuunanet/rea-ski-or-die-reconstruction?style=flat-square&label=%E2%98%85)](https://github.com/tuunanet/rea-ski-or-die-reconstruction) |
| Gemtree Desktop Games | [ucodia/desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia) | 🔧 | [![](https://img.shields.io/github/stars/ucodia/desktop-games-nostalgia?style=flat-square&label=%E2%98%85)](https://github.com/ucodia/desktop-games-nostalgia) |
| Paper (infinite-canvas design) | [michaelshimeles/paper-rs](https://github.com/michaelshimeles/paper-rs) | 🔧 | [![](https://img.shields.io/github/stars/michaelshimeles/paper-rs?style=flat-square&label=%E2%98%85)](https://github.com/michaelshimeles/paper-rs) |
| OBS Studio (screen recording) | [michaelshimeles/rec-rs](https://github.com/michaelshimeles/rec-rs) | 🔧 | [![](https://img.shields.io/github/stars/michaelshimeles/rec-rs?style=flat-square&label=%E2%98%85)](https://github.com/michaelshimeles/rec-rs) |
| TradingView chart interactions | [michaelshimeles/terminal-rs](https://github.com/michaelshimeles/terminal-rs) | 🔧 | [![](https://img.shields.io/github/stars/michaelshimeles/terminal-rs?style=flat-square&label=%E2%98%85)](https://github.com/michaelshimeles/terminal-rs) |
| Wispr Flow (dictation) | [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) | 🔧 | [![](https://img.shields.io/github/stars/az9713/wispr-flow-rea-teardown?style=flat-square&label=%E2%98%85)](https://github.com/az9713/wispr-flow-rea-teardown) |
| PowerToys Color Picker | [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab) | 🔧 | [![](https://img.shields.io/github/stars/iammukeshm/hexgrab?style=flat-square&label=%E2%98%85)](https://github.com/iammukeshm/hexgrab) |
| Logitech G HUB | [Slyvan25/OpenGHub](https://github.com/Slyvan25/OpenGHub) | 🔧 | [![](https://img.shields.io/github/stars/Slyvan25/OpenGHub?style=flat-square&label=%E2%98%85)](https://github.com/Slyvan25/OpenGHub) |
| PreSonus AudioBox VSL driver | [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP) | 🔧 | [![](https://img.shields.io/github/stars/grisuno/VSL-DSP?style=flat-square&label=%E2%98%85)](https://github.com/grisuno/VSL-DSP) |
| First-gen Apple TV Siri Remote | [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) | 🤖 | [![](https://img.shields.io/github/stars/a-funk/open-appleremote?style=flat-square&label=%E2%98%85)](https://github.com/a-funk/open-appleremote) |

## Contents

- [Start here](#start-here)
- [Find by software](#find-by-software)
- [Official resources](#official-resources)
- [Official showcases](#official-showcases)
- [🔧 Community cases: REA use stated](#-community-cases-rea-use-stated)
  - [Classic game reconstruction](#classic-game-reconstruction)
  - [Desktop apps and tools](#desktop-apps-and-tools)
  - [Hardware, protocols and drivers](#hardware-protocols-and-drivers)
  - [Security analysis and evaluation](#security-analysis-and-evaluation)
- [🧪🤖 AI rebuilds and reverse engineering: REA not stated](#-ai-rebuilds-and-reverse-engineering-rea-not-stated)
- [Plugins and integrations](#plugins-and-integrations)
- [Tutorials and deep dives](#tutorials-and-deep-dives)
- [Related MCP reverse-engineering tools](#related-mcp-reverse-engineering-tools)
- [Other REA lists and aggregators](#other-rea-lists-and-aggregators)
- [Notable posts on X (Twitter)](#notable-posts-on-x-twitter)
- [Community discussions](#community-discussions)
- [Press coverage](#press-coverage)
- [Legal and controversy](#legal-and-controversy)
- [Contributing](#contributing)

## Official resources

- [morluto/rea](https://github.com/morluto/rea) - The main REA repository. One MCP server for reverse engineering across binaries, applications and runtime behavior; `npx rea-agents setup` connects it to your agent.
- [rea.tools](https://rea.tools/) - Official site with [guides](https://rea.tools/guides/), [showcases](https://rea.tools/showcase/) and a blog.
- [rea-agents (npm)](https://www.npmjs.com/package/rea-agents) - The published CLI and MCP server package.
- [REA Skill on skills.sh](https://skills.sh/morluto/rea/reverse-engineer-anything) - An agent skill that installs only the investigation workflow instructions.
- [MCP tool catalog](https://github.com/morluto/rea/blob/main/docs/mcp-contracts.md#generated-catalog) - Auto-generated list of every tool, provider and CLI command.
- [morluto/awesome-reverse-engineering](https://github.com/morluto/awesome-reverse-engineering) - The REA author's general list of reverse-engineering tools and learning resources.
- [Discord](https://discord.gg/GkcryMnJDM) - Official Q&A and Show and Tell.

## Official showcases

- [DX-Ball: recovering the stereo-pan function](https://rea.tools/showcase/dx-ball/) - Follows one sound call to the helper that turns position into stereo pan and completes the partial pseudocode as C. The rebuilt code passes 3,205 original-x86 test cases and its 63 compiled bytes match exactly. [Reconstruction repo](https://github.com/N0zoM1z0/dx-ball)
- [Notion: tracing the Electron clipboard bridge](https://rea.tools/showcase/notion/) - Traces the renderer clipboard API through preload and IPC to the main process and decodes the rich-text clipboard format.
- [TH04: recovering a DOS bullet-ring calculation](https://rea.tools/showcase/th04/) - Analyzes 16-bit code from the PC-98 game Touhou Gensokyo, recovers the fixed-angle and aimed-angle math, and compares it with period compiler output. [Reconstruction repo](https://github.com/N0zoM1z0/th04)
- [Aegis: how an authenticator generates login codes](https://rea.tools/showcase/aegis/) - Traces TOTP code generation inside an Android app.
- [CTF: solving a flag checker](https://rea.tools/showcase/ctf/) - Uses REA on a DownUnderCTF reversing challenge.
- [Blog: The industrial revolution of reverse engineering](https://rea.tools/blog/touhou-reconstruction) - Official write-up of reconstructing Touhou Project games at scale with agents.
- [Blog: Does reverse engineering need bigger models?](https://rea.tools/blog/reverse-engineering-models) - How different models perform on reverse-engineering tasks.

## 🔧 Community cases: REA use stated

Every project below says in its README that it used REA.

### Classic game reconstruction

- [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) - Reconstruction of the 1996 Windows 95 game DX-Ball 1.07 with differential tests against the original x86 and byte-level comparison under a pinned MSVC version. The full repo behind the official showcase.
- [N0zoM1z0/th04](https://github.com/N0zoM1z0/th04) - Source reconstruction of the PC-98 Touhou Gensokyo, binary-matched with the Borland compiler.
- [N0zoM1z0's Touhou Project series](https://github.com/N0zoM1z0?tab=repositories) - The same author's agent-driven reconstructions of [th08](https://github.com/N0zoM1z0/th08), [th105](https://github.com/N0zoM1z0/th105), [th095](https://github.com/N0zoM1z0/th095), [th09](https://github.com/N0zoM1z0/th09) and [th10](https://github.com/N0zoM1z0/th10), plus [th08-web](https://github.com/N0zoM1z0/th08-web) (C++ compiled to WebAssembly) and [touhou-reconstruction-factory](https://github.com/N0zoM1z0/touhou-reconstruction-factory), which manages the reconstruction projects.
- [ucodia/desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia) - Ports Gemtree's 2000 Desktop Games (Stress Reducers) to macOS and the browser. Claude Code + REA + Ghidra decompiled the interpreter and recovered the image compression, asset record format, 55 ms timer and coordinate system.
- [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) - A from-scratch Rust + SDL2 rewrite of the snowball-fight minigame from the 1990 MS-DOS game Ski or Die.
- [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) - C++20 clean-room reimplementation of Battlefield 2's Refractor 2 engine with REA investigation tooling. Requires the original game.
- [OpenRsG/GunZRs](https://github.com/OpenRsG/GunZRs) - A Rust + Bevy rewrite of GunZ: The Duel that reads the original assets from a Steam install, with its own REA investigation harness.

### Desktop apps and tools

- [michaelshimeles/paper-rs](https://github.com/michaelshimeles/paper-rs) - A native infinite-canvas design app rewritten clean-room in Rust (egui/wgpu) after studying Paper with REA and Claude Code.
- [michaelshimeles/rec-rs](https://github.com/michaelshimeles/rec-rs) - A Rust macOS screen and camera recorder written clean-room after reverse-engineering analysis of OBS Studio.
- [michaelshimeles/terminal-rs](https://github.com/michaelshimeles/terminal-rs) - A Bloomberg-style trading terminal in Rust whose GPU chart interactions draw on notes from analyzing TradingView with REA's website mode.
- [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) - A static REA teardown of Wispr Flow's audio capture, transcription and paste flow. Each finding is labeled confirmed, inferred or unknown, and a minimal local version is rebuilt in 64 lines.
- [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab) - A .NET 10 tool written after studying the MIT-licensed PowerToys Color Picker with REA.
- [GitHub discussion: from REA to a QuickBooks-style desktop app](https://github.com/morluto/rea/discussions/2198) - A community member documents building a Mac + Windows accounting app with REA.

### Hardware, protocols and drivers

- [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP) - Linux kernel module for PreSonus AudioBox VSL USB audio interfaces; the DSP protocol analysis was done with REA through the LazyOwn framework.
- [Slyvan25/OpenGHub](https://github.com/Slyvan25/OpenGHub) - A Linux-native open-source alternative to Logitech G HUB built on HID++ protocol research, with support for mice and wheel force feedback.

### Security analysis and evaluation

- [NullLabTests/OpenBSD_netcat_REA](https://github.com/NullLabTests/OpenBSD_netcat_REA) - Full static analysis of the netcat-openbsd 1.234-1 binary with REA + Ghidra, including flowcharts and method notes.
- [az9713/REA-demo](https://github.com/az9713/REA-demo) - "REA analyzes REA": runs REA on its own package, makes falsifiable predictions, then grades them against the source and records what went wrong.
- [GitHub discussion: checking a production Next.js + Stripe app for leaks from the outside](https://github.com/morluto/rea/discussions/1406) - Uses website mode to audit the author's own live app.
- [GitHub discussion: stripped bzip2](https://github.com/morluto/rea/discussions/2254) - Compares REA's output line by line with build artifacts and official documentation.

## 🧪🤖 AI rebuilds and reverse engineering: REA not stated

These projects took off on X and GitHub at the same time as REA and are often discussed alongside it as proof of how complex AI-built software can get, but their READMEs do not say they used REA.

- 🧪 [storytold/photocraft](https://github.com/storytold/photocraft) - The ArtCraft community's pure-Rust clean-room Photoshop-style image editor, with GPU compositing, adjustment layers, curves and more. Passed 50k stars within one to two weeks.
- 🧪 [storytold/wordcraft](https://github.com/storytold/wordcraft) - A Word-style word processor from the same family, with track changes, citations, mail merge and .docx read/write.
- 🧪 [storytold/gridcraft](https://github.com/storytold/gridcraft) - An Excel-style spreadsheet from the same family, with formulas and charts.
- 🧪 [storytold/vectorcraft](https://github.com/storytold/vectorcraft) - An Illustrator-style vector editor from the same family. FilmCraft, LightCraft, PdfCraft, DeckCraft, CADCraft and others are under [storytold](https://github.com/storytold).
- 🧪 [AsyncFinn/rook](https://github.com/AsyncFinn/rook) - A Rust reimplementation of the Roblox engine, conformance-tested against Roblox Studio recordings.
- 🧪 [tallowmere/free-heroes4](https://github.com/tallowmere/free-heroes4) - A C++23 reimplementation of the Heroes of Might and Magic IV engine. Requires the GOG game files; work in progress.
- 🤖 [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) - Makes the first-gen Apple TV Siri Remote work on Linux over Bluetooth: unlocks the remote, decodes touch and button reports and recreates tvOS-style gestures. Pure Python standard library, MIT. The author says the reverse engineering took about 45 minutes.

## Plugins and integrations

- [zhaofeng130/dsh-rea](https://github.com/zhaofeng130/dsh-rea) - DeepSeek Harness adapter that registers the REA skill and `rea` / `rea_doctor` tools in every session.
- [ya123-4/rea-dsh-plugin](https://github.com/ya123-4/rea-dsh-plugin) - DeepSeek Harness plugin that registers the REA MCP as `mcp__rea__*` tools plus the skill in one install.
- [sheilacraig/dsh-rea-mcp](https://github.com/sheilacraig/dsh-rea-mcp) - Config-only DeepSeek Harness bundle that mounts REA through the built-in MCP client.
- [cognixws/picode-rea](https://github.com/cognixws/picode-rea) - PiCode extension that enables only REA's static analysis tools.
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Claude Code mod that records the evidence REA returns in real time, requires conclusions to cite a real `evidence_id`, and exports to Markdown.
- [laaielichter/reverseport](https://github.com/laaielichter/reverseport) - REA-inspired CLI + MCP focused on porting reverse-engineering results to Godot, Unity, Unreal and three.js.
- [rea-agents Homebrew formula](https://github.com/moonfruit/homebrew-tap/blob/main/Formula/rea-agents.rb) - Community-maintained Homebrew install.

## Tutorials and deep dives

- [ringozzt/rea-research](https://github.com/ringozzt/rea-research) - 🇨🇳 In-depth Chinese technical study: architecture, evidence model, what the DX-Ball numbers really mean, trust model, the gap between stars and installs, and the controversy. Recommended first read.
- [valorisa/Reverse-Engineer-Anything](https://github.com/valorisa/Reverse-Engineer-Anything) - 🇫🇷 Unofficial French teaching guide, including the legal framework for reverse engineering.
- [pablodiazjorge/rea-lab](https://github.com/pablodiazjorge/rea-lab) - REA setup, exercises and tool evaluations on Windows + Ghidra.
- [jinshi666888/rea-playbook](https://github.com/jinshi666888/rea-playbook) - Hands-on lab: a minimal Electron target, evidence extraction with `file:line` citations and MCP probes, covering the full decompile → understand → rebuild loop without a native decompiler.
- [REA: Reverse Engineer Anything with AI Agents & MCP (HoangYell)](https://hoangyell.com/rea-explained/) - English introduction.
- [Reverse Engineer Anything: What the Viral REA MCP Actually Does (MindStudio)](https://www.mindstudio.ai/blog/reverse-engineer-anything-mcp) - What REA actually does once you strip away the hype.
- [Agentic Reverse Engineering: What REA Is and How to Start (El Solitario)](https://elsolitario.org/en/2026/10/10/rea-reverse-engineering-for-coding-agents/) - Getting-started tutorial.
- [How To Use REA To Clone Any Software In Minutes (Eric Tech, YouTube)](https://www.youtube.com/watch?v=FnB9tHKBJXQ) - Video tutorial; the Wispr Flow teardown above follows it.

## Related MCP reverse-engineering tools

Tools REA orchestrates, or similar reverse-engineering tools built for agents.

- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) - MCP server that connects IDA Pro to LLMs; REA's IDA support builds on it.
- [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) - MCP server for Ghidra.
- [N0zoM1z0/touhou-reverse-engineering](https://github.com/N0zoM1z0/touhou-reverse-engineering) - Evidence-first IDA + MCP reverse-engineering notes; the groundwork for the Touhou reconstruction series.

## Other REA lists and aggregators

- [sqwu/rea-gems](https://github.com/sqwu/rea-gems) - A daily auto-updated gallery of REA cases pulled from the official showcases, GitHub, HN and Reddit.
- [miles990/rea-awesome](https://github.com/miles990/rea-awesome) - REA cases ranked with a single scoring rubric, updated daily, with JSON / RSS / llms.txt.
- [kaixinbaba/awesome-rea](https://github.com/kaixinbaba/awesome-rea) - Directory of open-source reverse engineering, reimplementations and compatible alternatives ([awesomerea.com](https://awesomerea.com)); REA use not required.
- [zhuyansen/awesome-ai-reverse-engineering](https://github.com/zhuyansen/awesome-ai-reverse-engineering) - AI reverse-engineering tools with a safety rating for each repo, in Chinese and English.
- [DiscoverBox/awesome-ai-reverse](https://github.com/DiscoverBox/awesome-ai-reverse) - 🇨🇳 AI-assisted reverse-engineering tools: MCP servers, skills, plugins and agents for web, binaries, mobile and traffic analysis.

## Notable posts on X (Twitter)

View counts were taken on 2026-10-14 and are for reference only.

### Hands-on cases

- [Baoyu: reverse engineering the Claude Slides editor with REA](https://x.com/dotey/status/2109151666020794711) - 🇨🇳 Downloaded the web scripts and stylesheets, had Codex install the REA skill to recover the minified code, then had Claude Code rewrite it into a clean project. Step-by-step notes included. Code lives in `apps/slides-editor` of [JimLiu/baocut](https://github.com/JimLiu/baocut) (source-available, not an open-source license). About 180k views.
- [A.I.Warper](https://x.com/AIWarper/status/2109060856466264566) - Used REA + Opus 5.5 to decompile a Steam game they had bought into C# and run it in Unity in under 30 minutes. About 467k views, the most widely shared personal test.
- [Vaibhav Sisinty: what people built this week](https://x.com/VaibhavSisinty/status/2109618846453977359) - Roundup thread: the Steam game decompile, the first-gen Apple TV remote, an air conditioner remote, an LG TV Plex client and more. Most of the original posts do not say they used REA; they belong to the wider wave of AI reverse engineering.
- [alex funk: reverse engineering the first-gen Apple TV remote in 45 minutes](https://x.com/alexzfunk/status/2108585025205592408) - "software is kinda solved." Gets the Siri Remote working on Linux over Bluetooth, open-sourced as [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote). Neither the post nor the README mentions REA.
- [Ilter Canberk: reverse engineering a home AC](https://x.com/icanberk/status/2109031477484937571) - Reverse engineered how the AC is controlled, vibe coded a menu bar app, then ported it to smart glasses with Codex. REA not mentioned.
- [Vaibhav Sisinty: a native Plex client for an LG TV](https://x.com/VaibhavSisinty/status/2108103450995417177) - Retells a Reddit case: annoyed by the 30-second Plex launch, the author went from C to Rust with Claude Code, built an OpenGL UI framework, and got launch down to 3 seconds. REA not mentioned.

### Introductions and reach

- [Matthew Berman](https://x.com/MatthewBerman/status/2108245653843509415) - "Reverse Engineer Anything 😂 Software is done." One of the posts that set off the wave.
- [0xMarioNawfal](https://x.com/RoundtableSpace/status/2109165852578992582) - "Closed source is dead," posted during the 25k-stars-in-a-day spike; about 920k views. An earlier [feature overview](https://x.com/RoundtableSpace/status/2107059472753664261) went out on October 5.
- [International Cyber Digest](https://x.com/IntCyberDigest/status/2108699960782774733) - Posted while it was #1 on GitHub Trending: "Software is dead, long live software!"
- [Trending GitHub Repositories](https://x.com/trending_repos/status/2107443007217701076) - Repo of the day, about 3,000 stars in 24 hours.
- [Rohan Paul](https://x.com/rohanpaul_ai/status/2108423886509683053) - Feature overview: one MCP server across binaries, applications and runtime behavior.
- [Tech with Mak](https://x.com/techNmak/status/2108431092462338178) - "Someone gave Claude Code a decompiler," on how REA connects agents to Ghidra, Hopper and similar tools.
- [Hasan Toor](https://x.com/hasantoxr/status/2108524682727305344) - "Hand any app to your AI and have it rebuild the best feature inside it."
- [Larry Cheng](https://x.com/larryvc/status/2109344654198018095) - A one-line take from a VC: look at a finished app and work out how it works without its source.
- [Afiz](https://x.com/itsafiz/status/2107063919290573174) - "See a feature you love in an app? Your agent can reverse engineer it," with emphasis on running 100% locally.
- [Oliver Prompts](https://x.com/oliviscusAI/status/2106955446183411895) - Overview of decompiling, tracing execution and inspecting runtime behavior.
- [K2S](https://x.com/k2sbhai/status/2106796616716062777) - Four steps: install, `rea setup`, connect your agent, give it a feature to investigate.
- [Vaishnavi](https://x.com/_vmlops/status/2106690704244420687) - Early introduction.
- [Dan Kornas](https://x.com/DanKornas/status/2106032461968761052) - An October 2 introduction, one of the earliest before it went viral, listing evidence records, local analysis and other features.
- [CyrilXBT](https://x.com/cyrilXBT/status/2109490499321299364) - "Closed source used to mean protected. Now it just means slower to copy." Typical of the hype.
- [X trending topic page](https://x.com/i/trending/2108302228461080603) - X's own roundup of the REA story.

### Chinese, Japanese and other languages

- [Baoyu: REA lets AI agents reverse engineer software without source](https://x.com/dotey/status/2108794629172682783) - 🇨🇳 The most complete Chinese introduction: setup, what it can analyze, the three official showcases, where data goes, and reminders about compliance and that REA has no token. About 300k views.
- [lifcc](https://x.com/mylifcc/status/2108940999527690525) - 🇨🇳 "An open-source project gained over 20k stars in a day," on letting Claude Code or Codex study binaries and rebuild features.
- [婷](https://x.com/shijianzhongg/status/2107979591348543520) - 🇨🇳 "Today's hottest open-source project on GitHub," listing three uses: finding hidden features, checking for backdoors and learning from big-company code. About 170k views.
- [TechVerser](https://x.com/realfxw/status/2106734209473581308) - 🇨🇳 "AI is rewriting the rules of low-level reverse engineering," on REA packaging the reverse-engineering toolchain as an agent add-on.
- [Takashi Yoshikawa (author of a Japanese malware analysis textbook)](https://x.com/MalwareBibleJP/status/2108736281647931717) - 🇯🇵 A point-by-point summary from a malware-analysis and defender perspective: required tools, static vs. runtime analysis, where data goes, and the compliance statement.
- [midudev](https://x.com/midudev/status/2107834472091598854) - 🇪🇸 "Everyone is reverse engineering programs and games with AI," the most shared post in the Spanish-speaking dev community, about 150k views.
- [bearstech](https://x.com/bearstech/status/2109679666105655457) - 🇫🇷 Short French introduction.

### Official accounts

- [@morluto](https://x.com/morluto) - The REA author. [rea 6.4 release](https://x.com/morluto/status/2109138696008327226): "much, much faster," plus [morluto/flameox](https://github.com/morluto/flameox), the author's profiling tool for agents.
- [@reatools](https://x.com/reatools) - Official account; reposted the author's line "the homebrew computer club era of technology is back."

### Open-source roundup posts from the same week

REA often shows up next to other viral repos in "open-source alternatives to paid software" roundups.

- [brenz.](https://x.com/brenzhills/status/2108983461230845978) - 🇪🇸 "10 repos blowing up this month," with REA at #4 alongside VoiceStudio, ppt-master, gods-eye-view, diagram-design and paperclip.
- [Chris Pirillo](https://x.com/ChrisPirillo/status/2109843806187303400) - October 12 vibe coding and AI news roundup listing REA next to context-mode, diagram-design and others.
- [govin.eth | G哥](https://x.com/goan999999/status/2109544711400857688) - 🇨🇳 "6 open-source gems on GitHub that spell trouble for paid software": PPT Master, VoiceStudio, God's Eye View, Diagram Design, Paperclip and ECC. Does not mention REA, but covers the same batch of projects with the same story.

### Controversy

- [codila](https://x.com/0xCodila/status/2109623431763292649) - "REA is most dangerous thing on the internet right now," promoting it as a way to rebuild paid features for free. A typical example of the controversy (see below).
- [Jaden Williams](https://x.com/JadenJTW/status/2106890896981508329) - Quote-posted an early introduction with just "God help us all."

## Community discussions

- [Hacker News: Reverse engineer anything with agents, from app behavior down to native binaries](https://news.ycombinator.com/item?id=50058850)
- [Hacker News: Show HN: A MCP for Agents to reverse engineer binary code](https://news.ycombinator.com/item?id=48901763)
- [GitHub discussion: reducing token waste in REA workflows](https://github.com/morluto/rea/discussions/1958)
- [GitHub discussion: install notes and pitfalls on Fedora-based Linux](https://github.com/morluto/rea/discussions/1435)
- [GitHub discussion: Linux benchmarks (Node 22/24/26 startup and five local models)](https://github.com/morluto/rea/discussions/1998)

## Press coverage

- [An AI agent that reverse engineers any software just hit number one on GitHub (Startup Fortune)](https://startupfortune.com/an-ai-agent-that-reverse-engineers-any-software-just-hit-number-one-on-github/)
- [REA Tool Connects Claude Code and Cursor to Ghidra and IDA Pro (Cybersecurity News)](https://cybersecuritynews.com/reverse-engineer-anything-tool/)
- [New Open-Source REA Tool Lets AI Agents Reverse Engineer Software Without Source Code (CyberPress)](https://cyberpress.org/new-open-source-rea-tool/)
- [Matthew Berman promotes REA, which lets coding agents inspect apps without source code (RuntimeWire)](https://runtimewire.com/article/matthew-berman-rea-ai-reverse-engineering)
- [REA Reverse Engineering Tool: Can AI Clone Your App's Features? (MayhemCode)](https://www.mayhemcode.com/2026/10/rea-reverse-engineering-tool-can-ai.html)

## Legal and controversy

REA's rise has come with real controversy. Keep these points in mind when using or sharing cases:

- **Does clean room hold?** Critics argue that when the same agent does both the reverse engineering and the rebuild, it does not meet the separation of people that traditional clean-room development requires.
- **Limits of the tool.** The project does not claim to recover original source code or clone whole applications automatically. The DX-Ball 3,205 / 63 figures verify a single function, not a whole program (see the analysis in [rea-research](https://github.com/ringozzt/rea-research)).
- **Privacy and trust model.** Analysis runs locally, but tool results reach the model provider through the agent. The official SECURITY.md is explicit that REA is not a sandbox.
- **Commercial tool licenses.** Commercial tools such as IDA Pro, Hopper and JEB must be licensed legally; REA does not provide any licenses.
- **Official position.** REA is for lawful research, education, interoperability, software preservation, and analysis of software you own or are authorized to examine. See [DISCLAIMER.md](https://github.com/morluto/rea/blob/main/DISCLAIMER.md).

This list does not include projects whose main purpose is bypassing authorization, copying paid features or distributing copyrighted material.

## Contributing

Suggestions for new projects, cases and articles are welcome through issues or pull requests. Inclusion criteria:

1. **Open-source** projects come first; include a link to the source.
2. Tag every entry: 🔧 if REA use is stated, 🤖 if it was reverse engineered with AI help but no tool is named, 🧪 for AI-assisted clean-room reimplementations. If you are not sure, include the source in your PR and the maintainers will decide.
3. One line per entry, in the form `- tag [Name](link) - One sentence on what it does and how it was done.`
4. If the project rebuilds or reconstructs a specific piece of software, also add it to the [Find by software](#find-by-software) table.
5. No mirrors, plain forks, or projects whose main purpose is infringement or bypassing authorization.

The Chinese version is [README_zh.md](README_zh.md). Please update both files when you can; if you only edit one, mention it in the PR.
