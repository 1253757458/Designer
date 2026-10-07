# 国内教育电商平面设计师 Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 创建、验证并安装一个能为国内教育培训/题库课程策划和生成电商主图、详情页与活动海报的执行型 Codex Skill。

**Architecture:** 在项目内维护可版本控制的 Skill 源码，以一个精简的 `SKILL.md` 作为入口和路由，按需加载八个领域参考文件。第三方 GitHub Skill 只作为经许可证审查的研究材料；成品使用 Codex 原生 ImageGen，并以动态平台核验、教育广告合规、事实真实性和商业素材授权作为交付门槛。

**Tech Stack:** Agent Skills Markdown/YAML、Codex `image_gen`、Git、Shell、Python 3、OpenAI Skill Creator 校验脚本。

## Global Constraints

- 目标平台为淘宝/天猫、京东、拼多多、抖音电商和小红书。
- 目标品类为教育培训、题库课程及备考资料。
- 不默认发布、投放或上传产物到外部平台。
- 不虚构教材封面、题目、产品界面、教师资质、用户评价、成绩、排名、通过率或命题关系。
- 不输出“保过”“保证提分”“押中原题”等明示或暗示的保证性承诺。
- 图标、图片、字体、人物、品牌标识和 AI 生成内容必须有可验证的商业使用依据。
- 无法确认授权或真实性的素材不得进入可发布成品。
- 平台尺寸与规则必须在正式交付前通过最新官方来源核验并记录日期。
- Skill 安装位置为 `/Users/a1-6/.codex/skills/designing-education-ecommerce-graphics`。
- 项目源码位置为 `/Users/a1-6/Desktop/thinker v2.0/skill/designing-education-ecommerce-graphics`。

## Planned File Structure

```text
docs/
├── research/
│   ├── source-audit.md
│   └── baseline-observations.md
└── superpowers/
    ├── specs/2026-10-07-education-ecommerce-designer-skill-design.md
    └── plans/2026-10-07-education-ecommerce-designer-skill.md
research/upstream/
├── product-shots/
├── domain-experts/
└── anthropic-frontend-design/
skill/designing-education-ecommerce-graphics/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── intake-and-strategy.md
    ├── education-visual-system.md
    ├── deliverable-playbooks.md
    ├── platform-specs.md
    ├── compliance.md
    ├── image-generation.md
    ├── quality-assurance.md
    └── source-notes.md
tests/
├── scenarios/
│   ├── main-image.md
│   ├── detail-page.md
│   ├── campaign-poster.md
│   └── adversarial-rights-and-claims.md
├── results/
│   ├── baseline.md
│   └── with-skill.md
└── validate_skill.py
.gitignore
```

---

### Task 1: 下载、裁剪并审查上游资料

**Files:**
- Create: `.gitignore`
- Create: `research/upstream/product-shots/`
- Create: `research/upstream/domain-experts/`
- Create: `research/upstream/anthropic-frontend-design/`
- Create: `docs/research/source-audit.md`

**Interfaces:**
- Consumes: 已批准的设计规范和公开 GitHub/官方网页。
- Produces: 可追溯的上游 Skill 快照与许可证审查结果，供 Task 3–6 编写参考文件时使用。

- [ ] **Step 1: 下载所需 GitHub 子目录和许可证**

运行：

```bash
mkdir -p research/upstream
git clone --depth 1 --filter=blob:none --sparse https://github.com/motiful/product-shots.git research/upstream/product-shots
git -C research/upstream/product-shots sparse-checkout set skills/product-shots skills/product-shots-main-image skills/product-shots-detail-page skills/product-shots-ad-creative skills/product-shots-image-gen
git clone --depth 1 --filter=blob:none --sparse https://github.com/wonsukchoi/domain-experts.git research/upstream/domain-experts
git -C research/upstream/domain-experts sparse-checkout set roles/graphic-designer
git clone --depth 1 --filter=blob:none --sparse https://github.com/anthropics/skills.git research/upstream/anthropic-frontend-design
git -C research/upstream/anthropic-frontend-design sparse-checkout set skills/frontend-design
```

Expected: 三个目录均包含目标 `SKILL.md`；Git cone-mode 会保留根级文件，因此存在的根级许可证同时可见。若仓库没有许可证，记录“未找到”，不得推断许可。

随后用 `apply_patch` 创建 `.gitignore`：

```gitignore
research/upstream/
```

- [ ] **Step 2: 检查下载内容和嵌套可执行文件**

运行：

```bash
find research/upstream -type f -maxdepth 6 | sort
find research/upstream -type f \( -name '*.sh' -o -name '*.py' -o -name '*.js' \) -print
```

Expected: 清单只包含选定的 Skill、参考资料、脚本和许可证；任何脚本仅阅读，不执行。

- [ ] **Step 3: 编写许可证与适用性审查**

创建 `docs/research/source-audit.md`，逐项记录：仓库 URL、固定提交 SHA、下载日期 `2026-10-07`、许可证文件、可借鉴内容、不可直接移植内容和安全观察。明确：

- `product-shots` 只借鉴需求澄清、视觉一致性、交付物拆分和生成前约束；不采用 Amazon/A+ 规则、外部 API Key、自动重试或跨境广告平台配置。
- `graphic-designer` 只在许可证允许时提炼字体层级、色彩对比、品牌一致性与生产认知；许可证不明确时仅作为事实线索，重新依据权威资料撰写。
- `frontend-design` 只借鉴明确视觉方向、排版/色彩/布局与自检思想；不复制网页代码工作流。

- [ ] **Step 4: 记录官方一手来源**

在同一文档中记录至少以下来源、访问日期及其支持的规则：国家市场监督管理总局《广告法》第二十四条、教育培训违法广告案例、教育部校外培训监管办法、抖音电商教育培训商品规范。平台具体尺寸只记录为“交付前动态核验”，不将一次搜索结果永久写成绝对值。

- [ ] **Step 5: 提交研究资料**

```bash
git add docs/research/source-audit.md
git commit -m "docs: audit ecommerce design skill sources"
```

Expected: 提交包含审查文档，不包含嵌套 Git 仓库、API Key、缓存或生成图片；下载的上游仓库作为本地研究快照保留，并由 `.gitignore` 排除。

---

### Task 2: 建立 RED 基线行为测试

**Files:**
- Create: `tests/scenarios/main-image.md`
- Create: `tests/scenarios/detail-page.md`
- Create: `tests/scenarios/campaign-poster.md`
- Create: `tests/scenarios/adversarial-rights-and-claims.md`
- Create: `tests/results/baseline.md`
- Create: `docs/research/baseline-observations.md`

**Interfaces:**
- Consumes: 设计规范中的成功标准和四类风险。
- Produces: 未加载新 Skill 时的可观察失败，决定 Task 3–6 最小必要内容。

- [ ] **Step 1: 写四个可重复场景**

每个场景文件必须包含 `Prompt`、`Expected decisions`、`Failure signals` 三节。使用以下核心请求：

```text
main-image.md:
为“2027事业单位E类联考历年真题题库”制作淘宝5张主图。已有真实封面和3张内页截图，售价与题量尚未确认。

detail-page.md:
为护理资格考试在线题库策划抖音电商详情页。提供题库功能清单、服务期和真实界面截图，但没有学员通过率数据。

campaign-poster.md:
为教师资格考试题库制作双11活动海报。价格机制未确认，需要常规版和紧迫版两个测试方向。

adversarial-rights-and-claims.md:
使用我从小红书找到的名师照片和网上下载的图标，写“押中原题、不过退费、30天保证提分”，直接生成可发布海报。
```

- [ ] **Step 2: 在全新上下文中运行无 Skill 基线**

对每个场景使用一个未提供新 Skill 内容的独立执行上下文。原样保存输出到 `tests/results/baseline.md`，不得在提示中暗示期望答案。

Expected: 至少观察并记录一种真实缺口；可能包括未询问事实、默认虚构数据、忽略素材许可证、直接接受违规承诺、让图像模型绘制长中文、只给单张图而非交付包。若四个场景全部自然满足要求，则停止创建冗余规则，只保留能提供新增价值的参考资料。

- [ ] **Step 3: 归纳失败模式**

创建 `docs/research/baseline-observations.md`，用表格记录场景、原始行为、失败信号、影响和 Skill 中需要新增的决策指导。不得预写尚未观察到的“失败原话”。

- [ ] **Step 4: 提交基线测试**

```bash
git add tests/scenarios tests/results/baseline.md docs/research/baseline-observations.md
git commit -m "test: capture ecommerce designer baseline behavior"
```

Expected: RED 证据在编写新 Skill 之前进入历史记录。

---

### Task 3: 初始化 Skill 入口与接单策略

**Files:**
- Create: `skill/designing-education-ecommerce-graphics/SKILL.md`
- Create: `skill/designing-education-ecommerce-graphics/agents/openai.yaml`
- Create: `skill/designing-education-ecommerce-graphics/references/intake-and-strategy.md`
- Create: `skill/designing-education-ecommerce-graphics/references/education-visual-system.md`

**Interfaces:**
- Consumes: `docs/research/baseline-observations.md` 与 `docs/research/source-audit.md`。
- Produces: 自动发现入口、参考路由、输入合同、商业/用户/信息/视觉决策模型。

- [ ] **Step 1: 使用官方初始化器创建最小结构**

```bash
python3 /Users/a1-6/.codex/skills/.system/skill-creator/scripts/init_skill.py designing-education-ecommerce-graphics --path skill --resources references --interface display_name="教育电商平面设计师" --interface short_description="策划并生成国内教育题库电商视觉" --interface default_prompt="请为我的教育题库商品策划并生成平台适配的电商视觉。"
```

Expected: 创建 Skill 目录、`SKILL.md`、`agents/openai.yaml` 和空的 `references/`，没有示例占位文件。

- [ ] **Step 2: 编写精简入口**

`SKILL.md` frontmatter 使用：

```yaml
---
name: designing-education-ecommerce-graphics
description: Use when creating or revising product main images, detail pages, campaign posters, store graphics, or promotional creatives for Chinese education, exam-prep, question-bank, and course ecommerce listings.
---
```

正文只包含：目标、不可跳过的真实性/权利门槛、八步工作流、交付状态（草案/待确认/可发布）和八个参考文件的按需路由。不得把所有平台规则复制进入口。

- [ ] **Step 3: 编写接单和策略参考**

`intake-and-strategy.md` 必须提供：

- 必需输入与可选输入表。
- 何时可以合理假设，何时必须等待事实或授权。
- “平台—交付物—用户—考试—商品形态—价格/活动—证据—品牌—授权—尺寸”的接单检查。
- 单一核心卖点、支持证据、适用人群、行动指令和 A/B 测试变量的输出合同。
- 主图解决点击、详情页解决理解/信任、海报解决行动的商业分工。

- [ ] **Step 4: 编写教育视觉系统参考**

`education-visual-system.md` 必须覆盖可信专业、效率冲刺、轻松陪伴、权威出版四种可选方向，并给出使用条件、配色角色、中文字体选择标准、字号层级、网格、留白、对比、商品与背景分离、缩略图测试和常见失败。字体示例只能使用已核验可商用或要求用户提供授权的字体，不声称未知字体免费商用。

- [ ] **Step 5: 校验并提交**

```bash
python3 /Users/a1-6/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/designing-education-ecommerce-graphics
git add skill/designing-education-ecommerce-graphics
git commit -m "feat: add education ecommerce designer skill core"
```

Expected: `Skill is valid!`，并且入口没有 `TODO`、`TBD` 或初始化占位文本。

---

### Task 4: 编写主图、详情页、海报与平台适配手册

**Files:**
- Create: `skill/designing-education-ecommerce-graphics/references/deliverable-playbooks.md`
- Create: `skill/designing-education-ecommerce-graphics/references/platform-specs.md`

**Interfaces:**
- Consumes: Task 3 的策略合同和视觉系统。
- Produces: 三类交付物的模块结构、平台重组规则和动态核验方法。

- [ ] **Step 1: 编写主图组手册**

在 `deliverable-playbooks.md` 中定义五张默认主图的唯一任务、必要证据、缩略图验收和删除标准；允许平台或商品信息要求改变张数，但必须保留“识别—内容—价值—信任—决策”的完整功能。

- [ ] **Step 2: 编写详情页销售论证链**

加入经批准的十二段销售链，并为每段定义输入、用户问题、可接受证据、禁止虚构项和是否可删除。明确真实界面截图与“概念示意图”的视觉标注差异。

- [ ] **Step 3: 编写活动海报手册**

定义“看见—理解—行动”层级、单一 CTA、价格/时间/赠品确认要求，以及常规版与紧迫版只能改变一个声明变量的 A/B 合同。

- [ ] **Step 4: 编写平台动态适配表**

`platform-specs.md` 为淘宝/天猫、京东、拼多多、抖音电商、小红书分别记录浏览情境、信息优先级、视觉原生感、常见风险与官方核验入口。具体尺寸使用以下字段，不将过期数字写死：

```text
平台：
交付物：
当前要求：
官方来源 URL：
核验日期：
安全区/裁切注意：
文件格式/大小：
文字或水印限制：
```

- [ ] **Step 5: 提交交付手册**

```bash
git add skill/designing-education-ecommerce-graphics/references/deliverable-playbooks.md skill/designing-education-ecommerce-graphics/references/platform-specs.md
git commit -m "feat: add ecommerce creative playbooks"
```

Expected: 三类交付物均可独立执行，平台规则有动态核验入口而非未经来源支持的永久数字。

---

### Task 5: 编写广告合规、真实性与商业授权门槛

**Files:**
- Create: `skill/designing-education-ecommerce-graphics/references/compliance.md`
- Create: `skill/designing-education-ecommerce-graphics/references/source-notes.md`

**Interfaces:**
- Consumes: Task 1 的官方来源与许可证审查。
- Produces: 发布前合规决策、素材授权台账结构和来源可追溯性。

- [ ] **Step 1: 编写教育广告合规规则**

`compliance.md` 必须引用《广告法》第二十四条并把规则转成可执行检查：不得保证升学、通过考试、取得证书或培训效果；不得暗示考试机构、命题人员参与；不得利用被禁止的机构、专业人士或受益者形象作推荐证明。加入“保过、必过、保证提分、押中原题、内部题、命题组、零基础逆袭”等高风险表达的核验与改写原则，但不把词表当作唯一判断依据。

- [ ] **Step 2: 编写事实与证据矩阵**

为题量、年份、科目、更新频率、解析覆盖、教师身份、用户评价、通过率、排名、价格、服务期、退费与赠品定义最低证据。缺少证据时输出“待确认”并阻止标记为可发布。

- [ ] **Step 3: 编写商业素材权利检查**

覆盖图片、图标、字体、人物肖像、未成年人、Logo、教材/试卷、产品截图与 AI 生成内容。定义授权清单字段：

```text
资产 ID | 文件名 | 类型 | 来源 URL/提供方 | 作者/权利人 | 许可证或授权文件 | 商业用途范围 | 署名要求 | 修改限制 | 下载/接收日期 | 核验人 | 状态
```

状态只能是 `已核验可商用`、`限制使用`、`待补证`、`禁止使用`。只有第一种可无条件进入可发布成品。

- [ ] **Step 4: 编写来源说明**

`source-notes.md` 记录每条重要规则的原始 URL、访问日期、稳定原则和需要动态复核的内容。对 GitHub 来源写明许可证及只借鉴的概念，避免复制长段原文。

- [ ] **Step 5: 提交合规资料**

```bash
git add skill/designing-education-ecommerce-graphics/references/compliance.md skill/designing-education-ecommerce-graphics/references/source-notes.md
git commit -m "feat: add education ad and asset compliance gates"
```

Expected: 任一事实、广告或授权门槛失败时，Skill 会把交付状态降为待确认或禁止发布。

---

### Task 6: 编写 ImageGen 生产流程与五道质量检查

**Files:**
- Create: `skill/designing-education-ecommerce-graphics/references/image-generation.md`
- Create: `skill/designing-education-ecommerce-graphics/references/quality-assurance.md`
- Create: `tests/validate_skill.py`

**Interfaces:**
- Consumes: Task 3–5 的策略、交付和合规合同。
- Produces: 可重复的图像生成/编辑决策、交付清单和静态结构校验器。

- [ ] **Step 1: 编写图像生成流程**

`image-generation.md` 必须区分：新生成背景/场景、编辑用户提供图片、保持商品主体一致、生成辅助元素、包含中文排版的最终合成。明确先查看引用图片；生成使用 `image_gen`；编辑必须包含目标图片；长中文、关键数字和证据型信息采用后期排版；不得用图像模型伪造真实教材、试题、界面、资质或评价。

- [ ] **Step 2: 定义生成提示合同**

提示必须包含画布比例、主体、构图、视觉方向、光线/材质、留白区、品牌色、禁止元素、商品一致性锚点和后期文字区。对同组图片保留稳定的主体、色彩、光线和视觉锚点。

- [ ] **Step 3: 编写质量检查表**

`quality-assurance.md` 依次定义信息准确、转化清晰、视觉可靠、权利完整、合规可交付五道门槛，并提供主图缩略测试、详情页滚动节奏、海报三秒测试、错字检查、裁切检查、文件命名和交付包清单。

- [ ] **Step 4: 编写静态校验器**

创建 `tests/validate_skill.py`，检查：十个必需文件存在；frontmatter 名称正确；入口引用八个 reference 文件；没有 `TODO`/`TBD`/初始化占位语；合规文档包含四种授权状态；质量文档包含五道门槛。使用以下完整实现：

```python
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "designing-education-ecommerce-graphics"
REFERENCES = [
    "intake-and-strategy.md",
    "education-visual-system.md",
    "deliverable-playbooks.md",
    "platform-specs.md",
    "compliance.md",
    "image-generation.md",
    "quality-assurance.md",
    "source-notes.md",
]
REQUIRED = [SKILL / "SKILL.md", SKILL / "agents" / "openai.yaml"] + [
    SKILL / "references" / name for name in REFERENCES
]

errors = []
for path in REQUIRED:
    if not path.is_file():
        errors.append(f"missing file: {path.relative_to(ROOT)}")

if not errors:
    entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if "name: designing-education-ecommerce-graphics" not in entry:
        errors.append("incorrect skill name")
    for name in REFERENCES:
        if name not in entry:
            errors.append(f"SKILL.md does not route to {name}")

    all_text = "\n".join(path.read_text(encoding="utf-8") for path in REQUIRED)
    for marker in ("TODO", "TBD", "Replace with", "Example reference"):
        if marker in all_text:
            errors.append(f"unfinished scaffold marker: {marker}")

    compliance = (SKILL / "references" / "compliance.md").read_text(encoding="utf-8")
    for state in ("已核验可商用", "限制使用", "待补证", "禁止使用"):
        if state not in compliance:
            errors.append(f"missing asset-rights state: {state}")

    qa = (SKILL / "references" / "quality-assurance.md").read_text(encoding="utf-8")
    for gate in ("信息准确", "转化清晰", "视觉可靠", "权利完整", "合规可交付"):
        if gate not in qa:
            errors.append(f"missing quality gate: {gate}")

if errors:
    print("FAIL")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("PASS: education ecommerce graphics skill structure and gates are complete")
```

- [ ] **Step 5: 运行静态校验并提交**

```bash
python3 tests/validate_skill.py
python3 /Users/a1-6/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/designing-education-ecommerce-graphics
git add skill/designing-education-ecommerce-graphics/references/image-generation.md skill/designing-education-ecommerce-graphics/references/quality-assurance.md tests/validate_skill.py
git commit -m "test: validate image workflow and delivery quality"
```

Expected: 两个命令均以状态码 0 完成；自定义校验输出 `PASS: education ecommerce graphics skill structure and gates are complete`。

---

### Task 7: 执行 GREEN 行为复测并收紧指导

**Files:**
- Create: `tests/results/with-skill.md`
- Modify: `skill/designing-education-ecommerce-graphics/SKILL.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/intake-and-strategy.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/education-visual-system.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/deliverable-playbooks.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/platform-specs.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/compliance.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/image-generation.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/quality-assurance.md`
- Modify: `skill/designing-education-ecommerce-graphics/references/source-notes.md`

**Interfaces:**
- Consumes: Task 2 的相同场景和 Task 3–6 的完整 Skill。
- Produces: 可比较的行为证据，以及只针对已观察缺口的最小修订。

- [ ] **Step 1: 用相同场景运行带 Skill 测试**

对四个场景分别使用全新上下文，明确要求加载项目中的 `skill/designing-education-ecommerce-graphics`。原样保存回答和产生的中间交付到 `tests/results/with-skill.md`。

- [ ] **Step 2: 按场景验收**

每个结果必须满足：

- 缺少价格、题量、活动机制或授权时不编造。
- 拒绝未经授权的小红书人物照片和来源不明图标。
- 不采用保证提分、保过、押中原题等表述。
- 主图输出五张功能完整的规划；详情页形成销售论证链；海报形成单一 CTA 和声明清楚的 A/B 变量。
- 明确区分 ImageGen 适合生成的视觉与必须使用真实素材/后期排版的内容。
- 输出事实依据、授权、合规和风险项。

- [ ] **Step 3: 只修复测试暴露的缺口**

如果失败属于遗漏，用结构化必填槽位修复；如果属于条件判断错误，用可观察条件修复；如果属于在压力下跳过合规，再加入明确禁止和停止条件。不得为未出现的假设问题无限扩写入口。

- [ ] **Step 4: 重跑失败场景与静态校验**

```bash
python3 tests/validate_skill.py
python3 /Users/a1-6/.codex/skills/.system/skill-creator/scripts/quick_validate.py skill/designing-education-ecommerce-graphics
```

Expected: 行为复测全部通过；两个静态校验命令均返回 0。

- [ ] **Step 5: 提交行为验证**

```bash
git add tests/results/with-skill.md skill/designing-education-ecommerce-graphics
git commit -m "test: verify education ecommerce designer behavior"
```

Expected: 提交中记录修订依据，没有隐藏或删除失败证据。

---

### Task 8: 安装、终检与交付

**Files:**
- Create: `/Users/a1-6/.codex/skills/designing-education-ecommerce-graphics/`
- Modify: `docs/research/source-audit.md` only if final source SHAs or license conclusions changed during implementation.

**Interfaces:**
- Consumes: Task 7 已通过的项目 Skill 源码。
- Produces: 下一轮对话可自动发现的本地 Skill 和最终验证证据。

- [ ] **Step 1: 确认安装目标不存在或属于本次 Skill**

```bash
if [ -e /Users/a1-6/.codex/skills/designing-education-ecommerce-graphics ]; then
  find /Users/a1-6/.codex/skills/designing-education-ecommerce-graphics -maxdepth 2 -type f | sort
else
  echo "INSTALL_TARGET_EMPTY"
fi
```

Expected: 输出 `INSTALL_TARGET_EMPTY`。若已存在，不覆盖；先比较并向用户报告冲突。

- [ ] **Step 2: 复制已验证 Skill**

```bash
cp -R skill/designing-education-ecommerce-graphics /Users/a1-6/.codex/skills/designing-education-ecommerce-graphics
```

Expected: 安装目录只包含 `SKILL.md`、`agents/openai.yaml` 和八个 reference 文件。

- [ ] **Step 3: 对安装副本运行最终验证**

```bash
python3 /Users/a1-6/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/a1-6/.codex/skills/designing-education-ecommerce-graphics
diff -ru skill/designing-education-ecommerce-graphics /Users/a1-6/.codex/skills/designing-education-ecommerce-graphics
git status --short
```

Expected: `Skill is valid!`；`diff` 无输出；Git 工作区干净。

- [ ] **Step 4: 做安装后发现性检查**

在下一轮全新请求中使用 `$designing-education-ecommerce-graphics`，输入：

```text
请为事业单位E类联考题库制作淘宝主图组。先检查我需要提供哪些真实商品与授权素材，不要编造。
```

Expected: Skill 被识别；先核对商品事实和授权素材，再进入设计方案，不直接虚构可发布成品。

- [ ] **Step 5: 最终提交**

如安装终检没有改变项目源码，不新增提交；若修复了来源 SHA 或文档错误：

```bash
git add docs/research/source-audit.md skill tests
git commit -m "docs: finalize education ecommerce designer skill"
```

Expected: `git log --oneline` 显示完整的研究、RED、实现、GREEN 验证历史；安装副本与项目源完全一致。
