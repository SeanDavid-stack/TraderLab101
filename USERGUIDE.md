# TraderLab 101 — User Guide

**Version 2.3.11 · April 2026**

A complete walkthrough of every panel, every setting, and the full daily workflow.

> *"If this — then that. If not — then what?"*
> — Tom B., Traders Lab

---

## Table of Contents

1. [Getting Started](#1-getting-started)
2. [The Daily Workflow](#2-the-daily-workflow)
3. [Preflight Checklist](#3-preflight-checklist)
4. [Pre-Market Levels](#4-pre-market-levels)
5. [Open Context (Flowchart)](#5-open-context-flowchart)
6. [Live Price Tracker](#6-live-price-tracker)
7. [Structured Trades](#7-structured-trades)
8. [Mean Reversion Checklist](#8-mean-reversion-checklist)
9. [Statistics by Target](#9-statistics-by-target)
10. [Trade Log](#10-trade-log)
11. [Missed Trades](#11-missed-trades)
12. [Session Journal](#12-session-journal)
13. [Analytics Dashboard](#13-analytics-dashboard)
14. [What-If Lab](#14-what-if-lab)
15. [AI Trade Coach](#15-ai-trade-coach)
16. [Methodology Reference](#16-methodology-reference)
17. [Settings](#17-settings)
18. [Data, Privacy & Backups](#18-data-privacy--backups)
19. [Troubleshooting](#19-troubleshooting)
20. [License](#20-license)

---

## 1. Getting Started

### Installation

There is no installation. TraderLab 101 is a single HTML file that runs entirely in your browser.

1. Download `TraderLab101.html` from the [GitHub repository](https://github.com/SeanDavid-stack/TraderLab101)
2. Save it anywhere on your computer
3. Double-click to open in Chrome (recommended), or any modern browser
4. On first launch you will see a one-time welcome splash — read it, then click **Let's Go**

### First-Time Setup

Before your first session, open **Settings** (bottom of the left nav) and configure:

| Step | Where | What to Do |
|------|-------|-----------|
| 1 | INSTRUMENT | Click your preset (MES, ES, MNQ, NQ) or define a custom symbol with tick size, tick value, and round-trip commission |
| 2 | FEEDS | If you use Sierra Chart with BMBridge, enter your **Levels Feed URL** and **Live Price Feed URL** |
| 3 | GOALS | Set **Max Daily Loss**, **Max Trades**, and **Min Process Rating** |
| 4 | DATA | Set a **Log Name** (e.g. `Sean_ES_2026`) — this names every backup file |

If you don't use BMBridge, the live price feed automatically falls back to Yahoo Finance (≈15 minute delay).

### How Data Is Stored

All data lives in your browser's `localStorage`. This means:

- Your data stays on your computer — nothing is sent anywhere
- Data persists between browser sessions as long as you don't clear browser data
- If you clear browser cache, **your TraderLab data will be erased**

> **Critical:** Export a backup regularly. **Settings → DATA → Export All Data**.

---

## 2. The Daily Workflow

The recommended order of operations every trading day:

```
PREFLIGHT  →  PRE-MARKET  →  OPEN CONTEXT  →  LIVE PRICE  →  TRADE LOG
   ↓             ↓               ↓                ↓             ↓
 8 Qs       Levels +         Decision         Track price    Log entries
 + media    bias + fuel      flowchart        + tag levels   + targets
                                                                 ↓
                                                              MISSED → JOURNAL → ANALYTICS
                                                              + What-If + AI Coach
```

Each step builds context for the next. You can skip steps, but the analytics and bias-alignment scoring are richer when you complete the full chain.

---

## 3. Preflight Checklist

**Nav:** ✈ Preflight

Eight pre-session research questions to gather context before you touch the market.

### The 8 Questions

1. What is the **Opening Context**?
2. What is the **HTF Context**?
3. What did we do in the **previous RTH session**?
4. What did we do in the **ETH / Overnight session**?
5. Where are the **stops / fuel**?
6. Based on where the fuel is — **who is offside**?
7. Any **news or data events**?
8. **Top-down analysis** — overall read for today

### How to Use It

- Answers auto-save as you type (no Save button needed)
- Click **✅ Complete Preflight** when finished — saves a snapshot to today's journal and stamps a timestamp
- You may attach **Media** (chart screenshots or replay links) at the bottom of the panel
- If you skip Preflight, the Journal tab will show a soft warning

Preflight is optional but strongly recommended. The data feeds straight into the Journal so you can review what you saw vs. what happened.

---

## 4. Pre-Market Levels

**Nav:** ⬡ Pre-Market Levels

The hub for the entire session. Enter your levels, set bias, map the fuel, and confirm the open type.

### Importing Levels (Three Ways)

| Method | How |
|--------|-----|
| **BMBridge** | Enter your URL → click **Import**. Auto-fills from Sierra Chart's `STATS.csv`. |
| **CSV File** | Click **Choose CSV File** → select. IRT format auto-detected. |
| **Google Sheet** | Publish your sheet as CSV → paste the URL or content into the textarea. (Direct fetch is blocked by browser CORS for local files.) |

All three paths share the same **CSV Column Mapping** — configure once in Settings.

### Manual Entry Sections

- **Prior Day** — pHigh, pLow, pClose, pVPOC
- **Prior Value Area** — pVAH, pVAL
- **Overnight & Today's Open** — ONH, ONL, ON/VPOC, Today's Open
- **Custom Levels** — add any number of additional levels by name and price; drag to reorder

### Daily Bias

Click **▲ LONG**, **— NEUTRAL**, or **▼ SHORT**. Add a written reason — every change is timestamped and shown in the bias timeline (top of every page). Change bias as often as you need; each change is logged.

### Fuel Map

Click **+ Add Fuel Level**. For each level:
- Select **Buy fuel**, **Sell fuel**, or **Consolidation**
- Enter the price level
- Add a note explaining why participants are trapped there

Fuel levels appear in the Live Price level tracker and analytics.

### Open Type Detection

Once Today's Open, pHigh, and pLow are entered, TraderLab automatically determines the open type and highlights one of seven chips:

| Code | Meaning |
|------|---------|
| **HOR** | High Out of Range (gap up) |
| **LOR** | Low Out of Range (gap down) |
| **HIR-OV** | High In Range, Out of Value |
| **LIR-OV** | Low In Range, Out of Value |
| **HIR-IV** | High In Range, In Value |
| **LIR-IV** | Low In Range, In Value |
| **IR-IV** | In Range, In Value |

You can manually override the detection. Click **✅ Confirm Open Type** to lock it in — this activates the rest of the app and starts the session.

---

## 5. Open Context (Flowchart)

**Nav:** ⇢ Open Context

An interactive **if / then** decision tree built around your confirmed open type. This panel was redesigned in v2.3.x — it is no longer a static flowchart but a context-driven walk-through.

### How It Works

1. The first node loads based on your confirmed open type
2. Click **Yes** or **No** at each decision point
3. The flow advances along the matching branch
4. The **flow strip** at the top shows your breadcrumb of choices — click any prior node to back up

### Node Color Code

| Color | Meaning |
|-------|---------|
| 🔵 Blue | Question — choose a branch |
| 🟡 Gold | Action / instruction |
| 🟢 Green | Conclusion — outcome of the path |
| 🔴 Red | Warning — invalid setup or stop trading |

Decisions persist for the day — you can return any time during the session and the path is preserved.

---

## 6. Live Price Tracker

**Nav:** ◉ Live Price

Real-time (or near-real-time) price feed plus opening-print capture, IB management, and the level tracker.

### Live Feed

- Large price display with **Last**, **Change**, **RTH High / Low**, **RTH Open**
- Status banner shows the active feed:
  - **BMBridge OK** (green) — real-time
  - **Yahoo fallback** (gold) — ≈15 min delay
  - **Connecting…** (gray) — handshake in progress
- **Start / Stop** buttons control polling
- **📌 Set Opening Print** captures the live price as Today's Open if it isn't set yet

### Initial Balance

- **IBH** and **IBL** inputs lock the IB range
- After 10:30 AM ET, IB auto-fills from BMBridge if available
- Manual entry locks auto-fill so your numbers stick

### Level Tracker

A live table of every pre-market level (standard, custom, fuel) and its proximity to the current price. As price approaches a level, the row glows gold. Levels that have been hit during the session are flagged.

### Tag Log

A running log of every level that has been "tagged" (price reached) during the session — shown with timestamp and proximity. Tags also feed into trade reconciliation: if you take a trade with a target that matches a tagged level, the journal shows a reconciliation pill.

---

## 7. Structured Trades

**Nav:** ◆ Structured Trades

Eight trade setups with conditional checklists — process discipline over outcome.

### Alignment Indicator

A banner at the top shows whether the current setup direction matches your daily bias.
- **🟢 ALIGNED** — direction matches bias
- **🔴 COUNTER-BIAS** — direction is opposite
- **🟡 NEUTRAL** — bias is neutral

### Go / No-Go Conditions

A 7-checkbox card. **All seven must be checked** for the green **✓ ALL CONDITIONS MET** banner to appear. Conditions are non-negotiable — they exist to enforce process.

Conditions persist per session. Click **Reset** to clear and re-run.

### The 8 Setups

1. **Opening Trade** (Gap & In-Range)
2. **IBC** — Initial Balance Continuation
3. **IBF** — Initial Balance Failure
4. **Mean Reversion**
5. **VPOC Shift**
6. **BAR** — Break and Retest
7. **MID > VWAP > VPOC**
8. **VHVN > VPOC**

Each setup card is collapsible and contains qualifications, targets, and key rules. Click the card title to expand or collapse.

For full theory and statistics on each setup, use the [Methodology Reference](#16-methodology-reference) panel.

---

## 8. Mean Reversion Checklist

**Nav:** ↺ Mean Reversion

A focused, two-column checklist for mean-reversion trades. Built around the *Matryoshka* fractal-alignment concept — micro fractals nested inside larger ones.

- **Left column** — micro fractal conditions
- **Right column** — entry, targets, stops

### How to Use

1. Tick each condition as it is met
2. Progress bar fills as conditions are checked
3. Checkboxes persist within the session
4. Click **Reset** to clear

This panel is a discipline aid — it does not save trades. Log the trade in the Trade Log when you take it.

> Key principle: **DO NOT MOVE STOP**. Hold the structure or it isn't the trade.

---

## 9. Statistics by Target

**Nav:** ◈ Statistics

A historical performance table broken down by target level. Shows hit rates, average win, average loss, and net P&L per target.

### Columns

| Column | What It Means |
|--------|---------------|
| Target | Level name (DVPOC, VWAP, VAH, etc.) |
| Hit Rate % | How often the target was reached |
| Win Rate % | Of trades targeting it, how many were wins |
| Avg Win / Avg Loss | Dollar magnitudes |
| Trades | Count of trades targeting this level |
| Net P&L | Aggregate dollars |

### Interactions

- Click any column header to sort
- Click a row to highlight all trades that targeted that level
- Use the filter chips to show / hide setups

> Statistics are **illustrative only** — context always supersedes raw hit rates.

---

## 10. Trade Log

**Nav:** ◈ Trade Log

Where every trade is logged in detail. The form is at the top; the trade list is below.

### Stat Cards (top row)

A row of stat cards summarizing your trades. Cards are draggable (reorder) and toggleable (hide/show). Common cards: Total Trades, Win Rate, Profit Factor, Max DD, Avg Win, Avg Loss, ROI.

### Trade Entry Form

#### Row 1 — Setup
- **Date & Time** (hour : minute dropdowns)
- **Instrument** (preset or custom)
- **Setup** (8 built-ins + custom)
- **Direction** (Long / Short)

#### Row 2 — Prices
- **Entry Price**, **Stop Price**, **Trigger Type** (Limit / Market / Stop)

#### Scale-Outs (3 scales)
| Scale | Purpose |
|-------|---------|
| Scale 1 — Risk Neutral | Buy back your stop |
| Scale 2 — Target | Primary profit target |
| Scale 3 — Runner | Trail or final exit |

R-multiple is auto-calculated for each scale. The summary line shows total P&L in points, dollars, and R.

#### Targets

Click any of the target chips (DVPOC, VWAP, MID, pHigh, etc.) — or type a custom name. For each target row:
- **Price** auto-fills from your pre-market levels when possible
- **Outcome** — ✓ Hit / ↩ Bailed / ✗ Missed
- **Bail Reason** (only for Bailed): Price Action Change · Market Structure Shift · News · Fear/Emotion · Protecting P&L · Time · Other

#### Process Rating
- **A** — perfect process
- **B** — good, minor deviation
- **C** — off plan
- **F** — broke the rules

#### Execution Errors

Multi-select chips for execution errors (12 default types, customizable). When errors are tagged you can also enter the **ideal exit price** so analytics can compute the dollar cost of each error.

#### Emotional State

Multi-select chips for emotional state during the trade (Confident, Patient, Focused, Anxious, Frustrated, Greedy, Fearful, Revenge, Bored, Neutral).

#### Trigger Type & Bias at Trade

Trigger type (entry mechanic) plus your daily bias at the time of the trade — used for the bias-alignment analytics.

#### Advanced Fields (toggle)

Toggleable section with: Entry Structure, Exit Structure, Pullback, Scaling, Trade Duration, Target Reached flag, Traded in Value flag, Break-even Stop flag, Early Exit flag.

### Daily Goals Tracker

If goals are configured in Settings, a **TODAY** bar shows live progress: net P&L vs goal, trade count vs limit, loss vs max daily loss. Updates after every save.

### Stats by Setup

Below the cards, a per-setup breakdown shows trade count, win rate, avg R, risk-neutral rate, and total P&L for each setup you have used.

---

## 11. Missed Trades

**Nav:** ⊘ Missed Trades

Log trades you identified but didn't take.

### Modes

- **Simple** — entry / target / stop / contracts
- **Multi-scale** — separate Risk-Neutral, Target, and Runner exits, mirroring the Trade Log structure

The form shows a **live preview** as you type:

> Would have won: **+5.00 pts · +$25**
> Would have lost: **-3.00 pts · -$15**

### Why Did You Miss It?

Multi-select reasons: **Fear · Uncertainty · Hesitation · Distraction · Not at Desk · Didn't See Setup · Overtrading Concern · Recent Loss/Tilt · Conditions Not Met · Other.**

### What-If Integration

Missed trades feed the **What-If Lab** — you can simulate "what if I had taken these?" to see whether hesitation is costing you money or your filter is working.

---

## 12. Session Journal

**Nav:** ◻ Journal

The daily log. One entry per session.

### Date Navigation

- **◄ ►** arrows step through days
- **Today** jumps back to today
- **Date picker** opens a calendar
- **Session Heatmap** (collapsible) shows which days you have logged — click a date to jump

### Today vs. Past Days

| Mode | When |
|------|------|
| **Form mode** | Today's date with no saved session — fields are editable |
| **Review mode** | Past date with a saved session — shows a read-only summary with all metadata |

### Session Form Fields

- **Open Type** (auto-filled from confirmed session)
- **Day Type / Profile Shape**
- **Session Result**
- **IB Outcome**
- **Market Responsive**
- **Risk Neutral** (yes/no flag)
- **Checklist Used** (yes/no flag)
- **Preflight Done** (auto-filled from preflight completion)
- **Key Levels Traded**
- **Trade Notes / Auction Story**
- **Lesson / Rule Reinforced**
- **Chart Screenshots** (paste URLs)

### Setup Chips

Click the chips to tag which setups were in play today (multi-select). Selections feed analytics.

### Preflight Snapshot (8 fields)

Editable in the journal — keeps the snapshot in sync with the latest answers.

### Trade Filter & Review (collapsible)

- Filter chips for **Setup**, **Execution rating**, **Result**, **Direction**
- Scoped trade list for the current journal date
- **Alignment badges** on each trade — green (aligned with bias), red (counter-bias), gold (partial)
- **Hit pills** — show which targets were tagged

### Bug fix in v2.3.6

Switching tabs away from the Journal and back **no longer resets your in-progress fields**. Your typed text is preserved until you save, change the date, or refresh.

---

## 13. Analytics Dashboard

**Nav:** ⊞ Analytics

Comprehensive performance analysis. All data lives behind two filters at the top: **Date Range** and **Instrument**.

### Date Range Filter

`All` · `1W` · `1M` · `2M` · `3M` · `6M` · `YTD` · `Custom (From / To)`

### Instrument Filter

When you trade more than one instrument, a filter row appears. Click any instrument to isolate analytics.

### Fees Toggle

A single ON/OFF that toggles whether commission is included across every metric.

### Overview Cards

Stat cards at the top of the dashboard. Cards are **draggable** (reorder) and **toggleable** (hide/show). Common cards include:

- **Trades** · count of trades in the period
- **Win Rate %** · wins / total
- **Avg Win** · average win in dollars
- **Avg Loss** · average loss in dollars
- **Profit Factor** · gross wins ÷ gross losses
- **Max Drawdown** · largest peak-to-trough loss
- **Consecutive Wins / Losses** · longest streaks
- **ROI / Return on Trades**
- **Largest Win / Largest Loss**
- **Daily Consistency** · standard deviation of daily P&L
- **Sharpe-like Ratio**

Order and visibility persist across sessions.

### Chart Sections

Each section is **collapsible** and can be **reordered**. Dashboard state persists.

| # | Section | What It Shows |
|---|---------|---------------|
| 1 | Cumulative P&L | Equity curve, gross + net of fees |
| 2 | Daily P&L Calendar | Heatmap of green / red days |
| 3 | Streaks & Consistency | Max win/loss streaks, current streaks |
| 4 | P&L by Day of Week | Mon–Fri breakdown |
| 5 | P&L by Time of Day | Hour-of-day buckets |
| 6 | Drawdown Analysis | Peak-to-trough visualization |
| 7 | Trade Efficiency & Errors | Dollar cost of execution errors |
| 8 | Performance by Setup | Per-setup count, win rate, P&L |
| 9 | P&L by Direction | Long vs Short |
| 10 | P&L by Instrument | Per-symbol breakdown |
| 11 | P&L by Open Type | HOR / LOR / HIR / LIR / IR-IV |
| 12 | P&L by Bias Alignment | Aligned vs counter-bias |
| 13 | P&L by Trigger Type | Limit / Market / Stop |
| 14 | P&L by Emotional State | Emotional impact analysis |
| 15 | Trade Count vs Profitability | Sweet-spot finder |
| 16 | Weekly Summary | Last 12 weeks with running total |
| 17 | Tilt Detection | Sessions with consecutive losses, revenge trades |
| 18 | Bias Change Performance | Held vs flipped, by-bias P&L |
| 19 | Trade Duration | Avg winner vs loser hold time |
| 20 | P&L by Target | Hit / Bailed / Missed rates with bail reasons |
| 21 | Market Behavior vs Norms | Your hit rates vs methodology stats |

---

## 14. What-If Lab

**Nav:** 🔬 What-If Lab

A non-destructive performance simulator. Filter, slider, scenario — see the dollar impact instantly.

### Header Controls

- **Fees toggle** (ON / OFF)
- **💾 Save Preset** — store the current scenario
- **Preset pills** — load a saved scenario (active one is highlighted)

### Filter & Control Sections

All sections are collapsible. Each one updates P&L live.

- **Errors** — chips per error type with trade counts; toggle to remove
- **Emotional State** — chips per emotion; toggle to remove
- **Execution Quality** — minimum process rating cutoff (F / C / B / A)
- **Setups** — chips per setup; toggle to exclude
- **Triggers** — chips per trigger type; toggle to exclude
- **Trading Hours** — start/end-hour sliders to remove trades outside the window
- **Days of Week** — toggle Mon–Fri off
- **Session Filter** — RTH only or All
- **Against-Bias Trades** — checkbox to remove counter-bias trades
- **Stop-Loss Rules** — max stop in points (cap loss per trade)
- **Sizing Multiplier** — scale all trade sizes up or down
- **Daily Loss Limit** — input for max daily loss; auto-cuts remaining trades after hit
- **Full-Stop Reduction** — slider 0–100 % to reduce or eliminate full stops
- **Error-Trade Loss Reduction** — slider 0–100 % to reduce error-trade losses
- **Missed Trades** — checkbox to include all missed trades in the scenario

### Result Cards

| Card | What It Shows |
|------|---------------|
| Current P&L | Actual P&L over the period |
| Simulated P&L | P&L with filters applied |
| Delta | Improvement or decline in dollars |
| Impact | Dollar magnitude of the change |

### Optimizer

The Optimizer surfaces top recommendations like:

> **Remove C-rated trades:** +$2,500 impact (35 trades cut)

Use **Apply** to execute one recommendation, **Apply All** to stack them, or **Dismiss** to skip.

### Saving Presets

Click **💾 Save Preset**, name it, and the current set of filters is stored for one-click reload later.

---

## 15. AI Trade Coach

**Nav:** 🧠 AI Coach

Personalized coaching driven by your real trade data. Two modes — pick whichever fits.

### Mode 1 — Copy Prompt (free)

The coach packages your trade data + an analysis prompt and copies it to your clipboard. Paste into Claude.ai, ChatGPT, or any AI you prefer. No API key required, no cost.

### Mode 2 — In-App AI (Anthropic API)

Add an Anthropic API key in **Settings → AI COACH**. The coach calls the Claude API directly from your browser, streams the response back, and never sends your key or data to any TraderLab server.

Typical cost: **~$0.01–$0.05 per analysis**, depending on trade count.

### Three Analysis Types

| Type | What It Does |
|------|--------------|
| 📊 **Full Performance Review** | Edge leaks, strengths, patterns across all data |
| ⚠ **Error & Discipline Audit** | Errors, emotional trades, process breakdowns |
| 🎯 **Setup & Edge Analysis** | Which setups produce edge, best / worst times |

### Period Filter

`All Time` · `Last Month` · `Last 3 Months` · `YTD` — with live trade-count display.

### Privacy

In Mode 2 your API key stays in `localStorage` and is sent **only** to Anthropic's API. No traffic touches any TraderLab server (there is no TraderLab server).

---

## 16. Methodology Reference

**Nav:** 📖 Methodology

Read-only reference for every setup in Tom B.'s methodology. Nine accordion sections — click any header to expand.

1. Opening Trades (Gap & In-Range)
2. IBC — Initial Balance Continuation
3. IBF — Initial Balance Failure
4. Mean Reversion
5. VPOC Shift
6. BAR — Break and Retest
7. MID > VWAP > VPOC
8. VHVN > VPOC
9. Statistical Reference

Each section includes:
- Market mechanics and theory
- Setup conditions and context
- Required qualifications
- Primary, secondary, and extension targets
- Statistical hit rates by open type
- Tips, warnings, and key callouts

---

## 17. Settings

**Nav:** ⚙ Settings

A sticky header at the top of the panel jumps to each section: **INSTRUMENT · LABELS · GOALS · JOURNAL · FEEDS · AI COACH · DATA**.

### INSTRUMENT

Click a preset (MES, ES, MNQ, NQ) or define a custom symbol with tick size, tick value, and round-trip commission. A **global commission override** can be applied across all instruments.

**Yahoo Symbol** (optional) — drives the live-price fallback when BMBridge is unavailable. The four built-in presets auto-pick the right Yahoo ticker (MES/ES → `ES=F`, MNQ/NQ → `NQ=F`). For a custom instrument, leave blank to auto-derive (`<Symbol>=F`) or enter an explicit ticker like `YM=F`, `RTY=F`, `CL=F`, `GC=F`, `BTC-USD`, etc.

**Best practice — one log per instrument.** TraderLab's analytics, win rate, expectancy, and R-multiple math read cleanest when the log is scoped to a single symbol. If you trade multiple instruments, the simplest approach is one JSON backup per symbol — name them `Sean_NQ_2026.json`, `Sean_ES_2026.json`, etc. (Settings → DATA → Log Name) and switch between them with Export/Import.

If you do choose to keep multiple symbols in one log, that works too — TraderLab v2.3.10+ persists each trade's tick value, tick size, and commission at save time so historical numbers stay accurate even if you change your active instrument later. The Trade Log will show a per-symbol summary line and a soft banner pointing you at the **Analytics → Instrument filter** to scope the dashboard one symbol at a time.

### LABELS & DEFAULTS

Customize the chips that appear across the app:
- **Setups** — show / hide defaults, add custom
- **Errors** — same
- **Emotions** — same
- **Reasons Missed** — same

### GOALS

| Goal | What It Does |
|------|--------------|
| Max Daily Loss | Toast warning + Daily-Goals chip on Trade Log |
| Max Trades Per Day | Warning when count is reached |
| Min Process Rating | Warning when a trade is logged below your standard |

You can also set **Performance Thresholds** (green / gold / red cutoffs) for Win Rate, Profit Factor, Avg Win, etc. These cascade to color-coding in Trade Log, Analytics, and What-If.

### JOURNAL Dropdowns

Customize the four journal dropdowns: Profile Shape, Session Result, IB Outcome, Market Responsive. Add, remove, or reset each list.

### FEEDS & DATA IMPORT

- **BMBridge — Levels Feed URL** for pre-market level imports
- **BMBridge — Live Price Feed URL** for the real-time feed (can point to a different server / port than the levels feed)
- **Test** buttons to verify each
- **RTH Start Buffer** — minutes after 9:30 AM ET before hit detection activates (0–15)
- **CSV Column Mapping** — map CSV column labels to TraderLab fields. Works with BMBridge, file upload, and Google Sheets. IRT format auto-detected.

### AI COACH

- **Anthropic API Key** input (password field with 👁 toggle to reveal)
- **Test** button to verify the key
- The key lives in `localStorage` only; it is **not** sent to any TraderLab server

### DATA

- **Log Name** — base name for backup files (e.g. `Sean_ES_2026`)
- **Save Location** — folder hint (browser-dependent)
- **💾 Save** / **↓ Export** / **↑ Import** — JSON backups
- **↺ Clear Today's Session** — resets pre-market, bias, fuel; keeps trades and journal
- **✕ Clear Trade Log** — permanently delete all trades (export first)
- **✕ Clear All Sessions** — permanently delete all journal sessions
- **✕ Clear Everything** — nuclear option

---

## 18. Data, Privacy & Backups

### Where Data Lives

Everything is stored in your browser's `localStorage`. Nothing is ever transmitted. There is no server, no analytics, no telemetry, no account, no subscription.

### What Persists

| Key | What It Stores |
|-----|---------------|
| `tl_sessions` | Journal sessions |
| `tl_trades` | Trade log |
| `tl_missed` | Missed trades |
| `tl_pm` | Pre-market levels, bias, fuel |
| `tl_preflight` | Preflight answers |
| `tl_st_checks` | Structured-trade go/no-go state |
| `tl_instrument` | Default instrument |
| `tl_journal_dropdowns` | Journal dropdown customizations |
| `tl_bmurl` / `tl_bmurl_price` | BMBridge URLs |
| `tl_bmmap` | CSV column mapping |
| `tl_goals` | Daily goals |
| `tl_thresholds` | Performance color thresholds |
| `tl_an_*` | Analytics card / section visibility + order |
| `tl_tl_*` | Trade Log card visibility + order |
| `tl_whatif_presets` | What-If saved scenarios |
| `tl_ai_key` | Anthropic API key (Mode 2) |
| `tl_hits` | Tagged-level log |
| `tl_schema_version` | Schema version for migrations |

### Backups

Export a JSON backup regularly via **Settings → DATA → ↓ Export**. Imports merge with your existing data — they don't overwrite.

### Backwards Compatibility

Every new TraderLab 101 version is built to read data saved by earlier versions. You should never lose data on a version upgrade. If you ever do, restore from your most recent JSON backup.

---

## 19. Troubleshooting

### Google Sheets import fails

Local HTML files can't fetch from Google due to browser CORS rules. Workaround: open the published CSV URL in a new tab, **Ctrl+A**, **Ctrl+C**, paste into the textarea in TraderLab.

### BMBridge not connecting

Make sure BMBridge is running and the URL is correct. The HTML file must be served from the same origin **or** BMBridge must serve CORS headers. Use the **Test** button in Settings to verify.

### Data disappeared

You may have cleared browser cache. If you have a JSON backup, use **Settings → DATA → ↑ Import** to restore. Going forward, export weekly.

### Numbers look wrong

Verify your instrument settings. **MES** = 0.25 pt / $1.25 per tick. **ES** = 0.25 pt / $12.50 per tick. **MNQ** = 0.25 pt / $0.50 per tick. **NQ** = 0.25 pt / $5.00 per tick.

### Cards or sections missing

Check the **⚙ Toggle Cards** button (overview cards) or **⚙ Customize Dashboard** (chart sections). They may be hidden, not gone.

### Live feed not updating

Click **Stop** then **Start** in Live Price. If BMBridge is unreachable, the feed silently falls back to Yahoo Finance (~15 minute delay). Check the status banner.

---

## 20. License

TraderLab 101 is licensed under the **[PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0)** — a lawyer-drafted, SPDX-recognized license made for source-available, noncommercial-friendly projects.

**You may** download, run, share unmodified copies, and modify it for your own personal noncommercial use.

**You may not** sell it, sublicense it, build any commercial product / paid course / paid plugin / paid SaaS / commercial AI training set from any portion of it, or remove the embedded build identifiers used to detect unauthorized copies.

For commercial licensing, reach out via the [GitHub repository](https://github.com/SeanDavid-stack/TraderLab101).

See `LICENSE` for the full legal terms and the Required Notice that must travel with every copy.

---

*TraderLab 101 was created by SeanDavid, built on Tom B.'s Traders Lab methodology and Auction Market Theory.*
*"If this — then that. If not — then what?"*
