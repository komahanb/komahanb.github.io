---
layout: single
title: "Presentation As Title"
permalink: /presentation/
---

<div class="reveal">
  <div class="slides">
    <section data-markdown="{{ 'slides.md' | relative_url }}" data-separator="^---" data-separator-vertical="^--" data-transition="slide">
    </section>
  </div>
</div>

<script src="{{ '/assets/reveal/dist/reveal.js' | relative_url }}"></script>
<script src="{{ '/assets/reveal/plugin/markdown/markdown.js' | relative_url }}"></script>
<script>
    Reveal.initialize({
        plugins: [ RevealMarkdown ]
    });
</script>