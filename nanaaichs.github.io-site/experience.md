---
layout: page
title: Experience
permalink: /experience/
description: Research, engineering, internship, teaching, and professional experience.
---
<p class="eyebrow">Experience</p>
<h1>Experience</h1>
<p class="lead">Research, engineering, internship, teaching, leadership, and professional experience.</p>

<div class="stack-list large-gap">
{% for experience in site.data.experience %}
  <article class="timeline-item">
    <p class="meta">{{ experience.type }}{% if experience.period %} · {{ experience.period }}{% endif %}</p>
    <h2>{{ experience.title }}</h2>
    <p><strong>{{ experience.organization }}</strong>{% if experience.location %} · {{ experience.location }}{% endif %}</p>
    <p>{{ experience.summary }}</p>
    {% if experience.responsibilities %}<ul>{% for item in experience.responsibilities %}<li>{{ item }}</li>{% endfor %}</ul>{% endif %}
  </article>
{% endfor %}
</div>
