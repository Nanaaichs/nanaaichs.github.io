# 个人主页维护手册

## 1. 部署这套版本前

如果现有仓库里还存在旧结构，请先备份，然后删除会冲突的旧文件：

- 旧的 `index.html`（本版本使用 `index.md`）
- 旧的 `_data/projects.yml`（本版本使用 `_projects/` Collection）
- 任何与本压缩包同名但内容不同的旧 Layout / Include

GitHub Pages 设置保持：`main` 分支 + `/(root)`。

## 2. 日常维护对应关系

| 要更新的内容 | 只需要改哪里 |
| --- | --- |
| 姓名、身份、学校、简介 | `_data/profile.yml` |
| 研究方向 | `_data/research.yml` |
| 教育经历 | `_data/education.yml` |
| 科研/实习/工作经历 | `_data/experience.yml` |
| 技术栈 | `_data/skills.yml` |
| 外部链接、CV入口 | `_data/links.yml` |
| 新项目 | `_projects/新项目.md` |
| 论文 | `_data/publications.yml` |
| 奖项 | `_data/awards.yml` |
| 博客/技术文章 | `_posts/YYYY-MM-DD-slug.md` |
| 网站导航 | `_data/navigation.yml` |
| 视觉样式 | `assets/css/style.css` |

原则：同一项事实只维护一次，不要在多个页面重复手写。

## 3. 新增项目

复制 `templates/project-template.md` 到：

`_projects/项目英文slug.md`

例如：

`_projects/leo-channel-prediction.md`

重点维护：

- `summary`：一句话解释项目价值
- `problem`（正文）：解决什么问题
- `My Contribution`：你本人具体做了什么
- `technologies`：实际使用过的技术
- `outcomes`：结果、交付物、性能、论文、代码等
- `links`：公开 GitHub / Demo / Report

`featured: true` 会让项目自动出现在首页。

## 4. 新增论文

在 `_data/publications.yml` 中添加一条。第一次添加时，把文件里的 `[]` 替换为条目列表。

模板见 `templates/publication-template.yml`。

状态必须真实区分：

- Published
- Accepted
- Under Review
- Submitted
- In Preparation

公开主页不要把 Under Review / Submitted 写成已发表成果。

如果论文属于某个项目，在 `project_ids` 中写项目 `id`；同时可在对应 `_projects/*.md` 的 `related_publications` 中写论文 id。

## 5. 新增奖项

在 `_data/awards.yml` 中添加一条，模板见 `templates/award-template.yml`。

建议内部维护：

- 奖项名称
- 组织方
- 年份
- 级别
- 排名（如适用）
- 关联项目
- 公开证据链接

公开仓库不要上传未脱敏的身份证件、证书编号、家庭住址等敏感信息。

## 6. 新增博客文章

创建：

`_posts/YYYY-MM-DD-英文slug.md`

例如：

`_posts/2026-10-01-understanding-nr-ntn.md`

使用 `templates/post-template.md` 的 Front Matter。提交后，文章会自动出现在 `/writing/`，最新文章也会自动进入首页。

## 7. 更新技术栈

只改 `_data/skills.yml`。

不建议写“精通 / 95% / 五星”等主观等级。更好的维护方式是：技术栈负责列能力，项目页负责提供实际使用证据。

## 8. 更新 CV

把公开版 CV 放到：

`assets/pdf/cv.pdf`

然后把 `_data/links.yml` 中 CV 的：

`enabled: false`

改为：

`enabled: true`

CV 必须是适合公开的版本。

## 9. 项目、论文、奖项之间的关联

本版本预留了 id 关联：

- Project：`_projects/*.md` 中的 `id`
- Publication：`_data/publications.yml` 中的 `id`
- Award：`_data/awards.yml` 中的 `id`

例如：

Project `leo-ntn-access`
→ Publication `ntn-sync-2027`
→ Award `competition-2027`

项目详情页会根据 `related_publications` / `related_awards` 自动显示关联成果。

## 10. 推荐维护节奏

每完成一项成果就立即更新，不要等到评奖或求职前再补历史。

建议至少：

- 项目阶段性结果：随时更新
- 论文状态变化：立即更新
- 奖项：获奖后立即更新
- 技术栈：真正用于项目后再加入
- CV：每 2–3 个月或重要成果后更新
- 首页 Featured Projects：每半年检查一次

## 11. GitHub 网页端维护

小改动可以直接：

`仓库 → 文件 → Edit → Commit changes`

较大修改建议本地 Clone 后用 VS Code 编辑，再：

```bash
git add .
git commit -m "Update portfolio content"
git push
```

GitHub Pages 通常会自动重新部署。部署状态在 `Actions` 中查看。

## 12. 可选：本地预览

如果以后希望在提交前本地预览，需要安装 Ruby/Bundler，然后在仓库目录：

```bash
bundle install
bundle exec jekyll serve
```

浏览器打开 Jekyll 提示的本地地址即可。这个步骤不是日常维护的必需条件。

## 13. 求职 / 评奖时如何使用

这套站点的数据结构有三个目标：

1. 主页：30 秒快速了解你是谁、研究什么、做过什么。
2. 详情页：项目、论文、奖项均可继续追溯到证据。
3. 数据源：未来制作中文简历、英文 Resume、Academic CV、评奖材料时，从 `_data/` 与 `_projects/` 抽取，不再靠记忆重新整理。

优先维护“事实 + 个人贡献 + 结果 + 证据”，少维护空泛形容词。
