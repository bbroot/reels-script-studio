# 用户使用该成品的说明 / How to Use Your Generated Script

> 本说明随每份生成的脚本一起交付，帮助用户从"脚本"到"成片"。双语（中/英）。

---

## 一、快速上手：三步成片 / Quick Start: 3 Steps

**中文**
1. **启动**：在对话框输入"帮我写一个15秒短视频脚本"等触发句，按菜单回复 `1A,2E,3A,4C,5B`。
2. **补充**：填写产品名与核心卖点（越详细越准）。
3. **获取**：复制「AI 生成提示词」到对应平台，按「分镜表」拍摄/生成，用剪映剪辑。

**English**
1. **Launch**: Type a trigger like "write me a 15s short-video script", then reply with menu codes `1A,2E,3A,4C,5B`.
2. **Fill in**: Provide product name and key selling points (more detail = better output).
3. **Get result**: Copy the "AI prompt" into your platform, shoot/generate per the shot list, and edit in Jianying (CapCut).

---

## 二、AI 提示词怎么用 / Using the AI Prompt

**中文**
- **即梦**：粘贴到「AI 生成」框，已按四段式结构化，无需改。
- **Seedance**：直接粘贴完整提示词，含专业运镜术语，理解最佳。
- **小云雀**：中英文混合可直接用；要更明显子弹时间可加 `time freeze, 180-degree orbit`。
- **剪映**：分镜表作剪辑参考，或勾选导出 XML 导入字幕/配音。
- **优化技巧**：聚焦"场景+主体+动作+光影"四要素；加 `volumetric lighting, ray tracing` 提升真实感；人物加"面部一致，无变形"防变脸。

**English**
- **Jimeng**: Paste into the AI box; already in 4-segment structure, no edit needed.
- **Seedance**: Paste the full prompt directly; includes pro camera terms, best comprehension.
- **Xiaoyunque**: Mixed CN/EN works; add `time freeze, 180-degree orbit` for stronger bullet-time.
- **Jianying (CapCut)**: Use the shot list as edit reference, or export XML for captions/voiceover.
- **Tips**: Focus on "scene + subject + action + lighting"; add `volumetric lighting, ray tracing` for realism; add "consistent face, no distortion" to prevent character morphing.

---

## 三、核心技术参数 / Key Technical Settings

**中文**
- **分辨率**：720P 快速验证 / 1080P 主流 / 4K（Seedance 优先，品牌大屏）。
- **比例**：9:16 竖屏（抖音等）· 16:9 横屏（B站YouTube）· 1:1 方屏 · 21:9 电影宽屏。
- **模型模式**（Kino 类等）：K1 真人短剧 / K3 电商带货 / K7 影视级。

**English**
- **Resolution**: 720P quick test / 1080P standard / 4K (prefer for Seedance, brand/big screen).
- **Aspect**: 9:16 vertical (Douyin etc.) · 16:9 horizontal (Bilibili/YouTube) · 1:1 square · 21:9 cinematic.
- **Model mode** (Kino-like): K1真人短剧 / K3电商带货 / K7影视级.

---

## 四、后期衔接 / Post-Production

**中文**
- 推荐组合：本 Skill + 度加剪辑（卖点分析）+ 剪映（剪辑特效字幕）。
- 剪映：分镜表→「文本→智能字幕」；AI 配音选匹配音色；按镜时长切素材。
- Kino 视界：脚本→编剧角色微调→主体库生成角色卡→一键分镜出片。
- 日产 50 条参考：上午批量生成 → 人工审违禁词/品牌调性 → DeepSeek 批量标题 AB 测试。

**English**
- Stack: this Skill + Dujia (selling-point analysis) + Jianying (editing).
- Jianying: shot list → "Text → Smart Captions"; AI voiceover in matching tone; cut by shot duration.
- Kino: script → writer role tuning → character library → one-click shot generation.
- 50/day workflow: batch generate AM → manual review (banned words/brand tone) → DeepSeek title A/B tests.

---

## 五、质量验收清单 / QA Checklist

| 检查项 | 标准 | 不达标处理 |
|------|------|------|
| 钩子强度 | 前3秒明确钩子 | 告知"加强第1镜"，进化记录 |
| 人物一致性 | 面部/体型不变 | 提示词加"面部一致，无变形" |
| 光影真实度 | 阴影清晰无塑料感 | 加 `volumetric lighting, ray tracing` |
| 专业运镜≥2种 | 机械臂/子弹时间等 | 选"综合型"运镜 |
| 听感流畅 | 250–280 字/分 | 调整台词字数 |

---

## 六、避坑指南 / Pitfalls

**中文**
- **画质**：先生成静态图再转动态；初次用缓慢平移/小动作；固定角色参考图防变脸。
- **违禁词**：抖音严打"第一/最/国家级"；小红书对效果对比稍松；终检用巨量百应。
- **人工审核不可替代**：品牌调性、文化语境、情感一致性需人把关。
- **版权**：AI 生成画面也需确认版权合规。

**English**
- **Quality**: Generate a still first, then animate; start with slow pans/small moves; use a fixed character reference to avoid morphing.
- **Banned words**: Douyin bans "first / best / national-grade"; Xiaohongshu is looser on comparisons; final check via Juliang Baiying.
- **Human review is irreplaceable**: brand tone, cultural fit, emotional consistency need a human.
- **Copyright**: even AI-generated visuals must be rights-cleared.

---

## 七、进化机制 / Evolution

**中文**
- 每次说"记录这个经验"或"修改第X镜的XX"，Skill 会越用越懂你。
- 进化经验存于本地 `evolution.json`，不上传服务器，可在设备间手动复制同步。

**English**
- Say "record this experience" or "change shot X's XX" — the Skill learns you over time.
- Evolution data lives in local `evolution.json`, never uploaded; copy the file to sync across devices.
