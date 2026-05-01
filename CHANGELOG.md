# TraderLab 101 — Changelog

## v2.3.11 — Commission Required For Custom Instruments (April 2026)

Small UX safeguard following on from v2.3.10's multi-symbol work.

### NEW: Custom Instruments Require A Commission
TraderLab ships sensible default commissions for the four built-in presets (MES, ES,
MNQ, NQ). For any **custom symbol** (RTY, YM, CL, BTC, etc.), there's no sensible
default — your broker rate is yours alone. Previously, saving a custom symbol with
a blank commission silently stored `commission: 0`, which would propagate $0 fees
through analytics, daily goals, and What-If math forever.

The fix:
- **Settings → Custom Symbol** now blocks the Save button and surfaces a clear toast
  if a non-preset symbol is saved with commission `<= 0` or empty:
  *"Commission required for custom symbol 'XYZ' — enter your broker RT cost."*
- The commission input border turns red and gets focus.
- Other validation errors (missing name, bad tick size, bad tick value) now also
  highlight their respective fields in red — consistent feedback.

### NEW: UI Hints
- Custom Symbol commission label: *"RT — required for custom"* (gold)
- Commission placeholder: *"your broker RT $"*
- Inline note under the Custom Symbol row:
  *"ⓘ Presets (MES, ES, MNQ, NQ) auto-fill commission. Custom symbols require your
  actual RT cost so analytics and goals don't silently use $0 fees."*

### Backwards Data Compatibility
- The validation runs **only when the user clicks Save in Settings.** Existing custom
  instruments already in localStorage with `commission: 0` are not retroactively
  blocked — they continue to work via the existing fallback.
- JSON imports preserved as-is. No migration. No data loss.
- Presets remain exempt — saving "MES" with empty commission still works because
  the preset default fills in.

### Verified
- 6-case validation matrix: empty / negative / zero commission on custom blocks save;
  $1.25 commission on custom saves; preset MES with empty commission still saves;
  preset switches (MES/ES/MNQ/NQ) all work without invoking the validation path.
- Demo (old format, no new fields) still loads cleanly: 220 trades, 61 sessions,
  41 missed; all 15 panels render without errors.
- Old NQ trade fee fallback still produces correct $4.64 (2 × $2.32 NQ preset).
- New NQ trade saves with `commission: 2.32, tickValue: 5, tickSize: 0.25`.
- Round-trip export → wipe → import: 220 → 220 trades, first trade ID matches,
  zero JS console errors across the full test.

---

## v2.3.10 — Multi-Symbol Hardening + Multi-Symbol UX (April 2026)

A follow-on patch bundled with v2.3.9 that hardens the new symbol support against
custom instruments and gives multi-symbol traders a smoother experience.

### Why
v2.3.9 made the Yahoo Finance fallback follow the active instrument so users like
Mirza could trade NQ without the live feed silently pulling ES. While auditing
related paths, several downstream issues turned up that would break custom-instrument
trades (RTY, YM, CL, BTC, etc.) — and a separate UX gap for users who keep more
than one symbol in the same log.

### NEW: Per-Trade Tick Data Persisted
`saveTradeEntry` and `saveMissedTrade` now stamp the active **commission**, **tickValue**,
and **tickSize** onto each trade at save time. Without this, custom instruments fell
through to MES defaults in any analytics or What-If recalculation that recomputed
risk after the user switched their active instrument away from the symbol the trade
was made on. Old trades without these fields use the existing preset / active-instrument
fallback, so the change is purely additive — **no migration needed, no data loss**.

### NEW: ensureInstrumentOption Helper
When you edit a trade whose instrument isn't currently active (e.g. you traded YM in
the morning, switched to ES in the afternoon, opened to edit the YM trade), the
trade form's instrument dropdown now auto-injects YM as an option so the edit doesn't
silently fall back to whatever was selected. Same fix applied to the Missed Trades
form. The new option is tagged with class `historical-instr` so it stays distinct
from active and preset options.

### NEW: Yahoo Ticker Input Sanitization
The new "Yahoo Symbol" override field strips whitespace, uppercases, and rejects
characters Yahoo doesn't use (`A–Z 0–9 . - = ^` only). A toast surfaces the cleaned
value if it changed.

### NEW: Multi-Symbol UX (Trade Log)
When your log contains 2+ distinct instruments, the Trade Log panel now shows:
1. A soft **info banner** explaining the situation and pointing at the existing
   Analytics → Instrument filter (which scopes the entire dashboard to one symbol
   at a time). Dismissible — and reappears only if your distinct-instrument count
   later grows.
2. A **per-symbol summary chip row** above the trade list — `ES 80 · 55% · +$3,400` etc.
   Click any chip to instantly filter the trade list to that symbol; click "All" to
   restore.

This deliberately does NOT introduce a "single-symbol mode" toggle. The Instrument
filter is already strictly more flexible than a binary mode (per-symbol or aggregate
or any subset), and adding a mode would double the testing surface and hide aggregate
analytics from users who sometimes want them.

### NEW: Backwards-Compat Round-Trip Verified
The smoke test for this release imports the old-format demo dataset (220 trades / 61
sessions / 41 missed — none of which have the new commission/tick/yahoo fields),
walks every panel, exports the data, wipes localStorage, re-imports from the export,
and confirms identical state on both sides. Zero data loss across the round-trip,
zero JS console errors.

### Docs
USERGUIDE → INSTRUMENT and QUICKSTART → Step 2 now both call out the
"one log per symbol is simplest, but multi works" guidance with explicit pointers
to the Analytics Instrument filter for users who keep multiple symbols in one log.

### Backwards Data Compatibility
- All new fields (`t.commission`, `t.tickValue`, `t.tickSize`, `instrumentSettings.yahooTicker`,
  `tl_mixed_instr_dismissed_count`) are purely additive.
- Old trades without the new fields use the existing preset / active-instrument
  fallback; new trades use the persisted values.
- No localStorage key renamed or reshaped.

### Verified
- Demo (old format) loads cleanly: 220 trades, 61 sessions, 41 missed.
- All 15 panels render without errors.
- Old NQ trade (no `t.commission`) computes fee as $4.64 (2 × $2.32 NQ preset) — fallback works.
- New NQ trade saves with `commission: 2.32, tickValue: 5, tickSize: 0.25` — persistence works.
- Yahoo URLs follow active instrument across all three fetch paths.
- Edit-trade dropdown auto-injects historical custom symbol when active is different.
- Banner + summary chips render and dismiss correctly.
- Round-trip export → wipe → import preserves 100% of trades, sessions, missed.

---

## v2.3.9 — Live Price Feed Follows Active Instrument (April 2026)

Reported by Mirza in Discord: setting the instrument to NQ in Settings still pulled
ES data from the Yahoo fallback. Three Yahoo Finance fetch URLs were hardcoded to
`ES=F`. Now they follow the active instrument.

### FIX: Yahoo Fallback Uses Active Instrument's Ticker
- New `getYahooTicker()` helper resolves the right Yahoo symbol with this priority:
  1. `instrumentSettings.yahooTicker` (explicit override)
  2. `INSTRUMENT_PRESETS[name].yahooTicker` (built-in mapping)
  3. `name + '=F'` (sensible guess for any custom instrument)
  4. `ES=F` (final safe fallback)
- Built-in preset mappings: **MES → ES=F**, **ES → ES=F**, **MNQ → NQ=F**, **NQ → NQ=F**.
  Micros track their parent contract on Yahoo because Yahoo's micro feeds can be
  sparse / stale.
- All three Yahoo fetch helpers (direct, AllOrigins proxy, corsproxy.io) now use the
  resolved ticker.

### NEW: Yahoo Ticker Override In Settings
A new optional **Yahoo Symbol** field in **Settings → Instrument & Contract** lets
you point the live-price fallback at any Yahoo symbol — useful for custom
instruments outside the four presets (YM=F, RTY=F, CL=F, GC=F, etc.). Leave it blank
and TraderLab auto-picks based on your selected instrument. A live hint shows which
ticker will be fetched.

### NEW: Live Feed Re-Polls When Instrument Changes
Switching presets or saving a custom instrument now triggers an immediate `fetchPrice()`
call so the new ticker takes effect on the next render instead of waiting for the
next 5-second poll.

### NEW: Live-Price Status Label Shows Active Symbol
The "~15 min delay · Yahoo Finance" status text under the price now also surfaces
the symbol being fetched, e.g. "~15 min delay · Yahoo Finance · NQ=F", so it's
obvious which contract you're seeing.

### Backwards Data Compatibility
- `yahooTicker` on `instrumentSettings` is purely additive; absent = auto-pick.
- No localStorage key renamed or reshaped.
- All fixes from v2.3.6 / v2.3.7 / v2.3.8 carry forward.

### Verified
Smoke-tested in a headless preview: each preset resolves to the expected ticker,
custom-instrument names auto-derive (`YM` → `YM=F`), explicit overrides win, and
empty / corrupted state safely falls back to `ES=F`. All three Yahoo fetch paths
were verified to use the resolved ticker via fetch interception.

---

## v2.3.8 — Persist Commission Per Trade (April 2026)

Quick follow-up to v2.3.7 fixing one more bug from the same review.

### MEDIUM: Custom-Instrument Commissions Were Lost After Switching Active Instrument
For preset instruments (MES, ES, MNQ, NQ) commission lookup falls back to
`INSTRUMENT_PRESETS`, which is fine. But for **custom instruments** the fallback was
`(instrumentSettings.name === instrName ? instrumentSettings.commission : 0)` — so once
the user switched the active instrument away from a custom symbol, every previous trade
on that custom symbol fell through to **$0** in fee calculations (analytics, daily
goals, what-if).

**Fix:** the per-contract commission active at save time is now stamped onto each trade
(`t.commission`) and each missed trade. Six fee-calculation sites prefer `t.commission`
when present, then fall back to the preset/active-instrument lookup for backwards
compatibility with old data.

### Backwards Data Compatibility
- New `t.commission` field is purely additive. Existing trades without it continue to
  use the existing preset / active-instrument fallback.
- No localStorage key renamed or reshaped.
- All v2.3.7 fixes (UTC date, tab-state, imports, AI key, etc.) carry forward.

### Verified
Smoke-tested: a saved trade on a custom instrument with commission $7.77 retains that
value on the trade record even after the active instrument is switched to MES. Fee
calculations across goals tracker, analytics, equity curve, and what-if all read the
persisted value.

---

## v2.3.7 — Bug Sweep: Date/TZ, Tab-State, Imports, AI Key (April 2026)

A focused patch release fixing seven bugs surfaced by a static review. All fixes are
backwards-compatible with existing localStorage data.

### CRITICAL: Trade Dates Now Use ET, Not UTC
`fk()` previously used `d.toISOString().split('T')[0]`, which returned the **UTC** date.
Trades logged after roughly 8 PM Eastern were silently filed under the *next* calendar
day, splitting evening sessions across the wrong day in journal/analytics. Replaced with
`Intl.DateTimeFormat('en-CA', {timeZone:'America/New_York', ...})` so the trade-day
grouping matches the US futures session everywhere. DST is handled automatically.

> **Existing data:** old localStorage dates aren't rewritten — they were saved with the
> buggy UTC math. Most trades are unaffected (most users log mid-session). If you logged
> trades late in the evening before this release, those entries may show on the next
> calendar day in the journal; you can edit individual trades to correct the date.

### HIGH: Trade Log Form Survives Tab Switch
Same pattern as the v2.3.6 journal fix. `go('trades')` previously called
`clearTradeForm()` on every tab activation, wiping in-progress trade entries when users
tabbed away to check Settings, Live Price, Journal, etc. New `_tradesInitialized` guard
limits the clear+smartFill to the first visit; revisits preserve typed form state.
`saveTrade()` and `editTrade()` continue to manage their own form state explicitly.

### HIGH: AI Key Session-Only Storage Mode
The Anthropic API key was stored only in `localStorage` (plaintext, persistent). Added an
opt-in **Session-only storage** checkbox under Settings → AI Coach. When enabled, the
key lives in `sessionStorage` instead — cleared automatically when the browser closes.
The key automatically migrates between stores when you flip the toggle. Default behavior
is unchanged.

### MEDIUM: Defensive Direction/Bias Case
A handful of display paths used `t.dir==='long'` strict-equality, which silently fell
back to the wrong CSS class on legacy data with capitalized `'Long'`/`'Short'`. Added
`.toLowerCase()` defensive guards to: trade list rendering, journal review trade rows,
banner bias log, journal session-strip bias chip, and journal-review bias log. New data
already saves lowercase per v2.1.4 — this hardens the display side.

### MEDIUM: JSON Import Resilience
`migrateImport()` crashed on malformed JSON containing `null` trade entries
(`Cannot read properties of null (reading 'contracts')`). Now filters non-object entries
out of `tradeLog`, `missedTrades`, and `sessions` before normalization. Imported trades
also get missing `scales` / `errors` / `emotions` / `targets` / `screenshots` arrays
backfilled so subsequent renders never crash on hand-edited or partially-corrupted
backups.

### LOW: smartFillTradeForm Retries For Late Live Price
On first Trade Log visit, the form auto-fills the entry price from the live feed via a
50 ms timeout. If the BMBridge / Yahoo fetch hadn't completed yet (pre-market or slow
network), the entry was left blank. Now retries every 500 ms for up to 5 seconds (or
until the user navigates away), then quietly stops.

### LOW: hitLog Corruption Now Surfaces A Toast
If `tl_hits` localStorage was malformed (corrupted JSON), the app silently reset it to
empty on load. Now logs the error and shows a deferred warning toast: *"Hit log was
corrupted and has been reset."*

### Backwards Data Compatibility
- No localStorage key renamed or reshaped.
- `tl_ai_key_mode` (new) is purely additive — absent = old default behavior.
- `fk()` change does not rewrite existing dates; only new date assignments use ET.

### Verified
Each fix was smoke-tested against the demo dataset (220 trades, 61 sessions, 41 missed
trades). All 15 panels load without errors. The v2.3.6 journal fix continues to work.

---

## v2.3.6 — Journal State Fix, License Update (April 2026)

### BUG FIX: Journal No Longer Resets On Tab Switch
Tabbing away from the Journal (e.g. to Trade Log or Pre-Market) and back **no longer wipes the in-progress fields**. Reported by Anthony in Discord. Root cause: `go('journal')` always re-ran `loadJDate()`, which called `clearJForm()` and reloaded only saved data, blowing away any unsaved typing. Fix introduces `_journalLoadedKey` so the journal only re-initializes on first visit or when the date actually changes; all other date-change paths (`jNav`, `jToday`, `jGoToDate`, `cancelJEdit`, `saveSession`, date picker) keep their existing reload behavior.

### LICENSE: MIT → PolyForm Noncommercial 1.0.0
Switched from MIT (which permitted commercial reuse) to the lawyer-drafted, SPDX-recognized [PolyForm Noncommercial License 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0).

- ✅ Free to download, run, share unmodified copies, and modify for your own personal noncommercial use.
- ❌ Not free to sell, sublicense, or build any commercial product / paid course / paid plugin / paid SaaS / commercial AI training set from any portion of the source.
- ❌ Not free to remove or alter the embedded build identifiers (used to detect unauthorized copies).

The license carries a Required Notice that must travel with every copy. See `LICENSE` for full terms.

### DOCS
- **USERGUIDE.md fully rewritten** for v2.3.6 — now covers AI Coach, What-If Lab, Statistics by Target, Mean Reversion checklist, Structured Trades alignment / go-no-go, the redesigned Open Context flowchart, expanded Settings sections, and the full localStorage key map.
- **QUICKSTART.md added** — first-15-minutes guide with the daily workflow diagram, demo-data import path, and "habits that make TraderLab pay off" closing tips.
- **USERGUIDE.pdf and QUICKSTART.pdf** generated as clean white print-ready PDFs.
- HTML header comment + README license sections updated to reference PolyForm Noncommercial.

### COMMITMENT: Backwards Data Compatibility
Reaffirmed as a non-negotiable: every release must read existing localStorage data without loss. No localStorage key has been renamed or reshaped in this release. Demo data and any prior-version JSON backup remain importable.

---

## v2.3 — Setup Quality, Filters, Heatmap, Error Log (March 2026)

Schema version: 6 (auto-migrates from v5)

### NEW: Setup Quality vs Execution Rating
The old single Process Rating is now two separate ratings per trade. **Setup Quality** rates the trade idea itself (A/B/C/F). **Execution Rating** rates how you executed it (A/B/C/F). Both optional, both independent. New stat cards, analytics breakdowns, CSV export sections, and AI Coach analysis for each.

### NEW: Collapsible Filter Bars (All 3 Tabs)
Trade Log, Analytics, and Journal all have matching `▸ Filter Trades` collapsible panels with identical layout: SETUP chips, EXECUTION (A/B/C/F), SETUP QUALITY (All/A/B/C/F/Unrated), RESULT (All/Win/Loss/BE), DIRECTION (All/Long/Short). All with ✕ Clear Filters.

### NEW: Color-Coded Filter Chips
Active chips change color by meaning: A = green, B = cyan, C = gold, F = red, Win = green, Loss = red, Long = green, Short = red. Instant visual feedback.

### NEW: Trade Count Badges
Every filter chip shows its count: `IBC (12)`, `A (59)`, `Loss (4)`. Volume at a glance.

### NEW: Equity Curve Per Filter
Filter to "IBC only" or "A execution only" in Analytics and the equity curve re-renders for that filtered set.

### NEW: Session Calendar Heatmap (Journal)
Collapsible `▸ Session Calendar` with green/red cells, daily P&L, click any day to jump to that session. Month navigation arrows, gold border on current date.

### NEW: Journal Trade Review with Session Context
Filtered trades grouped by session date showing open type, bias, process rating, key levels, and session notes.

### NEW: Bias Accuracy Tracker (Analytics)
"Bias Accuracy — Are You Reading the Market Right?" Overall accuracy %, breakdown by LONG vs SHORT bias, win rate WITH vs AGAINST bias, net Bias Edge.

### NEW: P&L by Setup Quality + Top 3 Costliest (Analytics)
Setup Quality breakdown (A/B/C/F/Unrated) in Trade Efficiency. Top 3 costliest trades by dollar loss. Top 3 costliest error types.

### NEW: Error Log System
Built-in error logging captures validation blocks, save failures, import errors, and uncaught JS crashes. Viewable in Settings → Error Log with color-coded badges, timestamps, and details. Export as .txt for bug reports. Capped at 200 entries.

### IMPROVED: Direction Validation
Gold ⚠ warning + hard block when stop is on wrong side. Direction change recalculates immediately.

### IMPROVED: Local Screenshot Support
Paste Windows file paths directly. Quotes, `#` in filenames, and spaces handled automatically.

### IMPROVED: Import Error Messages
Import failures now show the actual error message instead of generic "invalid file."

### IMPROVED: Journal Dropdown Resilience
`applyJournalDropdowns()` now falls back to defaults when properties are missing, preventing crashes on import of partial data.

### UI POLISH
- Native disclosure triangles hidden (no double arrows)
- Dual-panel analytics row arrows repositioned to top-right
- Stats by Setup nested inside Overview
- Heatmap cells 38px with 10px P&L text
- Orphaned CSS removed

### BUG FIXES
1. **B-040** Best Trade card — `+$-10` green when all losers → fixed display logic
2. **B-041** CSV direction — raw lowercase in export → capitalized for display
3. **B-043** Goals dropdown — "Only perfect process" → "Only perfect execution"
4. **B-044** Visual chart tab — "By Process" → "By Execution"
5. **B-045** Analytics mini-breakdown — "A-Process" → "A-Execution"
6. **B-046** Filter bar labels — missing EXECUTION label → added with data-filter attrs
7. **B-047** Filter button logic — fragile child-index counting → data-filter attributes
8. **B-048** What-If Lab — "Minimum Process Rating" → "Minimum Execution Rating"
9. **B-049** AI Coach Full Review — "Process quality" → "Execution quality"
10. **B-050** AI Coach Error Audit — "Process rating impact" → "Execution rating impact"
11. **B-051** clearJFilters — showed both form AND review → always returns to form
12. **B-052** Journal heatmap — click day with trades but no session → nothing → now navigates via `jGoToDate()`
13. **B-053** clearTLFilters — `===All` didn't match `All (220)` → `startsWith('All')`
14. **B-054** clearJFilters — same textContent match issue → `startsWith('All')`

---

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
