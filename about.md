---
layout: default
title: About
permalink: /about/
---

# About Me

## {{ site.data.profile.name_zh }}

**{{ site.data.profile.position }} · {{ site.data.profile.university }}**

{{ site.data.profile.bio }}

## Research Interests

{% for interest in site.data.profile.research_interests %}
- {{ interest }}
{% endfor %}

## Links

- [GitHub]({{ site.data.profile.github.url }})
