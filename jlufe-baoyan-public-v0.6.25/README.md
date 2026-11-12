# 吉林财经大学保研 Skill

面向吉林财经大学统计与数据科学学院本科生的推免资料和工作流程。公开版 v0.6.25 覆盖七个专业／方向，按入学级别区分原统计学院、原应用数学学院与合并后待定规则。外校部分维护 19 个院校及科研院所入口，涵盖统计、应用统计、数学及有案例支撑的跨专业方向。校内政策、课程和各外校条目的核验日期见对应参考页，办理以学校和接收院系当届公告为准。

[使用方法、各平台接入和版本记录](jlufe-baoyan/read.md) · [普通对话版指令](CHAT-PROMPT.md)

- 校内资格、课程均分、附加分、名额、申报及执行口径待核 [统数学院政策](jlufe-baoyan/references/statistics-policy.md)
- 历年校院通知、表格直链、附件可读状态和吉财研究生接收章程 [历年通知与附件索引](jlufe-baoyan/references/jlufe-notice-index.md)
- 课程名称、模块学分和逐课表缺口 [培养方案资料](jlufe-baoyan/references/statistics-curricula.md)
- 外校相关专业、批次、门槛和官网来源 [19 个院校及科研院所入口](jlufe-baoyan/references/target-programmes.md)
- 英语、排名、竞赛科研、简历及联系导师 [外校准备](jlufe-baoyan/references/statistics-application-planning.md)
- 推免简历、个人陈述、推荐信、自我介绍、研究计划、导师邮件和面试 PPT 提纲 [文书模板索引](jlufe-baoyan/references/application-documents.md)

## 在智能体中使用

支持 ZIP 导入的客户端可从仓库 Releases 下载并导入 jlufe-baoyan-skill-v0.6.25.zip。手动安装时保留完整的 Skill 目录。普通对话可粘贴对话指令并上传相关参考页。 [各客户端接入说明](jlufe-baoyan/read.md)

可以这样提问。

> 使用 jlufe-baoyan。我是吉财2024级金融数学学生，想申请东北师范大学统计学方向。先分别核对校内适用规则和外校项目，再列出应查的当届文件及我需要补充的材料。

> 使用 jlufe-baoyan。我准备申请应用统计，请根据我提供的脱敏经历改写一页简历，把排名口径和待核信息另列。

## 理论必修均分复算

登录吉财教务系统，核对本人教学计划、学分和初修成绩，逐门填写后交给 Skill 复算。通识必修、学科必修、专业必修只计其中的理论课。 [逐课填报表](jlufe-baoyan/assets/theoretical-course-records.md)

在仓库根目录运行 `python jlufe-baoyan/scripts/weighted_average.py jlufe-baoyan/assets/course-input.example.json`。示例使用合成数据，输出均分 84.0000。实际数据按个人成绩单和对应年级培养方案标记，详见 [复算说明](jlufe-baoyan/references/course-calculation.md)。

## 资料与许可

从 v0.6.18 起，本项目原创内容采用 **PolyForm Noncommercial License 1.0.0**，源码可查阅，商业使用需另获授权。已经按 MIT 授权获得的旧版副本适用其原许可。学校公告、第三方资料和引用内容按原权利状态处理。个人材料应保存在自己的工作区。 [LICENSE](LICENSE) · [NOTICE](NOTICE)
