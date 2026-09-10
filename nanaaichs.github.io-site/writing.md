---
layout: page
title: Writing
permalink: /writing/
description: Technical articles, research notes, tutorials, and industry analysis.
---
<p class="eyebrow">Knowledge Base</p>
<h1>Writing</h1>
<p class="lead">Technical articles, research notes, tutorials, and industry analysis.</p>

{% if site.posts == empty %}
<p class="empty-state">No public articles yet. Add a Markdown file under <code>_posts/</code> to publish one.</p>
{% else %}
<div class="stack-list">
{% for post in site.posts %}
  <article class="list-item">
    <p class="meta">{{ post.date | date: "%Y-%m-%d" }}{% if post.category %} · {{ post.category }}{% endif %}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.summary %}<p>{{ post.summary }}</p>{% else %}<p>{{ post.excerpt | strip_html | truncate: 220 }}</p>{% endif %}
  </article>
{% endfor %}
</div>
{% endif %}
