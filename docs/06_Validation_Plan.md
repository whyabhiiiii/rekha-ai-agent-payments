# 06 · Validation Plan

**Status: not yet run.** This is my plan for testing Rekha's riskiest assumptions with real users before any build decision. The results will replace the **[Hypothesis]** labels in `01_Discovery_and_Research.md` and go into the case study.

**Why it matters for this project in particular.** Accenture found that only 9% of consumers are open to an agent buying on its own, even with guardrails they set themselves. So I can't assume that controls create trust. The survey and the usability tests below are built to check whether *specific, visible* controls change what people say and do.

---

## 1. What we're testing

The riskiest assumptions from `01_Discovery_and_Research.md` §8:

| # | Assumption | Method | Pass signal |
|---|---|---|---|
| A1 | AI-assistant users want agents to pay for routine purchases | Survey + interviews | ≥ 30% of AI users would delegate ≥ 1 category with controls |
| A2 | Fear of mistakes/fraud is the main blocker | Interviews | ≥ 5 of 8 cite control or safety unprompted |
| A3 | Users can set up a Rekha in < 90 s | Usability test | ≥ 80% success; median < 90 s |
| A4 | Users read step-up reasons and decide correctly | Usability test (seeded bad payment) | ≥ 90% reject the seeded attack |
| A6 | Fintech teams see strategic value | Expert interviews | ≥ 2 of 3 say they'd prioritise it in 2027 |

---

## 2. Two-week plan

| Day | Task | Output |
|---|---|---|
| 1 | Post screener (§3) in college groups, LinkedIn, alumni network, X/Twitter | 30+ screener responses |
| 2 | Launch survey (§5); publish fake-door page (§6) | Live links |
| 3–6 | 8 user interviews, 30 min each (§4) | Notes per interview |
| 5–8 | 3 expert interviews (§4.2): fintech PM, payments/risk person, agent developer | Notes |
| 7–9 | 5–6 usability tests with the prototype (§7) | Task metrics + quotes |
| 10 | Close survey (target n ≥ 150); pull fake-door numbers | Charts |
| 11–12 | Affinity map and synthesis (§8) | 5–7 insight cards |
| 13–14 | Update the case study and docs with what I learned | v2 case study |

---

## 3. Screener

1. How often do you use an AI assistant (ChatGPT, Gemini, Claude, Perplexity, Copilot, Meta AI…)?
   *Daily / A few times a week / A few times a month / Rarely / Never*
2. In the last month, how many times did you order groceries or essentials online (Blinkit, Zepto, Instamart, BigBasket, Flipkart Minutes, etc.)?
   *0 / 1–3 / 4–8 / 9+*
3. How many bills or recharges do you pay through UPI in a typical month?
   *0 / 1–2 / 3–5 / 6+*
4. Have you ever let an app or a person pay for something on your behalf (AutoPay, UPI Circle, a family member, an assistant)? *Yes / No*
5. Age band, city, occupation.
6. Are you OK with a 30-minute video call? *Yes / No*

**Select:** daily or weekly AI users with ≥ 4 online grocery orders/month (Delegators); plus 2–3 people aged 45+ or people who manage a parent's payments (Cautious bill-payers / Guardians). **Exclude:** people working on agent payments (they go in the expert track).

---

## 4. Interview scripts

### 4.1 User interview (30 minutes, Mom Test style)

**Rules:** ask about **past behaviour**, not hypotheticals. Don't pitch Rekha until the last 5 minutes. Don't ask "would you use…?". Silence is fine; let them fill it.

**Intro (2 min)**
> "Thanks for this. I'm researching how people use AI assistants and how they handle routine payments. There are no right answers, and I'm not selling anything. Is it OK if I take notes? [If recording: Is it OK if I record, only for my notes?]"

**Routine spending (6 min)**
1. Walk me through the last time you ordered groceries online. What triggered it? How long did it take?
2. Which bills or recharges did you pay last month? How do you remember them?
3. What's the most annoying routine payment you make? Why?

**AI usage (6 min)**
4. Tell me about the last thing you asked an AI assistant to help with.
5. Have you ever had an assistant help with shopping: comparing products, building a list, finding deals? What happened next? Who actually paid?
6. *(If they stopped before paying)* What made you take over at that point?

**Delegation and trust (8 min)**
7. Tell me about a time someone else paid for something on your behalf (family member, AutoPay, assistant). How did you set it up? Did anything go wrong?
8. Has a payment ever gone wrong for you: wrong amount, scam attempt, double charge? What did you do? How long did it take to fix?
9. If something you didn't intend got paid, what would you do first?

**Concept reaction (5 min, only now)**
10. Show the prototype's home screen and one ASK screen. "What do you think this does?" (Don't explain. Watch.)
11. "What would you want to control if an assistant paid for your groceries?"
12. "What would make you *not* use this?"

**Close (3 min)**
13. "Is there anything I should have asked but didn't?"
14. "Who else should I talk to about this?" (Referrals grow the sample.)

**Note template (fill right after each call)**

| Field | Notes |
|---|---|
| Participant (ID, segment, age band, city) | |
| Current behaviour (facts only) | |
| Pains (with direct quotes) | |
| Workarounds | |
| Fears / blockers about agents paying | |
| Reaction to concept (what they understood unprompted) | |
| Surprises | |
| Evidence for/against A1, A2 | |

### 4.2 Expert interview (30 minutes)

For: a PM at a UPI app, payment gateway or bank; someone in risk/fraud; an agent developer.

1. What's your team doing about agent-initiated payments in the next 12 months?
2. What worries you most about agents paying through your rails or app?
3. How do you handle disputes today for delegated payments (UPI Circle, AutoPay)? Where does it break?
4. *(Agent developers)* What payment information can your agent share at checkout: task intent, cart, sources it visited? What would stop you sharing it?
5. *(Risk)* Which signals would you trust most to catch a manipulated agent?
6. Show the decision-rules table (PRD §8). "What's missing? What's wrong?"
7. "If you had this, would it make your 2027 roadmap? What would have to be true?"

**Cold message for expert interviews (LinkedIn, ≤ 300 characters)**
> "Hi [Name], I'm a final-year engineering student researching how UPI apps should handle AI-agent payments. I've built a concept and a decision-rules draft. Could I get 20 minutes of your feedback? Happy to share everything I've learned."

---

## 5. Survey (target n ≥ 150; Google Forms / Tally)

**Intro:** "5-minute anonymous survey on AI assistants and routine payments. No personal data beyond age band and city."

1. How often do you use an AI assistant? *(Daily / Weekly / Monthly / Rarely / Never)* → if Never, skip to 13
2. Which do you use? *(multi-select)*
3. Have you used an assistant to help with shopping in the last 3 months? *(Yes / No)*
4. For which of these would you let an AI assistant **choose and pay**, within limits you set? *(multi-select: Groceries / Bills & recharges / Medicine refills / Train & bus tickets / Subscriptions / Food delivery / None)*
5. For those, roughly how much do you spend per month? *(< ₹1,000 / ₹1,000–3,000 / ₹3,000–6,000 / ₹6,000–10,000 / > ₹10,000)*
6. What worries you most about an assistant paying for you? *(rank top 3: Wrong item or quantity / Overspending / Being scammed or tricked / Can't undo / Privacy / Don't know what it's doing / Other)*
7. Which controls would you want? *(multi-select: Monthly budget / Per-purchase limit / Only certain apps or shops / Ask me before unusual purchases / See why it bought something / Pause all agents instantly / Family member can see or approve)*
8. How would you prefer to approve? *(Ask every time / Ask only if unusual / Don't ask, just tell me after / Weekly summary only)*
9. Would you accept a 30-minute wait on the first payment to a new shop above ₹2,000 if it reduced fraud? *(Yes / Only for bigger amounts / No)*
10. If your agent's payment went wrong, who would you contact first? *(UPI app / Bank / The agent app / The shop / I'd give up)*
11. How much would you trust an assistant to pay if you had these controls? *(1–5)*
12. Without them? *(1–5)*
13. Do you manage digital payments for a parent or older relative? *(Yes / No)*
14. Age band; city tier; occupation.
15. Want to try the prototype? *(optional contact)*

**Analysis plan:** % choosing ≥ 1 category in Q4 among AI users (tests A1); Q6 ranking (A2); Q11 vs Q12 paired difference (trust lift from controls; a paired t-test or Wilcoxon signed-rank); Q8 distribution (validates the autonomy ladder); Q9 (A8). Q11 against Q12 is the direct test of the thesis: does naming specific controls move stated trust, when a general promise of guardrails did not?

---

## 6. Fake-door test

A one-page site (Carrd, Framer or Notion) with:

> **Draw the line for your AI agents.**
> Let your assistant pay for groceries and bills, but only what you said, only where you said, and stop it in one tap.
> **[ Get early access ]**

Clicking leads to: *"Thanks! Rekha is a concept I'm researching. It isn't live yet. Would you answer 3 quick questions?"* (then link to the survey). **Be transparent; never collect payment details.**

Drive traffic from the same places as the screener and one LinkedIn post. **Metric:** click-through on "Get early access" among unique visitors. **Signal:** ≥ 8% is strong for a cold concept page; < 3% means the message or the need is weak.

---

## 7. Usability test plan (prototype)

**Participants:** 5–6 from the screener (4 Delegators, 1–2 Guardians or 45+).
**Setup:** open `prototype.html` on their phone or screen share; think-aloud.

| Task | Success criteria | Measure |
|---|---|---|
| T1. "Your agent should handle weekly groceries, up to ₹2,500, only from two apps, no alcohol. Set that up." | Saved Rekha matches all 4 constraints | Success, time, errors |
| T2. "Your agent is asking you something. Decide what to do." (Air-fryer ASK) | Rejects or approves groceries only; can say why | Success, explanation in own words |
| T3. "Something looks wrong. Stop all your agents." | Finds and uses kill switch | Time to find |
| T4. "Find out why your agent's last payment was blocked." | Explains payee mismatch in own words | Comprehension |
| T5. "How much of your grocery budget is left this week?" | Correct number | Success |

After each task: **Single Ease Question** (1–7, "How easy was that?"). At the end: the 3-item **Trust Index** from `03_Metrics_and_Experiments.md`.

**Report format:** a table of task × participant (✓ / ~ / ✗), median times, SEQ averages, the top 5 usability issues ranked by severity × frequency, and quotes.

---

## 8. Synthesis and updating the case study

1. **Affinity map:** one sticky per observation (fact or quote) → cluster → name each cluster as an insight.
2. **Insight card format:** *We observed [behaviour] in [n of N] participants. This suggests [interpretation]. So we will [decision].*
3. **Evidence ladder:** label each claim as Anecdote (1 person) → Pattern (≥ 3 of 8) → Quantified (survey) → Behavioural (fake door, usability).
4. **Update the docs:**
   - Replace each **[Hypothesis]** in `01` with the result: confirmed, changed or dropped.
   - Add a "What I learned" section to the case study with 3–5 insight cards and real numbers.
   - Update the RICE confidence values in the PRD.
   - **If the research kills an assumption, it stays in the write-up,** along with what changed because of it.

---

## 9. Ethics

- Get consent before recording; anonymise names in all write-ups.
- Never ask for UPI IDs, account numbers or real transaction screenshots.
- Fake-door visitors are told it's a concept immediately after clicking.
- Offer to share the findings with everyone who helped.
