# 教育电商平面设计 Skill：来源与许可证审查

下载和访问日期：2026-10-07。审查对象是研究输入，不是运行时依赖；未执行下载的脚本，未安装第三方 Skill，未配置 API Key。

## 快照方法与可追溯性

已尝试计划中的三个浅层 sparse clone 命令，但 github.com 连接超时或 TLS 断开。经任务协调者确认，改用官方 GitHub API 查询提交 SHA，再从官方 codeload 下载该提交的归档，仅提取目标子目录和许可证、README 元数据。因此以下目录是 **API 定位的提交固定归档快照，不是 sparse Git clone**。每个目录的 `SNAPSHOT.md` 保存获取方式、提交和下载链接；文件内容未改写。

| 本地目录（均在 research/upstream/ 下） | 上游仓库 | 固定提交 SHA | 选取范围 |
| --- | --- | --- | --- |
| product-shots | https://github.com/motiful/product-shots | `063c508b0b7f4db5cda89f10bdf20df25026dfc5` | skills/product-shots、product-shots-main-image、product-shots-detail-page、product-shots-ad-creative、product-shots-image-gen；根 LICENSE、README.md |
| domain-experts | https://github.com/wonsukchoi/domain-experts | `8392c1503d75ef2928c930cee195f1ada813ccc2` | roles/graphic-designer（含 references）；根 LICENSE、README.md |
| anthropic-frontend-design | https://github.com/anthropics/skills | `683bc88e56f3e09ba94f7055977f3d3aa499f202` | skills/frontend-design（含 LICENSE.txt）；根 README.md、THIRD_PARTY_NOTICES.md |

提交元数据与精确下载 URL：

- product-shots：[提交 API](https://api.github.com/repos/motiful/product-shots/commits/063c508b0b7f4db5cda89f10bdf20df25026dfc5)、[提交固定归档](https://codeload.github.com/motiful/product-shots/tar.gz/063c508b0b7f4db5cda89f10bdf20df25026dfc5)。
- domain-experts：[提交 API](https://api.github.com/repos/wonsukchoi/domain-experts/commits/8392c1503d75ef2928c930cee195f1ada813ccc2)、[提交固定归档](https://codeload.github.com/wonsukchoi/domain-experts/tar.gz/8392c1503d75ef2928c930cee195f1ada813ccc2)。
- frontend-design：[提交 API](https://api.github.com/repos/anthropics/skills/commits/683bc88e56f3e09ba94f7055977f3d3aa499f202)、[提交固定归档](https://codeload.github.com/anthropics/skills/tar.gz/683bc88e56f3e09ba94f7055977f3d3aa499f202)。

`.gitignore` 排除整个 `research/upstream/`；本地研究快照不进入提交或最终 Skill。归档中的图库、其他角色、其他 Skill、仓库自动化等均未提取。失败 clone 的残留 Git 元数据移至 `/tmp/task-1-product-shots-incomplete-git-20261007`，不位于交付目录中。

完整归档 SHA-256（用于核验本次下载；50 个提取的上游文件已逐字节与归档比对一致）：

- product-shots：`72aaea11b4894d36b4dd167c1c4bfd49470c5360eef9727ea659b4f56afa72ad`，提取 40 个文件。
- domain-experts：`bc3ed66ffac0aeb6a48ff1c05bc8276404f1ba9cad0cc84cbab0940449548d96`，提取 6 个文件。
- frontend-design：`30a1152c163d87852587347c242261d7dd85f2208f25bd9c4b6bf47266a5f4bf`，提取 4 个文件。

## 许可证、适用性与安全观察

### 1. motiful/product-shots

- 许可证：根 [LICENSE](https://raw.githubusercontent.com/motiful/product-shots/063c508b0b7f4db5cda89f10bdf20df25026dfc5/LICENSE)，MIT，Copyright (c) 2026 motiful；选定 SKILL.md 也声明 MIT。允许使用、修改、分发和商业使用；若复制或分发实质性内容，必须保留版权和许可声明。许可不代替商品图片、商标、字体或肖像授权。
- 可借鉴内容：只借鉴需求澄清、视觉一致性、交付物拆分和生成前约束。对应 hub 的 clarification-stages、brief-output-and-routing、design-element-standards，以及主图/详情页的 consistency-rules 与各交付物自检思路。新 Skill 以国内教育事实、用户品牌和原生 ImageGen 重新组织流程。
- 不可直接移植内容：不采用 Amazon/A+ 规则、外部 API Key、自动重试或跨境广告平台配置；不把其固定尺寸、安全区、文字大小、转化提升百分比和行业预设当作国内平台事实。澄清轮数与完整度阈值不允许覆盖真实性或授权资料缺失；统一禁止 screenshot/app interface 的提示词不能误删用户提供的真实教育产品截图。用户提供的文案也必须接受广告合规检查。
- 安全观察：唯一两个下载脚本是 `skills/product-shots-image-gen/scripts/setup.sh` 和 `generate.py`，均仅静态阅读。setup.sh 会调用 pip 安装 requests/Pillow，并探测环境变量及主目录密钥文件；generate.py 会读取密钥、向外部网关发送提示词和参考图、对部分请求自动重试、下载响应图片并写文件。还会记录提示词片段和错误响应片段，不能据其“密钥不入日志”的注释推断业务资料不会外泄。未执行、未读取本机密钥、未调用该网关、未上传素材。

### 2. wonsukchoi/domain-experts：graphic-designer

- 许可证：根 [LICENSE](https://raw.githubusercontent.com/wonsukchoi/domain-experts/8392c1503d75ef2928c930cee195f1ada813ccc2/LICENSE)，MIT，Copyright (c) 2026 Wonsuk Choi and Domain Experts contributors。完整归档中目标目录未见独立的许可证覆盖说明或例外；根许可为该角色提炼提供依据。若后续复制实质性内容，保留版权和许可声明。
- 可借鉴内容：只在许可证允许时提炼字体层级、色彩对比、品牌一致性与生产认知。此快照具备 MIT 许可，可提炼上述方法，仍以原创中文教育电商语境撰写。
- 不可直接移植内容：不复制其案例中的品牌、数字、字体配对、生产默认值或“行业标准”作为硬性规则；不将网页对比度指标自动等同于所有商品图片的法定门槛。若后续文件许可证不明确，仅将其作为事实线索，重新依据 W3C、字体发布者和生产方等权威资料撰写。
- 安全观察：所选目录只有 Markdown，无 .sh/.py/.js 和符号链接。角色标注 maturity 为 draft，正文说明尚无直接从业者复核；其事实与示例需独立核验，不能把模型生成的职业叙述当作一手规范。仓库根的安装和自动化说明未执行。

### 3. anthropics/skills：frontend-design

- 许可证：根级 LICENSE **未找到**（检查完整提交归档，不能推断全仓库统一许可）；目标目录有 [skills/frontend-design/LICENSE.txt](https://raw.githubusercontent.com/anthropics/skills/683bc88e56f3e09ba94f7055977f3d3aa499f202/skills/frontend-design/LICENSE.txt)，Apache-2.0，SKILL.md 指向该文件。允许商业使用、修改和分发；分发衍生作品需附许可证、保留相关声明、标明修改，并按适用范围保留 NOTICE。许可不授予上游商标使用权。
- 根 README 指出仓库中某些文档 Skill 只是 source-available，因此不能因 frontend-design 的 Apache-2.0 而推广至其他目录。根 THIRD_PARTY_NOTICES.md 已保留；其中列示的软件组件不在本次选取的 frontend-design Markdown 中，不能误判整个选取内容受 GPL 许可。
- 可借鉴内容：只借鉴明确视觉方向、排版/色彩/布局与自检思想，以具体教育商品、真实中文内容、受众与商业任务驱动视觉选择。
- 不可直接移植内容：不复制网页代码工作流、CSS 实现、响应式或动画约束；不把英文行长、默认颜色、Web 字体审美或网页占位文案规则直接当作教育电商排版规则。尤其不能因其鼓励构思占位内容而虚构教师资质、教材封面、成绩或评价。
- 安全观察：所选技能目录仅 SKILL.md 和 LICENSE.txt，无脚本或符号链接；所有上游文本均作为研究资料，内含安装指令或角色指令不构成当前任务授权。

## 国内官方一手来源与支持规则

以下均于 **2026-10-07** 访问。法律、主管机关要求、平台历史通知和当前平台规则分别记录；不能用平台历史页面证明今天仍适用。

| 官方来源 | 本次取得状态 | 支持的设计/核验规则 |
| --- | --- | --- |
| 国家市场监督管理总局：[《中华人民共和国广告法》](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/fgs/art/2023/art_5474cf75173c45d6a0379730fb4e8d97.html)，2021 年修正，第二十四条 | 取得正文 | 教育培训广告不得承诺升学、考试通过或培训效果；不得暗示考试机构、工作人员、命题人员参与；不得利用科研、学术、教育机构、行业协会、专业人士或受益者作推荐证明。真实性/授权充足也不能解除这些禁限。教师介绍与学员内容须先判断是否构成推荐证明。 |
| 国家市场监督管理总局：[江苏省市场监管局发布教育培训违法广告典型案例](https://www.samr.gov.cn/zt/ndzt/2025n/ggf/alzs/art/2025/art_869d7d22c7b64a329ba5916bd172f2cc.html) | 取得正文 | 公务员培训暗示命题关系、音乐考级宣传通过率、虚构考官团队、保证高分进面均有执法案例；通过率和培训效果承诺、命题关系及虚构资质需检查。案例用于解释风险，不把罚款金额写作固定处罚结论；受益者推荐证明禁限依据上行法律条款。 |
| 教育部：[《全国校外教育培训监管与服务综合平台应用管理办法》通知](https://www.moe.gov.cn/srcsite/A29/202503/t20250326_1184786.html)，教监管〔2025〕1号 | 直接打开异常；官方域名搜索返回正文，已核对第三、七、十一条 | 适用范围为面向学龄前儿童和中小学生的规定培训活动；检查机构、课程、人员和办学许可信息的真实性与适用范围。全国平台展示、资金监管要求不能推广成所有成人题库、出版物或成人职业培训的统一要求；合规码牌不能自行伪造。 |
| 教育部：[《校外培训行政处罚暂行办法》](https://www.moe.gov.cn/srcsite/A02/s5911/moe_621/202309/t20230912_1079788.html)，教育部令第53号 | 官方搜索取得正文 | 作为适用范围、未经审批培训及违法广告监管的补充来源；设计输入先辨别商品是否属于受监管校外培训，不以美化包装掩盖缺失资质。 |
| 抖音电商学习中心：[关于《【本地生活及虚拟】行业管理规范》修订的公示通知（2022.6.16）](https://school.jinritemai.com/doudian/wap/article/aHWCaz2C6fkY) | 直接打开为动态页面；官方域名搜索取得通知正文 | 指定链接实际是 2022 年公示通知，涉及教育培训课程、商品信息与宣传规范。只作为规范定位和交付信息检查的历史线索；需交付前确认现行正式生效版本，不能称为当前独立“教育培训商品规范”。 |
| 抖音电商学习中心：[《【本地生活及虚拟】行业管理规范》（修订）公示通知（2021.11.11）](https://school.jinritemai.com/doudian/wap/article/aHKMDB9f6YPX) | 官方搜索取得正文；历史通知 | 教育商品信息包含课程形式、获取渠道、适用对象、安排、教材与售后等；宣传需明确学习方式，禁保证结果和命题关系话术。用于形成动态核验清单，不固定历史门槛或发布时间。 |

法规第二十四条是本 Skill 教育广告判断的一手依据；不以“有证据”“真实学员”“用户已授权”替代禁限检查。商品事实、服务边界、字体/图片/肖像授权仍需分别查验。

### 平台规则与尺寸的动态核验

抖音指定历史通知 7.2.3 指向《「教育培训类商品」宣传规范》，但本次尚未获得该独立规范的当前官方正文与生效状态；不得据二手转载填入其现行条款。正式交付前在官方规则中心或商家后台重新查验商品类目、准入资质、商品信息、宣传规范和投放规则，记录页面标题、版本/生效日期、访问日期、URL 与适用场景；无法核实则保留待确认项，不标记为可发布。

淘宝/天猫、京东、拼多多、抖音电商、小红书的主图、详情页、活动图尺寸、安全区、文件格式/体积及文案限制，本次均只记录为 **“交付前动态核验”**。不把上游跨境尺寸、历史通知或一次搜索结果永久写成绝对值。商品详情、内容推广和付费广告分别核验，不互相替代。

## 本次审查结论

- 三个目标快照都包含目标 SKILL.md；product-shots 五个子技能齐全，domain-experts 的角色参考文件齐全，frontend-design 的目录级许可证齐全。
- MIT、MIT、Apache-2.0 许可均有实际文件依据；Anthropic 根许可证缺失已明确记录，没有推断许可。
- 下载的两个脚本仅阅读，所有上游安装/API/发布指令未执行；没有将图库或外部素材带入成品。
- 后续 Task 3–6 使用本审查限定的方法与官方来源定位，原创撰写参考文件；如复制实质性许可内容，另行保留要求的声明。
- 剩余动态项：抖音现行教育培训独立宣传规范和各平台尺寸须交付前核验；本审查不声称完成未来具体成品的法律、平台或素材授权审查。
