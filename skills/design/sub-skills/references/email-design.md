---
metadata:
  version: "1.0.0"
  based_on_repo: ArnavPuri/designskills, CosmoBlk/email-design
  based_on_version: main(c787301), main(c56bfe0)
  based_on_skill: email-design
---

# Email Design

Coded HTML email that renders across Outlook, Gmail, Apple Mail, and mobile: table layout, fluid-hybrid responsiveness, bulletproof buttons, email dark mode, size limits. Web dark themes are in [dark-mode](dark-mode.md); web pages in [landing-page-design](landing-page-design.md).

Tokens come from `.agents/design-context.md` (see [design-context](design-context.md)); with none, extend the project's existing brand values. Email clients don't support CSS variables, so inline the hex values: primary for buttons and links, neutral 900/800/500 for headings, body, and muted text, neutral 50/100 for the outer background, brand fonts first in each stack. The `#4F46E5`-style values below are placeholders. Settle the email type (welcome, newsletter, promotional, transactional) and the ESP (it may need its own merge tags and template syntax).

## Design Direction

Commit to an archetype, a colour strategy, and a voice before composing. Defaulting to minimal-lux because it feels safe is the usual failure; it fits maybe 30% of emails.

| Archetype | When | Hallmarks |
|-----------|------|-----------|
| Editorial | Newsletters, brand stories, long-form | Serif heads, full-bleed photo, generous leading, voice-rich |
| Bold mono | Promo, launches, statements | One saturated colour drenches the surface, big type, minimal copy |
| Minimal lux | Premium, transactional | Tinted neutrals, 472-520px width, one accent, never discount-led |
| Founder letter | Welcome, win-back, milestones, reply-driver | Plain-text feel, first person, short paragraphs, signed off, no template chrome |
| Punk / character | Retention, brand-voice carriers | Mascot or character, irreverent copy, custom imagery |
| Lookbook | Product, fashion, food, anything where the product is the design | Photo over copy, gallery layout, full-bleed hero |

Colour strategy:

- **Restrained**: tinted neutrals plus one accent at 10% of the surface or less. Default for transactional and minimal-lux.
- **Committed**: one saturated colour carries 30-60%. Default for brand-identity emails.
- **Drenched**: the surface is the colour. For heroes and statement emails.
- Tint neutrals toward the brand hue; avoid pure `#000` / `#fff`. Pull saturation back near black and white.
- Category-reflex check: if the palette is guessable from the category (fintech navy and gold, wellness white and sage, AI black and neon), rework it.

Rules that apply to every archetype:

- One typeface family; body 14-16px, headline 22-34px, at least 1.25 ratio between steps; 50-65 characters per line. No gradient text.
- Vary spacing for rhythm; uniform padding reads as a wireframe. Cards only when they're the best affordance; never nested.
- Real photography or commissioned illustration. Every hero serves a purpose (product, person, place, moment). Never fabricate stock-style images; use a clearly marked placeholder instead.
- Copy: inverted pyramid, short paragraphs, no restated headings, no em or en dashes in body. One CTA above the fold, two at most overall.
- Subject 45 characters or fewer, preheader 90 or fewer; both add information and the preheader never restates the subject.

### Whitespace

AI-drafted emails over-pad into a moonscape. Counter it:

- Asymmetric padding: most sections `padding-top: 0`, `padding-bottom: 32px`. The next section's top padding owns the rhythm.
- Hero sits flush to the header (8px gap or less), with the space below it.
- Last content block before the footer: 32-48px bottom padding at most.
- Never two spacer rows in a row, empty paragraphs, double `<br>`, an empty block used as a spacer, or margin and padding on the same side.
- Override ESP default padding explicitly, even if the ESP trims whitespace.

### Footer

In order:

1. Mission line: one sentence on why the company exists, not what it sells. Copy it verbatim from the ESP brand fields or the brand's site; if there's no verified line, omit it. Never invent one.
2. 3-5 social icons, 24-32px, real handles and URLs.
3. Physical address on one line (CAN-SPAM).
4. Visible "Unsubscribe" link, not a "preferences" euphemism.
5. Optional: contact email, why they're getting it.

Style: 12-13px, tinted neutral at 60-70% of body contrast, no extra spacer above.

### Brief and handoff

Before composing, settle a brief: name, subject, preheader, archetype, colour strategy, primary and secondary hex, voice descriptors, ordered sections (header, hero, headline, body, CTA, secondary body, footer), image slots, footer content. Then:

- **Context first.** Read brand state from the ESP or project files (`BRAND.md`, `PRODUCT.md`, prior templates) and mark each field known, inferable, or missing. Ask at most three questions in one message (email purpose, tone register, primary colour; mission line and socials/address only if the footer would be incomplete); otherwise infer and note defaults.
- **Image slots.** Resolve each to a real URL or an explicit user prompt, in order: brand assets already in the ESP, the brand site (`og:image`, homepage hero, `/press`, `/about`; prefer 1200px or wider), brand social profiles, then ask the user once.
- **Send.** Dry-run first and show the preview before any real send. Offer a test send to the account's `from_email` or an address the user names.

### Iteration

| Request | Response |
|---------|----------|
| Bolder | Escalate colour strategy, increase type contrast, shorten lines, move to bold mono or punk |
| Quieter | De-escalate colour, add whitespace selectively, drop secondary CTAs, move to minimal lux or editorial |
| More personality | Founder letter or punk; first-person copy; one unexpected element |
| Too plain | Usually the wrong archetype; ask once about bold mono or lookbook |
| Looks like AI | Diagnose one of category-reflex palette, stock-feeling imagery, or no voice, and fix only that |

## Constraints

| Rule | Why |
|------|-----|
| Table-based layout | Outlook for Windows (Word rendering engine) has no flexbox, grid, `max-width`, or reliable `float` |
| Inline CSS | Some clients strip or partly ignore `<style>` (Gmail for non-Google accounts, many webmail and older clients); keep `<style>` only for media queries and dark mode |
| No JavaScript | Stripped everywhere |
| No external CSS | Some clients block external resources |
| Max width 600px | Standard viewport (600-640px) |
| HTML under ~100KB | Gmail clips messages over 102KB; content, unsubscribe link, and tracking pixel hide behind "View entire message" |
| Web-safe fonts | Custom fonts need fallbacks |
| Alt text on all images | Images are often blocked by default |
| No CSS variables | Unsupported in most clients |
| Padding on `<td>`, not `<a>`, `<p>`, or `<div>` | Outlook desktop ignores padding and margin on many elements, plus `border-radius`, background images (without VML), and `rgba()` colors |

## Base Structure

```html
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="color-scheme" content="light dark" />
  <meta name="supported-color-schemes" content="light dark" />
  <meta name="format-detection" content="telephone=no, date=no, address=no, email=no" />
  <title>Email Subject Line</title>

  <!--[if mso]>
  <noscript>
    <xml>
      <o:OfficeDocumentSettings>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
  </noscript>
  <![endif]-->

  <style>
    :root { color-scheme: light dark; supported-color-schemes: light dark; }
    body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
    table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
    img { -ms-interpolation-mode: bicubic; border: 0; height: auto; line-height: 100%;
      outline: none; text-decoration: none; }
    body { margin: 0; padding: 0; width: 100% !important; height: 100% !important; }

    @media only screen and (max-width: 620px) {
      .email-container { width: 100% !important; max-width: 100% !important; }
      .fluid { max-width: 100% !important; height: auto !important; }
      .stack-column { display: block !important; width: 100% !important; }
      .stack-column-center { text-align: center !important; }
      .center-on-narrow { text-align: center !important; display: block !important;
        margin-left: auto !important; margin-right: auto !important; float: none !important; }
      table.center-on-narrow { display: inline-block !important; }
      .hide-on-mobile { display: none !important; }
      .padding-mobile { padding: 20px !important; }
    }

    /* Dark mode: Apple Mail, iOS Mail, Outlook for Mac/iOS/Android, some others */
    @media (prefers-color-scheme: dark) {
      .email-bg { background-color: #121212 !important; }
      .dark-bg { background-color: #1e1e1e !important; }
      .dark-text { color: #e6e6e6 !important; }
      .dark-text-secondary { color: #b3b3b3 !important; }
      h1, h2, h3 { color: #f2f2f2 !important; }
    }
    /* Outlook.com / Outlook apps: [data-ogsb] = backgrounds, [data-ogsc] = text colors */
    [data-ogsb] .email-bg { background-color: #121212 !important; }
    [data-ogsb] .dark-bg { background-color: #1e1e1e !important; }
    [data-ogsc] .dark-text { color: #e6e6e6 !important; }
    [data-ogsc] .dark-text-secondary { color: #b3b3b3 !important; }
  </style>
</head>

<body style="margin: 0; padding: 0; background-color: #f4f4f7; font-family: -apple-system,
  BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;" class="email-bg">
  <div role="article" aria-roledescription="email" aria-label="Email Subject Line" lang="en">

  <!-- Preheader (hidden). Keep under 100 characters. -->
  <div style="display: none; font-size: 1px; line-height: 1px; max-height: 0;
    max-width: 0; opacity: 0; overflow: hidden; mso-hide: all;">
    Your preview text goes here.
    &#847; &#847; &#847; <!-- stops the client pulling in body text -->
  </div>

  <table role="presentation" cellpadding="0" cellspacing="0" border="0"
    width="100%" style="background-color: #f4f4f7;" class="email-bg">
    <tr>
      <td align="center" style="padding: 20px 0;">
        <table role="presentation" cellpadding="0" cellspacing="0" border="0"
          width="600" class="email-container dark-bg"
          style="max-width: 600px; width: 100%; background-color: #ffffff; border-radius: 8px; overflow: hidden;">
          <!-- HEADER / HERO / CONTENT / CTA / FOOTER rows -->
        </table>
      </td>
    </tr>
  </table>
  </div>
</body>
</html>
```

## MSO Conditionals (Outlook)

Classic Outlook for Windows (2007-2021, 365 desktop) renders with Microsoft Word. New Outlook for Windows and Outlook.com use a browser engine, but classic Outlook is still widely used; keep supporting it.

```html
<!--[if mso]>
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600">
    <tr><td>
<![endif]-->

  <!-- fluid content -->

<!--[if mso]>
    </td></tr>
  </table>
<![endif]-->
```

Common fixes: force `border-collapse: collapse` and explicit widths in `[if mso]` style blocks. Rounded buttons in Outlook need VML:

```html
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="https://example.com"
  style="height:48px;width:200px;v-text-anchor:middle;" arcsize="17%" stroke="f" fillcolor="#4F46E5">
  <center style="color:#ffffff;font-family:Arial,sans-serif;font-size:16px;font-weight:600;">Get Started Free</center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-->
<a href="https://example.com" style="display:inline-block;padding:14px 32px;background-color:#4F46E5;
  color:#ffffff;text-decoration:none;border-radius:8px;font-size:16px;font-weight:600;">Get Started Free</a>
<!--<![endif]-->
```

## Responsive: Fluid Hybrid

Works without media queries in clients that don't support them.

```html
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600">
  <tr><td width="290" valign="top"><![endif]-->

<div style="display: inline-block; width: 100%; max-width: 290px; vertical-align: top;" class="stack-column">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
    <tr>
      <td style="padding: 20px;">
        <h2 style="margin: 0; font-size: 20px; color: #1a1a2e;">Column 1</h2>
        <p style="margin: 12px 0 0; font-size: 15px; line-height: 1.5; color: #555;">First column.</p>
      </td>
    </tr>
  </table>
</div>

<!--[if mso]></td><td width="290" valign="top"><![endif]-->

<div style="display: inline-block; width: 100%; max-width: 290px; vertical-align: top;" class="stack-column">
  <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
    <tr>
      <td style="padding: 20px;">
        <h2 style="margin: 0; font-size: 20px; color: #1a1a2e;">Column 2</h2>
        <p style="margin: 12px 0 0; font-size: 15px; line-height: 1.5; color: #555;">Second column.</p>
      </td>
    </tr>
  </table>
</div>

<!--[if mso]></td></tr></table><![endif]-->
```

## Typography

Put the design-context font first, then a web-safe stack:

- Sans: `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`
- Serif: `Georgia, 'Times New Roman', Times, serif`
- Mono: `'Courier New', Courier, monospace`

Gmail and Outlook ignore web fonts. Classic Outlook falls back to Times New Roman when the first font isn't installed; add `<!--[if mso]><style>h1,h2,h3,p,td,a { font-family: Arial, sans-serif !important; }</style><![endif]-->`. Where supported (Apple Mail, iOS Mail, Samsung Mail, Thunderbird), load web fonts in `<head>` with a `<link>` to the font provider's stylesheet. See [typography](typography.md) for general pairing.

| Element | Size | Weight | Line height |
|---------|------|--------|-------------|
| H1 (hero) | 28-32px | 700 | 1.2 |
| H2 (section) | 22-24px | 700 | 1.25 |
| H3 (subsection) | 18-20px | 600 | 1.3 |
| Body | 15-16px | 400 | 1.5 |
| Small / caption | 13px | 400 | 1.4 |

- Body at least 14px (some clients enforce it).
- `px`, not `rem` or `em`.
- Unitless line-height multiplier.
- Inline `color` on every text element.

## Bulletproof Buttons

Padding-based (best):

```html
<table role="presentation" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="border-radius: 8px; background-color: #4F46E5; mso-padding-alt: 14px 32px;" class="button-bg">
      <a href="https://example.com" target="_blank"
        style="display: inline-block; padding: 14px 32px; background-color: #4F46E5; font-size: 16px;
          font-weight: 600; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
          color: #ffffff; text-decoration: none; border-radius: 8px;">
        Get Started Free
      </a>
    </td>
  </tr>
</table>
```

- At least 44px tall, 150px+ wide.
- `display: inline-block` with padding, not fixed width.
- `background-color` on both `<td>` and `<a>`. Outlook ignores `<a>` padding; `mso-padding-alt` on the `<td>` restores the size, but only the text is clickable there.
- `border-radius` works in most clients, not classic Outlook (square corners). Use the VML button above for rounded Outlook buttons.

## Section Templates

Header:

```html
<tr>
  <td style="padding: 24px 32px; text-align: center;">
    <img src="https://example.com/logo.png" alt="Company Name" width="120" style="display: block; margin: 0 auto;" />
  </td>
</tr>
```

Hero. Use solid hex, not `rgba()`; classic Outlook doesn't support it.

```html
<tr>
  <td style="padding: 40px 32px; text-align: center; background-color: #4F46E5;" class="padding-mobile">
    <h1 style="margin: 0; font-size: 30px; font-weight: 700; color: #ffffff; line-height: 1.2;">
      Welcome to Our Platform
    </h1>
    <p style="margin: 16px 0 0; font-size: 16px; color: #E0E7FF; line-height: 1.5;">
      You're all set to start building amazing things.
    </p>
    <!-- CTA button here -->
  </td>
</tr>
```

Content block:

```html
<tr>
  <td style="padding: 32px;" class="padding-mobile">
    <h2 style="margin: 0; font-size: 22px; font-weight: 700; color: #1a1a2e; line-height: 1.25;" class="dark-text">
      What's inside
    </h2>
    <p style="margin: 12px 0 0; font-size: 15px; line-height: 1.6; color: #555;" class="dark-text-secondary">
      Here's what you can do to get started with your account.
    </p>
  </td>
</tr>
```

Feature row (icon plus text):

```html
<tr>
  <td style="padding: 0 32px 24px;" class="padding-mobile">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
      <tr>
        <td width="48" valign="top" style="padding-right: 16px;">
          <img src="https://example.com/icon-check.png" alt="" width="40" height="40" style="display: block;" />
        </td>
        <td valign="top">
          <h3 style="margin: 0; font-size: 16px; font-weight: 600; color: #1a1a2e;">Quick Setup</h3>
          <p style="margin: 4px 0 0; font-size: 14px; line-height: 1.5; color: #666;">
            Get up and running in less than 5 minutes.
          </p>
        </td>
      </tr>
    </table>
  </td>
</tr>
```

Footer. Use `#6b6b6b`, not `#999`: footer text still needs 4.5:1 on white.

```html
<tr>
  <td style="padding: 24px 32px; text-align: center; border-top: 1px solid #e5e7eb;">
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin: 0 auto;">
      <tr>
        <td style="padding: 0 8px;">
          <a href="#"><img src="https://example.com/icon-twitter.png" alt="Twitter" width="24" height="24" /></a>
        </td>
        <td style="padding: 0 8px;">
          <a href="#"><img src="https://example.com/icon-linkedin.png" alt="LinkedIn" width="24" height="24" /></a>
        </td>
      </tr>
    </table>
    <p style="margin: 16px 0 0; font-size: 13px; line-height: 1.5; color: #6b6b6b;">
      Company Name, 123 Street, City, State 12345<br />
      <a href="#" style="color: #6b6b6b; text-decoration: underline;">Unsubscribe</a>
      &nbsp;|&nbsp;
      <a href="#" style="color: #6b6b6b; text-decoration: underline;">Manage preferences</a>
    </p>
  </td>
</tr>
```

## Dark Mode

The base structure already includes the required pieces: `color-scheme` and `supported-color-schemes` meta tags and `:root` rule, a `prefers-color-scheme: dark` block, and `[data-ogsb]` / `[data-ogsc]` overrides for Outlook.com and the Outlook apps.

| Client | Behavior | What you control |
|--------|----------|------------------|
| Apple Mail, iOS Mail, Outlook Mac | Honor `prefers-color-scheme` | Full custom dark palette |
| Outlook.com, Outlook iOS/Android | Partial auto-invert | `[data-ogsb]` / `[data-ogsc]` overrides |
| Gmail app (iOS/Android) | Full or partial forced inversion | Nothing; design to survive it |

- Avoid pure black and white pairs; mid-dark backgrounds (`#121212`-`#1e1e1e`) with off-white text invert more gracefully.
- Keep brand colors on buttons as `background-color` on the `<td>` so inversion doesn't leave text unreadable.
- Use transparent PNGs where possible.
- Give dark logos a light outline or glow so they show on dark backgrounds.
- Test with images blocked; alt text should carry the message.

## Image Optimization

| Guideline | Value |
|-----------|-------|
| Max size per image | 200KB |
| Total size | HTML under 102KB (aim below 80KB) plus under about 1MB of images |
| Format | PNG for graphics, JPEG for photos |
| Retina | Serve 2x, set `width` to the 1x size |
| Alt text | Always; style it as a fallback |

```html
<!-- 600px visually, served at 1200px for retina -->
<img src="https://example.com/hero-1200.jpg" alt="Product showcase"
  width="600" style="display: block; width: 100%; max-width: 600px; height: auto;" />

<!-- Styled alt text shows when images are blocked -->
<img src="https://example.com/hero.jpg" alt="Spring Sale: 40% off everything" width="600"
  style="display: block; width: 100%; max-width: 600px; height: auto;
    font-family: sans-serif; font-size: 24px; font-weight: bold;
    color: #4F46E5; background-color: #EEF2FF; text-align: center; padding: 40px;" />
```

## Template Types

Welcome:

- Hero on a brand color background
- Personalized greeting ("Hi {first_name}")
- 3 quick-start steps with icons
- Primary CTA: "Get started" or "Complete your profile"
- Optional onboarding video thumbnail

Newsletter:

- Simple header with logo and date
- Featured article with large image
- 2-column article grid below
- 2-3 line excerpts with "Read more" links
- Footer with social links and unsubscribe

Promotional:

- Bold hero with the offer ("40% OFF")
- 2-column product grid: image, name, price, CTA each
- Urgency: "Ends Sunday" or a countdown
- Trust signals: free shipping, returns

Transactional:

- Minimal design, clear information
- Order confirmation: items, quantities, prices, total
- Shipping update: tracking number, delivery date
- Password reset: single CTA, security note
- No promotional content (improves deliverability)

Deliverability, all types:

- Bulk senders (Gmail and Yahoo rules since 2024): one-click unsubscribe headers (`List-Unsubscribe` and `List-Unsubscribe-Post`, RFC 8058), SPF/DKIM/DMARC, and a visible unsubscribe link.
- Always include a plain-text alternative part and a physical mailing address in the footer.

## Verification

- View at 390px and 1440px: desktop shows a centered 600px column; mobile stacks columns with no horizontal scroll.
- View a dark rendering and an images-off pass; the message and CTA must still read.
- Check file size after inlining: under about 100KB.
- Real client coverage (classic Outlook, Gmail app) needs an email-testing service or a test inbox; a browser can't emulate the Word engine. Flag this step as still needed if it can't be run.

## Checklist

- [ ] Table-based layout (no flexbox or grid)
- [ ] All critical styles inline
- [ ] Max width 600px
- [ ] All images have alt text and width/height
- [ ] Bulletproof buttons (padding-based or VML)
- [ ] MSO conditionals for Outlook
- [ ] Responsive from 320px to 600px (fluid hybrid)
- [ ] Web-safe fonts with fallback stack
- [ ] Hidden preheader set
- [ ] Dark mode meta tags and CSS included
- [ ] Images under 200KB each; HTML under 102KB
- [ ] Tested across major clients
- [ ] Unsubscribe and physical address in footer; `List-Unsubscribe` headers set in the ESP
- [ ] `role="presentation"` on all layout tables
- [ ] One archetype and colour strategy, no category-reflex palette
- [ ] Subject 45 characters or fewer, preheader 90 or fewer and adds information
- [ ] One CTA above the fold, two at most
- [ ] No double spacers, `<br><br>`, or margin plus padding on the same side
- [ ] Mission line verified or omitted; no em dashes in body
- [ ] Dry-run preview shown and test send offered before any real send
