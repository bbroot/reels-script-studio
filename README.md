# Reels Script Studio / 15秒爆款短视频脚本生成器（数据增强版 v3.5）

> 一个 OpenClaw Skill：用「选项式选择题」生成可直接用于 即梦 / 小云雀 / Seedance / 剪映 的 15 秒爆款短视频脚本，并随成品附「用户使用说明」。内置**数据驱动的爆款因子手册**（黄金3秒法则 / 五大爆款公式 / 四大共鸣情绪 / 七大共性规律 / 平台爆款率数据 / 转发钩子·热点BGM·本地标签策略，源自蝉妈妈·新榜 2025 实测），并带自进化机制，越用越懂你。

A QClaw/OpenClaw skill that generates production-ready 15-second viral short-video scripts via a multiple-choice menu, with platform-adapted AI prompts, a **data-driven viral playbook** (golden-3s rule, 5 viral formulas, 4 resonance emotions, 7 common laws, per-platform viral data, share-hook/BGM/local-tag tactics from Chama/Xinbang 2025), and a built-in self-evolution mechanism.

---

## ✨ 功能特性 / Features（v3.5 数据增强）

- **选项式交互**：用户只需回复 `1A,2E,3A,4C,5B,6ABC`（6 维含爆款杠杆），无需写提示词。
  Choice-based UI — reply with codes (6 dims incl. viral levers), no prompt engineering.
- **六大类型 + AI 创意赛道**：产品种草 / 知识科普 / 剧情叙事 / Vlog / 测评对比 / 热点评论 + AI 创意。
  6 types + AI-creative track covering the most common short-video formats.
- **专业运镜库**：机械臂环绕 / 子弹时间 / 推拉摇移 / 微距探针 / 综合型。
  Pro camera-move library (robotic arm, bullet-time, dolly, probe, combo).
- **四平台适配 + 爆款率数据**：即梦 / 小云雀 / Seedance / 剪映 的提示词结构与参数，**按平台自动匹配爆款因子**（抖音热点BGM 4–7× / 小红书搜索收藏 / 视频号转发链）。
  Platform adapters + per-platform viral tactics.
- **🚀 数据驱动爆款因子手册**（`references/viral-playbook.md`）：黄金3秒法则、五大爆款公式、四大共鸣情绪、七大共性规律、钩子原型库、转发钩子库、热点BGM/本地标签策略——全部来自蝉妈妈/新榜 2025 实测，量化进质量自检。
  Data-driven viral playbook with quantified QA benchmarks.
- **双语用户说明**：每份脚本附中英文「如何使用成品」指南（含黄金3秒/真实感溢价/BGM/本地标签避坑）。
  Bilingual "how to use your output" guide bundled with every script.
- **自进化**：经验沉淀到 `evolution.json`，核心冻结、经验累积。
  Self-evolution via `evolution.json` — core frozen, experience accumulates.

---

## 🚀 快速开始 / Quick Start

### 安装 / Install

```bash
# 方式一：SkillHub（ClawHub）
skillhub install reels-script-studio

# 方式二：GitHub 下载 .skill 后导入
# Download reels-script-studio.skill from GitHub releases, then import in QClaw
```

### 使用 / Usage

在对话中说（任选其一）：
Say any of these in chat:

- "帮我写一个15秒短视频脚本"
- "生成一个 Seedance 的脚本"
- "我要拍产品种草视频"

Skill 会弹出 6 维选项菜单（含「爆款杠杆」），按格式回复即可：
The skill shows a 6-dimension menu (incl. viral levers); reply like:

```
1A,2E,3A,4C,5B,6ABC
```

然后补充产品名与卖点，即可得到：分镜表 + AI 提示词 + 平台参数 + 质量自检(含爆款量化) + 使用说明。
Then provide product name & selling points to get: shot list + AI prompts + platform params + QA (with viral metrics) + usage guide.

---

## 📁 目录结构 / Structure

```
reels-script-studio/
├── SKILL.md                    # 主技能文件（核心冻结层）
├── evolution.json              # 自进化经验（持续更新，不改动核心）
├── references/
│   ├── templates.md            # 六大类型 + AI创意 模板（含爆款因子绑定）
│   ├── platform-adapters.md    # 四平台适配 + 爆款率数据 + BGM/本地标签
│   ├── viral-playbook.md       # 爆款因子手册（黄金3秒/五公式/四情绪/七规律/数据）
│   └── user-guide.md           # 双语用户使用说明（嵌入成品）
└── scripts/
    └── evolve.py               # 进化助手（记录/反馈/报告）
```

## 🧠 自进化 / Evolution

```bash
python3 scripts/evolve.py record --type "产品种草型" --platform "Seedance" --note "加强子弹时间"
python3 scripts/evolve.py feedback --text "第3镜摇移更快" --optimization "平滑→快速"
python3 scripts/evolve.py report
```

进化经验存于本地 `evolution.json`，不上传服务器，可在设备间手动复制同步。
Evolution data stays local in `evolution.json`; copy the file to sync across devices.

---

## 📜 License

MIT
