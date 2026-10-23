<script setup>
import { ref, computed, onMounted, onUnmounted, nextTick } from 'vue';
import { withBase } from 'vitepress';
import WorkflowTree from './WorkflowTree.vue';

const props = defineProps({ items: Array, section: String });
const query = ref('');
const enhanced = ref(false);
const root = ref(null);
const input = ref(null);
const visibleCount = ref(props.items.length);
const label = computed(() => props.section === 'skills' ? 'skill or sub-skill' : props.section.slice(0, -1));
const text = item => [item.name, item.description, ...(item.skills || [])].filter(Boolean).join(' ');
const matches = (text, terms) => terms.every(term => text.toLowerCase().includes(term));

function filter() {
  const terms = query.value.toLowerCase().split(/\s+/).filter(Boolean);
  let count = 0;
  for (const article of root.value.querySelectorAll('.entry')) {
    const parentMatch = matches(article.dataset.search, terms);
    const children = [...article.querySelectorAll('.sub-skill')];
    for (const child of children) child.hidden = !parentMatch && !matches(article.dataset.name + ' ' + child.dataset.search, terms);
    article.hidden = !parentMatch && !children.some(child => !child.hidden);
    if (!article.hidden) count++;
    for (const details of [...article.querySelectorAll('details')].reverse()) {
      if (details.classList.contains('entry-details')) {
        details.hidden = false;
      } else {
        details.hidden = terms.length > 0 && ![...details.querySelectorAll('.sub-skill')].some(child => !child.hidden);
      }
      if (terms.length) {
        if (!details.hasAttribute('data-was-open')) details.dataset.wasOpen = String(details.open);
        details.open = !article.hidden && !details.hidden;
      } else if (details.hasAttribute('data-was-open')) {
        details.open = details.dataset.wasOpen === 'true';
        delete details.dataset.wasOpen;
      }
    }
    root.value.querySelector(`.item-nav a[href="#${article.id}"]`).hidden = article.hidden;
  }
  visibleCount.value = count;
}

function revealAnchor() {
  let id;
  try { id = decodeURIComponent(window.location.hash.slice(1)); } catch { return; }
  const target = document.getElementById(id);
  if (!target || !root.value.contains(target)) return;
  if (target.closest('[hidden]')) { query.value = ''; filter(); }
  for (let element = target; element && element !== root.value; element = element.parentElement) {
    if (element.tagName === 'DETAILS') element.open = true;
  }
  target.querySelector(':scope > details')?.setAttribute('open', '');
  requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
}

function clear() { query.value = ''; filter(); input.value.focus(); }
onMounted(async () => {
  enhanced.value = true;
  await nextTick();
  revealAnchor();
  window.addEventListener('hashchange', revealAnchor);
  window.addEventListener('popstate', revealAnchor);
});
onUnmounted(() => {
  window.removeEventListener('hashchange', revealAnchor);
  window.removeEventListener('popstate', revealAnchor);
});
</script>

<template>
  <div ref="root">
    <section v-if="enhanced" class="search" aria-label="Filter the catalogue">
      <label for="item-search">Find a {{ label }}</label>
      <div class="search-row flex gap-3">
        <input id="item-search" ref="input" v-model="query" type="search" :placeholder="`Search ${section}…`" aria-controls="catalogue" aria-describedby="result-count" @input="filter">
        <button type="button" @click="clear">Clear</button>
      </div>
      <p id="result-count" class="result-count" role="status">{{ visibleCount }} of {{ items.length }} {{ section }}{{ query.trim() ? ' match your search' : '' }}.</p>
    </section>
    <div class="catalogue-layout">
      <nav class="item-nav" :aria-label="`Jump to ${section}`">
        <p>On this page</p>
        <a v-for="item in items" :key="item.id" :href="`#${item.id}`">{{ item.name }}</a>
      </nav>
      <section id="catalogue" :aria-label="`${section} catalogue`" class="min-w-0">
        <p v-if="visibleCount === 0" class="empty">No matches. Try a broader term or clear the search to browse all {{ section }}.</p>
        <article v-for="item in items" :id="item.id" :key="item.id" class="entry" :data-name="item.name" :data-search="text(item)">
          <details class="entry-details">
            <summary>
              <h2>{{ item.name }}</h2>
              <span v-if="item.invocationLabel || item.type" class="badge">{{ item.invocationLabel || item.type }}</span>
              <span v-if="item.description" class="description">{{ item.description }}</span>
            </summary>
            <div class="entry-body">
              <p v-if="item.invocation" class="invoke"><strong>How to ask</strong> <code>{{ item.invocation }}</code></p>
              <p v-if="item.url"><a :href="item.url">{{ section === 'sources' ? 'Visit source' : 'View original on GitHub' }} →</a></p>
              <template v-if="section === 'templates'">
                <p v-if="item.name === 'settings.json'" class="notice">Review every setting before use. Replace the absolute /Users/jny986/.claude-personal/ hook paths with your own scripts, or remove those hooks. Review plugins, permissions, notification choices and the status-line command. Merge selected settings into .claude/settings.json for a project or ~/.claude/settings.json for your account.</p>
                <p v-else>Place {{ item.name }} at the project root and customize the conventions for your project. Keep AGENTS.md and CLAUDE.md together when using the @AGENTS.md import.</p>
              </template>
              <div v-if="item.html" class="prose" v-html="item.html" />
              <template v-for="format in item.formats" :key="format.path">
                <h3>{{ format.name }}</h3>
                <p><a :href="format.url">{{ format.path }}</a></p>
                <div class="prose" v-html="format.html" />
              </template>
              <template v-if="item.tree && (Object.keys(item.tree.dirs).length || item.tree.subSkills.length)">
                <h3 class="eyebrow">Sub-skills</h3>
                <WorkflowTree :node="item.tree" :skill="item.name" />
              </template>
              <template v-if="item.skills">
                <h3>Used by</h3>
                <ul><li v-for="skill in item.skills" :key="skill"><a :href="withBase(`/skills.html#skill-${skill}`)">{{ skill }}</a></li></ul>
              </template>
            </div>
          </details>
        </article>
      </section>
    </div>
  </div>
</template>
