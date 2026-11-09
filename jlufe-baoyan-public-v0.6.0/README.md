# 吉林财经大学保研 Skill

面向吉林财经大学统计与数据科学学院本科生的推免资料和工作流程。公开版 v0.6.0 覆盖七个专业／方向，按入学级别区分原统计学院、原应用数学学院与合并后待定规则。外校部分只维护已收录的 17 所院校及统计、应用统计、数学和直接相关方向。核验日期为 2026-11-10，资料由个人整理，正式办理以学校和接收院系当届公告为准。

- 校内资格、课程均分、附加分、名额与申报 [统数学院政策](jlufe-baoyan/references/statistics-policy.md)
- 课程名称、模块学分和逐课表缺口 [培养方案资料](jlufe-baoyan/references/statistics-curricula.md)
- 外校相关专业、批次、门槛和官网来源 [17 所院校索引](jlufe-baoyan/references/target-programmes.md)
- 英语、排名、竞赛科研、简历及联系导师 [外校准备](jlufe-baoyan/references/statistics-application-planning.md)

## 在智能体中使用

下载仓库后保留完整的 [`jlufe-baoyan/`](jlufe-baoyan/SKILL.md) 文件夹。它包含标准 Agent Skills 入口、按需读取的参考资料和可选的 Python 均分脚本。安装位置按宿主选择。

| 宿主 | 使用方式 |
|---|---|
| Codex／ChatGPT 桌面 | 将 `jlufe-baoyan/` 复制到项目的 `.agents/skills/`。在 Codex 用 `$jlufe-baoyan`，在提供 Skill 选择的 ChatGPT 界面按其选择器调用。 [OpenAI Skills 文档](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | 将文件夹复制到 `.claude/skills/` 后调用 `/jlufe-baoyan`。 [Claude Code Skills](https://code.claude.com/docs/en/skills) |
| Claude 网页 | 账号支持自定义 Skills 时，在 Customize 的 Skills 页面上传包含整个 `jlufe-baoyan/` 文件夹的 ZIP。 [Claude 官方上传说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude) |
| DeepSeek Harness | 将文件夹复制到项目的 `.agents/skills/`，在对话中明确要求使用 `jlufe-baoyan`。 [DeepSeek Harness 技能文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) |
| Kimi Code | 将文件夹复制到项目的 `.agents/skills/` 后用 `/skill:jlufe-baoyan`。 [Kimi Code 技能文档](https://moonshotai.github.io/kimi-cli/en/customization/skills.html) |
| 普通对话里的 GPT、Claude、DeepSeek、Kimi、豆包 | 粘贴 [对话版指令](CHAT-PROMPT.md)，再上传或粘贴本次问题涉及的参考文件。具备联网功能时可提供原公告链接。 |
| 豆包工作 | 可先使用对话版。原生分发通过开放平台，按其企业认证、资源包和审核流程接入。 [豆包 Skill 接入指南](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide) |

兼容路径依据宿主官方文档。文件、联网、脚本执行和自动触发取决于实际客户端与账户权限。纯对话可手工复算并列出纳入学分和加权积。 [Agent Skills 规范](https://agentskills.io/specification)

可以这样提问。

> 使用 jlufe-baoyan。我是吉财2024级金融数学学生，想申请东北师范大学统计学方向。先分别核对校内适用规则和外校项目，再列出应查的当届文件及我需要补充的材料。

## 本地复算

在仓库根目录运行 `python jlufe-baoyan/scripts/weighted_average.py jlufe-baoyan/assets/course-input.example.json`。示例使用合成数据，输出均分 84.0000。实际数据按个人成绩单和对应年级培养方案标记，详见 [复算说明](jlufe-baoyan/references/course-calculation.md)。

## 资料与许可

本项目的原创脚本及说明采用 [MIT 许可证](LICENSE)。所引用的学校公告和第三方资料由原发布方提供，公开版收录原创摘要、来源和核验状态。个人材料应保存在自己的工作区。逐课培养方案、部分当届院级附件及原统计名额选拔次序仍待核对。
