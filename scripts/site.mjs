import { spawnSync } from 'node:child_process';
import './build-site-content.mjs';

const mode = process.argv[2];
if (!['dev', 'build'].includes(mode)) throw new Error('Expected dev or build');
const result = spawnSync('vitepress', [mode, 'site', ...process.argv.slice(3)], { stdio: 'inherit', shell: process.platform === 'win32' });
process.exit(result.status ?? 1);
