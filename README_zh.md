# Awesome REA [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md) | **简体中文**

> **用 AI Agent 把任何软件拆开、看懂、重做。** 收录 AI 逆向与 AI 复刻的开源项目、真实案例、工具、教程和讨论。每一条都人工核对过出处。

**REA 是什么？** 「REA（Reverse Engineer Anything）」最早是开源工具 [morluto/rea](https://github.com/morluto/rea) 的名字。它在 2026 年 10 月登上 GitHub Trending 第一、几天内涨到十几万 Star 之后，在社区里已经成了一类做法的代称：**没有源代码，也让 AI Agent 弄清一个软件是怎么工作的，再用自己的代码重做一遍。** 本列表按这个更宽的含义收录，并用标签区分每个项目和 REA 工具的关系：

| 标签 | 含义 |
|:---:|---|
| 🔧 | 项目 README 或作者帖子写明使用了 [morluto/rea](https://github.com/morluto/rea) |
| 🤖 | AI 辅助逆向完成，但没有写明用了 REA |
| 🧪 | AI 辅助的 clean-room 重实现，主要依据公开资料和行为观察，不以逆向二进制为主 |

> ⚠️ 逆向工程受各地法律、软件许可协议和服务条款约束。本列表只收录公开信息，仅供学习、研究、互操作和软件保存用途；使用前请确认你有权分析目标软件。详见 [合规与争议](#合规与争议)。

## 先看这些

- 🔧 [DX-Ball：63 字节逐字节一致](https://rea.tools/showcase/dx-ball/) - 从一次声音调用追到 1996 年游戏的声像函数，复原的 C 代码通过 3,205 个原版 x86 对照用例，编译产物和原版完全相同。
- 🔧 [一个人 + Agent 复原整套《东方 Project》](https://rea.tools/blog/touhou-reconstruction) - [N0zoM1z0](https://github.com/N0zoM1z0?tab=repositories) 复原了 th04、th08、th10 等多部作品，还把 th08 编译成 WebAssembly [在浏览器里玩](https://github.com/N0zoM1z0/th08-web)。
- 🧪 [storytold/photocraft](https://github.com/storytold/photocraft) - 纯 Rust 重写的 Photoshop 式图像编辑器，一两周 Star 超过 5 万；同系列还有 Word、Excel、Illustrator 式的应用。
- 🔧 [宝玉：逆向 Claude Slides 的编辑器](https://x.com/dotey/status/2109151666020794711) - 🇨🇳 从混淆的网页脚本还原出几乎完整的幻灯片编辑器，再让 Claude Code 重写成结构清晰的工程，附完整步骤。
- 🔧 [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) - 拆解 Wispr Flow 的语音输入流程，每条结论标注已证实、推断或未知，最后用 64 行代码在本地重建精简版。
- 🔧 [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) - C++20 clean-room 重实现《战地 2》引擎，附 REA 调查工具。
- 🤖 [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) - 作者说用大约 45 分钟逆向了初代 Apple TV 遥控器，让它通过蓝牙在 Linux 上工作。

## 按被替代的软件找

想找某个软件的开源复刻或复原？先查这张表。Star 数由 shields.io 实时显示。

| 被替代 / 复原的软件 | 开源项目 | 方式 | Star |
|---|---|:---:|---|
| Photoshop | [storytold/photocraft](https://github.com/storytold/photocraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/photocraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/photocraft) |
| Microsoft Word | [storytold/wordcraft](https://github.com/storytold/wordcraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/wordcraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/wordcraft) |
| Excel | [storytold/gridcraft](https://github.com/storytold/gridcraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/gridcraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/gridcraft) |
| Illustrator | [storytold/vectorcraft](https://github.com/storytold/vectorcraft) | 🧪 | [![](https://img.shields.io/github/stars/storytold/vectorcraft?style=flat-square&label=%E2%98%85)](https://github.com/storytold/vectorcraft) |
| Roblox 引擎 | [AsyncFinn/rook](https://github.com/AsyncFinn/rook) | 🧪 | [![](https://img.shields.io/github/stars/AsyncFinn/rook?style=flat-square&label=%E2%98%85)](https://github.com/AsyncFinn/rook) |
| 《英雄无敌 IV》引擎 | [tallowmere/free-heroes4](https://github.com/tallowmere/free-heroes4) | 🧪 | [![](https://img.shields.io/github/stars/tallowmere/free-heroes4?style=flat-square&label=%E2%98%85)](https://github.com/tallowmere/free-heroes4) |
| 《战地 2》Refractor 2 引擎 | [Moxnatiy/OpenBattlefield2](https://github.com/Moxnatiy/OpenBattlefield2) | 🔧 | [![](https://img.shields.io/github/stars/Moxnatiy/OpenBattlefield2?style=flat-square&label=%E2%98%85)](https://github.com/Moxnatiy/OpenBattlefield2) |
| 《GunZ: The Duel》 | [OpenRsG/GunZRs](https://github.com/OpenRsG/GunZRs) | 🔧 | [![](https://img.shields.io/github/stars/OpenRsG/GunZRs?style=flat-square&label=%E2%98%85)](https://github.com/OpenRsG/GunZRs) |
| DX-Ball 1.07 | [N0zoM1z0/dx-ball](https://github.com/N0zoM1z0/dx-ball) | 🔧 | [![](https://img.shields.io/github/stars/N0zoM1z0/dx-ball?style=flat-square&label=%E2%98%85)](https://github.com/N0zoM1z0/dx-ball) |
| 《东方 Project》PC-98 / Windows 作品 | [N0zoM1z0/th04](https://github.com/N0zoM1z0/th04) | 🔧 | [![](https://img.shields.io/github/stars/N0zoM1z0/th04?style=flat-square&label=%E2%98%85)](https://github.com/N0zoM1z0/th04) |
| 《Ski or Die》雪球大战 | [tuunanet/rea-ski-or-die-reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | 🔧 | [![](https://img.shields.io/github/stars/tuunanet/rea-ski-or-die-reconstruction?style=flat-square&label=%E2%98%85)](https://github.com/tuunanet/rea-ski-or-die-reconstruction) |
| Gemtree《Desktop Games》 | [ucodia/desktop-games-nostalgia](https://github.com/ucodia/desktop-games-nostalgia) | 🔧 | [![](https://img.shields.io/github/stars/ucodia/desktop-games-nostalgia?style=flat-square&label=%E2%98%85)](https://github.com/ucodia/desktop-games-nostalgia) |
| Paper（无限画布设计） | [michaelshimeles/paper-rs](https://github.com/michaelshimeles/paper-rs) | 🔧 | [![](https://img.shields.io/github/stars/michaelshimeles/paper-rs?style=flat-square&label=%E2%98%85)](https://github.com/michaelshimeles/paper-rs) |
| OBS Studio（录屏） | [michaelshimeles/rec-rs](https://github.com/michaelshimeles/rec-rs) | 🔧 | [![](https://img.shields.io/github/stars/michaelshimeles/rec-rs?style=flat-square&label=%E2%98%85)](https://github.com/michaelshimeles/rec-rs) |
| TradingView 图表交互 | [michaelshimeles/terminal-rs](https://github.com/michaelshimeles/terminal-rs) | 🔧 | [![](https://img.shields.io/github/stars/michaelshimeles/terminal-rs?style=flat-square&label=%E2%98%85)](https://github.com/michaelshimeles/terminal-rs) |
| Wispr Flow（语音输入） | [az9713/wispr-flow-rea-teardown](https://github.com/az9713/wispr-flow-rea-teardown) | 🔧 | [![](https://img.shields.io/github/stars/az9713/wispr-flow-rea-teardown?style=flat-square&label=%E2%98%85)](https://github.com/az9713/wispr-flow-rea-teardown) |
| PowerToys 取色器 | [iammukeshm/hexgrab](https://github.com/iammukeshm/hexgrab) | 🔧 | [![](https://img.shields.io/github/stars/iammukeshm/hexgrab?style=flat-square&label=%E2%98%85)](https://github.com/iammukeshm/hexgrab) |
| 罗技 G HUB | [Slyvan25/OpenGHub](https://github.com/Slyvan25/OpenGHub) | 🔧 | [![](https://img.shields.io/github/stars/Slyvan25/OpenGHub?style=flat-square&label=%E2%98%85)](https://github.com/Slyvan25/OpenGHub) |
| PreSonus AudioBox VSL 驱动 | [grisuno/VSL-DSP](https://github.com/grisuno/VSL-DSP) | 🔧 | [![](https://img.shields.io/github/stars/grisuno/VSL-DSP?style=flat-square&label=%E2%98%85)](https://github.com/grisuno/VSL-DSP) |
| 初代 Apple TV Siri Remote | [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) | 🤖 | [![](https://img.shields.io/github/stars/a-funk/open-appleremote?style=flat-square&label=%E2%98%85)](https://github.com/a-funk/open-appleremote) |

## 目录

- [先看这些](#先看这些)
- [按被替代的软件找](#按被替代的软件找)
- [官方资源](#官方资源)
- [官方案例](#官方案例)
- [🔧 社区案例：写明使用 REA](#-社区案例写明使用-rea)
  - [经典游戏复原](#经典游戏复原)
  - [桌面应用与工具复刻](#桌面应用与工具复刻)
  - [硬件、协议与驱动](#硬件协议与驱动)
  - [安全分析与评测](#安全分析与评测)
- [🧪🤖 AI 复刻与逆向项目：未写明使用 REA](#-ai-复刻与逆向项目未写明使用-rea)
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

## 🔧 社区案例：写明使用 REA

以下项目都在 README 中写明使用了 REA。

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

## 🧪🤖 AI 复刻与逆向项目：未写明使用 REA

这些项目和 REA 同期在 X 和 GitHub 上走红，常被拿来和 REA 一起讨论「AI 能做多复杂的软件工程」，但 README 没有写明使用 REA。

- 🧪 [storytold/photocraft](https://github.com/storytold/photocraft) - ArtCraft 社区用纯 Rust clean-room 重写的 Photoshop 式图像编辑器，GPU 合成、调整图层、曲线等，Star 数在一两周内超过 5 万。
- 🧪 [storytold/wordcraft](https://github.com/storytold/wordcraft) - 同系列的 Word 式文字处理器，支持修订、引用、邮件合并和 .docx 读写。
- 🧪 [storytold/gridcraft](https://github.com/storytold/gridcraft) - 同系列的 Excel 式电子表格，含公式与图表。
- 🧪 [storytold/vectorcraft](https://github.com/storytold/vectorcraft) - 同系列的 Illustrator 式矢量绘图工具。同系列还有 FilmCraft、LightCraft、PdfCraft、DeckCraft、CADCraft 等，见 [storytold](https://github.com/storytold)。
- 🧪 [AsyncFinn/rook](https://github.com/AsyncFinn/rook) - 用 Rust 重实现 Roblox 引擎，以 Roblox Studio 录制结果做一致性测试。
- 🧪 [tallowmere/free-heroes4](https://github.com/tallowmere/free-heroes4) - C++23 重实现《魔法门之英雄无敌 IV》引擎，需要 GOG 原版文件，尚未完成。
- 🤖 [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote) - 让初代 Apple TV Siri Remote 在 Linux 上通过蓝牙工作：解锁遥控器、解码触控和按键报文、还原 tvOS 风格手势。纯 Python 标准库，MIT。作者称大约 45 分钟完成逆向。

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

浏览量为 2026-10-14 查看时的数字，仅供参考。

### 实测与案例

- [宝玉：用 REA 逆向 Claude Slides 的编辑器](https://x.com/dotey/status/2109151666020794711) - 🇨🇳 下载网页端脚本和样式表，让 Codex 装上 REA Skill 还原混淆代码，再用 Claude Code 重写成结构清晰的工程，附完整步骤。代码在 [JimLiu/baocut](https://github.com/JimLiu/baocut) 的 `apps/slides-editor`（source-available，非开源协议）。约 18 万浏览。
- [A.I.Warper](https://x.com/AIWarper/status/2109060856466264566) - 用 REA + Opus 5.5 把自己买过的一款 Steam 游戏反编译成 C#，不到 30 分钟在 Unity 里跑起来。约 46.7 万浏览，是传播最广的个人实测帖。
- [Vaibhav Sisinty：这周大家用它做了什么](https://x.com/VaibhavSisinty/status/2109618846453977359) - 案例盘点串：Steam 游戏反编译、初代 Apple TV 遥控器、空调遥控、LG 电视 Plex 客户端等。其中多数原帖没有写明用了 REA，属于同一波「AI 逆向」热潮。
- [alex funk：45 分钟逆向初代 Apple TV 遥控器](https://x.com/alexzfunk/status/2108585025205592408) - 「software is kinda solved」，让 Siri Remote 通过蓝牙在 Linux 上工作，开源为 [a-funk/open-appleremote](https://github.com/a-funk/open-appleremote)。帖子和 README 都没有提到 REA。
- [Ilter Canberk：逆向自家空调](https://x.com/icanberk/status/2109031477484937571) - 逆向空调的控制方式后 vibe coding 了一个菜单栏小应用，后来又用 Codex 移植到智能眼镜。未提到 REA。
- [Vaibhav Sisinty：逆向 LG 电视做原生 Plex 客户端](https://x.com/VaibhavSisinty/status/2108103450995417177) - 转述 Reddit 上的案例：嫌官方 Plex 应用启动要 30 秒，用 Claude Code 从 C 写到 Rust，自己做了 OpenGL UI 框架，启动降到 3 秒。未提到 REA。

### 介绍与传播

- [Matthew Berman](https://x.com/MatthewBerman/status/2108245653843509415) - 「Reverse Engineer Anything 😂 Software is done.」引发大规模传播的帖子之一。
- [0xMarioNawfal](https://x.com/RoundtableSpace/status/2109165852578992582) - 「Closed source is dead」，单日 2.5 万 Star 时的介绍，约 92 万浏览。更早的一条[功能介绍](https://x.com/RoundtableSpace/status/2107059472753664261)发于 10 月 5 日。
- [International Cyber Digest](https://x.com/IntCyberDigest/status/2108699960782774733) - GitHub Trending 第一时的介绍：「Software is dead, long live software!」
- [Trending GitHub Repositories](https://x.com/trending_repos/status/2107443007217701076) - 当日趋势仓库播报，24 小时新增约 3,000 Star。
- [Rohan Paul](https://x.com/rohanpaul_ai/status/2108423886509683053) - 功能概览：一个 MCP 覆盖二进制、应用和运行时行为。
- [Tech with Mak](https://x.com/techNmak/status/2108431092462338178) - 「有人给 Claude Code 装了个反编译器」，介绍它如何把 Agent 接到 Ghidra、Hopper 等工具。
- [Hasan Toor](https://x.com/hasantoxr/status/2108524682727305344) - 「把任何应用交给 AI，让它重建里面最好的功能」。
- [Larry Cheng](https://x.com/larryvc/status/2109344654198018095) - 风险投资人视角的一句话介绍：看一个成品应用，不看源码就弄清它怎么工作。
- [Afiz](https://x.com/itsafiz/status/2107063919290573174) - 「看到喜欢的功能，就让 Agent 逆向它」，强调 100% 本地运行。
- [Oliver Prompts](https://x.com/oliviscusAI/status/2106955446183411895) - 反编译、追踪执行、检查运行时行为的功能介绍。
- [K2S](https://x.com/k2sbhai/status/2106796616716062777) - 四步上手：安装、`rea setup`、连接 Agent、给它一个要调查的功能。
- [Vaishnavi](https://x.com/_vmlops/status/2106690704244420687) - 早期介绍帖。
- [Dan Kornas](https://x.com/DanKornas/status/2106032461968761052) - 10 月 2 日的介绍，是走红前最早的几条之一，逐条列出证据记录、本地分析等特性。
- [CyrilXBT](https://x.com/cyrilXBT/status/2109490499321299364) - 「闭源以前意味着受保护，现在只意味着抄得慢一点」，夸张口吻的代表。
- [X 趋势话题页](https://x.com/i/trending/2108302228461080603) - X 官方聚合的「REA GitHub 工具让 AI 从二进制逆向应用功能」话题。

### 中文、日文及其他语言

- [宝玉：REA 让 AI 智能体帮你逆向没有源码的软件](https://x.com/dotey/status/2108794629172682783) - 🇨🇳 最完整的中文介绍：安装、能分析什么、三个官方案例、数据去向，以及合规和「REA 没有发币」的提醒。约 30 万浏览。
- [lifcc](https://x.com/mylifcc/status/2108940999527690525) - 🇨🇳「一个开源项目一天暴涨 2 万多 Star」，讨论以后可以直接让 Claude Code 或 Codex 研究二进制、重建功能。
- [婷](https://x.com/shijianzhongg/status/2107979591348543520) - 🇨🇳「GitHub 上今天的爆火开源项目」，列出挖隐藏功能、查后门、学大厂思路三种用法。约 17 万浏览。
- [TechVerser](https://x.com/realfxw/status/2106734209473581308) - 🇨🇳「AI 正在彻底重塑底层逆向工程的游戏规则」，介绍 REA 把逆向工具链封装成 Agent 外挂的思路。
- [吉川孝志（《マルウエアの教科書》作者）](https://x.com/MalwareBibleJP/status/2108736281647931717) - 🇯🇵 从恶意软件分析和防御方的角度逐条整理依赖工具、静态与运行时分析的区别、数据去向和合规声明。
- [midudev](https://x.com/midudev/status/2107834472091598854) - 🇪🇸「所有人都在用 AI 逆向程序和游戏」，西语开发者圈传播最广的一条，约 15 万浏览。
- [bearstech](https://x.com/bearstech/status/2109679666105655457) - 🇫🇷 法语简介。

### 官方账号

- [@morluto](https://x.com/morluto) - REA 作者。[rea 6.4 发布](https://x.com/morluto/status/2109138696008327226)：「快了很多」，并分享了用来做性能分析的 [morluto/flameox](https://github.com/morluto/flameox)。
- [@reatools](https://x.com/reatools) - 官方账号，转发了作者那句「the homebrew computer club era of technology is back」。

### 同期的开源项目盘点帖

REA 常和其他爆火仓库一起出现在「开源替代付费软件」类的盘点里。

- [brenz.](https://x.com/brenzhills/status/2108983461230845978) - 🇪🇸「这个月正在爆发的 10 个仓库」，REA 排第 4，同列的有 VoiceStudio、ppt-master、gods-eye-view、diagram-design、paperclip。
- [Chris Pirillo](https://x.com/ChrisPirillo/status/2109843806187303400) - 10 月 12 日的 Vibe Coding 与 AI 新闻汇总，REA 与 context-mode、diagram-design 等并列。
- [govin.eth｜G哥](https://x.com/goan999999/status/2109544711400857688) - 🇨🇳「GitHub 上这 6 个开源神器，付费软件的好日子要到头了」：PPT Master、VoiceStudio、God's Eye View、Diagram Design、Paperclip、ECC。没有提到 REA，但和上面两条是同一批项目、同一种叙事。

### 争议

- [codila](https://x.com/0xCodila/status/2109623431763292649) - 「REA is most dangerous thing on the internet right now」，宣扬用它免费复刻付费功能，是争议的典型代表（见下文）。
- [Jaden Williams](https://x.com/JadenJTW/status/2106890896981508329) - 转发早期介绍帖时只写了一句「God help us all.」

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
2. 按上面的标签标注：写明使用 REA 的标 🔧，AI 辅助逆向但没写明工具的标 🤖，AI clean-room 重实现标 🧪。拿不准时请在 PR 里附上出处，由维护者判断。
3. 每条一行，格式为 `- 标签 [名称](链接) - 一句话说明它做了什么、怎么做到的。`
4. 如果项目复刻或复原了某个具体软件，请同时把它加进 [按被替代的软件找](#按被替代的软件找) 的表格。
5. 不收录镜像、纯 fork，或以侵权、绕过授权为主要目的的项目。
