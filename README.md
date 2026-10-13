# Awesome REA [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 精选 **REA（Reverse Engineer Anything）** 相关的开源项目、真实案例、插件集成、教程与社区讨论。

**REA 是什么？** 本列表中的 REA 指 [morluto/rea](https://github.com/morluto/rea)：一个 MIT 协议的开源 MCP Server + CLI（npm 包 `rea-agents`），让 Claude Code、Codex、Cursor、Gemini CLI 等编码 Agent 在**没有源代码**的情况下检查原生二进制、JavaScript/Electron 应用、.NET 程序集、Android APK、固件和网站，解释某个功能是怎么实现的、给出证据，再在你自己的项目里重建它。它本身不做反编译，而是把 Hopper / Ghidra / IDA / JADX 等现有工具编排给 Agent 使用，并给每个结论附上 `evidence_id` 与局限说明。

**为什么火？** 2026 年 10 月 7 日 v5.0 发布后，REA 一天内登上 GitHub Trending 第一，几天内 Star 数从几千涨到十几万（截至 2026-10-13 约 18.9 万）。它让人们看到：以前要资深逆向工程师花几周做的事，比如逐字节复原 1990 年代游戏的函数、追踪 Electron 应用的 IPC 链路、复刻一整套桌面软件，现在可以由 AI Agent 完成。

> ⚠️ 逆向工程受各地法律、软件许可协议和服务条款约束。本列表只收录公开信息，仅供学习、研究、互操作和软件保存用途；使用前请确认你有权分析目标软件。详见 [合规与争议](#合规与争议)。

## 目录

- [官方资源](#官方资源)
- [官方案例](#官方案例)
- [社区案例：用 REA 做出来的东西](#社区案例用-rea-做出来的东西)
  - [经典游戏复原](#经典游戏复原)
  - [桌面应用与工具复刻](#桌面应用与工具复刻)
  - [硬件、协议与驱动](#硬件协议与驱动)
  - [安全分析与评测](#安全分析与评测)
- [同一波浪潮：AI 驱动的大型复刻项目](#同一波浪潮ai-驱动的大型复刻项目)
- [插件与集成](#插件与集成)
- [教程与深度调研](#教程与深度调研)
- [相关 MCP 逆向工具](#相关-mcp-逆向工具)
- [其他 REA 列表与聚合站](#其他-rea-列表与聚合站)
- [X（Twitter）热门帖子](#xtwitter热门帖子)
- [社区讨论](#社区讨论)
- [媒体报道](#媒体报道)
- [合规与争议](#合规与争议)
- [贡献](#贡献)

## 官方资源

- [morluto/rea](https://github.com/morluto/rea) - REA 主仓库。一个 MCP 覆盖二进制、应用和运行时行为的逆向，`npx rea-agents setup` 一键接入 Agent。
- [rea.tools](https://rea.tools/) - 官网，含[图文指南](https://rea.tools/guides/)、[案例](https://rea.tools/showcase/)和博客。
- [rea-agents（npm）](https://www.npmjs.com/package/rea-agents) - CLI 与 MCP Server 的发布包。
- [skills.sh 上的 REA Skill](https://skills.sh/morluto/rea/reverse-engineer-anything) - 只安装调查工作流指令的 Agent Skill。
- [REA 中文 README](https://github.com/morluto/rea/blob/main/README_zh.md) - 官方简体中文文档。
- [MCP 工具目录](https://github.com/morluto/rea/blob/main/docs/mcp-contracts.md#generated-catalog) - 自动生成的全部工具、Provider 和 CLI 命令清单。
- [morluto/awesome-reverse-engineering](https://github.com/morluto/awesome-reverse-engineering) - REA 作者维护的通用逆向工程工具与学习资源列表。
- [Discord 社区](https://discord.gg/GkcryMnJDM) - 官方 Q&A 与 Show and Tell。

## 官方案例

- [DX-Ball：复原声像计算函数](https://rea.tools/showcase/dx-ball/) - 从一次声音调用追到位置转声像的辅助函数，把不完整的伪代码补成 C。复原代码通过 3,205 个原版 x86 对照用例，63 字节编译产物逐字节一致。[复原仓库](https://github.com/N0zoM1z0/dx-ball)
- [Notion：追踪 Electron 剪贴板桥](https://rea.tools/showcase/notion/) - 从渲染进程的剪贴板 API 一路追过 preload、IPC 到主进程，解析富文本剪贴板格式。
- [TH04：复原 DOS 弹幕环计算](https://rea.tools/showcase/th04/) - 分析 PC-98 版《东方幻想乡》的 16 位指令，复原固定角度与自机狙角度计算，并与历史编译器输出比对。[复原仓库](https://github.com/N0zoM1z0/th04)
- [Aegis：身份验证器如何生成登录码](https://rea.tools/showcase/aegis/) - 在 Android 应用里追踪 TOTP 验证码的生成路径。
- [CTF：解一道 flag 校验题](https://rea.tools/showcase/ctf/) - 用 REA 解 DownUnderCTF 的逆向题。
- [博客：逆向工程的工业革命](https://rea.tools/blog/touhou-reconstruction) - 官方复盘用 Agent 批量复原东方 Project 游戏源码。
- [博客：逆向工程需要更大的模型吗？](https://rea.tools/blog/reverse-engineering-models) - 不同模型在逆向任务上的表现对比。

## 社区案例：用 REA 做出来的东西

以下项目都在 README 中写明使用了 REA。Star 数会变化，这里不列出。

### 经典游戏复原

- [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) - 用 REA 复原 1996 年 Windows 95 游戏 DX-Ball 1.07，有原版 x86 差分测试和固定 MSVC 版本的字节级比对。官方案例的完整仓库。
- [N0zoM1z0/th04](https://github.com/N0zoM1z0/th04) - 《东方幻想乡》PC-98 版源码复原，Borland 编译器二进制匹配。
- [N0zoM1z0 的东方 Project 复原系列](https://github.com/N0zoM1z0?tab=repositories) - 同一作者用 Agent 工作流复原的 [th08](https://github.com/N0zoM1z0/th08)、[th105](https://github.com/N0zoM1z0/th105)、[th095](https://github.com/N0zoM1z0/th095)、[th09](https://github.com/N0zoM1z0/th09)、[th10](https://github.com/N0zoM1z0/th10)，以及从源码移植到浏览器的 [th08-web](https://github.com/N0zoM1z0/th08-web)（C++ 编译成 WebAssembly）和统一管理复原工程的 [touhou-reconstruction-factory](https://github.com/N0zoM1z0/touhou-reconstruction-factory)。
- [ucodia/desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia) - 把 2000 年的 Gemtree《Desktop Games（Stress Reducers）》移植到 macOS 和浏览器。用 Claude Code + REA + Ghidra 反编译解释器，复原图像压缩编码、素材记录格式、55 ms 定时器和坐标系。
- [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) - 用 Rust + SDL2 从零重写 1990 年 MS-DOS 游戏《Ski or Die》的雪球大战小游戏。
- [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) - C++20 clean-room 重实现《战地 2》的 Refractor 2 引擎，附 REA 调查工具；需要原版游戏。
- [OpenRsG/GunZRs](https://github.com/OpenRsG/GunZRs) - 用 Rust + Bevy 重写《GunZ: The Duel》，直接读取 Steam 安装的原版资源，配有独立的 REA 调查框架。

### 桌面应用与工具复刻

- [michaelshimeles/paper-rs](https://github.com/michaelshimeles/paper-rs) - 用 REA + Claude Code 研究 Paper 后，以 Rust（egui/wgpu）clean-room 重写的原生无限画布设计应用。
- [michaelshimeles/rec-rs](https://github.com/michaelshimeles/rec-rs) - 参考 OBS Studio 逆向分析后 clean-room 重写的 Rust macOS 录屏/摄像头录制工具。
- [michaelshimeles/terminal-rs](https://github.com/michaelshimeles/terminal-rs) - Bloomberg 风格的 Rust 交易终端，GPU 图表交互参考了用 REA 网站模式分析 TradingView 的笔记。
- [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) - 用 REA 静态拆解 Wispr Flow 的语音采集、转写和粘贴流程，每条结论标注已证实、推断或未知，再用 64 行代码在本地重建一个精简版。
- [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab) - 用 REA 研究 MIT 协议的 PowerToys 取色器后写出的 .NET 10 小工具。
- [GitHub 讨论：从 REA 到一个 QuickBooks 风格的桌面应用](https://github.com/morluto/rea/discussions/2198) - 社区成员记录用 REA 做出 Mac + Windows 记账应用的过程。

### 硬件、协议与驱动

- [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP) - PreSonus AudioBox VSL 系列 USB 声卡的 Linux 内核模块，DSP 协议分析借助 LazyOwn 框架调用 REA 完成。
- [Slyvan25/OpenGHub](https://github.com/Slyvan25/OpenGHub) - Linux 原生的开源罗技 G HUB 替代品，基于 HID++ 协议研究，支持鼠标、方向盘力反馈等。

### 安全分析与评测

- [NullLabTests/OpenBSD_netcat_REA](https://github.com/NullLabTests/OpenBSD_netcat_REA) - 用 REA + Ghidra 对 netcat-openbsd 1.234-1 二进制做完整静态分析，有流程图和方法说明。
- [az9713/REA-demo](https://github.com/az9713/REA-demo) - 「REA 分析 REA」：用 REA 分析自己的安装包，先做可证伪的预测再对照源码自评，诚实记录了出错的地方。
- [GitHub 讨论：从外部检查生产环境 Next.js + Stripe 应用的泄露](https://github.com/morluto/rea/discussions/1406) - 用网站模式对自己的线上应用做安全自查。
- [GitHub 讨论：剥离符号的 bzip2](https://github.com/morluto/rea/discussions/2254) - 把 REA 的输出和构建产物、官方文档逐条对照。

## 同一波浪潮：AI 驱动的大型复刻项目

这些项目和 REA 同期在 X 和 GitHub 上走红，都是 AI 辅助的 clean-room 重实现，常被拿来和 REA 一起讨论「AI 能做多复杂的软件工程」。**它们的 README 没有写明使用 REA**，收录在这里作为背景参考。

- [storytold/photocraft](https://github.com/storytold/photocraft) - ArtCraft 社区用纯 Rust clean-room 重写的 Photoshop 式图像编辑器，GPU 合成、调整图层、曲线等，Star 数在一两周内超过 5 万。
- [storytold/wordcraft](https://github.com/storytold/wordcraft) - 同系列的 Word 式文字处理器，支持修订、引用、邮件合并和 .docx 读写。
- [storytold/gridcraft](https://github.com/storytold/gridcraft) - 同系列的 Excel 式电子表格，含公式与图表。
- [storytold/vectorcraft](https://github.com/storytold/vectorcraft) - 同系列的 Illustrator 式矢量绘图工具。同系列还有 FilmCraft、LightCraft、PdfCraft、DeckCraft、CADCraft 等，见 [storytold](https://github.com/storytold)。
- [AsyncFinn/rook](https://github.com/AsyncFinn/rook) - 用 Rust 重实现 Roblox 引擎，以 Roblox Studio 录制结果做一致性测试。
- [tallowmere/free-heroes4](https://github.com/tallowmere/free-heroes4) - C++23 重实现《魔法门之英雄无敌 IV》引擎，需要 GOG 原版文件，尚未完成。

## 插件与集成

- [zhaofeng130/dsh-rea](https://github.com/zhaofeng130/dsh-rea) - DeepSeek Harness 适配器，在每个会话里注册 REA Skill 以及 `rea` / `rea_doctor` 工具。
- [ya123-4/rea-dsh-plugin](https://github.com/ya123-4/rea-dsh-plugin) - DeepSeek Harness 插件，一次安装就能把 REA MCP 注册为 `mcp__rea__*` 工具并附带 Skill。
- [sheilacraig/dsh-rea-mcp](https://github.com/sheilacraig/dsh-rea-mcp) - 纯配置的 DeepSeek Harness bundle，用内置 MCP 客户端挂载 REA。
- [cognixws/picode-rea](https://github.com/cognixws/picode-rea) - PiCode 扩展，只启用 REA 的静态分析工具。
- [pablodiazjorge/rea-casebook](https://github.com/pablodiazjorge/rea-casebook) - Claude Code mod，实时记录 REA 返回的证据，要求结论必须引用真实的 `evidence_id`，可导出 Markdown。
- [laaielichter/reverseport](https://github.com/laaielichter/reverseport) - 受 REA 启发的 CLI + MCP，主打把逆向结果移植到 Godot、Unity、Unreal、three.js。
- [rea-agents Homebrew formula](https://github.com/moonfruit/homebrew-tap/blob/main/Formula/rea-agents.rb) - 社区维护的 Homebrew 安装方式。

## 教程与深度调研

- [ringozzt/rea-research](https://github.com/ringozzt/rea-research) - 🇨🇳 中文深度技术调研：架构、证据模型、DX-Ball 数字的真实含义、信任模型、Star 与安装量的差距，以及争议背景。推荐先读。
- [valorisa/Reverse-Engineer-Anything](https://github.com/valorisa/Reverse-Engineer-Anything) - 🇫🇷 法语非官方教学指南，含逆向工程的法律框架。
- [pablodiazjorge/rea-lab](https://github.com/pablodiazjorge/rea-lab) - Windows + Ghidra 环境下的 REA 搭建、练习题和工具评测。
- [jinshi666888/rea-playbook](https://github.com/jinshi666888/rea-playbook) - 动手实验：最小 Electron 靶机、带 `file:line` 引用的证据提取、MCP 探针，跑通「反编译 → 理解 → 重建」闭环，无需原生反编译引擎。
- [REA: Reverse Engineer Anything with AI Agents & MCP（HoangYell）](https://hoangyell.com/rea-explained/) - 英文入门讲解。
- [Reverse Engineer Anything: What the Viral REA MCP Actually Does（MindStudio）](https://www.mindstudio.ai/blog/reverse-engineer-anything-mcp) - 去掉炒作后，REA 实际能做什么。
- [Agentic Reverse Engineering: What REA Is and How to Start（El Solitario）](https://elsolitario.org/en/2026/10/10/rea-reverse-engineering-for-coding-agents/) - 上手教程。
- [How To Use REA To Clone Any Software In Minutes（Eric Tech，YouTube）](https://www.youtube.com/watch?v=FnB9tHKBJXQ) - 视频教程，Wispr Flow 拆解案例就是照着它做的。

## 相关 MCP 逆向工具

REA 编排的底层工具，或同类的「给 Agent 用的逆向工具」。

- [mrexodia/ida-pro-mcp](https://github.com/mrexodia/ida-pro-mcp) - 把 IDA Pro 接入大模型的 MCP Server，REA 的 IDA 支持基于它。
- [LaurieWired/GhidraMCP](https://github.com/LaurieWired/GhidraMCP) - Ghidra 的 MCP Server。
- [N0zoM1z0/touhou-reverse-engineering](https://github.com/N0zoM1z0/touhou-reverse-engineering) - 以证据为先的 IDA + MCP 逆向笔记，是复原系列的前期工作。

## 其他 REA 列表与聚合站

- [sqwu/rea-gems](https://github.com/sqwu/rea-gems) - 每天自动更新的 REA 案例画廊，抓取官方案例、GitHub、HN 和 Reddit。
- [miles990/rea-awesome](https://github.com/miles990/rea-awesome) - 按统一评分标准排名的 REA 案例榜，每日更新，提供 JSON / RSS / llms.txt。
- [kaixinbaba/awesome-rea](https://github.com/kaixinbaba/awesome-rea) - 开源逆向、重实现与兼容替代品目录（[awesomerea.com](https://awesomerea.com)），不要求使用 REA。
- [zhuyansen/awesome-ai-reverse-engineering](https://github.com/zhuyansen/awesome-ai-reverse-engineering) - AI 逆向工具列表，每个仓库都有安全评级，中英双语。
- [DiscoverBox/awesome-ai-reverse](https://github.com/DiscoverBox/awesome-ai-reverse) - 🇨🇳 AI 辅助逆向工具清单，覆盖 MCP、Skill、插件、Agent，涉及 Web、二进制、移动端和流量分析。

## X（Twitter）热门帖子

- [Matthew Berman](https://x.com/MatthewBerman/status/2108245653843509415) - 「Reverse Engineer Anything 😂 Software is done.」引发大规模传播的帖子之一。
- [International Cyber Digest](https://x.com/IntCyberDigest/status/2108699960782774733) - GitHub Trending 第一时的介绍：「Software is dead, long live software!」
- [Trending GitHub Repositories](https://x.com/trending_repos/status/2107443007217701076) - 当日趋势仓库播报，24 小时新增约 3,000 Star。
- [Rohan Paul](https://x.com/rohanpaul_ai/status/2108423886509683053) - 功能概览：一个 MCP 覆盖二进制、应用和运行时行为。
- [Afiz](https://x.com/itsafiz/status/2107063919290573174) - 「看到喜欢的功能，就让 Agent 逆向它」，强调 100% 本地运行。
- [Oliver Prompts](https://x.com/oliviscusAI/status/2106955446183411895) - 反编译、追踪执行、检查运行时行为的功能介绍。
- [Vaishnavi](https://x.com/_vmlops/status/2106690704244420687) - 早期介绍帖。
- [lifcc](https://x.com/mylifcc/status/2108940999527690525) - 🇨🇳「一个开源项目一天暴涨 2 万多 Star」，讨论以后可以直接让 Claude Code 或 Codex 研究二进制、重建功能。
- [TechVerser](https://x.com/realfxw/status/2106734209473581308) - 🇨🇳「AI 正在彻底重塑底层逆向工程的游戏规则」，介绍 REA 把逆向工具链封装成 Agent 外挂的思路。
- [codila](https://x.com/0xCodila/status/2109623431763292649) - 「REA is most dangerous thing on the internet right now」，宣扬用它免费复刻付费功能，是争议的典型代表（见下文）。

## 社区讨论

- [Hacker News：Reverse engineer anything with agents, from app behavior down to native binaries](https://news.ycombinator.com/item?id=50058850)
- [Hacker News：Show HN: A MCP for Agents to reverse engineer binary code](https://news.ycombinator.com/item?id=48901763)
- [GitHub 讨论：减少 REA 工作流的 token 浪费](https://github.com/morluto/rea/discussions/1958)
- [GitHub 讨论：Fedora 系 Linux 上的安装笔记与坑](https://github.com/morluto/rea/discussions/1435)
- [GitHub 讨论：Linux 上的基准测试（Node 22/24/26 启动与五个本地模型）](https://github.com/morluto/rea/discussions/1998)

## 媒体报道

- [An AI agent that reverse engineers any software just hit number one on GitHub（Startup Fortune）](https://startupfortune.com/an-ai-agent-that-reverse-engineers-any-software-just-hit-number-one-on-github/)
- [REA Tool Connects Claude Code and Cursor to Ghidra and IDA Pro（Cybersecurity News）](https://cybersecuritynews.com/reverse-engineer-anything-tool/)
- [New Open-Source REA Tool Lets AI Agents Reverse Engineer Software Without Source Code（CyberPress）](https://cyberpress.org/new-open-source-rea-tool/)
- [Matthew Berman promotes REA, which lets coding agents inspect apps without source code（RuntimeWire）](https://runtimewire.com/article/matthew-berman-rea-ai-reverse-engineering)
- [REA Reverse Engineering Tool: Can AI Clone Your App's Features?（MayhemCode）](https://www.mayhemcode.com/2026/10/rea-reverse-engineering-tool-can-ai.html)

## 合规与争议

REA 走红的同时也带来不少争议，选用和传播案例时值得注意：

- **clean-room 是否成立**：批评者认为，同一个 Agent 既做逆向又做重建，达不到传统 clean-room 开发要求的人员隔离。
- **能力边界**：官方并不声称能恢复原始源码或自动克隆整个应用。DX-Ball 的 3,205 / 63 是单函数级别的验证，不代表整程序克隆（见 [rea-research](https://github.com/ringozzt/rea-research) 的分析）。
- **隐私与信任模型**：分析在本地运行，但工具结果会经 Agent 发给模型供应商；官方 SECURITY.md 也明确它不是沙箱。
- **商业工具授权**：IDA Pro、Hopper、JEB 等商业工具必须合法取得授权，REA 不提供任何许可证。
- **官方立场**：REA 只用于合法的研究、教育、互操作、软件保存，以及分析你拥有或获授权检查的软件。见 [DISCLAIMER.md](https://github.com/morluto/rea/blob/main/DISCLAIMER.md)。

本列表不收录以绕过授权、复制付费功能或分发受版权保护资源为主要目的的项目。

## 贡献

欢迎通过 Issue 或 PR 推荐新的项目、案例和文章。收录标准：

1. 优先收录**开源**项目，并附上源码链接。
2. 「社区案例」需要在项目 README 或文章中写明使用了 REA；没有写明的放在「同一波浪潮」。
3. 每条一行，格式为 `- [名称](链接) - 一句话说明它做了什么、怎么用 REA 的。`
4. 不收录镜像、纯 fork，或以侵权、绕过授权为主要目的的项目。
