---
metadata:
  based_on_repo: kostja94/marketing-skills, coreyhaines31/marketingskills
  based_on_version: v1.0.0(8dd89c5), v2.13.0(e85f3cb)
  based_on_skill: x, social
---

# Platforms: X (Twitter)

Guides X post copy creation and optimization. Use for generating publish-ready posts, threads, and content that performs on X. Suitable for copy agents, design agents (image specs), and video agents (video post specs).

## Output: Publish-Ready Copy

This skill enables agents to generate X post copy that can be published directly. Output includes character-counted text, thread structure, and platform-compliant formatting.

## Character Limits

| Type | Limit | Notes |
|------|-------|-------|
| **Standard post** | 280 characters | Most users |
| **Premium** | 25,000 characters | X Premium subscribers |
| **URL** | Counts as 23 chars | t.co shortens all links |
| **Emoji** | ~2 chars each | Varies by emoji |

## Optimal Lengths (Engagement)

| Use Case | Characters | Purpose |
|----------|------------|---------|
| **General** | 71-100 | Sweet spot for engagement |
| **Promotional** | 120-130 | Product/offer posts |
| **Question** | 60-80 | Drive replies |
| **Retweet-friendly** | ~116 | Leaves room for "RT @user:" |

## Thread Format

- **Structure**: 3-5 connected posts; number as 1/5, 2/5, etc.
- **First post**: Strong hook; no "thread" in first line
- **Last post**: CTA, summary, or question
- **Each post**: ~80 chars; can stand alone

## Post Structure (Hook + Value + CTA)

| Part | Ratio | Guideline |
|------|-------|-----------|
| **Hook** | 10% | First 1-2 lines; question, fact, or emotion; ~50 chars |
| **Value** | 70% | Practical info; use thread for depth |
| **CTA** | 20% | Call for reply, question, or action |

End with open question to drive replies. Thread structure can extend impressions ~10x.

## Algorithm (Grok AI)

### Signal Weights

| Signal | Impact |
|--------|--------|
| **Replies** | Highest (~54-75x likes); quality > quantity |
| **Author replies** | Active reply chains ~75x visibility |
| **Bookmark** | 2026 signal; saves boost recommendation |
| **Media** | Images/video ~2x; video 2-4x exposure |
| **External links** | Reduce score ~50%; prefer internal refs |
| **Post limit** | 5-8/day; >10/day reduces later visibility ~80% |

**Content**: Open questions, controversial views, stories; avoid "RT if agree" bait.

### TweepCred

| Threshold | Effect |
|-----------|--------|
| **< 65** | Only last 3 posts enter For You |
| **New accounts** | Need +17 to appear in feed |
| **Blue V** | Auto 100 points |

Monitor account health; avoid spam, bulk ops, excessive links.

### Distribution

Posts tested in small group first; early interaction (first 30 min) decides reach. Niche consistency helps SimClusters match.

## Link Optimization

| Practice | Guideline |
|----------|-----------|
| **Penalty** | External links ~-50%; Regular accounts: link posts 0% engagement since 2025 |
| **Placement** | Put link in reply, not main post |
| **Ratio** | Max 1 link per 5 posts |
| **Premium** | Premium+ safest for links (~0.25-0.3% engagement) |
| **Preview** | Title ≤70 chars, description ≤200 chars; 1200×628 image |

## Premium Impact

| Tier | Reach | Link posts |
|------|-------|------------|
| **Regular** | <100/post | 0% engagement |
| **Premium ($8)** | ~600/post | ~0.25-0.3% |
| **Premium+ ($40)** | ~1550/post | Safest for links |

Premium ~10x reach vs Regular. If X is core channel, Premium helps.

## Video

- **Exposure**: 2-4x vs text
- **Length**: 8-30s short video preferred
- **VQV**: High video completion boosts score 2-3x

## Content Ratio

| Type | Share | Use |
|------|-------|-----|
| **Value** | 70% | Education, how-to, insights |
| **Interaction** | 20% | Polls, questions, AMA |
| **Promo** | 10% | Product, offers |

## Twitter Cards + SEO

Cards (og:image, title, description) boost CTR ~64%, engagement ~26%. Use for Social SEO; X traffic can accelerate Google indexing. For programmatic SEO (template + data pages at scale), use programmatic-seo.

## Image Specs (for Design Agents)

| Format | Dimensions | Use |
|-------|------------|-----|
| **Single image** | 1200×675 (16:9) | Best visibility; no crop |
| **Square** | 800×800 | Single image |
| **Profile** | 400×400 | Avatar |
| **Header** | 1500×500 (3:1) | Banner |
| **File** | ~5MB; JPG/PNG | Over 5MB may compress |

## Platform Tips

**Best for:** Tech, media, real-time commentary, community building
**Audience:** Tech-savvy, news-oriented, niche communities
**Best times:** Varies by audience; test and measure

**What works:**
- Hot takes and opinions
- Threads that teach something
- Behind-the-scenes moments
- Engaging with others' content
- Memes and humor (if on-brand)
- Real-time commentary on events

**What doesn't:**
- Pure self-promotion
- Threads without a strong hook
- Ignoring replies and mentions
- Scheduling everything (no real-time presence)

**Format tips:**
- Threads: Hook in tweet 1, promise value, deliver

## X Algorithm Playbook (xAI Open-Sourced Ranking)

How the X "For You" feed ranks posts, based on xAI's open-sourced algorithm ([xai-org/x-algorithm](https://github.com/xai-org/x-algorithm), May 2026 release — the Phoenix ranker and Grox content-understanding pipeline), and what to change in your posting practice because of it.

**Sourcing note:** the release publishes the ranking *structure* (which signals are scored and how they combine) but not the weight *values* (`params.rs` is withheld). Rules below are tagged **[verified]** when the mechanism is visible in the code, **[reported]** when the specific number or magnitude comes from secondary analysis of the release. Structure changes slowly; reported numbers age fast — treat them as directionally true.

### How ranking works (60-second version)

1. Candidate posts come from two sources: accounts the viewer follows (Thunder) and ML-retrieved posts from the global corpus (Phoenix retrieval). You are always competing for out-of-network reach, not just your followers' feeds.
2. Filters remove ineligible posts *before* scoring: too old, already seen or served, muted keywords, blocked/muted authors.
3. The Phoenix transformer predicts a probability for each engagement type — not one "quality score" but ~15 separate predictions.
4. Final score = weighted sum of those probabilities. Positive actions add; predicted negative actions (not-interested, mute, block, report) subtract.
5. An author-diversity scorer then decays the scores of repeated authors within a feed response, so your posts compete with each other.

The model has no hand-engineered "quality" features — it learns entirely from engagement histories. You can't optimize for the algorithm directly; you optimize for the specific *behaviors* it predicts. And notice what those behaviors are: staying to read, sending to a friend, following the author, joining the conversation. Those are the things a well-told story produces. Storytelling and genuine connection with your audience aren't a separate strategy from the mechanics below — they're what the mechanics reward. The rules tune distribution; the story earns the engagement.

### The signals your post is scored on [verified]

Every signal below is a separate weighted term in the scoring code:

| Signal | What to notice |
|--------|---------------|
| Favorite (like) | The baseline — and the weakest lever, given how many other signals exist |
| Reply | Conversation-starting posts earn a distinct signal |
| Repost | Public amplification |
| Quote **and** quoted-click | Two separate terms: engagement on a quote post *and* clicks through to the quoted post both score |
| Click | Opening the post detail |
| Profile click | Clicking through to your profile is its own scored action |
| Share, share-via-DM, share-via-copy-link | **Three separate share signals** — private sharing is explicitly modeled, not lumped into one |
| Video quality view | Only paid if video duration exceeds a minimum threshold (`MIN_VIDEO_DURATION_MS`); short clips earn zero video credit |
| Dwell (two forms) | Time spent reading is scored both as a threshold and as continuous time |
| Photo expand | Tapping to enlarge an image |
| Follow author | A post that converts a viewer into a follower earns its own signal |
| Not interested / mute / block / report | **Negative weights** — the model predicts these too, and they subtract from your score |

### The 10 rules

1. **Open with a specific claim in the first 8 words.** [reported] Dwell is scored two ways [verified], and scroll-past is the dwell-killer. Don't warm up — the hook *is* the post.

2. **Wait ~60 minutes between original posts.** [reported number] The author-diversity scorer is verified: within a feed response, each additional post from the same author gets a decayed score. Clustered posts cannibalize each other's reach.

3. **Name your topic in the first 10 words.** [reported] Topic-based candidate sourcing and followed-topic hydration are verified in the pipeline — the algorithm routes posts to topic followers, but only if it can tell what the topic is. Vague musings don't get routed.

4. **Write for the DM-forward, not the like.** [verified structure; relative weight reported] Share-via-DM is its own scored signal. The test for every post: "would someone send this to a friend?" beats "would someone like this?"

5. **Quote tweets score twice.** [verified structure] Quote engagement and quoted-click are separate terms. Quoting with added insight beats plain reposting — for both parties.

6. **Write for the follow.** [verified structure] Follow-author is a distinct signal. Posts that make a stranger think "I want more of this" outperform posts that make them think "ha, nice."

7. **Make them curious enough to click your profile.** [verified structure] Profile clicks are scored. This is the mechanical argument for a strong bio and pinned post: the algorithm rewards posts that trigger the click, and your profile converts it.

8. **Name specific things.** [verified mechanism] Two reasons: specificity is what enables topic routing (rule 3), and the muted-keyword filter removes posts *pre-scoring* — generic engagement-bait phrases are commonly muted; specific nouns ("Claude", "Stripe") rarely are.

9. **Video must clear the minimum duration — with captions.** [verified mechanism; ~8s reported] The video-quality-view weight only applies above `MIN_VIDEO_DURATION_MS`. Below the threshold, video earns zero video credit. Captions serve the dwell signals (most viewing is muted).

10. **Be present for the first 30 minutes.** [reported] Early replies compound: each reply you answer is a fresh engagement event, and reply chains feed the dwell and conversation signals. Post when you can stay, not when the scheduler fires.

### What kills reach [verified]

- **Muted keywords** — filtered before scoring even happens. Spammy CTA phrases and rage-bait vocabulary are widely muted.
- **Predicted negative actions** — if your post pattern-matches to content people block, mute, or hit "not interested" on, it's penalized *before anyone acts*. Engagement bait doesn't just annoy humans; it's a modeled negative.
- **Posting bursts** — author-diversity decay (rule 2). Your second post in an hour starts handicapped.
- **Already-seen content** — reposting the same content quickly hits the previously-seen/served filters. Evergreen reruns need spacing.

### Caveats

- **Weights are unpublished.** Claims like "shares are worth N× likes" are inference, not source. The safe conclusion is which behaviors are scored *at all* — and that private shares, follows, profile clicks, and dwell each matter independently.
- **This ages fast.** The repo gets updated releases; if you're reading this long after May 2026, check [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) for changes before treating numbers as current.
- **These rules are X-specific.** The general principles (hook early, specificity, reply presence) travel to other platforms; the mechanics (60-minute spacing, quote-double-counting, video minimums) do not.

> **Source conflicts (kostja wins, ours flagged):** our copy suggested 3-10 posts per day including replies. kostja caps original posts at 5-8 per day and says over 10 cuts later visibility ~80%, so the frequency line is dropped here. kostja also puts reply weight at ~54-75x a like, while our playbook below treats weight magnitudes as unpublished inference; kostja's figures stand as reported numbers. Our "wait ~60 minutes between original posts" rule is kept as a spacing rule and sits within kostja's 5-8 per day.

## Output Format

When generating X copy, provide:

1. **Post text** with character count
2. **Hashtags** (if used; 1-3 recommended)
3. **Thread structure** (if thread)
4. **Image specs** (if design agent needs dimensions)

## Related Skills

- **paid-ads-strategy**: X (Twitter) Ads for paid promotion; tech audiences, timely content; see Platform Selection
- **influencer-marketing**: X is key influencer platform
- [Reddit](reddit.md): Alternative community channel
- **programmatic-seo**: Programmatic SEO (template + data pages); X traffic can accelerate indexing
- **open-graph, twitter-cards**: OG and Twitter Card tags for X link previews
- **visual-content**: Cross-channel visual planning; X image specs in context
