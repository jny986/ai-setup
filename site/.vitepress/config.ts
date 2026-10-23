import { defineConfig } from 'vitepress';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  title: 'ai-setup',
  description: 'Reference documentation for the skills, agents and templates in jny986/ai-setup.',
  base: '/',
  lastUpdated: false,
  vite: { plugins: [tailwindcss()] },
  head: [['meta', { name: 'theme-color', content: '#fafbf7' }]],
});
