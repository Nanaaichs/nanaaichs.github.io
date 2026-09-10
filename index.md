---
layout: default
title: Home
permalink: /
---

<div class="hero">

# {{ site.data.profile.name_zh }}

**{{ site.data.profile.position }} · {{ site.data.profile.university }}**

### {{ site.data.profile.headline }}

{{ site.data.profile.bio }}

[Research](/research/) ·
[Projects](/projects/) ·
[Publications](/publications/) ·
[About](/about/)

</div>

## Current Research

My current research focuses on satellite communications,
5G NR Non-Terrestrial Networks, LEO satellite systems,
physical-layer synchronization and communication system simulation.

[View Research →](/research/)

## Featured Projects

{% for project in site.data.projects %}
{% if project.featured %}

### {{ project.name }}

**{{ project.category }} · {{ project.period }}**

{{ project.summary }}

{% for tech in project.technologies %}
`{{ tech }}`
{% endfor %}

[View all projects →](/projects/)

{% endif %}
{% endfor %}

## Selected Publications

{% if site.data.publications.size > 0 %}

{% for publication in site.data.publications limit:3 %}
- **{{ publication.title }}**  
  {{ publication.authors }}  
  *{{ publication.venue }}*, {{ publication.year }}
{% endfor %}

[View Publications →](/publications/)

{% else %}

Publications will be updated here.

{% endif %}

## Selected Awards

{% if site.data.awards.size > 0 %}

{% for award in site.data.awards limit:3 %}
- **{{ award.title }}**, {{ award.organization }}, {{ award.year }}
{% endfor %}

[View Awards →](/awards/)

{% else %}

Awards and honors will be updated here.

{% endif %}

## Recent Writing

{% if site.posts.size > 0 %}

{% for post in site.posts limit:3 %}
- [{{ post.title }}]({{ post.url | relative_url }}) · {{ post.date | date: "%Y-%m-%d" }}
{% endfor %}

[View Writing →](/writing/)

{% else %}

Technical articles and research notes will be published here.

{% endif %}
