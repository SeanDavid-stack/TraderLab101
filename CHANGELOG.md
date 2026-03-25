# Changelog

## v1.1 — March 25, 2026

### Bugfixes
- **CRITICAL: R-Multiple Calculation** — Fixed incorrect R on multi-contract trades. Old formula divided total P&L by per-contract risk; correct formula divides by total risk (rPts × contracts). A 2-contract full stop now shows -1R instead of -2R.
- **Panel Layout Fix** — Removed extra `</div>` in trade form that caused panels to leak and display simultaneously.
- **Full Stop Mode** — Form now resets to scale mode after saving. Previously stayed stuck in full stop mode.
- **Full Stop Save** — Save function now correctly reads from full stop price field instead of empty scale fields.
- **Notes Field** — Fixed textarea collapsing to minimum width. Now full-width with 3 rows.

### Data Migration (backward compatible)
- **Startup migration** — Auto-patches existing localStorage data on load: recalculates R on multi-contract trades, converts emotion strings to arrays, adds missing fields.
- **Import migration** — Patches incoming JSON files before applying. Old v1.0 exports import cleanly into v1.1.

### New Features
- **Trade Editing** — ✎ Edit button on every trade. Loads all data back into form, gold banner, Update Trade button. Trade ID preserved.
- **Per-Instrument Commission** — Each preset carries its own commission rate (MES $0.62, ES $2.32, MNQ $0.62, NQ $2.32). Custom instruments also have a commission field. Global override available.
- **Instrument Filter (Analytics)** — Filter entire dashboard by symbol when trading 2+ instruments. Combines with date range filter.
- **Import Levels — 3 Sources** — BMBridge (URL), CSV File (upload), Google Sheets (published URL with paste fallback for CORS).
- **Import Diagnostics** — Shows CSV headers, unmatched rows, and link to column mapping when 0 levels match.
- **Google Sheets Paste Fallback** — Auto-opens paste section when fetch fails due to CORS.
- **Collapsible Overview & Stats** — Overview cards and Stats by Setup are collapsible in Trade Log.

### UI/UX Improvements
- Settings split: "Live Price Feed" and "CSV Column Mapping" are separate cards.
- Commission moved from Daily Goals to Instrument & Contract section.
- Full Stop panel shows contract count, red border, -1R help text.
- All BMBridge-specific language removed from file/sheet import contexts.

## v1.0 — March 25, 2026

### Initial Public Release
- Preflight Checklist, Pre-Market Levels, Open Context Alignment, Bias Tracking
- Live Price Feed (BMBridge → Yahoo fallback)
- Trade Log with 3 scale-outs, R-multiple, 8 setups + custom, targets, process rating, execution errors, emotional state
- Missed Trades with What If? panel and reason breakdown
- Journal with bias timeline, preflight snapshot, review mode
- Analytics Dashboard with 13 cards, 15 chart sections, date range filter
- Methodology Reference with 9 sections
- Settings with instrument presets, goals, export/import
