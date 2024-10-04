---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
---

## Journal Articles

<div class="gallery">
{% assign count = 1 %}
{% for post in site.posts %}
    {% if post.categories contains "journals" %}
    <div class="gallery-item">
        <h3>{{ count }}. <a href="{{ post.url }}">{{ post.title }}</a></h3>
        <a href="{{ post.url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="gallery-image"/>
        </a>
        {% if post.image-caption %}
        <p class="image-caption">{{ post.image-caption }}</p>
        {% endif %}
    </div>
    {% assign count = count | plus: 1 %}
    {% endif %}
{% endfor %}
</div>

## Conferences Papers

<div class="gallery">
{% assign conference_count = 1 %}
{% for post in site.posts %}
    {% if post.categories contains "conferences" %}
    <div class="gallery-item">
        <h3>{{ conference_count }}. <a href="{{ post.url }}">{{ post.title }}</a></h3>
        <a href="{{ post.url }}">
            <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" class="gallery-image"/>
        </a>
        {% if post.image-caption %}
        <p class="image-caption">{{ post.image-caption }}</p>
        {% endif %}
    </div>
    {% assign conference_count = conference_count | plus: 1 %}
    {% endif %}
{% endfor %}
</div>
