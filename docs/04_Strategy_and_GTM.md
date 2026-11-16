# 04 · Strategy, Business Model and Go-to-Market

---

## 1. Vision, mission, strategy

- **Vision:** every Indian can hand routine spending to AI agents with the same confidence they have in UPI today.
- **Mission (3 years):** make the user's side of agent payments as well-built as the merchant's side: clear boundaries, honest explanations, fast recovery.
- **Strategy in one sentence:** ship Rekha *inside* a top UPI app at the moment users link their first agent, win the "agent linking" default in the window before NPCI's Unified Agent Protocol launches, and compound a cross-agent safety advantage nobody on the agent or merchant side can match.

---

## 2. Why now (summary)

1. **Agents already pay, and the official launch is waiting on safeguards.** Pine Labs' P3P has let agents pay over UPI after one upfront approval since June 2026, and Razorpay × NPCI run in-chat checkout pilots. NPCI's Unified Agent Protocol, with user-set limits and an agent registry, was reported in September 2026; its launch was then reported paused pending regulatory clearance, with user protection and liability the open questions. Safeguards are the gating item, the consumer-control experience is undefined, and there is still time to shape it.
2. **The regulator is asking for it.** RBI's April 2026 discussion paper proposes customer-set transaction limits, a kill switch, cooling-off periods and trusted-person approval for vulnerable users.
3. **Demand exists, trust doesn't.** 100M weekly ChatGPT users in India. 74% of consumers are open to agents doing shopping tasks for them, but only 9% to agents buying on their own.
4. **The supply side is crowded.** Razorpay, Cashfree, PayU, BharatPe and Visa all shipped agentic tools in Sept 2026. The user's side is empty.

---

## 3. Market sizing

**Unit:** agent-addressable routine consumer spend over UPI, per year. All assumptions are explicit and adjustable in the case-study site's calculator.

### Bottom-up

| Step | Assumption | Source / rationale | Value |
|---|---|---|---|
| UPI users | 55.49 crore | Ministry of Finance (June 2026) | 554.9M |
| Open to an agent deciding what to buy while they make the payment | 32% | Accenture 2026 (global; applying it to India is an assumption to validate) | |
| **TAM users** | | | **177.6M** |
| Routine agent-eligible spend per user per month | Groceries/quick commerce ₹3,000 + bills & recharges ₹1,500 + travel tickets ₹700 + subscriptions ₹300 | Assumption; validate in survey | ₹5,500 |
| **TAM (GMV/yr)** | 177.6M × ₹5,500 × 12 | | **₹11.7 lakh crore** (~3.7% of FY26 UPI value) |
| AI-active UPI users today | 100M | ChatGPT weekly users in India, Feb 2026, as a proxy | 100M |
| **SAM users** | 100M × 32% | | **32M** |
| **SAM (GMV/yr)** | 32M × ₹5,500 × 12 | | **₹2.11 lakh crore** |
| **SAM, autonomous only** | 100M × 9% (open to an agent buying on its own) × ₹5,500 × 12 | Accenture 2026 | **≈ ₹59,400 crore** |
| Partner app's share of these users | 30% | Assumption: a top-3 UPI app | |
| Adoption of Rekha among them by Year 3 | 20% | Assumption | |
| **SOM users (Year 3)** | 32M × 30% × 20% | | **1.92M** |
| Share of eligible spend delegated | 40% | Assumption | ₹2,200/month |
| **SOM (GMV/yr, Year 3)** | 1.92M × ₹2,200 × 12 | | **≈ ₹5,070 crore** |
| Payments/yr at ₹450 average | | | ≈ 112.6M (≈ 4.9 per user per month) |

**Why two SAM numbers.** The 32% covers purchases an agent prepares and the user still approves, which is Rekha's L0 mode. The 9% is the smaller group open to agents paying on their own today, which is Rekha's L1 to L3. The headline SAM uses 32% because Rekha serves both; the autonomous-only figure is the floor.

### Top-down cross-check

Quick commerce alone ran at about ₹11,000 crore GMV in a single month in early 2026, which annualises to roughly ₹1.3 lakh crore. If just 10% of quick-commerce orders were placed by agents by 2029, that's ≈ ₹13,200 crore. Our Year-3 SOM of ≈ ₹5,070 crore across *all* categories through *one* partner app is well inside that envelope. The bottom-up number is conservative.

### What would change my mind

- If the survey shows routine spend per AI-active user is < ₹3,000/month, SAM halves.
- If interviews show Indians are *less* willing than the global 32% to delegate selection, SOM falls proportionally.
- If NPCI caps agent payments far below UPI Circle (e.g. ₹2,000/month), the ceiling binds and Rekha's value shifts from "more autonomy" to "safety for small payments".

---

## 4. Who pays? (the zero-MDR problem)

UPI payments from bank accounts to merchants carry **zero merchant discount rate** for most transactions, so a payments-layer product can't take a cut of each transaction the way card products do. That's the hardest strategy question for Rekha.

**November 2026 update:** NPCI planned a 0.4% MDR on select merchant payments above ₹2,000 from 15 October 2026, then deferred it. As of 16 November there is no new start date, though an NPCI circular of 11 November sets up a small-merchant incentive scheme funded from MDR, which suggests it is coming. Even then, P2P transfers, merchant payments up to ₹2,000 and small merchants stay free (more than 95% of merchant payments). A typical agent grocery order (~₹450) stays zero-MDR, so the analysis below still holds. MDR on larger payments does make large merchants care more about agent checkout quality, which strengthens the later Rekha-as-a-service option.

### Options

| Model | How it makes money | Pros | Cons | Verdict |
|---|---|---|---|---|
| **A. Standalone consumer app** (₹49/month) | Subscription | Independent brand | Needs a UPI app licence (TPAP) to sit in the payment flow; low willingness to pay for security apps in India; expensive distribution | ❌ Reject |
| **B. Rekha-as-a-service** for banks and smaller UPI apps | Per-decision fee (e.g. ₹0.05–0.10) + platform fee | Clear revenue; many buyers | Long bank sales cycles; top UPI apps may build in-house | ⏳ Later (Phase 4) |
| **C. Feature inside a top UPI app** | Strategic value: agent-payment share, engagement and credit cross-sell, lower fraud and dispute costs | Distribution, PIN and consent infrastructure, owns the "link an agent" moment | No direct revenue line; must justify on strategic value | ✅ **Recommend for v1** |
| **D. Paid agent certification** | Fees from agent developers | Revenue from the supply side | Conflicts with NPCI's own registry; looks pay-to-play | ❌ Reject |

### Value case for option C (Year 3, assumptions explicit)

| Value stream | Logic | Annual value |
|---|---|---|
| Engagement and cross-sell | 1.92M users with active agents × ₹40 incremental yearly ARPU (credit, insurance, merchant offers) | ≈ ₹7.7 crore |
| Fewer disputes | 112.6M agent payments × (0.8% baseline → 0.3%) × ₹250 handling cost per dispute | ≈ ₹14.1 crore |
| Fraud losses avoided | ₹5,070 crore GMV × (4 bps → 1 bp) | ≈ ₹1.5 crore |
| **Quantified total** | | **≈ ₹23 crore/yr** |
| Strategic: keeping agent-payment share | If agents route payments through whichever UPI app users link, the app with credible controls wins the link. That's the real prize, and it's not in the total above. | Option value |

**Cost:** a team of about 12 (2 PM, 7 engineers, 1 designer, 1 data scientist, 1 risk analyst) is roughly ₹7–9 crore/yr in India, plus about ₹1 crore infrastructure. Decision cost per payment is negligible (rules + cached embeddings); the LLM is only used when a Rekha is created or edited.

**Conclusion:** option C pays back on quantifiable value alone by Year 3, and the strategic option value (agent-payment share) is the reason to start now rather than later. A second reason appeared in September 2026: the official launch of agent payments is reported paused over user protection and liability, so an app that can show working controls and dispute evidence is better placed to be allowed to launch.

---

## 5. Competitive strategy

### Right to win (inside a UPI app)

1. **Owns the moment of trust:** linking an agent happens in the UPI app, with the UPI PIN.
2. **Neutral to agents:** the app doesn't earn from the agent's choice of product, so it can credibly judge purchases. Agent platforms can't.
3. **Cross-agent view:** only the user's payment app sees every agent's payments, which enables duplicate detection (R18) and cross-agent attack patterns.

### Moats over time (7 Powers)

| Power | How Rekha builds it |
|---|---|
| **Network effects (data)** | Every blocked attack across all agents and merchants improves detection for every user |
| **Switching costs** | Rekhas, history and earned autonomy (Trust Ramp) live in the app |
| **Counter-positioning** | Agent platforms can't be the neutral judge of their own purchases without hurting conversion |
| **Process power** | Festive calendars, red-team suites, dispute-evidence standards |
| **Branding** | "Protected by Rekha" becomes a trust signal on agent checkout |

### "What if…" scenarios

| Scenario | Likelihood | Response |
|---|---|---|
| NPCI mandates standard agent controls for all apps | Medium | Good for the category. Rekha becomes the best implementation and contributes to the standard through the UAP working group. Differentiation shifts to intent-level controls, UX and detection quality. |
| A big agent platform ships strong in-agent controls | High | Users with more than one agent still need one view; banks and regulators prefer user-side controls. Integrate: show the agent's own limits inside Rekha. |
| A rival UPI app copies Rekha | High | Expected. Win on speed, agent partnerships signed during the pilot, and data network effects. |
| Card networks bring Verifiable Intent-style proofs to UPI through partners | Medium | Treat it as an input: read the signed intent as one more signal. Rekha's value stays in the user's own app: plain-language rules, a view across agents, and recovery. |
| Agent payments grow much slower than expected | Medium | Rekha's kill switch, limits and cooling windows still serve RBI's customer-controlled safeguards agenda for *all* digital payments, not just agents. |

---

## 6. Go-to-market

### Positioning and messaging

- **Tagline:** *Draw the line for your AI agents.*
- **One-liner a user would repeat:** "My agent can pay for groceries and bills, but only what I said, only where I said, and I can stop it in one tap."
- **Launch narrative:** "RBI asked for customer-controlled safeguards, and agent payments on UPI are waiting on them. Rekha is what those safeguards look like for AI agents."

### Phased plan

| Phase | When | Goal | Key actions | Exit |
|---|---|---|---|---|
| **0. Validate** | 6 weeks | Prove the problem is real | 8 user interviews, 3 fintech expert interviews, survey (n ≥ 150), fake-door landing page, prototype usability tests (`06_Validation_Plan.md`) | Assumptions A1–A3 pass |
| **1. Shadow** | 4 weeks | Prove the engine is accurate and fast | Run on the partner's agent-payment traffic (mandate-based today, UAP once live), log only | False-block ≤ 3% on review; p95 < 300 ms |
| **2. Closed beta** | 4 weeks | Prove it's usable and safe | 5,000 invited users, L0–L1 | Dispute ≤ 0.3%, CSAT ≥ 4 |
| **3. Pilot** | 12 weeks | Prove the North Star moves | 50,000 users in 3 metros; 2 agent partners; groceries + bills + recharges | PRD §2 goals |
| **4. GA** | After festive freeze | Scale | 1% → 100% rollout; Tier-1 launch | Guardrails hold at each step |
| **5. Platform** | Year 2 | Expand | Family Rekha, Hindi, Rekha-as-a-service, credit-on-UPI | |

**Timing call:** don't take GA live during Diwali or major sale weeks. Those are peak scam season and peak traffic, so a launch-week incident would be most likely and most damaging. Launch after the festive code freeze.

### Pilot design

- **Who:** users who have linked an agent, place ≥ 4 quick-commerce orders a month and pay ≥ 3 bills a month through the app; Android and iOS; Bengaluru, Delhi NCR, Mumbai.
- **Agents:** 2 partners (one general assistant, one shopping-focused).
- **Categories:** quick-commerce groceries, utility bills, mobile recharges.
- **Holdout:** 10% of eligible users get agent payments with only the rail's own limits (no Rekha), to measure Rekha's effect on agent adoption and disputes. This is ethical because the holdout gets the same protection as the status quo, not less.

### Channels

| Channel | Mechanism |
|---|---|
| **The linking moment (primary)** | Every agent link opens the Rekha builder with a safe starter Rekha |
| **Agent partners** | "Pay with UPI, protected by Rekha" in agent checkout |
| **In-app education** | Short explainers in English and Hindi; weekly digest |
| **Family loop (Phase 5)** | Guardians set up Family Rekha for parents, so parents become users and their peers see it |
| **PR / regulator** | Submit learnings to RBI's consultation process; NPCI UAP working group |

---

## 7. Roadmap (Now / Next / Later)

| Now (Q4 2026 – Q1 2027) | Next (Q2 – Q3 2027) | Later (Q4 2027 +) |
|---|---|---|
| Validation sprint | Trust Ramp | Family Rekha (guardian mode) |
| Shadow mode on agent-payment traffic | Verified-agent badge (registry) | Credit-on-UPI support |
| MVP: builder, decision engine, approvals, activity, kill switch | Hindi (Devanagari) input | Rekha-as-a-service for banks and smaller apps |
| Intent Lock + Injection Shield v1 | Partial approvals ("pay for groceries only") | Cross-rail: card agent tokens (Visa, Mastercard) |
| Report-a-problem + evidence pack (lite) | Full dispute tracking | AP2 mandate interoperability |
| Weekly digest | ML risk model v1 (can only escalate) | Business Rekhas for small merchants |

---

## 8. Stakeholders

### Power–interest map

| | Low interest | High interest |
|---|---|---|
| **High power** | RBI (keep satisfied: consultation input) · Large agent platforms | Partner UPI app leadership · PSP bank risk team · NPCI UAP team · Legal & compliance (**manage closely**) |
| **Low power** | General public | Pilot users · Merchants · Consumer groups (**keep informed**) |

### RACI

| Activity | PM (Rekha) | Eng lead | Design | Risk & fraud | Legal | PSP partner | Agent partners |
|---|---|---|---|---|---|---|---|
| Problem validation | **A/R** | C | R | C | I | I | C |
| Decision rules R00–R18 | A | R | I | **R** | C | C | I |
| Builder UX | A | C | **R** | C | I | I | I |
| Liability and dispute language | C | I | C | C | **A/R** | C | I |
| Shadow mode and rollout | **A** | R | I | R | I | C | C |
| Agent integration (intent, trace) | A | R | I | C | C | I | **R** |

R = Responsible, A = Accountable, C = Consulted, I = Informed.

---

## 9. Pre-mortem

> *It's October 2027 and Rekha has been shut down. What happened?*

| # | Failure story | Likelihood | Impact | Early signal | Mitigation (built into the plan) |
|---|---|---|---|---|---|
| 1 | Users never customised Rekhas; the starter Rekha was "good enough" and nobody saw value | Medium | High | W1 creation rate < 20% | Templates; builder opens at the linking moment; digest shows what Rekha caught |
| 2 | Approval fatigue: users set everything to L3 or unlinked agents | Medium | High | False-ASK rate > 40% | Anomaly-only ASKs; Trust Ramp; reason-first cards |
| 3 | A festive-season false-block wave caused a social-media backlash | Medium | Medium | False-block spikes by category | Festive calendar; shadow-test new catalog categories; fast tolerance switches (see RCA in `03`) |
| 4 | Agent platforms refused to pass intent and trace | Medium | High | Partner integration slips | Rekha-only and cart-only checks still work; make trace-sharing a condition of the "registered and protected" badge |
| 5 | NPCI's liability rules put losses on the app, so legal blocked launch | Low–Med | High | Liability draft | Evidence packs designed to settle disputes fast under any regime; active participation in the working group |
| 6 | A parser bug created a looser policy and an agent overspent | Low | High | Looser-than-intended rate in sampling | Asymmetric eval gate ≤ 0.5%; user confirms every field; caps validator |
| 7 | Agent payments grew slower than expected | Medium | Medium | UAP volumes | Kill switch and limits also serve RBI's customer-safeguards agenda for all digital payments |

---

## 10. Risk register (top 5, tracked weekly)

| Risk | Owner | Status |
|---|---|---|
| UAP launch paused; registry API timing unknown | Partnerships | Open: fall back to mandate-based agent payments, and treat agents as unregistered (L0 only) until a registry exists |
| Liability regime unclear | Legal | Open: evidence pack ready for any outcome |
| Decision latency > 300 ms on low-end devices or networks | Eng | Mitigated: server-side decisions only |
| Hinglish parsing accuracy below threshold | ML | Open: eval set being built |
| Partner bank risk appetite | PM | Open: shadow-mode results are the main persuasion tool |
