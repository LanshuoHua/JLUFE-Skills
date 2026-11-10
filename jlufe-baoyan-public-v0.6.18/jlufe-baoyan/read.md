# 吉林财经大学保研 Skill 使用与版本记录

当前版本 **v0.6.18**。面向吉林财经大学统计与数据科学学院本科生，覆盖七个专业或方向，维护指定的 17 所外校项目。政策与办理经验按来源和适用届别区分，实际报名以当届公告及办理单位答复为准。

## 使用方法

1. 下载独立 Skill ZIP 并解压。保留完整的 `jlufe-baoyan/` 文件夹，使 `SKILL.md`、`references/`、`scripts/` 和 `assets/` 保持原相对路径。有旧安装时，替换完整目录或在宿主中重新上传 ZIP，然后确认 `SKILL.md` 版本。 [Skill 入口](SKILL.md)
2. 提问时提供入学年、学籍专业和当前要处理的阶段。查院校时补充目标学校、院系、专业和招生年度。需要测算时，再提供相关排名、成绩和脱敏材料。 [个人信息模板](assets/profile-and-evidence.md)
3. 校内资格、加分、名额和截止日期从统数学院政策及历年通知查起。查外校时先从项目索引进入具体院校，再核对对应批次。需要复算理论必修均分时，先确认课程范围和学分。 [统数学院政策](references/statistics-policy.md) · [历年通知](references/jlufe-notice-index.md) · [外校项目](references/target-programmes.md) · [复算说明](references/course-calculation.md)

> 使用 jlufe-baoyan。我是吉财 2024 级金融数学学生，想申请东北师范大学统计学。请分别核对校内适用规则和目标项目，列出已知条件、待查的当届文件和需要我补充的材料。

## 接入各家模型和客户端

以下是按官方文档核对的接入路径。Skill 的发现、文件读取、联网和 Python 运行取决于宿主及账号权限。安装后先让宿主打开 `references/statistics-policy.md`，并回答一次带入学年和专业的问题，检查参考文件可读、届别判断正确。

| 客户端 | 安装与调用 |
|---|---|
| **OpenAI Codex 桌面、CLI 或 IDE** | 把解压后的文件夹放到项目的 `.agents/skills/jlufe-baoyan/`。在 Codex 中用 `$jlufe-baoyan`，CLI 或 IDE 也可用 `/skills` 选择。桌面侧栏的 Skills 可查看已识别技能。 [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills) |
| **ChatGPT 桌面、网页或移动端** | 在已有的 Skill 或插件提供该技能时，用 `@` 选择。OpenAI 文档将独立 Skill 列为桌面、Codex CLI 和 IDE 功能，网页与移动端可使用已安装插件中提供的技能。普通对话使用下方方式。 [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills) |
| **Claude 网页** | 账号有自定义 Skills 时，在 Settings 的 Capabilities 开启代码执行和文件创建，再进入 Customize → Skills → 创建 Skill → Upload a skill，上传独立 ZIP。团队账号的开关由管理员管理。 [Claude 官方帮助](https://support.claude.com/en/articles/12512180-use-skills-in-claude) |
| **Claude Code** | 把文件夹放到项目的 `.claude/skills/jlufe-baoyan/`，输入 `/jlufe-baoyan` 调用。 [Claude Code 文档](https://code.claude.com/docs/en/skills) |
| **DeepSeek Harness** | 把文件夹放到项目根的 `.agents/skills/` 或 `.dsh/skills/`。在 Harness 中输入 `/` 选择技能，或输入 `/jlufe-baoyan`。使用普通 DeepSeek 对话时可按下方方式提供文件。 [目录规则](https://deepseek-harness.github.io/deepseek-harness/reference/subsystems/skills) · [调用方式](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/client/ui-skill/README.md) |
| **Kimi Agent、Kimi Work** | Kimi Agent 中用 `/` 或输入框旁的 `+` 选择已安装技能。Kimi Work 桌面支持上传本地 ZIP，优先上传完整独立包。通过链接安装时，使用已发布且可访问的技能地址。 [Kimi 技能](https://www.kimi.com/features/skills) · [Kimi 帮助](https://www.kimi.com/help/plugins-and-skills/use-skills-in-agent) |
| **Kimi Code CLI** | 把文件夹放到项目的 `.agents/skills/jlufe-baoyan/`，输入 `/skill:jlufe-baoyan`。 [Kimi Code 文档](https://moonshotai.github.io/kimi-cli/en/customization/skills.html) |
| **豆包工作** | 在侧栏的「技能·连接器·伙伴」打开技能页，选择导入本地技能文件，再从输入框的「更多技能」调用。以当前客户端校验结果为准。通过豆包开放平台公开上架另有企业认证、资源格式和审核要求。 [豆包工作官方产品说明](https://www.feishu.cn/content/article/7677519271848610746) · [豆包开放平台指南](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide) |

### 普通对话或自建智能体

1. 上传 [SKILL.md](SKILL.md)，或将其正文粘贴进对话。按任务再上传相关参考页。查吉财校内规则时可用 [统数学院政策](references/statistics-policy.md)。查东北师大时可用 [外校第一组](references/targets/a.md) 和 [外校准备](references/statistics-application-planning.md)。
2. 告诉模型「按这些文件回答，区分校内推荐和外校接收，列出适用届别、出处和待核事项」。仓库版另提供 `CHAT-PROMPT.md`。普通对话无法读取相对路径时，把需要的引用文件一并上传或粘贴。
3. 自建智能体可以把 `SKILL.md` 作为工作指令，并按需检索本地参考文件。使用脚本时，在自己的 Python 环境运行。OpenAI Responses API 也提供上传 Skill ZIP 后在 Shell 工具环境引用技能 ID 的入口。 [OpenAI API Skills](https://developers.openai.com/api/docs/guides/tools-skills)

在解压后的 `jlufe-baoyan/` 内运行下列命令，可以用合成数据复算。示例均分为 `84.0000`。 [复算说明](references/course-calculation.md)

```powershell
python scripts/weighted_average.py assets/course-input.example.json
```

## 版本记录

按已存档的 Skill 包和修订记录整理。早期条目说明当时的改动，现行口径看最新政策页。每次发版同步补一条记录，并核对 `SKILL.md`、仓库 README 和 ZIP 中的版本号。

| 版本 | 本版更新 |
|---|---|
| v0.6.18 | 补东师 2027 年应用统计候补在研招网待录取开放后按顺序电话通知的流程。新增使用与接入说明、逐版变更记录和非商业许可。 |
| v0.6.17 | 澄清东师只有一轮预推免综合考核，考核后的第一批为拟录取，第二、第三批为候补。 |
| v0.6.16 | 新增东师 2027 年应用统计考核案例，分别记录官网要求、纸质承诺书和抽题等实操。 |
| v0.6.15 | 补专业排名证明所列字段，记录专业总人数和本人名次，课程范围另核。 |
| v0.6.14 | 补排名证明随成绩公布更新的时点，以及套磁、夏令营通常先用五学期排名。 |
| v0.6.13 | 补向学院教学秘书登记排名证明、向学校教务处开全课程成绩单的办理路径。 |
| v0.6.12 | 补原统计班级名额空缺暂无已知先例的记录，空缺去向单列待核。 |
| v0.6.11 | 明确 2028 届及以前两原院各自按本院同届最高原始总分折算，补原统计共同一作以署名第一位为准。 |
| v0.6.10 | 补原统计两篇不同论文逐篇获认定后可累加原始分，以及适用期刊目录和学生第一作者要求。 |
| v0.6.9 | 明确不同赛事、不同作品逐项按各自团队人数均分后累计，队内排序差异赋分记为可能调整。 |
| v0.6.8 | 补同一项竞赛只计最高获奖成绩，适用于不同作品或跨年获奖。 |
| v0.6.7 | 收录数模和市调分别以不同作品获奖、均经认定时可累计的案例。 |
| v0.6.6 | 补统数学院报名截止即材料收件截止，要求按时提交获奖证书或学院认可的证明。 |
| v0.6.5 | 记录原统计班级名额线同分暂无已知先例，实际同分时核对学院正式名次。 |
| v0.6.4 | 确认原统计先选班级名额，再按剩余合格报名者的综合成绩分配年级余数。 |
| v0.6.3 | 补班级前 25% 的执行口径，以及 39 人无并列时第 10 名可通过排名门槛的例子。 |
| v0.6.2 | 新增校内执行口径待核清单和外校补件、复试、候补案例的收录方法。 |
| v0.6.1 | 整合校院历年通知、附件状态、空表入口与吉财研究生接收章程。 |
| v0.6.0 | 整理指定 17 所外校的项目与来源索引，发布面向多家智能体的源码包、独立 Skill ZIP 与对话指令。 |
| v0.5.1 | 校准校内外语门槛、外校申请并行时间线及公告时点，补金融数学资料缺口和厦大统计学夏令营条件。 |
| v0.5.0 | 新增英语与排名档位、科研竞赛、简历、导师联系和分阶段准备，补原应用数学推免东师公开个案。 |
| v0.4.4 | 新增原统计和原应用数学的历年推免去向，区分用户观察与公开个案。 |
| v0.4.3 | 区分全部必修初修资格与理论必修均分，更新课程复算说明和示例。 |
| v0.4.2 | 修订 40 人保底的用途，明确 2027 届 17 人为合并学院总额，当时暂列两种选拔顺序。 |
| v0.4.1 | 明确当时名额初稿的班内排序也使用推免综合成绩，细化 2027 届示例。 |
| v0.4.0 | 补齐七专业旧院分流与 2025 级起备考参考，首次整理 40 人组及 2027 届名额初稿。 |
| v0.3.0 | 新增统数专项政策和原始材料索引，整理原统计 2027 届附加分及折算办法。 |
| v0.2.0 | 新增统数七专业及方向培养方案索引，整理可取得的课程名称、模块学分和逐课缺口。 |
| v0.1.0 | 建立校级和学院政策、外校申请流程及课程学分加权复算工具。 |

## 许可与来源

从 v0.6.18 起，公开发布的原创 Skill 指令、说明、摘要、模板、脚本及对话指令采用 **PolyForm Noncommercial License 1.0.0**。源码可查阅，授权用途及分发条件以许可正文为准。商业使用需另获授权，分发时随附许可正文或官方链接及项目版权通知。 [LICENSE](LICENSE) · [NOTICE](NOTICE) · [许可原文](https://polyformproject.org/licenses/noncommercial/1.0.0)

已经按 MIT 授权获得的旧版副本继续按其原许可处理。学校公告、第三方资料及引用内容按原权利状态处理。 [MIT 许可原文](https://opensource.org/license/mit)
