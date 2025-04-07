---
layout: page
title: "Haonan's Blog"
permalink: /blog/
---

<h1 style="color: purple; text-align: center;">Haonan's Blog</h1>

{% for post in site.posts %}
  <div style="margin-bottom: 2em;">
    <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
    <p><small>{{ post.read_time }} min read ・ {{ post.date | date: "%B %d, %Y" }}</small></p>
    <p>📁 {{ post.tags | join: ", " }}</p>
    <hr>
  </div>
{% endfor %}

