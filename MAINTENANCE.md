# 中英文双语个人主页维护手册

## 1. 网站结构

本版本使用同一个 GitHub Pages 仓库维护中英文两套展示：

- 英文首页：`https://nanaaichs.github.io/`
- 中文首页：`https://nanaaichs.github.io/zh/`

导航栏右侧提供 `中文 / EN` 切换。同一项结构化履历数据只维护一份，中英文通过同一 YAML 条目的 `en` / `zh` 字段读取。

## 2. 部署

把本压缩包内容放到 `nanaaichs.github.io` 仓库根目录。GitHub Pages 保持：

`Settings → Pages → Deploy from a branch → main → /(root)`

如果旧仓库还存在旧版 `_data/projects.yml`、旧 `_projects/*.md` 或旧 Layout，请以本版本为准覆盖。建议先备份旧仓库。

## 3. 日常维护表

| 内容 | 维护文件 |
| --- | --- |
| 姓名、身份、学校、简介 | `_data/profile.yml` |
| 研究方向 | `_data/research.yml` |
| 教育经历 | `_data/education.yml` |
| 科研 / 实习 / 工作经历 | `_data/experience.yml` |
| 技术栈 | `_data/skills.yml` |
| 项目内容 | `_data/projects.yml` |
| 论文 | `_data/publications.yml` |
| 奖项 | `_data/awards.yml` |
| GitHub / Scholar / ORCID / CV | `_data/links.yml` |
| 中英文导航名称 | `_data/navigation.yml` |
| 英文文章 | `_posts/` 中 `lang: en` 的文章 |
| 中文文章 | `_posts/` 中 `lang: zh` 的文章 |
| 页面文字标签 | `_data/ui.yml` |
| 样式 | `assets/css/style.css` |

## 4. 双语数据怎么写

例如个人简介：

```yaml
headline:
  en: Satellite Communications · 5G NR NTN · Physical Layer
  zh: 卫星通信 · 5G NR NTN · 物理层
```

以后修改这一个条目，英文与中文页面会同步读取各自字段。

原则：**事实只维护一次，语言分别写在同一个数据项内。**

## 5. 新增项目

项目真正的数据只写在 `_data/projects.yml`。复制 `templates/project-data-template.yml` 的结构，在列表末尾新增一项。

除了数据条目，还需要两个很薄的“路由文件”，它们不存项目内容，只负责生成中英文 URL：

- `_projects/<slug>-en.md`
- `_projects/<slug>-zh.md`

可复制 `templates/project-route-en.md` 和 `templates/project-route-zh.md`，把 `PROJECT_ID`、`PROJECT_SLUG` 替换掉即可。

也可以运行：

```bash
python scripts/new_project_routes.py PROJECT_ID PROJECT_SLUG
```

例如：

```bash
python scripts/new_project_routes.py leo-channel-prediction leo-channel-prediction
```

`featured: true` 会让项目自动出现在中英文首页的代表项目区域。

## 6. 新增论文

在 `_data/publications.yml` 添加一条。中英文标题、类型、状态使用双语字段；作者、期刊名、DOI 等通常无需翻译。

模板：`templates/publication-template.yml`

论文状态必须真实区分：

- Published / 已发表
- Accepted / 已录用
- Under Review / 审稿中
- Submitted / 已投稿
- In Preparation / 准备中

## 7. 新增奖项

在 `_data/awards.yml` 添加一条，模板见 `templates/award-template.yml`。

建议维护名称、组织方、年份、级别、排名、关联项目和公开证据。公开仓库不要放未脱敏证书编号、身份证件、家庭住址等敏感信息。

## 8. 新增经历

在 `_data/experience.yml` 增加条目。中英文标题、组织、类型、地点、简介、职责均写在同一条记录中。

模板：`templates/experience-template.yml`

## 9. 技术栈

只改 `_data/skills.yml`。不建议使用“精通”“95%”“五星”等主观等级；项目详情负责证明技术实际用在哪里。

## 10. 博客 / Writing

博客与履历数据不同，**不要求中英文强制一一翻译**。

英文文章模板：`templates/post-template-en.md`

中文文章模板：`templates/post-template-zh.md`

英文文章示例 Front Matter：

```yaml
lang: en
permalink: /writing/2026/10/01/example/
```

中文文章：

```yaml
lang: zh
permalink: /zh/writing/2026/10/01/example/
```

如果一篇文章确实有对应翻译，可在两篇文章中分别写 `alternate_url`，导航栏的语言按钮就会直接跳到对应译文；没有译文时，语言按钮默认回到另一语言首页。

## 11. CV 与外部链接

把公开版 CV 放到 `assets/pdf/cv.pdf`，再把 `_data/links.yml` 中 CV 的 `enabled` 改为 `true`。

Google Scholar、ORCID 等同理。链接本身只维护一次，名称可中英文分别显示。

## 12. 项目、论文、奖项关联

项目使用 `id`；论文和奖项也使用 `id`。项目数据中的：

- `related_publications`
- `related_awards`

可以写对应 id。项目详情页会自动读取并以当前语言显示关联成果。

## 13. 页面文件为什么有两套，但数据没有两套

例如：

- `projects.md`：英文项目总览路由
- `zh/projects.md`：中文项目总览路由

它们几乎只有 Front Matter，真正项目内容都来自同一个 `_data/projects.yml`。

因此新增或修改项目正文时，不需要维护两份页面内容。

## 14. 推荐维护节奏

- 新项目阶段性成果：及时更新
- 论文状态变化：立即更新
- 奖项：获奖后立即更新
- 技术栈：真正用于项目以后再加入
- CV：重要成果后更新，或每 2–3 个月检查一次
- 中英文关键履历字段：尽量同时补齐
- 博客：按内容需要选择中文、英文或双语

## 15. GitHub 网页端与本地维护

小改动可以直接在 GitHub 网页：`文件 → Edit → Commit changes`。

较大修改建议 Clone 后用 VS Code：

```bash
git add .
git commit -m "Update bilingual portfolio"
git push
```

部署状态在 GitHub `Actions` 中查看。

## 16. 本地预览（可选）

安装 Ruby / Bundler 后：

```bash
bundle install
bundle exec jekyll serve
```

然后打开 Jekyll 给出的本地地址。日常使用 GitHub 网页维护时，这一步不是必需的。
