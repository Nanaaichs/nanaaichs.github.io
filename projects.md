---
layout: page
title: Projects
permalink: /projects/
description: Selected research, engineering, and software projects.
---
<p class="eyebrow">Portfolio</p>
<h1>Projects</h1>
<p class="lead">Selected research, engineering, and software projects. Each project page records the problem, my contribution, implementation, and evidence.</p>

{% assign sorted_projects = site.projects | sort: "order" %}
<div class="card-grid">
{% for project in sorted_projects %}
  <article class="card project-card">
    <p class="meta">{{ project.category }} · {{ project.period }} · {{ project.status }}</p>
    <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
    <p>{{ project.summary }}</p>
    <div class="tag-row">{% for tech in project.technologies %}<span class="tag">{{ tech }}</span>{% endfor %}</div>
    <p class="card-link"><a href="{{ project.url | relative_url }}">View Project →</a></p>
  </article>
{% endfor %}
</div>
