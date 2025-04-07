---
layout: page
title: Blog
permalink: /blog/
---

<div class="post-list">
  {% for post in site.posts %}
    <div class="post-preview">
      <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
      <p><small>{{ post.read_time }} min read ・ {{ post.date | date: "%B %d, %Y" }}</small></p>
      <p>Tags: {{ post.tags | join: ", " }}</p>
      <hr>
    </div>
  {% endfor %}
</div>

