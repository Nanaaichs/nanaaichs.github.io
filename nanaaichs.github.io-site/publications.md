---
layout: page
title: Publications
permalink: /publications/
description: Journal, letter, conference, patent, and other academic outputs.
---
<p class="eyebrow">Academic Output</p>
<h1>Publications</h1>
<p class="lead">Journal articles, letters, conference papers, patents, and other academic outputs are maintained here with their actual status.</p>

{% if site.data.publications == empty %}
<p class="empty-state">Publication records will be added here. Use <code>_data/publications.yml</code> as the single source of truth.</p>
{% else %}
<div class="stack-list">
{% assign sorted_publications = site.data.publications | sort: "year" | reverse %}
{% for publication in sorted_publications %}
  <article class="list-item publication-item">
    <p class="meta">{{ publication.type }} · {{ publication.year }} · {{ publication.status }}</p>
    <h2>{{ publication.title }}</h2>
    <p>{{ publication.authors }}</p>
    <p><em>{{ publication.venue }}</em></p>
    <p class="link-row">
      {% if publication.doi != "" %}<a href="{{ publication.doi }}">DOI</a>{% endif %}
      {% if publication.pdf != "" %}<a href="{{ publication.pdf }}">PDF</a>{% endif %}
      {% if publication.code != "" %}<a href="{{ publication.code }}">Code</a>{% endif %}
    </p>
  </article>
{% endfor %}
</div>
{% endif %}
