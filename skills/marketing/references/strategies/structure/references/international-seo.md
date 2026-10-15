---
metadata:
  based_on_repo: coreyhaines31/marketingskills
  based_on_version: v2.11.29(c7d7dfb)
  based_on_skill: seo-audit
---

# International SEO

Use when the site serves multiple languages or regions. The audit checklist comes first; the evidence and source URLs behind each check follow it.

## Audit Checklist

### Hreflang

Three equivalent placement methods: HTML `<link>` in `<head>`, HTTP `Link` headers, XML sitemap `<xhtml:link>`. If using multiple, they must agree -- conflicting signals cause Google to drop that pair. For 10+ locales, prefer sitemap-based (no page weight, no per-request cost).

**Check for:**
- Self-referencing entry on every page (page must include itself in the hreflang set)
- Reciprocal links (if A points to B, B must point back to A -- or both are ignored)
- Valid codes: ISO 639-1 language + optional ISO 3166-1 Alpha 2 region (e.g., `en`, `en-GB` -- never `en-UK`)
- Consider `x-default` for unmatched language/region users, pointing to an appropriate fallback; it is recommended, not required for other valid annotations.
- All target URLs return 200, are indexable, and match their canonical URL
- No duplicate language-region codes pointing to different URLs

**Common errors:** Missing self-referencing entries. No return tag / one-directional links. Invalid codes like `en-UK` (use `en-GB`). Non-canonical, 404, or blocked targets. Conflicting HTML and sitemap annotations. Report the affected URLs and relationships; do not infer that one broken annotation invalidates every other reciprocal pair. Google can still process valid bidirectional relationships. See [Google's localized-page guidance](https://developers.google.com/search/docs/specialty/international/localized-versions#guidelines-for-all-methods).

**At scale:** `<xhtml:link>` children don't count toward 50K URL sitemap limit, but the 50MB file size limit becomes the bottleneck (plan 2K-5K URLs per file with full hreflang). Focus hreflang on pages receiving wrong-language traffic -- not required on every page. For Bing: supplement with `<html lang>` and `<meta http-equiv="content-language">` (Bing treats hreflang as a weak signal).

### Canonicalization for Multilingual Sites

- Each locale page must self-canonical (e.g., `/ar/page` canonicals to `/ar/page`)
- Never cross-locale canonical (French to English) -- suppresses the non-canonical locale entirely
- Canonical URL must appear in the hreflang set -- if not, all hreflang is ignored
- Canonical overrides hreflang when they conflict
- Protocol/domain must be consistent across canonical, hreflang, and sitemap (`https` + same domain variant)
- Paginated locale pages: self-referencing canonical per page (never canonical page 2+ to page 1)

**Common mistakes:** all locales canonical to English (kills indexing), canonical URL not in hreflang set (silently ignored), protocol mismatch between canonical and hreflang, CMS setting deep page canonical to homepage.

### International Sitemaps

**Check for:**
- `xmlns:xhtml` namespace on `<urlset>`, each `<url>` includes `<xhtml:link>` for all locales including itself
- If a fallback is needed, include an appropriate `x-default` alternate; all URLs absolute (full protocol + domain)
- Sitemap index in Search Console and robots.txt; split by content type, not by locale

**Next.js caveat:** `alternates.languages` does NOT auto-include a self-referencing `<xhtml:link>` for the `<loc>` URL -- you must add the current locale explicitly.

### Locale URL Structure

**Recommended:** Subdirectories (`/en/`, `/ar/`). **Acceptable:** Subdomains or ccTLDs. **Not recommended:** URL parameters (`?lang=en`).

**Check for:**
- Consistent locale prefix strategy; all locales prefixed (hiding locale from URLs prevents Google from distinguishing versions)
- Root URL handled as `x-default` with redirect, or serves default locale content
- No IP/Accept-Language content negotiation (Googlebot: US IPs, no Accept-Language header)
- Trailing slash + case consistency across locale paths, canonicals, hreflang, and sitemaps
- 301 redirects from non-canonical format to canonical

**Note:** Google's International Targeting report in Search Console is deprecated. Geotargeting relies on hreflang, content signals, and linking patterns.

### Content Quality Across Locales

**Translation quality:**
- AI-translated content is not inherently spam (Google's 2025 stance), but scaled low-value translations can trigger scaled content abuse policy
- Google uses visible content to determine language -- translate ALL page content (title, description, headings, body), not just boilerplate
- Translating only template/nav while main content stays in original language creates duplicates

**Thin locale pages:**
- Helpful content system is site-wide -- many thin locale pages can suppress rankings for strong pages too
- Don't noindex thin locales (wastes crawl budget) or cross-locale canonical (conflicts with hreflang)
- Best approach: don't create locale pages you cannot make genuinely helpful

**Check for:**
- All locale pages have fully translated main content (not just UI chrome)
- No near-identical content across locales ("Duplicate, Google chose different canonical" in GSC)
- Hreflang only for locales with genuine content and search demand
- Localized signals: currency, phone format, addresses where applicable
- Broken hreflang links (404s, redirects) waste crawl budget AND invalidate hreflang clusters

---

# Evidence & Sources

---

## Hreflang

### Placement Methods

Google supports three equivalent methods: HTML `<link>` in `<head>`, HTTP `Link` headers, and XML sitemap `<xhtml:link>` elements. Google confirmed no method is prioritized over another.

Google combines signals from both HTML and sitemaps. If the same language-region pair points to different URLs across methods, Google drops that pair rather than guessing.

- [Google Search Central: Localized Versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [SEJ: Google Combines Hreflang Signals](https://www.searchenginejournal.com/google-combines-hreflang-signals-from-html-sitemaps/389219/)

### Reciprocal Requirement

Google's docs: "If page X links to page Y, page Y must link back to page X. If not, those annotations may be ignored or not interpreted correctly."

Every page must include itself (self-referencing) in the hreflang set. Missing self-referencing is the #1 error found by Semrush audits. A study of 374,756 domains found 67% of hreflang implementations had issues.

- [Google Search Central: Localized Versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Semrush: 9 Common Hreflang Errors](https://www.semrush.com/blog/hreflang-errors/)
- [SE Land: 31% of International Websites Contain Hreflang Errors](https://searchengineland.com/study-31-of-international-websites-contain-hreflang-errors-395161)

### x-default

This is a recommended fallback for unmatched language/region users, not a mandatory condition for valid language annotations. Report its absence as a design recommendation when a fallback is useful, rather than declaring the whole hreflang implementation invalid.

Introduced April 2013. Designates the fallback page for users whose language/region matches no declared variant. Can point to the same URL as one of the language-specific alternates. If used, include it consistently in the complete annotation set on each variant page.

- [Google Blog: x-default hreflang](https://developers.google.com/search/blog/2013/04/x-default-hreflang-for-international-pages)
- [Google Blog: How x-default can help you (2023)](https://developers.google.com/search/blog/2023/05/x-default)

### Language & Region Codes

Language: ISO 639-1 (2-letter). Region: ISO 3166-1 Alpha 2 (2-letter). Format: `language[-script][-region]`.

You cannot specify a region code alone. Common mistakes: `en-UK` (should be `en-GB`), `es-419` (not ISO 3166-1). A study found 8.9% of sites using hreflang contain invalid language codes.

- [Google Search Central: Localized Versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [SE Land: 31% Study](https://searchengineland.com/study-31-of-international-websites-contain-hreflang-errors-395161)

### Hreflang at Scale (20+ locales)

With 20 locales, HTML `<head>` hreflang adds ~1.5KB per page for zero user benefit. Sitemap-based hreflang has zero runtime performance impact. `<xhtml:link>` child elements do NOT count toward the 50,000 URL sitemap limit (only `<loc>` elements count).

John Mueller recommends focusing hreflang on pages receiving wrong-language traffic, not every page: "I wouldn't do it for any of the other pages of the site because it's so complex & hard to manage."

- [SERoundtable: Child Elements Don't Count](https://www.seroundtable.com/google-child-elements-dont-count-towards-sitemap-url-limit-34377.html)
- [SERoundtable: Where To Focus Hreflang](https://www.seroundtable.com/using-hreflang-34127.html)
- [Yoast: hreflang Ultimate Guide](https://yoast.com/hreflang-ultimate-guide/)

### Google vs Bing

Bing treats hreflang as a "weak signal." Bing relies on `content-language` meta tag, HTML `lang` attribute, ccTLDs, and server location. Yandex supports hreflang like Google.

For both engines: implement hreflang (Google/Yandex) + `<html lang="...">` + `<meta http-equiv="content-language">` (Bing).

- [Digital Ready Marketing: Bing Doesn't Use Hreflang](https://digitalreadymarketing.com/bing-doesnt-use-hreflang-annotation-what-does-it-use/)
- [Yoast: hreflang Ultimate Guide](https://yoast.com/hreflang-ultimate-guide/)

---

## Canonicalization & i18n

### Choose Canonicals by Content and Language

Use self-referencing canonicals for distinct locale pages, including genuinely translated content. Do not consolidate different-language translations merely because they describe the same product.

For similar or duplicate regional pages in the **same language**, Google recommends choosing a preferred canonical and using consistent `hreflang` annotations. For example, equivalent German content at `example.de/` and `example.com/de/` can share a preferred canonical; every regional URL is not required to canonicalize to itself.

- [Google: Handling duplicate multilingual/multi-regional pages](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites#handling-duplicate-pages-with-multilingualmulti-regional-sites)
- [Google: Consolidate Duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

### Align Canonical and Hreflang Signals

Keep canonical targets and `hreflang` clusters consistent with the chosen content/language strategy. `hreflang` identifies localized alternatives; it does not force Google to index each URL independently. Canonicals are signals to Google's selection process, not an indexing guarantee.

The preferred canonical must be a URL inside the `hreflang` cluster. Google ignores `hreflang` on a URL that is canonicalized to another one.

- [Google: Consolidate Duplicate URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)

### Near-Duplicate Regional Variants

Mueller (2023 Office Hours): "If the content is completely the same, and we can't tell any difference, then for simplicity and user experience we may just show one version -- even if hreflang is present."

Google may consolidate identical or near-duplicate regional content despite `hreflang`. Use the same-language preferred-canonical strategy above where appropriate; do not promise that either self-canonicals or cosmetic differences will keep every regional URL indexed.

- [International Web Mastery: Same-Language Duplicate Pages](https://internationalwebmastery.com/blog/how-google-handles-canonicalization-of-same-language-duplicate-near-duplicate-pages/)
- [Google: Managing Multi-Regional Sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)

### Pagination Across Locales

Google: "Don't use the first page of a paginated sequence as the canonical page. Instead, give each page its own canonical URL." Each paginated page in each locale gets self-referencing canonical. `rel="next/prev"` deprecated March 2019.

- [Google: Pagination Best Practices](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)

---

## International Sitemaps

### Structure

Each `<url>` entry includes `<xhtml:link>` alternates for every locale. Requires `xmlns:xhtml="http://www.w3.org/1999/xhtml"` namespace.

Split sitemaps by content type, not by locale. Splitting by locale creates maintenance problems because every locale sitemap must reference every other locale (reciprocal requirement).

- [Google Search Central: Localized Versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Lumar: How Google Handles Hreflang](https://www.lumar.io/office-hours/hreflang/)

### Size Limits

50,000 URLs / 50MB uncompressed per sitemap. Only `<loc>` elements count toward the 50K limit. But with 20 hreflang alternates per entry, the 50MB file size limit becomes the bottleneck. Plan for 2,000-5,000 URLs per sitemap when using full hreflang.

- [Google: Build and Submit a Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [SERoundtable: Sitemap 50,000 Limit](https://www.seroundtable.com/google-sitemap-50-000-limit-based-on-location-urls-not-alternative-urls-33843.html)

### Submission

Submit the sitemap index in Search Console AND reference it in robots.txt. Individual child sitemaps can be submitted separately for per-sitemap reporting.

- [Google: Build and Submit a Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)

### Next.js Caveat

Next.js `alternates.languages` does NOT automatically include a self-referencing `<xhtml:link>` for the `<loc>` URL. You must explicitly include the `<loc>` URL's own language in the `languages` object.

- [Next.js Docs: sitemap.xml](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/sitemap)

---

## URL Structure

### Strategies Compared

Google treats subdirectories and subdomains equivalently. Mueller: "From our point of view...they say subdomains and subdirectories are essentially equivalent."

URL parameters (`?lang=en`) are explicitly "Not recommended" per Google docs.

- [Google: Managing Multi-Regional Sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)

### Default Language

Mueller recommends: set `/` as x-default, put each language in its own prefix. Without marking `/` as x-default, "to Google it can look like '/' is a separate page from the others."

- [Google Blog: x-default](https://developers.google.com/search/blog/2023/05/x-default)
- [Google Blog: Creating the Right Homepage](https://developers.google.com/search/blog/2014/05/creating-right-homepage-for-your)

### Content Negotiation / IP Redirects

Google strongly advises against locale-adaptive pages. Googlebot crawls from US IPs and does not send Accept-Language headers. Separate URLs + hreflang are required.

- [Google: Locale-Adaptive Pages](https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages)

### Trailing Slash Consistency

Mueller: trailing slash is "a significant part of the URL and will change the URL if it's there or not." Pick one format for all locale paths, internal links, canonicals, hreflang, and sitemaps.

Mueller (2025): "Consistency is the biggest technical SEO factor."

- [SERoundtable: Consistency Is The Biggest Technical SEO Factor](https://www.seroundtable.com/google-consistency-seo-40427.html)

### Search Console Geotargeting

The International Targeting report is deprecated. Google now relies entirely on hreflang, content language analysis, and linking patterns. You can add subdirectory properties for per-locale reporting.

- [Google Support: International Targeting Deprecated](https://support.google.com/webmasters/answer/12474899?hl=en)

### Framework Locale Modes

Use `localePrefix: 'always'` (next-intl) or equivalent. Never hide locale from URLs -- Google needs unique URLs per language. Using `'never'` mode disables alternate links entirely.

- [next-intl: Routing Configuration](https://next-intl.dev/docs/routing/configuration)
- [Next.js Discussion #18419](https://github.com/vercel/next.js/discussions/18419)

---

## Content Quality Across Locales

### Auto-Translated Content (2025 Stance)

Google removed longstanding guidance advising against auto-translated content in mid-2025. Current stance: "Our policies do not strictly define content that has been translated by AI as spam." The scaled content abuse policy mentions translation as a possible vector, but does not ban it.

Reddit scaled AI translations to 35+ languages with Google's knowledge. The key distinction is intent and quality, not the method.

- [Google Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Glenn Gabe: Auto-Translating Content](https://www.gsqi.com/marketing-blog/auto-translating-content-google-scaled-content-abuse/)
- [SE Land: Reddit AI Translations](https://searchengineland.com/google-comments-on-reddits-use-of-ai-to-translate-its-pages-456908)

### Thin Locale Pages

Google: "Localized versions of a page are only considered duplicates if the main content of the page remains untranslated." Pages with only translated boilerplate get clustered as duplicates.

Do NOT use noindex for unwanted locale pages (wastes crawl budget). Do not canonicalize distinct translations to another language merely to hide thin content. Best approach: don't create locale pages you can't make genuinely helpful.

- [Google: Localized Versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- [Google: Crawl Budget Management](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget)

### Helpful Content System Impact

Merged into core ranking March 2024. Site-wide signal: "any content -- not just unhelpful content -- on sites determined to have relatively high amounts of unhelpful content overall is less likely to perform well in Search."

Low-quality translated pages can drag down the entire site. This is the strongest argument against creating locale pages that aren't genuinely helpful.

- [Google Blog: Helpful Content Update](https://developers.google.com/search/blog/2022/08/helpful-content-update)
- [Amsive: What Changed in 2024](https://www.amsive.com/insights/seo/googles-helpful-content-update-ranking-system-what-happened-and-what-changed-in-2024/)

### Partial Translation

Google: "Translating only the boilerplate text of your pages while keeping the bulk of your content in a single language...can create a bad user experience." Google uses visible content (not lang attribute) to determine page language.

Translate ALL content on a page if you create a locale version. Untranslated metadata (title, description) in the wrong language reduces CTR.

- [Google: Managing Multi-Regional Sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)

### Crawl Budget

Only a concern for 1M+ pages or 10K+ pages changing daily. But alternate URLs (hreflang targets) do consume crawl budget. Broken hreflang links waste budget AND invalidate signals.

- [Google: Crawl Budget Management](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget)
- [Google Blog: Crawl Budget](https://developers.google.com/search/blog/2017/01/what-crawl-budget-means-for-googlebot)

### Locale-Specific Signals

Google identifies audience via: "local addresses and phone numbers on the pages, the use of local language and currency, links from other local sites, or signals from your Business Profile."

- [Google: Managing Multi-Regional Sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)
