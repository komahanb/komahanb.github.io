---
layout: single
title: "Presentation"
permalink: /presentation/
---

<div class="reveal">
  <div class="slides">
    <section data-markdown="{{ '/assets/reveal/slides/presentation.md' | relative_url }}" data-separator="^---" data-separator-vertical="^--">
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