# TraderLab 101

**A complete trading journal, analytics dashboard, and methodology reference tool built for Auction Market Theory traders.**

Single HTML file. Zero dependencies. Runs locally in your browser. Your data never leaves your computer.

![Version](https://img.shields.io/badge/version-1.0-gold)
![License](https://img.shields.io/badge/license-MIT-blue)
![Dependencies](https://img.shields.io/badge/dependencies-none-green)

---

## What Is This?

TraderLab 101 is an all-in-one trading tool designed around Tom B.'s Traders Lab methodology and Auction Market Theory. It handles everything from pre-session research to post-session review — preflight checklists, pre-market levels, open context alignment, structured trade setups, trade logging with scale-outs, missed trade tracking, journaling, and a full analytics dashboard with 15+ chart sections.

**This is not a generic journal.** Every field, every stat, every alignment badge is purpose-built for how the Traders Lab community actually trades ES/MES futures.

## Quick Start

1. **Download** `TraderLab101.html`
2. **Open** it in Chrome (or any modern browser)
3. **Start** with Pre-Market Levels → enter your levels → confirm open type → trade

**Want to see it with data?** Download `traderlab-demo.json`, then go to Settings → Import Backup → select the file. This loads 61 sessions, 220 trades, and 41 missed trades so you can explore the analytics, journal, and charts immediately.

That's it. No install. No server. No account. No subscription.

## Features

### Session Workflow
- **Preflight Checklist** — 8 pre-session questions with completion tracking
- **Pre-Market Levels** — manual entry, CSV file import, BMBridge auto-import, or Google Sheets
- **Open Context Alignment** — statistical decision tree for all 5 open types (HOR, LOR, HIR, LIR, IR-IV)
- **Bias Tracking** — Long/Short/Neutral with timestamped change log and reasons
- **Live Price** — BMBridge real-time feed with auto-fallback to Yahoo Finance (~15 min delay)
- **Level Tracker** — monitors which pre-market levels get hit during the session

### Trade Log
- 3 scale-outs with R-multiple calculation (Risk Neutral + Target + Runner)
- 8 built-in setups + custom setups
- Target tracker with 17 level chips + custom targets, price, outcome (Hit/Bailed/Missed), and bail reasons
- Exit time + auto-calculated trade duration
- Process rating (A/B/C/F)
- 12 execution error types with ideal exit and error cost calculation
- Emotional state tagging (multi-select)
- Per-instrument commission tracking
- 11 toggleable, draggable stat cards

### Missed Trades
- Simple mode (entry/target/stop) or multi-scale (RN + Target + Runner)
- 10 miss reasons with multi-select
- What If? panel — shows actual P&L vs combined if all missed trades were taken
- Reason breakdown with win/loss split per reason

### Journal
- Auto-filled open type from confirmed session
- Bias timeline (color-coded)
- Preflight completion flag with warning if skipped
- Full preflight snapshot saved to each session
- Screenshots, notes, lessons
- Review mode for past sessions with complete data

### Analytics Dashboard
- **13 overview cards** — Win Rate, Net P&L (with commission), Profit Factor, Expectancy, Avg R, Risk Neutral Rate, Full Stop Rate, Avg Win/Loss, Recovery Factor, First Trade WR, Win Rate After Loss, Break Even Rate, Trading Days
- **15 chart sections** — Equity curve (gross + net), calendar heatmap, streaks, day of week, time of day, drawdown, trade efficiency, P&L by setup/direction/instrument/open type/trend/trigger/emotion, sweet spot finder, weekly summary, tilt detection, bias change performance, trade duration, P&L by target with bail reasons, market behavior vs historical norms
- **Date range filter** — All, 1W, 1M, 2M, 3M, 6M, YTD, custom range
- **Instrument filter** — view analytics for specific symbols
- All cards and sections are toggleable and draggable

### Methodology Reference
- 9 accordion sections covering all setups from the PDFs
- Opening trades, IBC/IBF, Mean Reversion, VPOC Shift, BAR, MID>VWAP>VPOC, VHVN>VPOC
- Statistical hit rates by open type

### Settings
- Instrument presets (MES, ES, MNQ, NQ) with per-instrument commission
- CSV column mapping editor (works with BMBridge, file upload, and Google Sheets)
- Journal dropdown customization
- Daily goals (max loss, max trades, min process rating)
- Full data export/import (JSON)
- Granular data clearing options

## Data & Privacy

All data is stored in your browser's `localStorage`. Nothing is sent anywhere. There is no server, no analytics, no tracking. Your trading data stays on your machine.

**Export your data regularly** — `localStorage` can be cleared if you clear browser data. Use Settings → Export Backup to save a JSON file.

## Import Levels

Three ways to get your pre-market levels in:

| Method | How |
|--------|-----|
| **BMBridge** | Auto-imports from Sierra Chart via BMBridge URL |
| **CSV File** | Upload any CSV with level names in column 1, prices in column 2 or 3 |
| **Google Sheets** | Publish sheet as CSV → paste content (fetch blocked from local files due to CORS) |

All three use the same column mapping — configure once in Settings → CSV Column Mapping.

## Browser Support

Tested in Chrome. Works in Firefox, Edge, and Safari. Designed for desktop — functional on mobile but optimized for a monitor setup alongside your charts.

## Attribution

- **Traders Lab** is Tom B.'s trading community and methodology
- **TraderLab 101** is this tool, created by SeanDavid
- Built on Auction Market Theory principles as taught by Tom B.
- Statistical data sourced from Tom B.'s published research

*"If this — then that. If not — then what?"*

## License

MIT License — free to use, modify, and distribute. See [LICENSE](LICENSE) for details.

## Feedback

This is v1.0 — the first public release. If you find bugs or have feature ideas, open an issue on this repo or reach out via the Traders Lab Discord.
