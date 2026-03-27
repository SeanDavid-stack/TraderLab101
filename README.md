# TraderLab 101

**v2.1.1 · Free trading journal + performance simulator for ES/MES futures traders**
Built on Auction Market Theory · Tom B.'s Traders Lab methodology

---

## What Is This?

A single HTML file that runs in your browser. No server, no accounts, no subscriptions. All your data stays on your computer in localStorage. Open the file, start trading.

TraderLab 101 is a complete trading workflow — from pre-market preparation through trade logging, analytics, and performance simulation. It was built specifically for futures traders using Auction Market Theory and structured trade setups.

---

## Features

### Session Workflow (7-Step Stepper)
- **Preflight Checklist** — 8 research questions, editable after completion, ↺ Reset & Redo, editable in Journal
- **Pre-Market Levels** — Log key levels, settlement, set bias, map fuel, detect open type
- **Custom Levels** — add any level you want tracked (Weekly VPOC, VWAP, S/R, etc.)
- **Opening Print System** — pre-RTH estimate → auto-confirm from feed → manual capture. Layered workflow with source badges (⚡ live, 📌 captured, manual)
- **Open Context Alignment** — If/then flowcharts for 7 open types
- **Live Price Feed** — near real-time level detection with IB auto-fill at 10:30 ET
- **Visual progress stepper** with next-step prompts and nav completion badges

### Level Tracking & Detection
- **Near real-time level tagging** (~2–10s delay) with proximity gradient (5 intensity levels)
- **Settlement + Custom Levels** — fully tracked alongside standard levels
- **Three tag sources**: Live (✓), reconciled (✓ ◈), manual (✓ ✎)
- **IB auto-fill** — session high/low at 10:30 ET, with 1.5× and 2.0× extensions
- **RTH stale data protection** — configurable buffer, freshness detection

### Trade Management
- **Trade Log** — 3 scale-outs + runner, R-multiple tracking
- **📎 Media attachments** — chart screenshots (thumbnails) + video replay links (🎬 clickable) per trade
- **Customizable labels** — execution errors, emotions, missed reasons, triggers all configurable in Settings
- **4 entry trigger types** — track which triggers produce edge
- **Missed Trade Log** — full edit support, period + instrument filters, what-if impact, top 3 costliest reasons
- **Smart defaults** — auto-fill entry price + auto-select direction from live feed

### Analytics Dashboard
- **Equity curve** (gross + net), **6 visual SVG charts**, **15+ analysis sections**
- **Collapsible & reorderable sections** with persistent state
- **Global fee toggle** — synced across Analytics, Trade Log, Missed Trades, What-If Lab
- **Period + instrument filters** · **CSV analytics export** (30+ computed metrics)
- Calendar view, tilt detection, sweet spot finder

### 🔬 What-If Lab — Performance Simulator
10 simulation panels: errors, emotions, quality, timing, triggers, improvements, sizing, stop caps, daily discipline, missed trades. Edge Optimizer ranks 15+ dimensions by P&L impact.

### 🧠 AI Trade Coach
- **Free mode** — copy data + prompt to clipboard for any AI
- **API mode** — optional Anthropic key for in-app analysis (~$0.03/call)

### Import System
- **BMBridge dual feeds** — separate level import + live price URLs
- **CSV / IRT / Google Sheets** — format auto-detected
- **User-configurable column mapping** with ★ Custom Level routing
- **Unmapped labels auto-add** as custom levels

### Data Safety & Migration
- **SACRED rule** — user data is never deleted, renamed, or overwritten
- **Schema versioning** (currently v4) with dual migration paths (page load + import)
- **Backward compatible** — v1.x, v2.0, v2.1, v2.1.1 backups all import cleanly

---

## Quick Start

1. Download `TraderLab101_v2_1_1.html`
2. Open in Chrome (or any modern browser)
3. Go to **Settings** — select instrument, set commission
4. Follow the 7-step workflow: Preflight → Levels → Open Context → Live Price → Trade → Missed → Journal
5. Review in **Analytics**, simulate in **What-If Lab**
6. **Export backups regularly** via Settings

---

## Data & Privacy

- All data in browser localStorage — nothing sent to any server
- Optional: AI Coach API calls (you initiate), live price feeds
- Export/import JSON backups with full schema migration
- Your data, your control

---

## Requirements

- Modern web browser (Chrome recommended)
- Internet needed only for: Google Fonts, live price feed, AI Coach API
- Works offline for all other features

---

## Instruments

Pre-configured: MES, ES, MNQ, NQ. Custom instruments via Settings.

---

## Backward Compatibility

| Source Version | Import Into v2.1.1 | What Happens |
|---------------|-------------------|--------------|
| v1.x (no schema) | ✅ | Full migration: adds dates, normalizes trades, adds defaults |
| v2.0 (schema 2) | ✅ | Adds customLevels, screenshots, normalizes new fields |
| v2.1 (schema 3) | ✅ | Adds missed trade screenshots |
| v2.1.1 (schema 4) | ✅ | No migration needed |

---

## License

MIT License. Free to use. Built for the Traders Lab community.
Created by **SeanDavid** · Based on **Tom B.**'s Traders Lab methodology
