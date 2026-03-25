# TraderLab 101 — User Guide

**Version 1.0 · March 2026**

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Pre-Session Workflow](#pre-session-workflow)
3. [During the Session](#during-the-session)
4. [Trade Log](#trade-log)
5. [Missed Trades](#missed-trades)
6. [Journal](#journal)
7. [Analytics Dashboard](#analytics-dashboard)
8. [Methodology Reference](#methodology-reference)
9. [Settings & Configuration](#settings--configuration)
10. [Data Management](#data-management)
11. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Installation

There is no installation. TraderLab 101 is a single HTML file that runs in your browser.

1. Download `TraderLab101.html`
2. Save it anywhere on your computer
3. Double-click to open in Chrome (recommended) or any modern browser
4. You'll see a one-time welcome splash — read it, click "Let's Go"

### First-Time Setup

Before your first session, go to **Settings** (bottom of the left nav) and configure:

1. **Instrument & Contract** — Click your instrument preset (MES, ES, MNQ, NQ) or add a custom one. This sets tick size, tick value, and default commission for P&L calculations.

2. **Commission** — Each preset includes a default commission (e.g. $0.62/RT for MES). You can adjust this per-instrument or set a global override that applies to all instruments.

3. **Live Price Feed** (optional) — If you use Sierra Chart with BMBridge, enter your BMBridge URL for real-time price data. If not configured, TraderLab uses Yahoo Finance automatically (~15 min delay).

4. **CSV Column Mapping** (optional) — If you import levels from a CSV file or Google Sheet, configure the mapping between your CSV column names and TraderLab's level fields.

### How Data Is Stored

All data lives in your browser's `localStorage`. This means:
- Your data stays on your computer — nothing is sent to any server
- Data persists between sessions as long as you don't clear browser data
- If you clear browser cache/data, your TraderLab data will be erased
- **Always export backups regularly** via Settings → Export Backup

---

## Pre-Session Workflow

The recommended flow before every session:

### Step 1: Preflight Checklist

Navigate to **Preflight** in the left nav. Answer at least 3 of the 8 pre-session questions:

1. What is the Opening Context?
2. What is the HTF Context?
3. What did we do in the previous RTH session?
4. What did we do in the ETH/Overnight session?
5. Where are the stops/fuel?
6. Based on where the fuel is — who is offside?
7. Any news or data events?
8. Top-down analysis — overall read for today

When finished, click **✅ Complete Preflight**. This:
- Saves a snapshot of your answers to today's journal
- Auto-sets the journal's preflight status
- Shows a green timestamp confirmation

If you skip this step, the Journal tab will show a red warning banner.

### Step 2: Pre-Market Levels

Navigate to **Pre-Market Levels**. Enter your key levels:

**Import options (top of page):**
- **BMBridge** — Enter your URL and click Import for auto-fill from Sierra Chart
- **CSV File** — Upload any CSV with level names in column 1 and prices in column 2 or 3
- **Google Sheet** — Paste a published Google Sheet CSV URL (or paste CSV content manually if fetch is blocked)

**Manual entry:** Fill in the level fields directly:
- Prior Day: pHigh, pLow, pClose, pVPOC
- Value Area: pVAH, pVAL
- Overnight: ONH, ONL, ON/VPOC, Today's Open

**Bias:** Click ▲ LONG, — NEUTRAL, or ▼ SHORT at the top to set your directional bias. Change it anytime during the session — every change is logged with a timestamp and reason.

**Fuel Map:** Add trapped participant levels below the main levels. Click + Add Fuel Level, select buyers/sellers, enter the price level and notes about why participants are trapped there.

### Step 3: Open Context Alignment

Navigate to **Open Context**. Once you've entered Today's Open, pHigh, and pLow, TraderLab automatically determines the open type (HOR, LOR, HIR, LIR, or IR-IV) and displays a statistical decision tree.

Follow the flowchart by clicking Yes/No at each decision point. This guides you through:
- Whether the market is responsive or impulsive
- Whether to trade with or against the gap
- What day type to expect
- Which trade plans apply

The open type also feeds into analytics and journal entries.

---

## During the Session

### Live Price Tracker

Navigate to **Live Price** to see:
- Current ES/MES price with change from prior close
- Targets hit today (count)
- Initial Balance levels (auto-fill after 10:30am ET if using BMBridge)
- Level Tracker — shows every pre-market level with distance from current price and hit/near status

The feed auto-detects BMBridge (real-time) and falls back to Yahoo Finance (~15 min delay) if BMBridge is unavailable. A status banner at the bottom shows which feed is active.

### Structured Trades

Navigate to **Structured Trades** to see the Go/No-Go checklist for all 8 setups. Each setup shows alignment badges:
- ▶ **In Play** (green) — conditions met, setup is valid
- ◆ **Waiting** (gold) — some conditions met, waiting for confirmation
- ⚠ **Not In Play** (red) — conditions not met

---

## Trade Log

Navigate to **Trade Log** to log and review trades.

### Logging a Trade

The form at the top captures:

**Row 1:** Date, Setup, Direction (Long/Short), Instrument, Time (hour:minute dropdowns)

**Row 2:** Entry Price, Stop Price, Trigger Type (Limit/Market/Stop)

**Scale-Outs:** Up to 3 scales with exit price and contracts per scale:
- Scale 1 — Risk Neutral (buy back your stop)
- Scale 2 — Target (primary profit target)
- Runner / Final Exit (trail or full exit)

R-multiple is auto-calculated for each scale. The summary line shows total P&L in points, dollars, and R.

**Targets:** Click any of the 17 target chips (DVPOC, VWAP, MID, pHigh, etc.) to add a target row. Each target has:
- Name (auto-labeled from chip)
- Price (auto-fills from pre-market levels when possible)
- Outcome: ✓ Hit / ↩ Bailed / ✗ Missed
- Bail Reason (only when Bailed): Price Action Change, Market Structure Shift, News, Fear/Emotion, Protecting P&L, Time, Other

You can also type custom target names.

**Process Rating:** A (perfect process), B (good, minor deviation), C (off plan), F (broke the rules)

**Exit Time:** Optional hour:minute dropdowns — auto-calculates trade duration

**Notes:** Free-text for entry reason, observations, what happened

**Execution Errors:** Expandable section with 12 error chips (multi-select) plus ideal exit price for error cost calculation

**Emotional State:** 10 emoji chips (multi-select): Confident, Patient, Focused, Anxious, Frustrated, Greedy, Fearful, Revenge, Bored, Neutral

### Stat Cards

The overview shows 11 cards: Win Rate, Avg R, Profit Factor, Total P&L, Risk Neutral Rate, Full Stop Rate, A-Process Win Rate, Expectancy, Best Trade, Avg Win/Loss, Break Even Rate.

- Click **⚙ Toggle Cards** to show/hide specific cards
- **Drag cards** to rearrange — order persists
- Cards auto-size to fill available space

### Daily Goals Tracker

If you've configured goals in Settings, a "TODAY" bar appears showing:
- Today's net P&L (with fees)
- Trade count vs limit
- Loss vs max daily loss
- All updated live after each trade save

### Stats by Setup

Below the stat cards, a breakdown shows per-setup performance: trade count, win rate, avg R, Risk Neutral rate, and total P&L.

---

## Missed Trades

Navigate to **Missed Trades** to log trades you identified but didn't take.

### Logging a Missed Trade

**Simple mode (default):** Entry price, target/price reached, stop price, contracts

**Multi-scale mode:** Click "Expand for multi-scale" to enter separate RN, Target, and Runner exits — mirrors the actual trade log structure. Remaining contracts auto-calculate as hitting your stop.

**Live preview** shows "Would have won: +5.00 pts · +$25" or "Would have lost: -3.00 pts · -$15" as you type.

**Why did you miss it?** Select one or more reasons: Fear, Uncertainty, Hesitation, Distraction, Not at Desk, Didn't See Setup, Overtrading Concern, Recent Loss/Tilt, Conditions Not Met, Other.

### What If? Panel

Shows side-by-side comparison:
- **Actual P&L** — your real trading results
- **If All Missed Trades Taken** — combined P&L with trade count and win rate

The insight line tells you whether hesitation is costing you money ("missed winners outweigh missed losers") or your filter is working ("trades you skipped were net negative").

### Reason Breakdown

Bar chart showing each miss reason with count, win/loss split, and P&L. Answers: "When I miss due to fear, are those mostly winners I should have taken?"

### Trade List

Each entry shows as color-coded:
- **+$250 missed** (red) — would-have-been winner
- **-$75 dodged** (green) — would-have-been loser

---

## Journal

Navigate to **Journal** to record and review daily sessions.

### Session Entry

Use the date navigator (◄ ► Today) to select a date. For today, the form is editable. For past dates with saved sessions, review mode shows a read-only summary.

Fields include:
- Open Type (auto-filled from session)
- Profile Shape (how the day resolved)
- Session Result
- IB Outcome
- Market Responsive
- Risk Neutral, Checklist Used, Preflight Done
- Key Levels Traded
- Trade Notes / Auction Story
- Lesson / Rule Reinforced
- Chart Screenshots (paste URLs)

### Review Mode

Past sessions display a formatted review with:
- Session metadata badges
- Pre-market levels snapshot
- Preflight checklist answers (if completed)
- Fuel map
- Targets tagged
- Bias timeline with changes
- All trades for that day with P&L summary

---

## Analytics Dashboard

Navigate to **Analytics** for the full performance dashboard.

### Filters

**Date Range:** All, 1W, 1M, 2M, 3M, 6M, YTD, or custom From/To dates. The entire dashboard re-renders for the selected period.

**Instrument:** When you trade 2+ instruments, a filter row appears. Click any instrument to isolate analytics for that symbol.

### Overview Cards (13)

All cards are toggleable (click ⚙ Toggle Cards) and draggable (grab and reorder). Order and visibility persist across sessions.

- **Win Rate** — W/L/BE breakdown
- **Net P&L** — with commission deducted when configured; subtitle shows gross + fees
- **Profit Factor** — gross wins ÷ gross losses
- **Expectancy** — average P&L per trade (gross and net)
- **Avg R-Multiple** — average R across all setups
- **Risk Neutral Rate** — percentage of trades that reached risk-neutral
- **Full Stop Rate** — percentage of trades that took the full -1R loss
- **Avg Win / Loss** — dollar amounts with ratio
- **Recovery Factor** — net P&L ÷ max drawdown
- **First Trade Win Rate** — performance on first trade of each session
- **Win Rate After Loss** — bounce-back rate (measures tilt resilience)
- **Break Even Rate** — percentage of scratch trades
- **Trading Days** — session count with trades/day average

### Chart Sections (15)

Each section can be toggled on/off via ⚙ Customize Dashboard.

1. **Equity Curve** — cumulative P&L with gross (solid) and net-of-fees (dashed) lines
2. **Daily P&L Calendar** — month heatmap with green/red cells and month navigation
3. **Streaks & Consistency** — max win/loss streaks, current streaks, green/red day counts
4. **P&L by Day of Week** — which days are most profitable
5. **P&L by Time of Day** — performance by RTH time buckets
6. **Drawdown & Trade Efficiency** — max drawdown depth + execution error cost breakdown
7. **P&L by Setup** — bar chart with trade count, win rate, and P&L per setup
8. **By Direction & Instrument** — long vs short, per-instrument breakdown
9. **By Open Type & Trend** — performance filtered by open type and trend alignment
10. **By Trigger & Emotion** — market/limit/stop + emotional state analysis
11. **Sweet Spot Finder** — trade count per day vs profitability
12. **Weekly Summary** — last 12 weeks with running total
13. **Tilt Detection** — flags sessions with consecutive losses, revenge trades, or high volume
14. **Bias Change Performance** — held vs flipped, P&L by bias at time of trade
15. **Trade Duration** — avg winner vs loser hold time, performance by hold time bucket
16. **P&L by Target** — hit/bailed/missed rates with bail reason breakdown
17. **Market Behavior vs Historical Norms** — your observed hit rates compared to methodology statistics

---

## Methodology Reference

Navigate to **Methodology** (under Reference in the left nav) for a complete reference of all trade setups from Tom B.'s methodology. Nine accordion sections cover:

1. Opening Trades (Gap & In-Range)
2. IBC — Initial Balance Continuation
3. IBF — Initial Balance Failure
4. Mean Reversion
5. VPOC Shift
6. BAR — Break and Retest
7. MID > VWAP > VPOC
8. VHVN > VPOC
9. Statistical Reference

Each section includes entry criteria, invalidation rules, target structure, and key statistics.

---

## Settings & Configuration

### Instrument & Contract

- Click a preset (MES, ES, MNQ, NQ) or define a custom symbol with tick size, tick value, and commission
- Commission is per round-trip, per contract
- The global commission override applies to all instruments if set; otherwise per-instrument defaults are used

### Live Price Feed

- Enter your BMBridge URL for real-time data from Sierra Chart
- If not set or unavailable, Yahoo Finance is used automatically
- Click Test Connection to verify

### CSV Column Mapping

- Used by all import methods (BMBridge, CSV file, Google Sheets)
- Maps the first column in your CSV to TraderLab level fields
- Edit labels to match your data source
- Click Reset to Defaults to restore BMBridge-standard mapping

### Journal Dropdown Options

- Customize the options in journal dropdowns (profile shapes, session results, IB outcomes, responsiveness)
- Add/remove options, reset to defaults

### Daily Goals

- **Max Daily Loss ($)** — toast warning when limit reached
- **Max Trades Per Day** — warning when trade count hits limit
- **Min Process Rating** — warning on trades below your standard
- Goals are checked every time you save a trade

---

## Data Management

### Export

Settings → Export Backup downloads a JSON file containing all sessions, trades, missed trades, levels, settings, goals, and journal data. **Do this regularly.**

### Import

Settings → Import Backup restores from a JSON file. Data is merged with existing data (not replaced).

### Clear Options

- **Clear Session** — resets today's pre-market levels and bias
- **Clear All Trades** — deletes trade log (1 confirm)
- **Clear All Sessions** — deletes journal sessions (2 confirms)
- **Clear Missed Trades** — deletes missed trades (1 confirm)
- **Clear Everything** — nuclear option, deletes all data (2 confirms + auto-reload)

---

## Troubleshooting

### Google Sheets import fails
Local HTML files can't fetch from Google due to browser security (CORS). Use the paste method: open the published CSV URL in a new tab, Ctrl+A, Ctrl+C, paste into the textarea in TraderLab.

### BMBridge not connecting
Ensure BMBridge is running and the URL is correct. The HTML file must be served from the same origin or BMBridge must have CORS headers enabled. Test with the Test Connection button in Settings.

### Data disappeared
Check if you cleared browser data. If you have a JSON backup, use Import to restore. Going forward, export regularly.

### Numbers look wrong
Verify your instrument settings (tick size, tick value) match your actual instrument. MES = 0.25 pts / $1.25 per tick. ES = 0.25 pts / $12.50 per tick.

### Cards or sections missing
Check ⚙ Toggle Cards (for overview cards) or ⚙ Customize Dashboard (for chart sections). Cards/sections may be toggled off.

---

*Created by SeanDavid · Based on Tom B.'s Traders Lab methodology*
*"If this — then that. If not — then what?"*
