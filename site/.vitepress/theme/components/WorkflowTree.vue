<script setup>
defineProps({ node: Object, skill: String });
const count = node => node.subSkills.length + Object.values(node.dirs).reduce((sum, child) => sum + count(child), 0);
</script>

<template>
  <div class="workflow-tree">
    <details v-for="(child, name) in node.dirs" :key="name">
      <summary>{{ name }} <span class="count">({{ count(child) }})</span></summary>
      <WorkflowTree :node="child" :skill="skill" />
    </details>
    <ul v-if="node.subSkills.length" class="sub-skills">
      <li v-for="child in node.subSkills" :id="child.id" :key="child.id" class="sub-skill" :data-search="child.name + ' ' + child.description">
        <h4><a :href="child.url">{{ child.name }}</a></h4>
        <p>{{ child.description }}</p>
        <code>{{ child.invocation }}</code>
      </li>
    </ul>
  </div>
</template>
