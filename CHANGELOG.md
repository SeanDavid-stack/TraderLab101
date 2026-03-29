# TraderLab 101 — Changelog

## v2.1.4 — Direction Fix, Stop Validation, Local Screenshots (March 2026)

### NEW: Direction Validation
- Changing direction dropdown now triggers immediate recalculation of R, P&L, and result
- Live gold ⚠ warning when stop is on wrong side for direction (Long with stop above entry, Short with stop below entry)
- Hard validation blocks saving when stop is on wrong side — prevents data entry errors

### NEW: Local Screenshot Support
- Paste Windows file paths directly — quotes, backslashes, `#` in filenames, and spaces are all handled automatically
- `sanitizeMediaUrl()` helper: strips outer quotes, converts `\` to `/`, encodes `#` `%` `?` and spaces, prepends `file:///`
- `parseMediaUrls()` replaces 6 duplicate split/trim/filter patterns with one sanitizing helper
- `isImageUrl()` updated to detect extensions through encoded characters
- Local file errors show `📁 Local file — open in browser` instead of `⚠ Cannot load`
- Placeholder text updated on all 3 screenshot fields to show local path example
- Note: local file display depends on browser — works best when TraderLab is opened as a local HTML file

### BUG FIXES
1. **Direction case mismatch** — Trade Log saved `'long'` (lowercase), Missed Trades saved `'Long'` (capitalized). Analytics "By Direction" rows showed 0 trades for all trade log entries. Standardized to lowercase everywhere with `.toLowerCase()` for legacy data safety.
2. **Direction dropdown missing onchange** — changing direction after entering prices didn't recalculate R achieved, P&L, or result. Added `onchange` handlers to both Trade Log and Missed Trades forms.
3. **Missed trade log CSS class** — always applied "short" styling regardless of actual direction. Fixed with lowercase normalization.
4. **Edit info bar display** — direction showed raw lowercase in edit mode info bars. Now capitalizes for display.
5. **Edit-load direction normalization** — simplified trade log and missed trade edit-load to handle both legacy capitalized and new lowercase values.

---

## v2.1.2 — Unified Setups, Performance Thresholds (March 2026)

Schema version: 5 (auto-migrates from v4)

### NEW: Unified Setup Management
Setups are now fully customizable — hide defaults, add your own, all from Settings. Same eye-toggle pattern as errors, emotions, reasons, and triggers. Affects all surfaces: Trade Log, Missed Trades, Journal, Analytics, What-If Lab, AI Coach. Existing custom setups migrate automatically.

### NEW: Performance Thresholds (Settings → Goals)
Define what green, gold, and red mean for your strategy — stat card colors are no longer hardcoded. Six configurable metrics: Win Rate, Profit Factor, Risk Neutral Rate, Full Stop Rate, A-Process Win Rate, Break Even Rate. Colors apply everywhere. Per-metric reset and "Reset All to Defaults" buttons.

### NEW: What-If Lab Setup Filter on Missed Trades
When "Include all missed trades" is ON, filter by setup in addition to reason. Persists in saved presets.

### NEW: Settings Page Overhaul
- Sticky jump-link navigation — INSTRUMENT · LABELS · GOALS · JOURNAL · FEEDS · AI COACH · DATA
- Each label category gets its own card, ordered by trade lifecycle
- Interactive "Appears in:" descriptions with clickable tab links
- "↺ Reset" button on each label card — unhides defaults, removes custom items
- Whole chip clickable (not just the eye icon)

### NEW: Trade Log & Missed Trades Consistent Filtering
Trade Log and Missed Trades now have 2M period button and custom date range (From/To + Apply), matching Analytics. All three pages have identical period filtering.

### BUG FIXES
1. **Hidden setup preserved on edit** — editing a trade with a hidden setup no longer silently wipes the setup field.
2. **CSV export break-even count** — was comparing `'BE'` instead of `'Break Even'`.
3. **Trade Log stats fee toggle** — Total P&L and Expectancy now show net values when fees are ON.
4. **AM/PM time parsing** — created shared `parseTradeHour()` helper, fixed 9 locations.
5. **What-If Lab missed reason filter** — old presets with display-string keys auto-migrate.
6. **What-If Lab scroll position** — no longer jumps to top on slider/chip interaction.
7. **Duplicate label prevention** — case-insensitive blocking with toast message.
8. **Setup required on Missed Trades** — now validated as required.
9. **Hide warning with trade count** — confirm dialog when hiding a label used by existing trades.

### ARCHITECTURAL
- `_safeSave()` wrapper on all 85+ `localStorage.setItem()` calls — quota error shows toast
- Custom setup IDs use timestamps instead of slugs
- Gold glow on forms during edit mode
- Sticky headers gap fix on Analytics and Missed Trades

---

## v2.1.1 — Label Fixes (March 2026)

### BUG FIXES
1. AI Coach stale label variables — custom labels showed raw IDs in AI prompts. Added `getAllLabels()` refresh on AI Coach tab open.
2. CSV export raw IDs for errors/emotions — added label lookups before row generation.

---

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
