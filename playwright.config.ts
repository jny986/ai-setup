import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/site',
  fullyParallel: true,
  use: { baseURL: 'http://127.0.0.1:4173/ai-setup/' },
  webServer: {
    command: 'npm exec -- vp run site:preview --port 4173',
    url: 'http://127.0.0.1:4173/ai-setup/',
    reuseExistingServer: !process.env.CI,
  },
});
