# 03 · Metrics and Experiments

---

## 1. North Star Metric

### Trusted Autonomous Payments (TAP) per week

> **The number of agent-initiated payments in a week that were completed inside a Rekha without needing a step-up, and were not reported, disputed or reversed within 7 days.**

**Why this metric:**
- It captures **user value** (the agent did the job without bothering me) and **trust** (it got it right) in one number.
- It's a **leading indicator** of the business outcome: more trusted autonomous payments means more agent commerce flowing through the partner's UPI app.
- The team can move it directly through better Rekhas, smarter step-ups, Trust Ramp and safety.
- The 7-day dispute filter makes it **self-guarding**. Loosening rules to cut step-ups would raise disputes and remove those payments from the count.

**Alternatives considered and rejected:**

| Candidate | Why not |
|---|---|
| Agent GMV (₹) | Rewards bigger payments, which means more risk; one large order outweighs many small trusted ones |
| Number of Rekhas created | Vanity metric: creation without use isn't value |
| Number of blocks | Perverse: the team would "win" by blocking more |
| % auto-allowed | Easy to game by loosening rules; no quality filter |
| Weekly active users | Doesn't capture whether the agent actually did the job |

---

## 2. Metric tree

<!--tree-->
- **North Star: Trusted Autonomous Payments per week**
    - **Breadth:** users with at least one active Rekha
        - Agent link rate
        - Rekha creation rate (week 1)
        - Rekha retention (still active at day 30)
    - **Frequency:** agent payments per active user per week
        - Number of Rekha purposes per user
        - Autonomy mix: % of agents at L1 or above
        - Trust Ramp acceptance
    - **Quality:** % of payments auto-allowed and not disputed
        - Auto-allow rate
        - False-ASK rate (asks the user approves unchanged)
        - Dispute rate within 7 days
        - False-block rate

### Input metrics

| Metric | Definition | Pilot target | Owner |
|---|---|---|---|
| Agent link rate | % of eligible users who link ≥ 1 agent | 15% | Growth PM |
| Rekha creation rate (W1) | % of linked users who save a customised Rekha in week 1 | ≥ 35% | Rekha PM |
| Time to first Rekha | Median seconds from builder open to save | < 90 s | Design |
| Rekha day-30 retention | % of Rekhas still active and used at day 30 | ≥ 50% | Rekha PM |
| Autonomy mix | % of active agents at L1 or above | ≥ 40% by week 8 | Rekha PM |
| Auto-allow rate | % of agent payments ALLOWed without step-up | ≥ 60% | Risk PM |
| False-ASK rate | % of ASKs approved unchanged within 2 minutes (a proxy for "you didn't need to ask") | ≤ 35% | Risk PM |
| Step-up response time | Median time to approve or reject | < 45 s | Design |

---

## 3. Guardrails (must not get worse)

| Guardrail | Threshold | Why |
|---|---|---|
| Fraud loss on agent payments | ≤ the partner's UPI P2M baseline (basis points of value) | Rekha must not make agent payments riskier than normal UPI |
| Dispute rate (7-day) | ≤ 0.3% of agent payments | Trust |
| False-block rate | ≤ 2% (BLOCKs the user later marks "this was fine") | Don't break legitimate commerce |
| Decision latency | p95 < 300 ms, p99 < 600 ms | UPI success rates |
| UPI success rate for agent payments | Within 1 pp of non-agent P2M | Partner's core KPI |
| Kill-switch activation rate | Alert if > 3× the 4-week average in a day | Early warning of an incident or a confusing release |
| Complaints to partner support about agents | ≤ 0.5 per 1,000 agent payments | Support cost and brand |

**Goodhart check:** the team is measured on TAP *and* the guardrails together. Any experiment that lifts TAP while breaching a guardrail is a failed experiment.

---

## 4. HEART framework

| | Goal | Signal | Metric |
|---|---|---|---|
| **Happiness** | Users feel in control | Survey after week 2 | **Trust Index** (below) ≥ 4.2/5 |
| **Engagement** | Users rely on agents for routine spend | Weekly agent payments | Agent payments per active user per week |
| **Adoption** | Users set boundaries | Rekhas saved | Rekha creation rate (W1) |
| **Retention** | Users keep agents linked | Agents still linked | Linked-agent retention at day 30 / 60 |
| **Task success** | Setup and approvals are easy | Builder completion; correct approvals | Builder completion ≥ 80%; time to first Rekha < 90 s; drill accuracy ≥ 90% |

### Trust Index (3-item in-app survey, 1–5 scale)

1. "I know what my agents are allowed to spend money on."
2. "If an agent made a mistake, I could fix it quickly."
3. "I'm comfortable letting my agent pay for routine things without asking me."

---

## 5. Activation and the funnel

**Activation (hypothesis):** *user saves a customised Rekha **and** has their first protected payment within 7 days.* Hypothesis: users who reach this are ≥ 2× more likely to have an agent linked at day 30. Validate in the pilot with a cohort comparison.

| Funnel step | Pilot target (from previous step) |
|---|---|
| Eligible user sees agent-link prompt | n/a |
| Links an agent | 15% |
| Saves a customised Rekha | 60% |
| First protected payment within 7 days | 70% |
| Still linked at day 30 | 65% |
| Reaches L1+ autonomy | 50% |

---

## 6. Dashboards

| Dashboard | Audience | Tiles |
|---|---|---|
| **Weekly business review** | Leadership, partner | TAP trend, users with Rekhas, auto-allow rate, dispute rate, fraud loss vs baseline |
| **Risk operations (real time)** | Risk & fraud | BLOCKs by reason code (hourly), R14/R17 spikes, kill-switch rate, top merchants by ASK rate, new payees |
| **AI quality** | ML + PM | Parser looser-than-intended rate (sampled), user edits per Rekha draft, Intent Lock false-ASK rate, eval regression status |
| **Experience** | Design + PM | Time to first Rekha, builder drop-off by step, step-up response time, Trust Index |

### SQL: North Star

```sql
-- Trusted Autonomous Payments per ISO week
SELECT
  DATE_TRUNC('week', d.created_at AT TIME ZONE 'Asia/Kolkata') AS week_ist,
  COUNT(*) AS trusted_autonomous_payments
FROM decisions d
JOIN payments p ON p.request_id = d.request_id
LEFT JOIN disputes x
  ON x.request_id = d.request_id
 AND x.created_at <= p.completed_at + INTERVAL '7 days'
WHERE d.decision = 'ALLOW'
  AND p.status = 'SUCCESS'
  AND p.reversed = FALSE
  AND x.request_id IS NULL               -- no dispute or report within 7 days
  AND p.completed_at <= NOW() - INTERVAL '7 days'  -- only fully matured payments
GROUP BY 1
ORDER BY 1;
```

---

## 7. Experiments

Sample sizes use a two-sided test at α = 0.05 and 80% power:
n per arm ≈ (1.96 + 0.84)² × [p₁(1−p₁) + p₂(1−p₂)] ÷ (p₂ − p₁)²

### E1: Trust Ramp nudge

| | |
|---|---|
| **Hypothesis** | We believe offering a one-tap upgrade to L1 after 5 clean payments, with the agent's track record, will increase the share of agents at L1+ because users trust evidence of past behaviour (Accenture: 31% say low-cost, low-risk purchases would make them more comfortable). |
| **Population** | Users whose agent has ≥ 5 clean payments at L0 |
| **Variants** | Control: no prompt (users can change autonomy in settings). Treatment: Trust Ramp card in the activity feed and digest. |
| **Primary metric** | % of eligible agents at L1+ at day 28 after eligibility |
| **Baseline → MDE** | 20% → 23% (+3 pp absolute) |
| **Sample size** | **2,940 per arm** (5,880 total) |
| **Duration** | ~4 weeks to accrue at expected eligibility rates in a 50k pilot, plus 28-day measurement |
| **Guardrails** | Dispute rate among upgraded agents; kill-switch rate; ASK→reject rate after upgrade |
| **Decision rule** | Ship if primary is significant **and** guardrails don't worsen beyond noise. If uptake rises but disputes rise too, the ramp threshold (5 payments) is too low: test 10. |

### E2: Plain-language builder vs form builder

| | |
|---|---|
| **Hypothesis** | We believe the plain-language builder will increase Rekha completion vs a classic form, because users describe intent more naturally than they fill structured fields. |
| **Variants** | Control: form (purpose dropdown, merchants, amount, period). Treatment: text box + structured confirm card. |
| **Primary metric** | Rekha save rate among users who open the builder |
| **Baseline → MDE** | 55% → 62% (+7 pp) |
| **Sample size** | **774 per arm** |
| **Secondary** | Time to save; fields edited after parse; looser-than-intended rate (sampled human review) |
| **Guardrails** | Looser-than-intended rate must stay ≤ 0.5% (a safety guardrail inside a UX test) |
| **Watch out for** | Novelty effect: compare week 1 vs week 2 of exposure before deciding |

### E3: Reason-first approval card ("safety drills")

| | |
|---|---|
| **Hypothesis** | We believe leading the approval card with the reason ("Not groceries: air fryer, ₹3,999") rather than the amount will raise correct rejections of suspicious requests, because users decide on the first line they read. |
| **Method** | Opt-in **safety drills**, borrowed from corporate phishing simulations. Users who opt in occasionally receive a realistic simulated suspicious request. No money moves; it's revealed as a drill after they respond. This gives ground truth without exposing anyone to real fraud. |
| **Primary metric** | % of drill requests correctly rejected |
| **Baseline → MDE** | 80% → 88% |
| **Sample size** | **326 per arm** (drill responses) |
| **Guardrails** | Time to decide on real ASKs; drill opt-out rate (if > 20%, drills are annoying) |

### Pitfalls checklist (applies to all)

- **Sample ratio mismatch:** check the split is 50/50 within ±1% before reading results.
- **No peeking:** fixed horizon, or a sequential test with pre-registered stopping rules.
- **Novelty:** compare early vs late exposure.
- **Interference:** users with Family Rekha share agents; randomise by household.
- **Multiple comparisons:** one primary metric per test; secondaries are directional only.
- **Variance reduction:** CUPED with each user's pre-period agent-payment count.

---

## 8. How we test safety features (and why not with an A/B test)

You **cannot** run a control arm where Injection Shield is off for real users. That means knowingly letting manipulated payments through. Instead:

1. **Shadow mode** (Phase 0): the engine logs what it *would* do on real traffic without enforcing. A risk analyst reviews a stratified sample of 1,000 decisions to estimate precision and recall.
2. **Red-team suite:** 20 scripted attack scenarios (`05_Trust_Safety_Threat_Model.md`) run against every release. Recall must be ≥ 95%.
3. **Staged rollout with monitoring:** 1% → 10% → 50% → 100%, watching false-block rate and partner success rate at each step.
4. **Safety drills** (E3) to measure the human part of the loop.

---

## 9. Root-cause analysis: worked example

> **Prompt:** "On 21 Oct 2026, the false-block rate tripled from 1.6% to 4.9%. Users are complaining on social media that Rekha is blocking their Diwali orders. What do you do?"

**Step 1: Clarify the metric and scope.** False-block = BLOCK or ASK-then-rejected decisions that users later mark "this was fine". The jump started around 18:00 IST on 20 Oct. Is this all agents or one? All merchants or some? All cities?

**Step 2: Check the data first.** Was there an instrumentation change? A new "mark as fine" button placement could inflate reports. *Finding: no client release in 7 days; logging volumes normal. The rise is real.*

**Step 3: Internal changes.** Rule or threshold deploys? Parser model update? Merchant data sync? *Finding: no rule changes. The merchant catalog sync ran as usual.*

**Step 4: External factors.** Diwali sales started 20 Oct. Quick-commerce merchants launched festive gift bundles ("Diwali dry-fruit hamper", "pooja kit"). Order sizes are up.

**Step 5: Segment.** Break false-blocks down by reason code:

| Reason | Share of false-blocks, normal week | Share, 20–21 Oct |
|---|---|---|
| R11 Intent mismatch | 34% | **71%** |
| R13 Price anomaly | 22% | 14% |
| R12 Quantity spike | 18% | 9% |
| Others | 26% | 6% |

R11 dominates, concentrated in 3 quick-commerce merchants and in items with category "Gifting/Festive".

**Step 6: Hypothesis.** Festive bundle SKUs are new, so they're missing from the reference catalog and tagged with a new "Gifting" category. A grocery Rekha's intent ("weekly groceries") doesn't map to "Gifting", so Intent Lock scores them low even when the bundle is mostly groceries (dry fruits, sweets).

**Step 7: Validate.** Pull 200 R11 false-blocks: 168 (84%) contain at least one SKU created after 15 Oct with category "Gifting". Hypothesis confirmed.

**Step 8: Fix now, fix properly, prevent.**
- **Now (hours):** for registered agents at allow-listed merchants, temporarily treat "Gifting" items whose components map to the Rekha's categories as in-scope, capped at the Rekha budget. Send a clear in-app note to affected users.
- **Properly (days):** ingest merchants' festive catalogs 7 days ahead; map bundles to component categories.
- **Prevent (process):** add a "festive calendar" to the risk ops runbook (Diwali, Holi, Eid, Christmas, big sale days); run shadow-mode checks on new catalog categories before they go live.
- **Guardrail check:** confirm R14 (payee mismatch) and R05 (P2P) are untouched. Festive season is also scam season, and the fix must not loosen hard rules.

**Takeaway:** structure (data → internal → external → segment → hypothesis → validate → fix/prevent) beats guessing, and every fix is checked against a guardrail.

---

## 10. A second, shorter example

> "Rekha creation rate in week 1 fell from 38% to 27% after the partner app's 4.12 release."

The same method, compressed:
- Data: did the `rekha_created` event change name or move to a different screen?
- Internal: did 4.12 move the builder entry point? Change the default template? Add a PIN step earlier?
- Segment: Android vs iOS, app version, language, new vs existing users, agent type.
- Likely cause in this kind of case: an entry point moved below the fold, or a new mandatory step (such as PIN before preview) added friction.
- Validate: funnel by step, by app version, in the week before and after.
