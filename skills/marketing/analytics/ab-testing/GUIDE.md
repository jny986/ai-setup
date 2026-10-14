---
name: ab-testing
description: When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program. Also use when the user mentions "A/B test," "split test," "experiment," "test this change," "variant copy," "multivariate test," "hypothesis," "should I test this," "which version is better," "test two versions," "statistical significance," "how long should I run this test," "growth experiments," "experiment velocity," "experiment backlog," "ICE score," "experimentation program," or "experiment playbook." For tracking implementation, use analytics-tracking. For page-level conversion optimization, use conversion-optimization.
metadata:
  version: 1.0.0
  based_on_repo: coreyhaines31/marketingskills
  based_on_version: v2.11.27(28e4a81)
  based_on_skill: ab-testing
---

# Analytics: A/B Testing

Guides design of statistically valid A/B tests and ongoing experimentation programs.

## Initial Assessment

**Project context:** Read the product marketing context when present. Without it, use available project material or user-provided facts and ask for missing information.

Before designing a test, understand:

1. **Test Context** - What are you trying to improve? What change are you considering?
2. **Current State** - Baseline conversion rate? Current traffic volume?
3. **Constraints** - Technical complexity? Timeline? Tools available?

---

## Core Principles

### 1. Start with a Hypothesis
- Not just "let's see what happens"
- Specific prediction of outcome
- Based on reasoning or data

### 2. Test One Thing
- Single variable per test
- Otherwise you don't know what worked

### 3. Statistical Rigor
- Pre-determine sample size and stopping rule
- Call the test only at that sample size (see The Peeking Problem)

### 4. Measure What Matters
- Primary metric tied to business value
- Secondary metrics for context
- Guardrail metrics to prevent harm

---

## Hypothesis Framework

### Structure

```
Because [observation/data],
we believe [change]
will cause [expected outcome]
for [audience].
We'll know this is true when [metrics].
```

### Example

**Weak**: "Changing the button color might increase clicks."

**Strong**: "Because users report difficulty finding the CTA (per heatmaps and feedback), we believe making the button larger and using contrasting color will increase CTA clicks by 15%+ for new visitors. We'll measure click-through rate from page view to signup start."

---

## Test Types

| Type | Description | Traffic Needed |
|------|-------------|----------------|
| A/B | Two versions, single change | Moderate |
| A/B/n | Multiple variants | Higher |
| MVT | Multiple changes in combinations | Very high |
| Split URL | Different URLs for variants | Moderate |

---

## Sample Size

### Quick Reference

| Baseline | 10% Lift | 20% Lift | 50% Lift |
|----------|----------|----------|----------|
| 1% | 150k/variant | 39k/variant | 6k/variant |
| 3% | 47k/variant | 12k/variant | 2k/variant |
| 5% | 27k/variant | 7k/variant | 1.2k/variant |
| 10% | 12k/variant | 3k/variant | 550/variant |

For other baselines, duration math, multi-variant adjustments, online calculators, or when the required sample is too large, load [references/sample-size-guide.md](references/sample-size-guide.md).

---

## Metrics Selection

### Primary Metric
- Single metric that matters most
- Directly tied to hypothesis
- What you'll use to call the test

### Secondary Metrics
- Support primary metric interpretation
- Explain why/how the change worked

### Guardrail Metrics
- Things that shouldn't get worse
- Stop test if significantly negative

### Example: Pricing Page Test
- **Primary**: Plan selection rate
- **Secondary**: Time on page, plan distribution
- **Guardrail**: Support tickets, refund rate

---

## Designing Variants

### What to Vary

| Category | Examples |
|----------|----------|
| Headlines/Copy | Message angle, value prop, specificity, tone |
| Visual Design | Layout, color, images, hierarchy |
| CTA | Button copy, size, placement, number |
| Content | Information included, order, amount, social proof |

### Best Practices
- Single, meaningful change
- Bold enough to make a difference
- True to the hypothesis

---

## Traffic Allocation

| Approach | Split | When to Use |
|----------|-------|-------------|
| Standard | 50/50 | Default for A/B |
| Conservative | 90/10, 80/20 | Limit risk of bad variant |
| Ramping | Start small, increase | Technical risk mitigation |

**Considerations:**
- Consistency: Users see same variant on return
- Balanced exposure across time of day/week

---

## Implementation

### Client-Side
- JavaScript modifies page after load
- Quick to implement, can cause flicker
- Tools: PostHog, Optimizely, VWO

### Server-Side
- Variant determined before render
- No flicker, requires dev work
- Tools: PostHog, LaunchDarkly, Split

---

## Running the Test

### Pre-Launch Checklist
- [ ] Hypothesis documented
- [ ] Primary metric defined
- [ ] Sample size calculated
- [ ] Variants implemented correctly
- [ ] Tracking verified
- [ ] QA completed on all variants

### During the Test

- Monitor for technical issues
- Check segment quality
- Document external factors
- Keep variants and traffic sources fixed until the test ends

### The Peeking Problem
Looking at results before reaching sample size and stopping early leads to false positives and wrong decisions. Pre-commit to sample size and trust the process.

---

## Analyzing Results

### Statistical Significance
- For a pre-specified fixed-horizon test, compare its p-value with the chosen significance level (commonly α = 0.05).
- A p-value describes how incompatible the data are with the null model: the probability, **assuming that model and its assumptions**, of a result at least as extreme as the observed one. It is not the probability that the result is random, that the null is true, or that a variant will win again.
- A 95% confidence interval comes from a procedure with 95% coverage over repeated samples under its assumptions. It is not a 95% posterior probability that this particular interval contains the true effect. Report the interval and effect size alongside the p-value.
- Use the planned analysis and stopping rule. Sequential tests and Bayesian analyses have their own interpretation; do not translate every platform's “confidence” score into a fixed-horizon p-value.

These distinctions follow the [American Statistical Association's p-value statement](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf). Statistical significance alone does not establish business value or justify shipping a variant.

### Analysis Checklist

1. **Reach sample size?** If not, result is preliminary
2. **Statistically significant?** Check confidence intervals
3. **Effect size meaningful?** Compare to MDE, project impact
4. **Secondary metrics consistent?** Support the primary?
5. **Guardrail concerns?** Anything get worse?
6. **Segment differences?** Mobile vs. desktop? New vs. returning?

### Interpreting Results

| Result | Conclusion |
|--------|------------|
| Significant winner | Check effect size, uncertainty and guardrails before implementing |
| Significant loser | Keep control, learn why |
| No significant difference | Report the effect interval: it may still allow meaningful benefit and harm, or may exclude effects worth pursuing. Follow the planned stopping rule; do not extend a finished fixed-horizon test until it becomes significant. Plan a new test if needed. |
| Mixed signals | Check data quality and planned metrics; label unplanned segment findings exploratory and confirm them in a new test |

---

## Documentation

Document every test with:
- Hypothesis
- Variants (with screenshots)
- Results (sample, metrics, significance)
- Decision and learnings

**For templates**: See [references/test-templates.md](references/test-templates.md)

---

## Growth Experimentation Program

When the user wants an ongoing program rather than a single test (backlog, ICE prioritization, velocity targets, a playbook of winners, review cadence), load [references/experimentation-program.md](references/experimentation-program.md).

---

## Task-Specific Questions

1. What's the smallest improvement worth detecting?
2. Have you tested this area before?

---

## Related Skills

- **conversion-optimization**: Generating test ideas based on CRO principles
- **analytics-tracking**: Setting up test measurement
- **attribution**: Incrementality, the same controlled-experiment mindset applied to channels
- **copywriting**: Creating variant copy
