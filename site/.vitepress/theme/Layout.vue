<script setup>
import { computed } from 'vue';
import { Content, useData, withBase } from 'vitepress';
import Catalogue from './components/Catalogue.vue';
import data from '../content.json';
import { useCodeCopyFeedback } from './useCodeCopyFeedback';

useCodeCopyFeedback();

const { frontmatter, page } = useData();
const section = computed(() => frontmatter.value.section);
const links = ['Home', 'Skills', 'Agents', 'Templates', 'Sources'];
</script>

<template>
  <a class="skip" href="#main">Skip to content</a>
  <div class="wrap">
    <div class="topbar flex flex-wrap items-center justify-between gap-4">
      <a class="brand" :href="withBase('/')">ai-setup / Reference</a>
      <nav aria-label="Main navigation" class="flex flex-wrap gap-x-5 gap-y-2">
        <a v-for="name in links" :key="name" :href="withBase(name === 'Home' ? '/' : `/${name.toLowerCase()}.html`)" :aria-current="(name === 'Home' ? page.relativePath === 'index.md' : section === name.toLowerCase()) ? 'page' : undefined">{{ name }}</a>
      </nav>
    </div>
    <main id="main">
      <template v-if="page.isNotFound">
        <header><p class="eyebrow">404</p><h1>Page not found</h1><p><a :href="withBase('/')">Return to the reference home</a>.</p></header>
      </template>
      <template v-else>
        <header><span class="eyebrow">{{ frontmatter.eyebrow || 'The tools in this package' }}</span><h1>{{ frontmatter.title }}</h1><p>{{ frontmatter.description }}</p></header>
        <div class="page-copy prose"><Content /></div>
        <Catalogue v-if="section" :key="section" :items="data[section]" :section="section" />
      </template>
    </main>
    <footer>Maintained in <a href="https://github.com/jny986/ai-setup">jny986/ai-setup</a>. Content follows the latest main branch. <a href="https://github.com/jny986/ai-setup/blob/main/LICENSE">License and attribution</a>.</footer>
  </div>
</template>
