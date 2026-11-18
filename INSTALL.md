# 安装说明 · reels-script-studio v3.6.0

本技能遵循通用的 **Agent Skills** 规范（根目录 `SKILL.md` + YAML frontmatter，可选 `scripts/` `references/` `assets/`）。同一份源码可安装到以下 4 类 Agent，**无需修改内容**。

> ⚠️ 安装时请复制**整个技能目录**，不要只复制 `SKILL.md`，否则 `scripts/`、`references/`、`assets/` 会缺失导致功能不可用。
> 装完后**新开一个对话**才会加载技能。

## 方式速查

| Agent | 安装方式 | 用户级目录（所有项目可用） | 项目级目录（仅当前项目） |
|---|---|---|---|
| **WorkBuddy** | 图形界面导入，或直接放目录 | `~/.workbuddy/skills/reels-script-studio/` | `<项目>/.workbuddy/skills/reels-script-studio/` |
| **豆包工作** | 客户端「技能」→「上传技能」上传整个文件夹 / ZIP | 客户端内管理，无需命令行 | 同左 |
| **Claude Code** | 直接放目录 | `~/.claude/skills/reels-script-studio/` | `<项目>/.claude/skills/reels-script-studio/` |
| **Cursor / CodeBuddy** | 直接放目录 | `~/.agents/skills/reels-script-studio/` | `<项目>/.agents/skills/reels-script-studio/` |

## 各平台步骤

### 1. WorkBuddy

- **推荐（图形界面）**：设置 → 技能 → 添加技能 → 上传技能包，选择本目录的 ZIP。
- **命令行**：把整个目录复制到 `~/.workbuddy/skills/reels-script-studio`。

```bash
cp -R . ~/.workbuddy/skills/reels-script-studio
```

### 2. 豆包工作（字节跳动）

1. 打开豆包工作客户端 → 左侧「插件 / 技能 / 伙伴」→「技能」页。
2. 右上角「+ 添加」→「上传技能」，选择本目录的**ZIP 或整个文件夹**。
3. 技能要求：压缩包根目录必须有 `SKILL.md`，且开头是 YAML（含 `name` / `description`）——本技能已满足。
4. 调用：新工作任务里直接说需求自动匹配，或输入 `/` `/@` 搜索 `reels-script-studio`。
5. 注意：云端电脑与本地电脑的技能默认不互通；任务运行在云电脑时需用技能商店上传的版本。

### 3. Claude Code

```bash
# 用户级（所有项目可用）
cp -R . ~/.claude/skills/reels-script-studio

# 或项目级（随仓库提交，团队共享）
mkdir -p <项目>/.claude/skills && cp -R . <项目>/.claude/skills/reels-script-studio
```

技能会在会话启动时自动加载；也可在对话中用 `/reels-script-studio` 显式调用。

### 4. Cursor / CodeBuddy 及其他兼容 Agent

这类 Agent 多数采用 `~/.agents/skills/` 或其自有目录（CodeBuddy 为 `~/.codebuddy/skills/`）。通用做法：

```bash
mkdir -p ~/.agents/skills && cp -R . ~/.agents/skills/reels-script-studio
# CodeBuddy: cp -R . ~/.codebuddy/skills/reels-script-studio
```

若某 Agent 仅接受单个 Markdown 文件作为技能正文，请把 `SKILL.md` 作为正文导入，并将 `scripts/`、`references/`、`assets/` 作为附件或工作区文件一并上传。

## 环境变量（可选）

本技能为跨平台设计，可用环境变量覆盖默认路径：

(本技能无必须环境变量；evolution.json 为自进化数据文件，勿删。)
- `AGENT_SKILLS_DIR`：本技能所在的 skills 根目录（供跨技能调用定位，如 `~/.workbuddy/skills`）。

## 验证安装

```bash
# 1. 确认目录结构完整
ls <agent-skills-dir>/reels-script-studio/SKILL.md
# 2. 若带 scripts/，跑一次帮助/自检（以实际脚本为准）
python scripts/evolve.py report
```

## 来源与版本

- 上游：https://github.com/bbroot/reels-script-studio
- 当前版本：**v3.6.0**（详见 SKILL.md frontmatter 的 `version` 字段）
- 许可证：见仓库 LICENSE（若有）
