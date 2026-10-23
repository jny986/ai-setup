import { test, expect } from '@playwright/test';
import { readFileSync } from 'node:fs';

const skillCount = JSON.parse(readFileSync('site/.vitepress/catalogue.json', 'utf8')).skills.length;

test.describe('clipboard actions', () => {
// Clipboard contents are shared across browser contexts, so run these in order.
test.describe.configure({ mode: 'serial' });

test('templates display and copy the complete original file contents', async ({ page, context }) => {
  await context.grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.goto('./');
  await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Templates', exact: true }).click();
  const templates = JSON.parse(readFileSync('site/.vitepress/catalogue.json', 'utf8')).templates;
  for (const template of templates) {
    const item = page.locator(`#${template.id}`);
    await item.locator('summary').click();
    const expected = readFileSync(template.path, 'utf8');
    expect(await item.locator('.prose pre code').textContent()).toBe(expected);
    await item.getByRole('button', { name: 'Copy code', exact: true }).click();
    await expect.poll(() => page.evaluate(() => navigator.clipboard.readText())).toBe(expected);
    await expect(item.getByRole('button')).toHaveText('Copied!');
  }
});

test('code copy buttons copy the displayed command with keyboard feedback', async ({ page, context }) => {
  await context.grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.goto('./');
  const block = page.locator('.language-sh').first();
  const code = await block.locator('pre code').innerText();
  await page.evaluate(() => navigator.clipboard.writeText('clipboard sentinel'));
  await block.getByRole('button', { name: 'Copy code', exact: true }).focus();
  await page.keyboard.press('Enter');
  await expect.poll(() => page.evaluate(() => navigator.clipboard.readText())).toBe(code);
  await expect(block.getByRole('button')).toHaveText('Copied!');
  await expect(block.getByRole('button')).toHaveText('Copy');
  await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Skills', exact: true }).click();
  await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: 'Home', exact: true }).click();
  const setup = page.locator('.language-sh').nth(1);
  await setup.getByRole('button', { name: 'Copy code', exact: true }).click();
  await expect.poll(() => page.evaluate(() => navigator.clipboard.readText())).toBe(await setup.locator('pre code').innerText());
  await expect(setup.getByRole('button')).toHaveText('Copied!');
});
});

test('code copy buttons have readable labels and stay inside the code block on mobile', async ({ page }) => {
  await page.setViewportSize({ width: 360, height: 780 });
  await page.goto('./');
  const block = page.locator('.language-sh').first();
  const button = block.getByRole('button', { name: 'Copy code', exact: true });
  await expect(button).toHaveText('Copy');
  const bounds = await block.boundingBox();
  const control = await button.boundingBox();
  expect(control!.x).toBeGreaterThan(bounds!.x);
  expect(control!.x + control!.width).toBeLessThanOrEqual(bounds!.x + bounds!.width);
  expect(control!.height).toBeGreaterThanOrEqual(40);
  await page.screenshot({ path: 'test-results/mobile-code-copy.png', fullPage: true });
});

test('all five routes and shared navigation work under the project base', async ({ page }) => {
  const errors: string[] = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('./');
  for (const section of ['Skills', 'Agents', 'Templates', 'Sources', 'Home']) {
    await page.getByRole('navigation', { name: 'Main navigation' }).getByRole('link', { name: section, exact: true }).click();
    await expect(page.getByRole('link', { name: section, exact: true }).first()).toHaveAttribute('aria-current', 'page');
    await expect(page.locator('h1')).toBeVisible();
  }
  expect(errors).toEqual([]);
});

test('multiple accordions, keyboard, parent/child search, empty state and clear', async ({ page }) => {
  await page.goto('skills.html');
  const search = page.getByRole('searchbox');
  await expect(search).toBeVisible();
  await page.locator('#skill-tdd summary').first().focus();
  await page.keyboard.press('Enter');
  await expect(page.locator('#skill-tdd > details')).toHaveAttribute('open', '');
  await page.locator('#skill-git > details > summary').click();
  await expect(page.locator('#skill-tdd > details')).toHaveAttribute('open', '');
  await search.fill('code-review');
  await expect(page.locator('#skill-git')).toBeVisible();
  await expect(page.locator('#skill-git > details')).toHaveAttribute('open', '');
  await expect(page.locator('#skill-git .sub-skill').filter({ hasText: '/git code-review' })).toBeVisible();
  await search.fill('merge-base');
  await expect(page.locator('#subskill-skills-git-sub-skills-commit-md')).toBeHidden();
  await page.evaluate(() => { location.hash = 'subskill-skills-git-sub-skills-commit-md'; });
  await expect(page.locator('#subskill-skills-git-sub-skills-commit-md')).toBeVisible();
  await expect(search).toHaveValue('');
  await search.fill('zz-no-such-item-zz');
  await expect(page.getByRole('status')).toContainText(`0 of ${skillCount} skills`);
  await expect(page.getByText('No matches.', { exact: false })).toBeVisible();
  await page.getByRole('button', { name: 'Clear', exact: true }).click();
  await expect(page.locator('.entry:visible')).toHaveCount(skillCount);
  await expect(search).toBeFocused();
  await expect(page.locator('#skill-tdd > details')).toHaveAttribute('open', '');
});

test('anchors reveal items on direct loads, client navigation and browser history', async ({ page }) => {
  await page.goto('skills.html#skill-tdd');
  await expect(page.locator('#skill-tdd > details')).toHaveAttribute('open', '');
  await page.locator('.item-nav a[href="#skill-git"]').click();
  await expect(page.locator('#skill-git > details')).toHaveAttribute('open', '');
  await page.goBack();
  await expect(page).toHaveURL(/#skill-tdd$/);
  await expect(page.locator('#skill-tdd > details')).toHaveAttribute('open', '');
  await page.goto('sources.html');
  await page.locator('.entry > details > summary').first().click();
  await page.locator('.entry-body a[href*="skills.html#skill-"]').first().click();
  await expect(page.locator('.entry-details[open]')).toHaveCount(1);
});

test('all content is available with JavaScript disabled', async ({ browser }) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  await page.goto('http://127.0.0.1:4173/ai-setup/skills.html');
  await expect(page.locator('.entry')).toHaveCount(skillCount);
  await expect(page.getByRole('searchbox')).toHaveCount(0);
  await page.locator('#skill-tdd > details > summary').click();
  await expect(page.locator('#skill-tdd .prose')).toBeVisible();
  await page.goto('http://127.0.0.1:4173/ai-setup/');
  await expect(page.locator('button.copy').first()).toBeHidden();
  await context.close();
});

test('mobile pages reflow with expanded long instructions and usable navigation', async ({ page }) => {
  await page.setViewportSize({ width: 360, height: 780 });
  for (const route of ['index', 'skills', 'agents', 'templates', 'sources']) {
    await page.goto(`${route}.html`);
    for (const summary of await page.locator('.entry > details > summary').all()) await summary.click();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await expect(page.getByRole('navigation', { name: 'Main navigation' })).toBeVisible();
    if (route === 'index') await page.screenshot({ path: 'test-results/mobile-home.png', fullPage: true });
  }
  await page.goto('skills.html');
  await page.screenshot({ path: 'test-results/mobile-skills.png' });
  await page.setViewportSize({ width: 1440, height: 1000 });
  await page.screenshot({ path: 'test-results/desktop-skills.png' });
});
