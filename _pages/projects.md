---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

Research projects in computational mathematics, physical modeling, and design optimization.

{% assign projects = site.projects | sort: 'date' | reverse %}
{% for post in projects %}
  {% include archive-single.html %}
{% endfor %}
