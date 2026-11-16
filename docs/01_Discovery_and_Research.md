# 01 · Discovery and Research

- **Product:** Rekha (रेखा, "line"): draw the line for your AI agents.
- **Stage:** Problem discovery is complete from secondary research. Primary research (interviews, survey, usability tests) is designed in `06_Validation_Plan.md` and is the next step.
- **How to read this:** every user-level claim is labelled **[Evidence]** (a published source) or **[Hypothesis]** (still to be tested with users).
- **Last updated:** 17 November 2026.

---

## 1. Problem statement

> AI agents in India can now pay over UPI, but the only control a user gets is a **monthly amount cap**. A cap limits *how much* an agent can lose. It says nothing about *what* the agent is allowed to buy, *from whom*, or *whether this payment matches what I actually asked for*. So most people won't let agents pay at all, and the ones who do are exposed to mistakes and manipulation that a cap can't catch.

**The trust gap in one line [Evidence]:** 74% of consumers are open to an AI agent completing specific shopping tasks for them. Only **9%** are open to it buying on its own, even with guardrails they set themselves (Accenture, *Talk to my AI agent*, Consumer Pulse 2026: 25,590 consumers in 16 countries, surveyed January 2026).

**Rekha's thesis [Hypothesis]:** the 9% were already offered guardrails in the abstract, so a promise of guardrails is not enough. Rekha's bet is that the gap narrows when three things are true. First, controls work at the level people think in (intent: *"weekly groceries, under ₹2,500, from these two apps, no alcohol"*) instead of the level the rails think in (amount: *"₹15,000 per month"*). Second, people can see each check and undo a mistake. Third, autonomy is earned on small, low-risk purchases. Accenture's data points the same way: 31% say low-cost, low-risk purchases would make them more comfortable.

---

## 2. Why now: the 2024–2026 timeline

| When | What happened | Why it matters for Rekha |
|---|---|---|
| 2024 | NPCI launches **UPI Circle**: delegate payments to a secondary user (full delegation capped at ₹15,000/month and ₹5,000/transaction) | Delegation rail exists, but it was designed for family members, not software |
| Sep 2025 | Google announces **AP2** (Agent Payments Protocol) with Intent, Cart and Payment mandates, 60+ partners | Industry converging on "bind the payment to the user's intent", which is Rekha's core idea |
| Oct 2025 | **NPCI × OpenAI × Razorpay** pilot agentic UPI payments in ChatGPT (Axis Bank, Airtel Payments Bank; BigBasket among first merchants) | Agent payments in India are real, starting with groceries |
| Nov 2025 | **DPDP Rules 2025** notified (13 Nov); phased to May 2027 | Intent and cart data is personal data; privacy-by-design is mandatory |
| Feb 2026 | **Razorpay × NPCI** launch agentic UPI checkout on Anthropic's **Claude** (pilot; Zomato, Swiggy, Zepto) | A second AI assistant gets UPI checkout; food and quick commerce lead |
| Feb 2026 | ChatGPT reaches **100M weekly active users in India**, its second-largest market | A large, agent-ready user base exists |
| Mar 2026 | **Mastercard and Google publish Verifiable Intent**: an open standard that records who the agent is, what the user asked for and what was bought | The card world is converging on proof of intent. Nothing equivalent exists for a UPI user. |
| Mar 2026 | **Razorpay Agent Studio**; **Cashfree Here** (with Mastercard, Swiggy) | Merchant and payment-gateway side is being built fast |
| Apr 2026 | **RBI discussion paper** on digital-payment fraud safeguards: cooling-off periods, trusted-person approval for vulnerable users, **customer-set limits and a kill switch** | The regulator is asking for exactly the controls Rekha provides |
| Jun 2026 | **Pine Labs P3P goes live**: AI agents complete UPI payments after a single upfront authorisation, using one-time mandates and Reserve Pay | Agents can already pay today. The only user control is the size of the mandate. |
| Jun 2026 | Accenture consumer study: 85% / 74% / 32% / 9% across four levels of agent autonomy | Quantifies the trust gap, and shows that offering guardrails alone doesn't close it |
| Jun 2026 | RBI issues final bank directions on digital-fraud conduct and compensation, effective **1 Jan 2027** | Customer-protection obligations on banks arrive in 2027 |
| Aug 2026 | UPI hits a record **24.51 billion** transactions in a month; turns 10 | Scale of the rail |
| **Sep 2026** | **NPCI's agent-payments launch is paused.** Reuters (1 Sep) reported a Unified Agent Protocol (also written "Unified Agentic Protocol"): small agent payments without per-payment approval, user-set rules and limits, built on UPI Circle and Reserve Pay, with an agent registry. Business Standard (11 Sep) then reported the launch was put on hold pending regulatory clearance, with user protection and liability the open questions. Neither NPCI nor RBI has confirmed details on the record. | Safeguards are the gating item. The user-side control layer and the dispute story are exactly what is missing. |
| 10 Sep 2026 | Visa, Mastercard and Ant International start work on shared "Know Your Agent" principles | Networks are standardising how agents are identified, not what users can control |
| 11 Sep 2026 | **Visa** launches agentic commerce experiences in India with banks and major payment gateways | Card networks are moving too; the market will be multi-rail |
| 25 Sep 2026 | Razorpay, Cashfree, BharatPe, PayU launch agentic AI suites | Supply side is crowded; the consumer trust side isn't |
| Oct 2026 | UPI's record month: **25.47 billion** transactions, ₹31.53 lakh crore. NPCI defers a planned **0.4% MDR** on select merchant payments above ₹2,000; no new start date as of mid-November | Scale keeps growing; most small merchant payments stay free, which shapes "who pays" |
| Nov 2026 | DPDP consent-manager framework in force (13 Nov). CERT-In guidance on agentic AI reportedly covers permissions, delegation, logging and emergency stops | Consent, revocation and kill switches become standard expectations |

**The window:** agents can already pay over UPI (P3P, in-chat pilots). The official protocol to scale it is paused while safeguards are worked out, and RBI has publicly asked for customer-set limits and kill switches. The first UPI app to show credible agent controls and dispute evidence is best placed to launch, and can shape the protocol while it is still being designed.

---

## 3. Market facts

| Fact | Value | Source |
|---|---|---|
| UPI users onboarded | 55.49 crore (June 2026) | Ministry of Finance reply, via CA Club India |
| UPI volume, Oct 2026 (record) | 25.47 billion transactions, ₹31.53 lakh crore; ~822M/day; average daily value above ₹1 lakh crore for the first time | NPCI data via Free Press Journal / Entrepreneur India |
| UPI merchant fees | 0.4% MDR planned on select merchant payments above ₹2,000 from 15 Oct 2026, then deferred; no new start date as of 16 Nov 2026. P2P transfers, merchant payments up to ₹2,000 and small merchants stay free (more than 95% of merchant payments) | The Week; SCC Online; MediaNama |
| UPI volume, FY2025-26 | 24,161.69 crore transactions, ₹314.23 lakh crore | Ministry of Finance, via CA Club India |
| ChatGPT weekly users in India | 100 million (Feb 2026) | Sam Altman, via Social Samosa |
| Consumers open to working with an agent to find the best option | 85% | Accenture 2026 |
| …to an agent completing specific shopping tasks on request | 74% | Accenture 2026 |
| …to an agent deciding what to buy while they make the payment | 32% | Accenture 2026 |
| …to an agent buying on its own, with guardrails they set | 9% | Accenture 2026 |
| …who say low-cost, low-risk purchases would make them more comfortable | 31% | Accenture 2026 |
| US online adults trusting agents for routine purchases | 24% (Mar 2025) | Forrester |
| UPI fraud, FY2024-25 | 12.64 lakh cases, ₹981 crore | Ministry of Finance in Lok Sabha |
| Prompt-injection attacks on web agents | "partially succeeded in 86% of cases" (Meta research) | The Register, Oct 2025 |
| Agentic commerce by 2030 (global) | $3–5 trillion (McKinsey); US agentic GMV $190–385B (Morgan Stanley) | Digital Commerce 360; Yahoo Finance |
| Quick commerce, India | ~7.8M orders/day; ~₹11,000 crore GMV in one month in early 2026 | Digital in Asia |
| UPI Circle limits | Full delegation: ₹15,000/month, ₹5,000/transaction; up to 5 delegates | PhonePe Business; Ujjivan SFB |
| Reserve Pay | Funds blocked for multiple debits (cap ₹10,000, up to 90 days; may be revisited for agents) | Reuters via The Star |

---

## 4. Existing-product teardown: why today's tools break for agents

This is the "existing product" half of the project: an analysis of what already exists, where it falls short for agents, and what Rekha borrows from each.

| Existing tool | What it does well | Where it breaks for AI agents | What Rekha keeps |
|---|---|---|---|
| **UPI Circle, full delegation** | Lets someone else pay from your account within caps, no PIN each time | **Amount-only.** It can't express "groceries only" or "not to a new person". One cap covers everything the delegate does. You only see what happened afterwards. | The rail and its caps; Rekha sub-divides them |
| **UPI Circle, partial delegation** | Every payment needs the primary user's PIN | Safe but defeats automation. Approving everything leads to **approval fatigue**: people approve without reading (the same failure as MFA "push bombing" in security) | Step-up approval, but *only when something is unusual* |
| **Reserve Pay** | Blocks funds once, allows multiple debits | Tied to one merchant relationship; agents shop across many merchants | Budget envelopes |
| **UPI AutoPay (e-mandates)** | Recurring payments to a fixed merchant | Fixed merchant, fixed/max amount; one mandate per relationship; can't handle open-ended shopping | Bill-pay Rekhas use the same mental model |
| **In-chat checkout** (e.g. ChatGPT × Razorpay pilot) | Smooth: discover, decide and pay inside the conversation | **Controls live inside the agent's own product**, so the agent marks its own homework. Three agents mean three separate control panels and no single view of what all your agents spent. | Seamless checkout as the default path |
| **Bank card controls** | On/off, channel limits | Card-level, not agent-level; no idea what was bought | Kill switch |
| **Google AP2** | Signed *intent* mandate + *cart* mandate that must match: the right idea | A developer protocol, not a consumer product; global and card-first; adoption depends on agent platforms | Intent-to-cart matching (Rekha's "Intent Lock") |
| **Mastercard Verifiable Intent** (cards, Mar 2026) | A signed record linking who the agent is, what was asked and what was bought | Card rails; built for networks, issuers and developers, not a control a UPI user sets in their own app | Proof of intent, kept for disputes |
| **Pine Labs P3P** (live, Jun 2026) | Agent pays after one upfront authorisation (one-time mandate / Reserve Pay) | After that single approval, the **mandate amount is the only check**. It sits on the merchant/gateway side, so it can't see your other agents. | Upfront approval, but scoped per purpose |
| **NPCI Unified Agent Protocol** (launch paused) | Planned agent registry, delegated limits, interoperability, settlement finality | Will define the rail and rules; leaves **user experience and dispute evidence** to apps; needs RBI approval; liability still open | Registry lookups ("Verified agent" badge); the rail's limits as the outer boundary |

**Synthesis:** on UPI, every existing tool controls *amount* or *merchant*. None controls *intent*. The work that comes closest (AP2 and Mastercard's Verifiable Intent on cards, in-chat checkout) sits with networks, developers and agents. **The user's side, inside the UPI app, is still empty.**

---

## 5. Users

### Segments

| Segment | Size signal | Primary job | Rekha priority |
|---|---|---|---|
| **Urban AI-native delegators** (22–40, metro, daily AI-assistant users, frequent quick-commerce users) | Overlap of 100M ChatGPT WAU and frequent online shoppers | Offload routine purchases | **Beachhead (pilot)** |
| **Family guardians** (25–45, manage parents' digital life) | Large; the "tech person" in most Indian families | Let parents benefit from agents safely | Phase 2 |
| **Cautious bill-payers** (45+, tier-1/2, have seen UPI scams) | Large, lower AI adoption today | Never miss a bill, never get cheated | Phase 2 (via guardians) |
| **Small merchants / sole proprietors** | Very large | Agent pays vendors, utilities | Later (business Rekhas) |

**Beachhead rationale:** the delegators already use agents and already shop online weekly, so the value of Rekha shows within days. They're also the most likely early users of today's agent checkouts and of any UAP pilot.

### Proto-personas **[Hypothesis, validate with interviews]**

**Priya, 29, product designer, Bengaluru: "The Delegator"**
- Uses an AI assistant daily; orders groceries on quick commerce 3×/week; pays 6 bills a month.
- *Wants:* "I want my weekly groceries and bills to just happen."
- *Fears:* the agent orders 10 kg instead of 1 kg; a fake "discount" page tricks it; she won't notice until the bank SMS.
- *Current workaround:* lets the agent build the cart, then pays manually. Saves maybe 30% of the effort.

**Rajesh, 54, shop owner, Lucknow: "The Cautious Bill-Payer"**
- Uses UPI daily for business; has been targeted by "refund" scam calls; his son set up most of his apps.
- *Wants:* electricity, gas and phone recharges paid on time without remembering dates.
- *Fears:* "Someone will empty my account and the bank will say I authorised it."
- *Current workaround:* son pays some bills from his own phone; occasional late fees.

**Arjun, 34, IT manager, Gurugram: "The Family Guardian"**
- Manages his parents' (in Kanpur) phones, bills and medicine orders remotely.
- *Wants:* parents' assistant can reorder medicines and pay bills; he sees everything and can stop anything.
- *Fears:* parents approving something they don't understand.
- *Current workaround:* parents call him before every online payment.

**B2B stakeholders (Rekha ships inside a UPI app, so these matter as much as end users):**
- **Head of Payments Product at a UPI app:** wants agent-commerce share without becoming the face of an agent fraud scandal.
- **Fraud/risk lead at a PSP bank:** wants lower dispute volume and clear evidence when agents go wrong.
- **Agent developer:** wants high payment success with minimal friction, and a "verified" signal that increases user trust.
- **Merchant (quick commerce):** wants agent orders to convert, without chargebacks or disputes.

### Jobs To Be Done

**Core job [Hypothesis]**
> When I hand a routine purchase to an AI agent, I want to set exactly how far it can go, so I can stop thinking about it without worrying that it will overspend, be tricked, or buy the wrong thing.

| Job type | Job statement |
|---|---|
| Functional | Get routine purchases and bills done without my attention |
| Functional | Know at a glance what every agent spent, where, and why |
| Functional | Undo or dispute a wrong agent payment quickly |
| Emotional | Feel in control; not feel foolish for trusting a bot |
| Social | Be the responsible one who protects the family's money |

**Competing solutions for the job ("what do people hire today?"):** paying manually; letting the agent build the cart and paying yourself; asking a family member; AutoPay for fixed bills; not using agents at all. The last one, *not using agents*, is the real competitor.

---

## 6. Pain points and opportunities

| # | Opportunity (user need) | Evidence level |
|---|---|---|
| O1 | "I don't know what my agent is allowed to do." Controls are unclear or amount-only. | [Evidence] UPI Circle limits and the reported UAP design are amount-based; [Hypothesis] users feel this |
| O2 | "I'm scared it'll be tricked." Fear of manipulation and fraud. | [Evidence] Prompt-injection research; UPI fraud scale; Acosta: top concerns include unapproved purchases and fraud |
| O3 | "If it messes up, I'm stuck." No clear undo or dispute path. | [Evidence] UAP liability regime under discussion; [Hypothesis] user concern |
| O4 | "Too many approval pings and I stop reading them." | [Evidence] MFA-fatigue analogue in security; [Hypothesis] for payments |
| O5 | "My parents can't manage this safely." | [Evidence] RBI proposal: trusted-person approval for vulnerable users; [Hypothesis] demand |
| O6 | "I'd trust it more once I've seen it work." | [Evidence] Accenture: 31% say low-cost, low-risk purchases would make them more comfortable |

---

## 7. Opportunity Solution Tree

<!--tree-->
- **Outcome:** more routine purchases completed by agents without per-payment approval, with fraud and disputes at or below baseline
    - **O1 · Unclear controls**
        - Plain-language Rekha builder that produces a structured policy card. *Test: plain-language builder against a form.*
        - Autonomy ladder, L0 to L3, with safe presets
    - **O2 · Fear of being tricked**
        - Intent Lock: the cart must match the intent. *Test: Intent Lock in shadow mode on pilot traffic.*
        - Injection Shield: payee, price and provenance checks
        - Verified-agent badge from the NPCI registry
    - **O3 · No way back**
        - Kill switch: pause every agent in one tap
        - One-tap dispute with an automatic evidence pack
        - Cooling window for first-time payees
    - **O4 · Approval fatigue**
        - Step-up only on anomalies, with the reason first
        - Trust Ramp: autonomy earned after clean payments. *Test: Trust Ramp nudge.*
        - Weekly agent digest
    - **O5 · Vulnerable family members**
        - Family Rekha: guardian co-approval

---

## 8. Assumption map

Risk = importance if wrong × how little evidence we have. Test the top-right first.

| # | Assumption | Risk type | Importance | Evidence today | Test | Pass signal |
|---|---|---|---|---|---|---|
| A1 | AI-assistant users *want* agents to pay for routine purchases | Value | High | Medium (Accenture 32%) | Survey (n ≥ 150) + 8 interviews | ≥ 30% of AI users say they'd delegate at least one category with controls |
| A2 | Fear of mistakes/fraud, not lack of need, is the main blocker | Value | High | Medium | Interviews: ask about the last time they *didn't* let an agent pay | ≥ 5 of 8 cite control or safety |
| A3 | Users can set up a Rekha in under 90 seconds | Usability | High | None | Prototype usability test (5–6 users) | ≥ 80% task success, median < 90 s |
| A4 | Users understand step-up reasons and decide correctly | Usability | High | None | Usability test with seeded "bad" payments | ≥ 90% correct reject on seeded attacks |
| A5 | Agent platforms will share intent and decision trace | Feasibility | High | Low | 3 expert interviews with agent developers; read UAP and AP2 specs | Specs or devs support passing intent + cart |
| A6 | A UPI app or PSP bank sees strategic value | Viability | High | Medium (RBI direction, UAP) | 3 expert interviews with fintech PMs | ≥ 2 say "we'd prioritise this in 2027" |
| A7 | Decisions can be made in < 300 ms p95 | Feasibility | Medium | Medium (rules are cheap; LLM kept off the hot path) | Engineering spike | Benchmark |
| A8 | Users will accept a cooling window for first-time payees | Usability | Medium | Low | Survey preference question | ≥ 60% accept for amounts > ₹2,000 |
| A9 | Guardians will set up Family Rekha for parents | Value | Medium | Low | 4 guardian interviews | ≥ 3 would set up within a week |

---

## 9. Competitive landscape

### Map by layer

```
 USER'S SIDE  │  Rekha  ← intent-level controls, cross-agent view, disputes, kill switch
──────────────┼──────────────────────────────────────────────────────────────────────
 AGENT        │  ChatGPT, Gemini, assistants with in-chat checkout (each controls only itself)
 PROTOCOLS    │  Google AP2 · Mastercard Verifiable Intent · OpenAI/Stripe ACP · Pine Labs Grantex · NPCI UAP (paused)
 NETWORKS     │  UPI (UPI Circle, Reserve Pay, AutoPay) · Visa Trusted Agent Protocol · Mastercard Agent Pay
 MERCHANT/PG  │  Pine Labs P3P (live) · Razorpay Agentic Payments & Agent Studio · Cashfree Here · PayU · Juspay
```

### Comparison

| Player | Layer | Intent-aware? | Cross-agent view? | User-side? | India UPI? | Threat to Rekha |
|---|---|---|---|---|---|---|
| NPCI UAP (launch paused) | Rail + registry | No (limits) | N/A | Partly (sets limits) | Yes | **Tailwind**: defines the outer boundary Rekha works within |
| UPI Circle | Rail | No | No | Yes | Yes | Base layer |
| Google AP2 | Protocol | **Yes** | No | No (developer) | Not yet | Complement; Rekha can consume AP2 mandates |
| OpenAI/Stripe ACP | Merchant protocol | Partly | No | No | Limited | Complement |
| In-chat checkout (ChatGPT etc.) | Agent | Partly | **No** | No (agent's side) | Yes (pilot) | Medium: "good enough" controls inside each agent |
| Mastercard Agent Pay + Verifiable Intent (with Google, Mar 2026) | Network (cards) | **Yes** (signed record of identity, intent and action) | No | No (networks, issuers, developers; an issuer's app can revoke an agent) | Cards | Medium: it validates intent-matching. Rekha is the UPI, user-side version. |
| Visa Trusted Agent Protocol (Oct 2025) | Network (cards) | No (verifies the agent to the merchant) | No | No | Cards | Low |
| Visa × Mastercard × Ant "Know Your Agent" (Sep 2026) | Networks | No (agent identity and monitoring) | No | No | No | Low; shows where standards are heading |
| Pine Labs P3P + Grantex (live, Jun 2026) | Merchant gateway + agent authorisation | Partly (scoped permissions, expiry, mandate amount) | No | No (merchant side) | **Yes** | **Medium to high**: the closest live product on UPI. No cross-agent view, and no check of the cart against what the user asked. |
| Skyfire KYAPay | Agent identity + payments (global) | Partly (authorisation scope in the token) | No | No (developers, businesses) | No | Low |
| Razorpay / Cashfree / PayU | Merchant PG | No | No | No | Yes | Low: merchant-side |
| UPI apps (PhonePe, Google Pay, Paytm…) | Consumer app | Not yet | Possible | **Yes** | Yes | **The natural owner.** Rekha is designed to ship *inside* one of them. |

*The card-network and startup rows rely on press coverage and company posts. I have not tested those products.*

### Positioning statement

> **For** people who use AI agents for routine spending, **who** don't trust them with money yet, **Rekha is** an agent-permissions layer inside your UPI app **that** lets you set what each agent may buy, from whom and up to how much, and checks every payment against what you asked for. **Unlike** the limits inside each agent's own app or plain UPI caps, **Rekha** sits on your side, covers every agent in one place, and stops payments that don't match your intent.

---

## 10. Key insights (the "aha" moments)

1. **The risk isn't how much. It's what.** Caps limit damage; intent-matching prevents it. A prompt-injected agent can stay perfectly within a ₹15,000 cap while buying the wrong thing from the wrong merchant.
2. **Agent-side controls have a conflict of interest.** The platform that earns from completed purchases shouldn't be the only one deciding whether a purchase is OK.
3. **"Human in the loop" fails when the loop is constant.** Approval fatigue turns humans into rubber stamps. Ask rarely, ask clearly, and the human becomes a real safeguard again.
4. **A promise of guardrails isn't enough; trust is earned.** Accenture's 9% were already offered guardrails they set themselves. What helps is experience: 31% say low-cost, low-risk purchases would make them more comfortable. So Rekha starts agents small and lets them *earn* autonomy, which is where the Trust Ramp comes from.
5. **People want a role, not a choice between all or nothing.** Far more people are open to an agent deciding while they pay (32%) than to an agent buying alone (9%). Rekha's autonomy ladder gives them four positions, not two.

---

## Sources

- Accenture, *Talk to my AI agent* (Consumer Pulse 2026): https://www.accenture.com/in-en/insights/consulting/talk-my-ai-agent
- Accenture Consumer Pulse 2026, full report (PDF): https://www.accenture.com/content/dam/accenture/final/accenture-com/document-fy26/q4/Accenture-Consumer-Pulse-2026.pdf
- UAP launch put on hold (Business Standard, 11 Sep 2026): https://www.business-standard.com/finance/news/upi-s-ai-protocol-temporarily-on-hold-as-npci-builds-safeguards-126091101413_1.html
- Mastercard Verifiable Intent (Mastercard, Mar 2026): https://www.mastercard.com/in/en/news-and-trends/stories/2026/verifiable-intent.html
- Ant International, Mastercard and Visa on Know Your Agent (The Asian Banker, 10 Sep 2026): https://www.theasianbanker.com/press-releases/ant-international-mastercard-and-visa-initiate-collaboration-on-know-your-agent-interoperability-to-scale-agentic-commerce
- Skyfire, *The trust gap in AI agent payments* (Mar 2026): https://skyfire.xyz/the-trust-gap-in-ai-agent-payments/
- Pine Labs on Grantex and the agent economy (YourStory, Nov 2026): https://yourstory.com/2026/11/how-pine-labs-is-building-for-the-agent-economy-cto-sanjeev-kumar-on-trust-control-and-execution
- NPCI's UPI MDR FAQs explained (SCC Online, 16 Sep 2026): https://www.scconline.com/blog/post/2026/09/16/npci-released-upi-mdr-faqs-explained/
- UPI MDR still pending; Vyapaar Saksham scheme (MediaNama, 16 Nov 2026): https://medianama.com/2026/11/223-npci-upi-mdr-vyapaar-saksham-scheme
- Forrester consumer pulse (US): https://www.forrester.com/report/many-us-consumers-believe-in-agentic-commerce-but-few-trust-it-to-make-purchases/RES188737
- Acosta-cited trust concerns, via Let's Data Science: https://letsdatascience.com/news/consumers-place-growing-trust-in-ai-shopping-agents-1e3ca4f7
- India preparing agentic payments on UPI (Reuters via The Star, 1 Sep 2026): https://www.thestar.com.my/tech/tech-news/2026/09/01/india-preparing-rollout-of-agentic-payments-on-upi-sources-say
- NPCI's GFF 2026 announcements (Inc42, 11 Sep 2026; UAP not among them): https://inc42.com/buzz/gff-2026-npci-unveils-unified-ticketing-takes-rupay-credit-card-on-upi-to-us-uae/
- NPCI agent framework coverage incl. chairman quote (CareerIndia): https://www.careerindia.com/news/ai-agent-upi-payments-npci-framework-fintech-hiring-trends-2026-011-65443.html
- UAP and RBI approval (Business Standard via Vision IAS): https://visionias.in/current-affairs/upsc-daily-news-summary/article/2026-07-09/business-standard/economy/india-may-allow-agentic-ai-led-upi-transactions-under-new-npci-protocol
- Pine Labs P3P launch (Pine Labs press release, Jun 2026): https://www.pinelabs.com/media-analyst/the-ai-agent-can-now-pay-pine-labs-launches-p3p-indias-first-agentic-payment-protocol-built-on-upi
- Razorpay × NPCI agentic payments on Claude (Razorpay newsroom, Feb 2026): https://razorpay.com/newsroom/razorpay-npci-launch-agentic-payments-on-claude-powering-zomato-swiggy-zepto-at-the-india-ai-impact-summit/
- UPI October 2026 record (Free Press Journal): https://www.freepressjournal.in/business/upi-transactions-hit-2547-billion-in-october-value-soars-to-3153-lakh-crore
- UPI MDR deferred until after Diwali (The Week, 13 Oct 2026): https://www.theweek.in/news/biz-tech/2026/10/13/npci-defers-upi-mdr-until-after-diwali.html
- RBI final digital-fraud directions, effective 1 Jan 2027 (Moneylife): https://moneylife.in/article/rbi-notifies-digital-fraud-compensation-rules-gives-banks-more-time-delays-rollout/80882.html
- CERT-In agentic AI audit guidance (Let's Data Science summary): https://letsdatascience.com/news/cert-in-issues-ai-security-auditing-guidelines-covering-agen-6e37b2b9
- NPCI agentic payments report (Inc42): https://inc42.com/?p=570783
- India preparing agentic payments on UPI (The Star / Reuters): https://www.thestar.com.my/tech/tech-news/2026/09/01/india-preparing-rollout-of-agentic-payments-on-upi-sources-say
- NPCI × OpenAI × Razorpay ChatGPT pilot (Storyboard18): https://storyboard18.com/digital/razorpay-npci-partner-with-openai-for-agentic-payments-on-chatgpt-82299.htm
- UPI Circle explained (PhonePe Business): https://business.phonepe.com/articles/upi-circle-what-it-is-how-it-works-and-who-can-use-it
- UPI Circle limits (Ujjivan SFB): https://www.ujjivansfb.bank.in/banking-blogs/banking-services/upi-circle-delegated-payments-how-it-works-limits
- UPI September 2026 data (StartupTalky): https://startuptalky.com/upi-transactions-september-2026/
- UPI August 2026 record (StartupTalky): https://startuptalky.com/india-upi-transactions-august-2026-record-volume/
- UPI users 55.49 crore and FY26 totals (CA Club India): https://www.caclubindia.com/news/upi-crosses-55-49-crore-users-in-june-2026-fy26-transactions-hit-rs-314-lakh-crore-26671.asp
- ChatGPT 100M weekly users in India (Social Samosa): https://www.socialsamosa.com/news-2/india-100-million-weekly-active-chatgpt-users-11121146
- UPI fraud FY25 (BOOM, Finance Ministry in Lok Sabha): https://www.boomlive.in/web-stories/india/upi-fraud-cases-and-losses-rise-over-five-years-finance-ministry-tells-lok-sabha-2755
- RBI discussion paper press release (Apr 2026): https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=62535
- RBI proposals summary (Taxmann): https://www.taxmann.com/post/blog/rbi-proposes-new-digital-payment-fraud-safeguards/
- Google AP2 explained (CloudNews): https://cloudnews.tech/google-launches-ap2-the-open-protocol-for-ai-agent-payments-how-it-works-who-supports-it-and-what-it-means-for-merchants-and-users/
- AP2 legal view (Loeb & Loeb): https://www.loeb.com/en/insights/passle/2025/10/the-rise-of-agentic-commerce-what-googles-ap2-protocol-means-for-shopping-and-marketing
- Prompt injection in AI browsers (The Register): https://www.theregister.com/2025/10/28/ai_browsers_prompt_injection
- F-Secure, *Can AI shopping agents be trusted?*: https://www.f-secure.com/en/partners/insights/can-ai-shopping-agents-be-trusted-we-built-one-to-find-out
- PromptFix attacks on agentic browsers (OECD AI incidents): https://oecd.ai/en/incidents/2025-08-21-0e45
- Razorpay, Cashfree, BharatPe, PayU agentic suites (Windsor Drake): https://windsordrake.com/market-intelligence/product-launches/razorpay-cashfree-bharatpe-payu-product-launch-2026-09-25
- Razorpay Agent Studio (Bankers Adda): https://www.bankersadda.com/razorpay-launches-ai-agent-studio-to-automate-business-payments/
- Visa agentic commerce India launch (Windsor Drake): https://windsordrake.com/market-intelligence/product-launches/visa-product-launch-2026-09-11
- McKinsey agentic commerce forecast (Digital Commerce 360): https://www.digitalcommerce360.com/2025/10/20/mckinsey-forecast-5-trillion-agentic-commerce-sales-2030/
- Morgan Stanley agentic commerce forecast (Yahoo Finance): https://finance.yahoo.com/news/morgan-stanley-sees-multi-path-093502239.html
- India quick commerce 2026 (Digital in Asia): https://digitalinasia.com/india-quick-commerce-blinkit-zepto-instamart/
- DPDP Rules timeline (Sansa Legal): https://www.sansalegal.com/post/dpdp-act-2023-and-rules-2025-phased-implementation-timeline-and-business-compliance-deadlines
