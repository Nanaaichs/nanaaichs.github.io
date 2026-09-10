---
layout: page
title: Research
permalink: /research/
description: Research directions in satellite communications, 5G NR NTN, and physical-layer signal processing.
---
<p class="eyebrow">Research</p>
<h1>Research</h1>
<p class="lead">My research centers on satellite communications, 5G NR Non-Terrestrial Networks, and physical-layer receiver design.</p>

{% assign sorted_research = site.data.research | sort: "order" %}
<div class="stack-list large-gap">
{% for item in sorted_research %}
  <article class="research-block">
    <h2>{{ item.title }}</h2>
    <p>{{ item.summary }}</p>
    {% if item.topics %}<ul>{% for topic in item.topics %}<li>{{ topic }}</li>{% endfor %}</ul>{% endif %}
  </article>
{% endfor %}
</div>
