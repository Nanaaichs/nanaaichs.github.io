---
layout: page
title: About
permalink: /about/
description: About, education, technical skills, and external links.
---
{% assign profile = site.data.profile %}
<p class="eyebrow">About</p>
<h1>About Me</h1>
<p class="lead">{{ profile.bio }}</p>

<h2>Education</h2>
<div class="stack-list compact-list">
{% for education in site.data.education %}
  <article class="list-item">
    <p class="meta">{{ education.period }}</p>
    <h3>{{ education.degree }}{% if education.field != "" %} in {{ education.field }}{% endif %}</h3>
    <p><strong>{{ education.institution }}</strong>{% if education.location %} · {{ education.location }}{% endif %}</p>
    <p>{{ education.description }}</p>
    {% if education.advisor != "" %}<p><strong>Advisor:</strong> {{ education.advisor }}</p>{% endif %}
    {% if education.thesis != "" %}<p><strong>Thesis:</strong> {{ education.thesis }}</p>{% endif %}
  </article>
{% endfor %}
</div>

<h2>Technical Skills</h2>
<div class="skill-grid">
{% for group in site.data.skills %}
  <section class="skill-group">
    <h3>{{ group.category }}</h3>
    <div class="tag-row">{% for item in group.items %}<span class="tag">{{ item }}</span>{% endfor %}</div>
  </section>
{% endfor %}
</div>

<h2>Links</h2>
<ul class="plain-list">
{% for link in site.data.links %}
  {% if link.enabled %}<li><a href="{{ link.url }}">{{ link.name }}</a></li>{% endif %}
{% endfor %}
</ul>
