# TraderLab 101 — Quick Start

**Version 2.3.12 · Get going in about 15 minutes**

This guide takes you from "first download" to "logged a trade and looked at analytics" without the long-form theory. For everything else, see [USERGUIDE.md](USERGUIDE.md).

---

## What You're About To Do

```
1. Download & open         (1 min)
2. Set your instrument     (1 min)
3. Load demo data          (1 min)    ← fastest way to see the app full of data
4. Walk through a session
   ├─ Preflight            (2 min)
   ├─ Pre-Market Levels    (3 min)
   ├─ Confirm Open Type    (1 min)
   ├─ Log a trade          (3 min)
   └─ Save the journal     (2 min)
5. Look at Analytics       (2 min)
6. Back up your data       (30 sec)
```

---

## Step 1 — Download & Open

1. Go to the [GitHub repository](https://github.com/SeanDavid-stack/TraderLab101)
2. Download **`TraderLab101.html`**
3. Save it anywhere on your computer
4. Double-click to open in **Chrome** (recommended)

> No installation. No accounts. No server. Your data stays on your machine.

You will see a one-time welcome splash. Read it, click **Let's Go**.

---

## Step 2 — Set Your Instrument

Click **⚙ Settings** at the bottom of the left nav, then click the **INSTRUMENT** link in the sticky header.

Click your preset:

| Preset | Tick | Tick Value | Default Commission (RT) |
|--------|------|------------|--------------------------|
| **MES** | 0.25 pt | $1.25 | ~$0.62 |
| **ES** | 0.25 pt | $12.50 | ~$4.18 |
| **MNQ** | 0.25 pt | $0.50 | ~$0.62 |
| **NQ** | 0.25 pt | $5.00 | ~$4.18 |

Adjust the commission to match your broker. That's it for setup.

> **Trading multiple symbols?** TraderLab is cleanest when each log is one instrument. The simplest pattern: one JSON backup per symbol (e.g. `Sean_NQ_2026.json`, `Sean_ES_2026.json`) and switch with Settings → DATA → Export/Import. If you'd rather keep them all in one log, that works too — the Trade Log will show a per-symbol summary chip row and the Analytics tab has an **Instrument filter** that scopes every chart to one symbol at a time. Full guide: [MULTI_SYMBOL_NOTES.md](MULTI_SYMBOL_NOTES.md) (PDF in repo).
>
> **Trading a custom symbol?** (RTY, YM, CL, GC, BTC, etc.) Define it in **Settings → Custom Symbol** with tick size, tick value, AND commission. The commission field is required — the app blocks save without it so analytics never silently use $0 fees. There's also an optional **Yahoo Symbol** field for the live-price fallback (`YM=F`, `RTY=F`, `CL=F`, `BTC-USD`, etc.) — leave blank to auto-derive.

---

## Step 3 — Load Demo Data (Optional but Highly Recommended)

The fastest way to see the app at full strength is to load the demo data.

1. In the same **Settings** panel, scroll to **DATA**
2. Click **↑ Import Backup**
3. Select **`traderlab-demo-trades.json`** (in the same folder as the HTML)

You now have **61 sessions, 220 trades, and 41 missed trades** to explore. Skip to **Step 7** if you want to look at the analytics first, then come back here for a real session walkthrough.

> When you're ready to start fresh, **Settings → DATA → ✕ Clear Everything**.

---

## Step 4 — Preflight (2 min)

Click **✈ Preflight** in the left nav. Answer at least three of the eight pre-session questions:

1. What is the Opening Context?
2. What is the HTF Context?
3. What did we do in the previous RTH session?
4. What did we do in the ETH/Overnight session?
5. Where are the stops/fuel?
6. Based on where the fuel is — who is offside?
7. Any news or data events?
8. Top-down analysis — your overall read

Click **✅ Complete Preflight** when done. Your answers are stamped with a timestamp and attached to today's journal automatically.

---

## Step 5 — Pre-Market Levels (3 min)

Click **⬡ Pre-Market Levels**. Three ways to get your levels in:

| Method | How |
|--------|-----|
| **BMBridge** | Enter URL → click **Import** |
| **CSV File** | Click **Choose CSV File** → select |
| **Type them in** | Just fill the boxes manually |

Fill in at minimum:

- **Prior Day:** pHigh, pLow, pClose, pVPOC
- **Value Area:** pVAH, pVAL
- **Overnight + Today's Open:** ONH, ONL, Today's Open

Then set your **bias** at the top — click **▲ LONG**, **— NEUTRAL**, or **▼ SHORT**. Add a sentence for *why*.

Optional: add **Fuel Levels** at the bottom (places where participants are trapped). Click **+ Add Fuel Level** for each.

The **Open Type** auto-detects from your levels. When you're happy with it, click **✅ Confirm Open Type** to lock it in. This activates the rest of the app.

---

## Step 6 — Live Price & a First Trade (3 min)

Click **◉ Live Price** to see the live feed. If BMBridge isn't configured, the feed falls back to Yahoo Finance (~15 minute delay) — fine for getting a feel.

When you take a trade, click **◈ Trade Log** and fill in:

1. **Date / Time / Setup / Direction / Entry / Stop**
2. **Scale 1 (Risk Neutral)** — exit price + contracts
3. **Scale 2 (Target)** — exit price + contracts
4. **Scale 3 (Runner)** — final exit + contracts
5. Click any **target chip** (DVPOC, VWAP, MID, etc.) and mark the outcome — ✓ Hit, ↩ Bailed, or ✗ Missed
6. **Process Rating** — A / B / C / F (be honest)
7. **Exit Time** — for duration tracking
8. Optional: tag any **execution errors** and **emotional state** chips

Click **Log Trade**. You'll see:

- A new row in the trade list below
- Your stat cards update at the top
- A toast confirmation

---

## Step 7 — Save the Journal (2 min)

Click **◻ Journal**. Today's date is auto-selected.

Most fields are pre-filled from your session:

- Open Type — auto from confirmed session
- Preflight answers — auto from completed Preflight
- Bias timeline — auto from Pre-Market

Add the human-context fields:

- **Day Type / Profile Shape** — what kind of day did it become?
- **Session Result** — Win / Loss / Break Even / No Trade
- **IB Outcome / Market Responsive** — quick characterization
- **Key Levels Traded**
- **Trade Notes / Auction Story** — what happened, in your own words
- **Lesson** — one sentence you want to remember

Click **Save Session**. You can always come back later — past dates open in **review mode** with a clean read-only summary.

---

## Step 8 — Look at Analytics (2 min)

Click **⊞ Analytics**. The dashboard auto-renders from your data.

What to look at first:

| Card / Section | What It Tells You |
|----------------|-------------------|
| **Win Rate** | Are you net positive on count? |
| **Profit Factor** | Are your wins big enough relative to losses? |
| **P&L by Setup** | Which setups actually pay you? |
| **P&L by Time of Day** | When are you sharp vs. tired? |
| **Tilt Detection** | Did you have any revenge / overtrade days? |
| **P&L by Bias Alignment** | Do you make money trading with your bias? |

Use the date-range filter at the top (`All`, `1W`, `1M`, `2M`, `3M`, `6M`, `YTD`, `Custom`) to scope the dashboard.

---

## Step 9 — Back Up Your Data (30 sec)

**Settings → DATA → ↓ Export Backup**

Saves a timestamped JSON file. Do this **at least weekly**. If you ever clear browser cache, this file is your only way back.

> A user's data must never be lost. The app is built to read backups from any prior version — restore is always available.

---

## Where To Go Next

| If you want to… | Open |
|-----------------|------|
| Read the full reference for every panel | [USERGUIDE.md](USERGUIDE.md) |
| Read the trading methodology | **📖 Methodology** in the left nav |
| Try simulated changes ("what if I cut C-rated trades?") | **🔬 What-If Lab** |
| Get personalized AI coaching from your trade history | **🧠 AI Coach** (free copy-prompt mode, or in-app via Anthropic API key) |
| See the changelog and known issues | [CHANGELOG.md](CHANGELOG.md) |
| Report a bug or request a feature | [GitHub Issues](https://github.com/SeanDavid-stack/TraderLab101/issues) |

---

## A Few Habits That Make TraderLab Pay Off

1. **Do Preflight every day, even if it's two sentences.** The data feeds the journal and analytics.
2. **Rate your process honestly.** A C-rated win is more dangerous than a B-rated loss.
3. **Log missed trades.** Hesitation patterns are the loudest signal in the data.
4. **Export weekly.** Five seconds. Save your work.
5. **Look at analytics on weekends, not during the session.** Decisions during the trade should come from your plan, not from the dashboard.

---

*"If this — then that. If not — then what?"*
*— Tom B., Traders Lab*
