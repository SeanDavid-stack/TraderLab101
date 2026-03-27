# TraderLab 101 — User Guide

**Version 2.1 · March 2026**

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Preflight Checklist](#preflight-checklist)
3. [Pre-Market Levels](#pre-market-levels)
4. [Custom Levels](#custom-levels)
5. [Open Context Alignment](#open-context-alignment)
6. [Level Tracking & Live Price](#level-tracking--live-price)
7. [Trade Log](#trade-log)
8. [Trade Screenshots](#trade-screenshots)
9. [Missed Trades](#missed-trades)
10. [Journal](#journal)
11. [Analytics Dashboard](#analytics-dashboard)
12. [What-If Lab](#what-if-lab)
13. [AI Trade Coach](#ai-trade-coach)
14. [CSV Import & Column Mapping](#csv-import--column-mapping)
15. [Settings & Configuration](#settings--configuration)
16. [Data Management & Migration](#data-management--migration)
17. [Troubleshooting](#troubleshooting)

---

## Getting Started

### Installation

No installation needed. TraderLab 101 is a single HTML file.

1. Download `TraderLab101.html`
2. Save anywhere on your computer
3. Double-click to open in Chrome (recommended)
4. Read the welcome splash, click "Let's Go"

### First-Time Setup

Go to **Settings** (bottom of nav) and configure:

1. **Instrument** — select preset (MES/ES/MNQ/NQ) or add custom
2. **Commission** — per-instrument or global override
3. **BMBridge** (optional) — Levels Feed URL + Live Price Feed URL
4. **RTH Buffer** — minutes to wait after 9:30 ET before reconciling (default 3)
5. **CSV Column Mapping** (optional) — map your source labels to TraderLab fields
6. **Daily Goals** — max loss, max trades, commission override

### How Data Is Stored

All data lives in browser localStorage:
- Stays on your computer — nothing sent to servers
- Persists between sessions unless you clear browser data
- **Export backups regularly** via Settings → Export Backup
- Migration system protects data across version updates

---

## Preflight Checklist

### Completing Preflight

1. Navigate to **Preflight** in the left nav
2. Answer at least 3 of the 8 questions
3. Click **✅ Complete Preflight**
4. Snapshot saves to today's journal automatically

### Editing After Completion

Your answers are always editable — completion is never a lock-out:

- **On the Preflight tab:** Edit any field, completion status preserved, journal snapshot auto-updates
- **↺ Reset & Redo:** Appears after completing. Keeps all answers, removes the completion flag. Edit and re-complete when ready.
- **In the Journal:** Open the 📋 Preflight Answers section — same 8 fields, fully editable. Changes sync back to the Preflight tab and storage.

### Where Preflight Data Lives

1. **localStorage (`tl_preflight`)** — saves on every keystroke
2. **`pmData.preflightSnap`** — attached when you click Complete
3. **Session record** — baked in permanently when you Save Session in Journal
4. **Export backup** — included in JSON file

---

## Pre-Market Levels

### Standard Fields

| Field | Section |
|-------|---------|
| pHigh, pLow, pClose, pVPOC | Prior Day Levels |
| Settlement | Prior Day Levels |
| pVAH, pVAL | Prior Value Area |
| ONH, ONL, ON/VPOC, Today's Open | Overnight & Today's Open |

### Import Sources

- **BMBridge** — uses configured Levels Feed URL
- **CSV File** — upload any CSV with level names and prices
- **Google Sheet** — paste published CSV URL or raw content
- **Manual** — type directly into fields

### Bias

Click ▲ LONG, — NEUTRAL, or ▼ SHORT. Changes logged with timestamp and reason.

### Fuel Map

Add trapped participant levels: buyers/sellers/stops with price and notes.

---

## Custom Levels

### Adding

In the purple **Custom Levels** card on Pre-Market Levels:

- **Name only:** Type name, press Enter. Gold border = needs price. Fill later.
- **Name + price:** Type name, tab, enter price, press Enter or + Add.
- **From CSV:** Unmapped labels with valid prices auto-add as custom levels.

### Managing

- Edit price inline anytime
- ✕ removes the level
- Levels without a price are skipped by the tracker (safe placeholder)

### Full Integration

Once a price is set, the custom level is tracked in: level tracker (purple CUSTOM group), live detection, reconciliation, tag log, manual tag/untag, journal snapshots (purple ★ pills), and new-day clear.

### CSV Routing

In Settings → CSV Column Mapping, every dropdown includes:
- Standard fields (◎ Prior High, ◎ Settlement, etc.)
- Your custom levels (★ Custom: VWAP, etc.)
- Create option (★ + New Custom Level)

---

## Open Context Alignment

Once Today's Open, pHigh, and pLow are entered, TraderLab auto-detects the open type (HOR/LOR/HIR/LIR/IR-IV) and shows a decision tree. Click **Confirm** to lock it.

---

## Level Tracking & Live Price

### Price Feed

Polling order: BMBridge Price Feed → BMBridge Levels Feed → Yahoo Finance (~15 min delay).

### RTH Stale Data Protection

Prevents false tags from overnight data:
- Tracks last pre-RTH price
- Waits for configured buffer after 9:30 ET
- Tags only fire once fresh data confirmed
- Mid-session opens accept data immediately

### Tag Sources

| Badge | How Tagged |
|-------|-----------|
| ✓ tagged | Live detection (price within 0.50 pts) |
| ✓ tagged ◈ | Reconciliation (session range passed through) |
| ✓ tagged ✎ | Manual (⊕ button click, cyan badge) |

### IB Auto-Fill

At 10:30 ET, IBH/IBL auto-fill from session range. 1.5× and 2.0× extensions calculated.

---

## Trade Log

### Logging a Trade

1. Select **Setup** (8 built-in + custom)
2. Pick **Direction** (auto-suggested from feed)
3. Enter **Entry** and **Stop** (entry auto-filled from live price)
4. Fill **Scale-outs** (Scale 1 = RN, Scale 2 = target, Scale 3 = runner)
5. Tag **Targets** → set price → mark Hit/Bailed/Missed
6. Rate **Process** (A/B/C/F)
7. Tag **Errors** and **Emotions**
8. Add **Notes** and **📷 Screenshots**
9. Click **Log Trade**

### Daily Goals Tracker

Shows today's P&L (always real fees, immune to toggle), trade count vs max, loss limit warnings.

---

## Trade Screenshots

Attach chart images to individual trades:

1. Expand the **📷 Screenshots** section in the trade form
2. Paste image URLs — one per line (Imgur, Gyazo, ShareX, Google Drive, etc.)
3. Live thumbnail previews show as you type
4. Supports multiple images per trade

**Display:**
- Purple **📷 3** badge on collapsed trade cards (shows count at a glance)
- Clickable thumbnails in expanded trade detail
- Thumbnails in journal trade review
- Populated back into form when editing a trade

---

## Missed Trades

### Logging

Enter date, direction, entry, stop, estimated exit, and select reasons (multi-select).

### Filters

- **Period:** All / 1W / 1M / 3M / 6M / YTD
- **Instrument:** auto-appears with 2+ instruments

### What-If Impact

Shows P&L if you'd taken these trades. Top 3 costliest miss reasons ranked by dollar impact.

---

## Journal

### Saving a Session

1. Navigate to **Journal**
2. Fill in open type, day type, result, process, setups
3. Edit **📋 Preflight Answers** if needed (syncs back to Preflight tab)
4. Write notes and lessons
5. Add screenshot URLs
6. Click **Save Session**

### What Gets Saved

Levels (including custom), fuel map, bias log, hit log, preflight answers, trade screenshots, and all form fields — permanently in the session record.

### Editing Past Sessions

Click ✎ on any session card → loads all fields back into the form (including preflight answers). Modify and re-save.

---

## Analytics Dashboard

### Filters

- **Period:** All / 1W / 1M / 2M / 3M / 6M / YTD / custom
- **Instrument:** All or specific
- **Fee toggle:** Fees ON (net) or OFF (gross) — synced globally

### Visual Charts

6 tabbed SVG charts: Daily P&L, Win Rate Trend, R Distribution, By Setup, By Process, By Time.

### Sections

15+ collapsible, reorderable sections. ⚙ Sections to show/hide. ✕ Close button on dropdown. State persists.

### CSV Export

↓ Export CSV → 30+ computed metrics, 10 breakdown tables. Respects filters and fee toggle.

---

## What-If Lab

10 simulation panels modeling changes to your trading. Fee toggle synced with global state. Edge Optimizer ranks 15+ dimensions. Save/load presets.

---

## AI Trade Coach

- **Free:** Copy data + prompt to clipboard → paste into any AI
- **API:** Anthropic key in Settings → in-app analysis (~$0.03/call)
- Three types: Full Review, Error Audit, Setup Analysis

---

## CSV Import & Column Mapping

### Supported Formats

1. **Standard:** col1 = name, col2 = price
2. **Three-column:** col1 = name, col2 or col3 = price
3. **IRT:** auto-detected — col1 = symbol, col2 = price variable, col3 = label

### Setting Up Mappings

Settings → CSV Column Mapping:
1. Type CSV label exactly as it appears
2. Select target from dropdown (standard field, custom level, or + New Custom Level)
3. Click Add

Mappings save to localStorage. One-time setup per data source.

### Unmapped Labels

Labels without a mapping that have valid prices → auto-added as custom levels. No clicks needed.

---

## Settings & Configuration

### Instruments

MES ($1.25/tick, $0.62 comm), ES ($12.50/tick, $2.50 comm), MNQ ($0.50/tick, $0.62 comm), NQ ($5.00/tick, $2.50 comm). Custom instruments supported.

### BMBridge

Two URLs: ◎ Levels Feed (imports) + ⚡ Live Price Feed (real-time). Auto-test on Settings open.

### Daily Goals

Max daily loss, max trades, commission override. Goals tracker always shows real fees.

---

## Data Management & Migration

### Export / Import

- **Export:** Settings → Export Backup → JSON file with `schemaVersion`
- **Import:** Settings → Import Backup → auto-migrates from any version

### Updating Versions

1. Export backup (always do this first)
2. Replace HTML file with new version
3. Open — migration runs automatically
4. Verify data intact

### Migration Rules (SACRED)

- Migrations only ADD fields with safe defaults
- Migrations NEVER delete, rename, or overwrite
- Every migration is idempotent
- Documented in `DATA SCHEMA & MIGRATION` comment block

### Backward Compatibility

| From | To v2.1 | Result |
|------|---------|--------|
| v1.x | ✅ | Full migration |
| v2.0 | ✅ | Adds new fields |
| v2.1 | ✅ | No changes needed |

---

## Troubleshooting

### "0 levels matched" on CSV import
Unmapped labels auto-add as custom levels. To map to standard fields: Settings → CSV Column Mapping.

### Live price not updating
Check BMBridge URL in Settings. Click Test buttons. Falls back to Yahoo (~15 min delay).

### Levels not being tagged
Verify price is set (gold border = missing). Tags only fire during RTH. Check RTH buffer setting.

### Fee numbers inconsistent
Fee toggle syncs globally. Goals tracker always shows real fees regardless of toggle.

### Data lost after browser update
Import your backup: Settings → Import Backup. **Always export backups regularly.**

### Preflight answers disappeared
If you didn't Save Session in Journal, answers only exist in localStorage until new day clear. Always save your journal.

---

*"If this — then that. If not — then what?"*
*TraderLab 101 v2.1 · Created by SeanDavid · Based on Tom B.'s Traders Lab methodology*
