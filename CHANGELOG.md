# TraderLab 101 — Changelog

## v2.1 — Custom Levels, Screenshots, Migration System (March 2026)

### NEW: Custom Levels
Add any price level you want tracked — Weekly VPOC, VWAP, support/resistance, or anything else.
- Add by name only (price later) or name + price
- Fully integrated: level tracker, live detection, tag log, reconciliation, manual tag/untag
- Saved in journal session snapshots, displayed as purple ★ pills in review
- CSV import auto-adds unmapped labels as custom levels
- Settings → CSV Column Mapping includes ★ Custom targets and ★ + New Custom Level

### NEW: Settlement Field
Standard field in Prior Day Levels. Mappable via CSV (`Settle`, `SETL`, `Y/SETT`). Fully tracked.

### NEW: Trade Screenshots
Attach multiple chart images per trade (URL-based, one per line).
- Live thumbnail previews in trade form
- Purple 📷 badge on trade cards showing count
- Clickable thumbnails in expanded trade detail and journal review
- Populated when editing trades
- Migration adds `t.screenshots=[]` to all existing trades

### NEW: Preflight Editing
- ↺ Reset & Redo button after completing (keeps answers, unlocks form)
- Editing answers no longer wipes completion state (was a bug)
- 📋 Preflight Answers section in Journal form — editable, syncs bidirectionally
- Edits in Journal sync back to Preflight tab + storage
- Save Session captures preflight from journal form fields

### NEW: Data Migration System
Formal architecture to protect user data across version updates.
- `migrateLocalStorage()` runs on every page load BEFORE data loads
- `migrateImport(d)` runs on JSON backup import
- SACRED rule: only ADD fields with safe defaults, never delete/rename/overwrite
- All migrations are idempotent
- SCHEMA_VERSION bumped to 3

### NEW: Missed Trades Instrument Filter
Auto-appears with 2+ instruments. Period + instrument filters chain correctly.

### IMPROVED: Fee Toggle Sync
All four pages (Analytics, Trade Log, Missed Trades, What-If Lab) share one state. Daily goals tracker immune — always shows real fees.

### IMPROVED: UI Consistency
- Trade Log header matches wi-filter-bar style
- ⚙ Sections dropdown has ✕ Close button
- Custom levels in journal session review cards

### BUG FIXES
1. testBMBridge crash — null check on status element
2. setAnPeriod/setAnInstr deselects fee toggle — added exclusion guard
3. clearPM() missing settle and customPMLevels
4. Custom level keys used array index — now uses name-based keys
5. Custom level null price crash — explicit null guard
6. getMTFilteredTrades fell back to unfiltered data — chains both filters
7. What-If Lab fees independent from global — three sync fixes
8. savePreflight wiped completion state on every keystroke

---

## v2.0 — What-If Lab + AI Coach (March 2026)

### NEW: 🔬 What-If Lab — Performance Simulator
10 simulation panels with Edge Optimizer, presets, fee toggle, period/instrument filters.

### NEW: 🧠 AI Trade Coach
Free mode (copy prompt) + API mode (Anthropic key). Three analysis types.

### NEW: BMBridge Dual Feeds
Separate level import + live price URLs. Auto-test on Settings open.

### NEW: RTH Stale Data Protection
Pre-RTH price tracking, configurable buffer, freshness detection.

### NEW: Visual UI Enhancements
7-step stepper, next-step prompts, nav badges, session strip, smart defaults, proximity gradient.

### NEW: Visual Charts, Collapsible Analytics, Global Fee Toggle
6 SVG charts. Reorderable sections. One fee button syncs everywhere.

### NEW: Missed Trades Enhancements, CSV Analytics Export
Period filter, top 3 costliest reasons, computed stats export.

### BUG FIXES (12 fixes)
FS+Error overwrite, fee 2x, per-instrument risk, slider drag, stat coloring, and more.

---

## v1.1 — Foundation (March 2026)

Pre-market levels, preflight checklist, open context flowcharts, live price feed, trade log with scale-outs, 12 errors, 10 emotions, process ratings, triggers, missed trades, journal, analytics (15+ sections), custom setups, instrument presets, export/import.
