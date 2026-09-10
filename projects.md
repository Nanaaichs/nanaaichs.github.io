---
layout: default
title: Projects
permalink: /projects/
---

# Projects

Selected research, engineering and software projects.

{% for project in site.data.projects %}

## {{ project.name }}

**{{ project.category }} · {{ project.period }} · {{ project.status }}**

{{ project.summary }}

**My Role**

{{ project.role }}

**Technologies**

{% for tech in project.technologies %}
`{{ tech }}` {% endfor %}

**Highlights**

{% for item in project.highlights %}
- {{ item }}
{% endfor %}

{% if project.github != "" %}
[GitHub]({{ project.github }})
{% endif %}

{% if project.demo != "" %}
[Demo]({{ project.demo }})
{% endif %}

{% if project.report != "" %}
[Report]({{ project.report }})
{% endif %}

---

{% endfor %}
