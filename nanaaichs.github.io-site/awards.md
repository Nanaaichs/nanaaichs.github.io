---
layout: page
title: Awards
permalink: /awards/
description: Awards, scholarships, competition honors, and recognition.
---
<p class="eyebrow">Recognition</p>
<h1>Awards & Honors</h1>
<p class="lead">Awards, scholarships, competition honors, and other recognition. Public entries should contain only information suitable for disclosure.</p>

{% if site.data.awards == empty %}
<p class="empty-state">Awards will be added here. Use <code>_data/awards.yml</code> for structured maintenance.</p>
{% else %}
<div class="stack-list">
{% assign sorted_awards = site.data.awards | sort: "year" | reverse %}
{% for award in sorted_awards %}
  <article class="list-item">
    <p class="meta">{{ award.year }}{% if award.level %} · {{ award.level }}{% endif %}{% if award.ranking != "" %} · {{ award.ranking }}{% endif %}</p>
    <h2>{{ award.title }}</h2>
    <p>{{ award.organization }}</p>
    {% if award.description %}<p>{{ award.description }}</p>{% endif %}
  </article>
{% endfor %}
</div>
{% endif %}
