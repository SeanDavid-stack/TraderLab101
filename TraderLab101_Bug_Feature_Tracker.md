# TraderLab 101 — Bug & Feature Tracker

*Current: v2.1.1  |  Next Build: v2.2  |  Updated: 27 Mar 2026*

---

## Legend

| 🐛 BUG | ✨ FEATURE | 🎨 POLISH | ⚡ PERF | 📦 BUILD | 🔒 DATA |
|---------|-----------|-----------|---------|----------|---------|
| Something broken | New capability | UX / visual | Speed / efficiency | Packaging / deploy | Schema / migration |

| OPEN | IN PROGRESS | PARKED | DONE | HIGH / MED / LOW |
|------|-------------|--------|------|------------------|
| Not started | Being worked on | Won't fix / deferred | Resolved | Priority levels |

---

## 🐛 Known Bugs — Carried Forward

| ID | Type | Description | Priority | Status | Notes | Added |
|----|------|-------------|----------|--------|-------|-------|
| B-K1 | 🐛 BUG | `var` declarations after init IIFE cause hoisting as `undefined` — recurring pattern | **HIGH** | **PARKED** | Not a single bug — it's an architecture constraint. All declarations must be inside or before the IIFE. Has affected: `selectedSetups`, `currentProc`, `hitLog`, `INSTRUMENT_PRESETS`, `SETUP_LABELS` | Mar 2026 |
| B-K2 | 🐛 BUG | Raw `JSON.parse` on localStorage crashes app silently on corrupt data | **HIGH** | **PARKED** | Must use `_safeParse(key, fallback)` helper everywhere. `hitLog` specifically needs IIFE-wrapped init. `tl_hits` is the most common offender. | Mar 2026 |
| B-K3 | 🐛 BUG | `panel.scrollTop = 0` targets wrong element — `.content` is the scrollable container | **LOW** | **PARKED** | Cosmetic — scroll doesn't reset on tab switch if applied to `.panel` instead of `.content` | Mar 2026 |
| B-K4 | 🐛 BUG | `</div><!-- /content -->` placement — closing tag too early leaves panels outside scroll container | **MED** | **PARKED** | Must enclose all panels. Easy to break when adding new panels. | Mar 2026 |

---

## 🐛 New Bugs — Queued for v2.2

| ID | Type | Description | Priority | Status | Notes | Added |
|----|------|-------------|----------|--------|-------|-------|
| B-030 | 🐛 BUG | PM time parsing broken — `parseInt('1:30 PM'.split(':')[0])` returns `1`, not `13`. All PM trades bucket into 09:30–10:00 slot in CSV export, AI Coach time analysis, What-If cutoff hour filter. At least 6 locations. | **MED** | **OPEN** | Pre-existing across multiple versions. Need a shared `parseTradeHour(timeStr)` helper that handles AM/PM conversion. Affects: `exportAnalyticsCSV`, `buildAIPrompt`, `wiCalcStats`, What-If cutoff hour, ETH filter. | 27 Mar 2026 |
| B-031 | | | | **OPEN** | | |
| B-032 | | | | **OPEN** | | |

---

## ✨ Feature Requests — Queued for v2.2

| ID | Type | Description | Priority | Status | Notes | Added |
|----|------|-------------|----------|--------|-------|-------|
| F-033 | ✨ FEATURE | | **LOW** | **OPEN** | | |
| F-034 | ✨ FEATURE | | **LOW** | **OPEN** | | |
| F-035 | ✨ FEATURE | | **LOW** | **OPEN** | | |

---

## 🎨 Polish & UX Improvements

| ID | Type | Description | Priority | Status | Notes | Added |
|----|------|-------------|----------|--------|-------|-------|
| P-001 | 🎨 POLISH | | **MED** | **OPEN** | | |
| P-002 | 🎨 POLISH | | **LOW** | **OPEN** | | |

---

## ⚡ Performance

| ID | Type | Description | Priority | Status | Notes | Added |
|----|------|-------------|----------|--------|-------|-------|
| E-001 | ⚡ PERF | | **MED** | **OPEN** | | |
| E-002 | ⚡ PERF | | **LOW** | **OPEN** | | |

---

## 📦 Build & Packaging

| ID | Type | Description | Priority | Status | Notes | Added |
|----|------|-------------|----------|--------|-------|-------|
| K-001 | 📦 BUILD | | **MED** | **OPEN** | | |

---

## 🔒 Data & Schema

| ID | Type | Description | Priority | Status | Notes | Added |
|----|------|-------------|----------|--------|-------|-------|
| D-001 | 🔒 DATA | SACRED rule enforcement — every schema update must increment `SCHEMA_VERSION`, add migration in both `migrateLocalStorage()` and `migrateImport()`, only add fields, never delete/rename/overwrite | **HIGH** | **ONGOING** | Currently at Schema 4. | Mar 2026 |

---

## ✅ Completed — v2.1.1

| ID | Type | Description | Priority | Status | Notes | Added | Resolved |
|----|------|-------------|----------|--------|-------|-------|----------|
| B-030 | 🐛 BUG | AI Coach stale label variables — `WI_ERROR_LABELS`, `WI_EMO_LABELS`, `WI_TRIGGER_LABELS` not refreshed on AI Coach tab open. Custom labels showed raw IDs in prompts. | **MED** | **DONE** | Added same refresh line as What-If tab to `if(id==='aicoach')` block | 27 Mar 2026 | 27 Mar 2026 |
| B-031 | 🐛 BUG | CSV export used raw error/emotion IDs — `chased` instead of `Chased Entry`, `confident` instead of `😎 Confident` | **LOW** | **DONE** | Added `getAllLabels('errors')` and `getAllLabels('emotions')` lookups in `exportAnalyticsCSV()` | 27 Mar 2026 | 27 Mar 2026 |
| F-030 | ✨ FEATURE | Edit & Media Parity (Missed Trades) — Edit after entry with full form population, edit banner, cancel. Screenshot/media attachments with live previews, badge, thumbnails. | **MED** | **DONE** | Schema 4: adds `screenshots:[]` to missed trades. `editMissedTrade(id)` populates all fields. What-If Lab trade entry parked. | 27 Mar 2026 | 27 Mar 2026 |
| F-031 | ✨ FEATURE | Custom Labels & Defaults — All 4 chip categories (errors, emotions, missed reasons, triggers) now customizable. Hide defaults, add custom items. Settings UI card. All analytics/WI/AI Coach/CSV use dynamic lookups. | **MED** | **DONE** | `tl_custom_labels` localStorage key. `getActiveItems(cat)` for forms, `getAllLabels(cat)` for analytics. Export/import included. | 27 Mar 2026 | 27 Mar 2026 |
| F-032 | ✨ FEATURE | Media field — Screenshots renamed to Media. Image URLs render as thumbnails, video/other URLs render as 🎬 clickable links. Smart badge (📷 2 🎬 1). Schema field stays `screenshots` (SACRED). | **MED** | **DONE** | Shared `renderMediaItem()` + `renderMediaBadge()` + `isImageUrl()`. All 8 rendering locations converted. | 27 Mar 2026 | 27 Mar 2026 |
| F-031 | ✨ FEATURE | Custom Labels & Defaults — All 4 chip categories (execution errors, emotions, missed trade reasons, trigger types) customizable from Settings. Hide defaults you don't use, add custom labels. Hide-not-delete model: hidden items still appear in analytics for historical trades. Uniform 👁 toggle for both defaults and customs. | **MED** | **DONE** | `tl_custom_labels` localStorage key. `getActiveItems(cat)` for form chips, `getAllLabels(cat)` for analytics. 4 dynamic chip builders replace static HTML. All hardcoded label lookups in Analytics, What-If, and Missed Trades replaced with dynamic lookups. Export/import includes `customLabels`. | 27 Mar 2026 | 27 Mar 2026 |

---

## ✅ Completed — v2.1

| ID | Type | Description | Priority | Status | Notes | Added | Resolved |
|----|------|-------------|----------|--------|-------|-------|----------|
| B-020 | 🐛 BUG | `testBMBridge` crash when status element null — semicolon made second statement run unconditionally outside `if` block | **HIGH** | **DONE** | Wrapped in proper braces `if(status){ ... }` | Mar 2026 | Mar 2026 |
| B-021 | 🐛 BUG | `setAnPeriod` deselects fee toggle button — `querySelectorAll('.tl-sf-btn').forEach(remove active)` hit fee toggle too | **MED** | **DONE** | Added `if(b.id!=='anFeeToggle')` guard | Mar 2026 | Mar 2026 |
| B-022 | 🐛 BUG | `setAnInstr` same fee toggle deselect issue as B-021 | **MED** | **DONE** | Same fix — added exclusion guard | Mar 2026 | Mar 2026 |
| B-023 | 🐛 BUG | What-If Lab fees independent from global toggle — `wiState.feesEnabled` hardcoded to `false`, never synced | **MED** | **DONE** | Three fixes: default reads localStorage, tab open syncs, toggle writes back | Mar 2026 | Mar 2026 |
| B-024 | 🐛 BUG | `clearPM()` missing `settle` and `customPMLevels` fields | **MED** | **DONE** | Added `settle` to field list, `customPMLevels=[]` | Mar 2026 | Mar 2026 |
| B-025 | 🐛 BUG | Custom level keys used array index — `custom_0`, `custom_1` shifted on remove, breaking hitLog lookups | **HIGH** | **DONE** | Changed to `custom_` + level name for stable identifiers | Mar 2026 | Mar 2026 |
| B-026 | 🐛 BUG | Custom level null price crash — `isNaN(null)` / `parseFloat(null)` behavior varies by browser | **HIGH** | **DONE** | Added explicit `cl.price == null` guard | Mar 2026 | Mar 2026 |
| B-027 | 🐛 BUG | `getMTFilteredTrades` fell back to unfiltered data — period filter used `missedTrades` instead of instrument-filtered `trades` | **MED** | **DONE** | Changed to `return trades.filter(...)` | Mar 2026 | Mar 2026 |
| B-028 | 🐛 BUG | `savePreflight()` wiped completion state — created fresh object on every keystroke, losing `_completed` | **HIGH** | **DONE** | Reads existing state first, preserves flags | Mar 2026 | Mar 2026 |
| B-029 | 🐛 BUG | Goals tracker affected by fee toggle — used `getCommissionForTrades()` which respects toggle | **MED** | **DONE** | Inline fee calculation, immune to toggle state | Mar 2026 | Mar 2026 |
| F-020 | ✨ FEATURE | Custom Levels — add any price level, fully integrated into tracker, live detection, tag log, reconciliation, manual tag/untag, journal snapshots, CSV import auto-adds | **HIGH** | **DONE** | Purple ★ pills in review. Keys use `custom_` + name. `_cl:` field mappings for BMBridge. | Mar 2026 | Mar 2026 |
| F-021 | ✨ FEATURE | Settlement Field — standard field in Prior Day Levels, mappable via CSV (`Settle`, `SETL`, `Y/SETT`), fully tracked | **MED** | **DONE** | Included in session snapshots and journal review | Mar 2026 | Mar 2026 |
| F-022 | ✨ FEATURE | Trade Screenshots — multiple chart images per trade (URL-based), live thumbnails, purple 📷 badge, clickable in detail and journal review | **MED** | **DONE** | Migration adds `t.screenshots=[]` to all existing trades | Mar 2026 | Mar 2026 |
| F-023 | ✨ FEATURE | Preflight Editing — ↺ Reset & Redo button, 📋 Preflight Answers in Journal form, bidirectional sync, edits preserved on save | **MED** | **DONE** | Edits in Journal sync back to Preflight tab + storage | Mar 2026 | Mar 2026 |
| F-024 | ✨ FEATURE | Data Migration System — `migrateLocalStorage()` on load, `migrateImport()` on backup import, SACRED rule, idempotent migrations | **HIGH** | **DONE** | SCHEMA_VERSION bumped to 3 | Mar 2026 | Mar 2026 |
| F-025 | ✨ FEATURE | Missed Trades Instrument Filter — auto-appears with 2+ instruments, period + instrument filters chain correctly | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| P-020 | 🎨 POLISH | Fee Toggle Sync — all four pages share one state, goals tracker immune | **MED** | **DONE** | Single source: `anShowFees` + `localStorage('tl_an_fees')` | Mar 2026 | Mar 2026 |
| P-021 | 🎨 POLISH | Trade Log header matches `wi-filter-bar` style | **LOW** | **DONE** | Standardized filter bar CSS across all pages | Mar 2026 | Mar 2026 |
| P-022 | 🎨 POLISH | ⚙ Sections dropdown has ✕ Close button | **LOW** | **DONE** | | Mar 2026 | Mar 2026 |
| P-023 | 🎨 POLISH | Custom levels in journal session review cards | **LOW** | **DONE** | Displayed as purple ★ pills | Mar 2026 | Mar 2026 |

---

## ✅ Completed — v2.0

| ID | Type | Description | Priority | Status | Notes | Added | Resolved |
|----|------|-------------|----------|--------|-------|-------|----------|
| B-001 | 🐛 BUG | FS + Error reduction overwrite — error loss reduction read from original trade, not post-FS-modified | **MED** | **DONE** | Now reads from modified trade | Mar 2026 | Mar 2026 |
| B-002 | 🐛 BUG | Error loss reduction didn't sync pts/R — only cut dollars | **MED** | **DONE** | Recalculates using per-trade instrument tick value | Mar 2026 | Mar 2026 |
| B-003 | 🐛 BUG | Winner R boost didn't sync pts — scaled dollars but not points/R | **MED** | **DONE** | Scales all three uniformly | Mar 2026 | Mar 2026 |
| B-004 | 🐛 BUG | Fee 2× discrepancy — commission already round-trip, got doubled | **HIGH** | **DONE** | Removed erroneous ×2, rewrote `wiCalcStats` | Mar 2026 | Mar 2026 |
| B-005 | 🐛 BUG | `avgRiskDollars` used global instrument — mixed ES/MES calculated wrong | **MED** | **DONE** | Per-trade instrument tick value lookup | Mar 2026 | Mar 2026 |
| B-006 | 🐛 BUG | Missed trade defaults hardcoded — used 3 rPts and 1 contract instead of actual averages | **MED** | **DONE** | Reads from trade data | Mar 2026 | Mar 2026 |
| B-007 | 🐛 BUG | Daily loss limit ignored fees — accumulated gross P&L, not net | **MED** | **DONE** | Subtracts per-trade commission | Mar 2026 | Mar 2026 |
| B-008 | 🐛 BUG | Optimizer Apply All crash — nullified results then tried to read them | **HIGH** | **DONE** | Saves recommendations before reset | Mar 2026 | Mar 2026 |
| B-009 | 🐛 BUG | `apply` property name conflict — collided with `Function.prototype.apply` | **HIGH** | **DONE** | Renamed to `applyFn` | Mar 2026 | Mar 2026 |
| B-010 | 🐛 BUG | Slider drag killed by DOM rebuild — `oninput` triggered full re-render, destroying the slider | **MED** | **DONE** | `oninput` → display update only, `onchange` → full render | Mar 2026 | Mar 2026 |
| B-011 | 🐛 BUG | Stat card coloring by direction of change — positive delta colored green even when value was negative | **LOW** | **DONE** | Colored by what the value IS (positive=green) | Mar 2026 | Mar 2026 |
| B-012 | 🐛 BUG | Format types wrong on some cards — trades showed $, drawdown showed ± | **LOW** | **DONE** | Trades=count, Avg=abs, P&L=signed dollar | Mar 2026 | Mar 2026 |
| F-001 | ✨ FEATURE | What-If Lab — Performance Simulator with 10 simulation panels, Edge Optimizer, presets, fee toggle, period/instrument filters | **HIGH** | **DONE** | 13 stat cards, sticky layout, collapsible panels | Mar 2026 | Mar 2026 |
| F-002 | ✨ FEATURE | AI Trade Coach — Mode 1 (clipboard prompt for any AI), Mode 2 (Anthropic API key, ~$0.03/call), three analysis types: Full Review, Error Audit, Setup Analysis | **HIGH** | **DONE** | | Mar 2026 | Mar 2026 |
| F-003 | ✨ FEATURE | BMBridge Dual Feeds — separate level import + live price URLs, auto-test on Settings open | **MED** | **DONE** | `tl_bmurl` for levels, `tl_bmurl_price` for live price | Mar 2026 | Mar 2026 |
| F-004 | ✨ FEATURE | RTH Stale Data Protection — pre-RTH price tracking, configurable buffer (default 3 min), freshness flag, fallback grace period | **MED** | **DONE** | Activates only when price moves from pre-market value | Mar 2026 | Mar 2026 |
| F-005 | ✨ FEATURE | Visual UI Enhancements — 7-step stepper, next-step prompts, nav badges, session strip, smart defaults, proximity gradient | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| F-006 | ✨ FEATURE | Visual Charts — 6 tabbed SVG charts: Daily P&L, Win Rate Trend, R Distribution, By Setup, By Process, By Time | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| F-007 | ✨ FEATURE | Collapsible Analytics — 15+ reorderable sections with ▲▼ buttons, gold flash animation, sticky headers, persistent state | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| F-008 | ✨ FEATURE | Global Fee Toggle — `anShowFees` stored as `tl_an_fees`, affects all P&L calculations including missed trades | **MED** | **DONE** | Commission = contracts × rate. Goals tracker immune. | Mar 2026 | Mar 2026 |
| F-009 | ✨ FEATURE | Missed Trades Enhancements — period filter, top 3 costliest reasons | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| F-010 | ✨ FEATURE | CSV Analytics Export — 30+ computed metrics, 10 breakdown tables, respects filters and fee toggle | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| F-011 | ✨ FEATURE | IRT Auto-Detection — CSV parser detects IRT format via header/data pattern matching, pre-mapped labels include pHI/pLO/pVAH/pVAL/pVPOC/CLOSE/OPEN/ONVPOC and Y-prefix variants | **MED** | **DONE** | Migration adds new IRT labels without losing existing customizations | Mar 2026 | Mar 2026 |

---

## ✅ Completed — v1.1 (Foundation)

| ID | Type | Description | Priority | Status | Notes | Added | Resolved |
|----|------|-------------|----------|--------|-------|-------|----------|
| F-F01 | ✨ FEATURE | Pre-market levels — pHigh, pLow, pClose, pVPOC, pVAH, pVAL, ONH, ONL, ONVPOC, Today's Open, IB High/Low | **HIGH** | **DONE** | Full level tracker with live detection and tag log | Mar 2026 | Mar 2026 |
| F-F02 | ✨ FEATURE | Preflight checklist — structured pre-session preparation workflow | **HIGH** | **DONE** | | Mar 2026 | Mar 2026 |
| F-F03 | ✨ FEATURE | Open context flowcharts — visual decision trees for each open type (HOR, LOR, HIR, LIR, IR-IV) | **HIGH** | **DONE** | Based on Tom B. / Traders Lab methodology | Mar 2026 | Mar 2026 |
| F-F04 | ✨ FEATURE | Live price feed — BMBridge connection with Yahoo Finance fallback (~15 min delay) | **HIGH** | **DONE** | ~5s poll interval, green banner when connected | Mar 2026 | Mar 2026 |
| F-F05 | ✨ FEATURE | Trade log — save, edit, delete with scale-out support, 12 execution errors, 10 emotions, process ratings (A/B/C/F), triggers | **HIGH** | **DONE** | | Mar 2026 | Mar 2026 |
| F-F06 | ✨ FEATURE | Missed trades — log trades you should have taken with reason tracking | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| F-F07 | ✨ FEATURE | Journal — session snapshots with levels, fuel, bias log, hits, preflight answers | **HIGH** | **DONE** | | Mar 2026 | Mar 2026 |
| F-F08 | ✨ FEATURE | Analytics dashboard — 15+ sections with overview metrics | **HIGH** | **DONE** | | Mar 2026 | Mar 2026 |
| F-F09 | ✨ FEATURE | Custom setups — user-defined trade setup labels | **MED** | **DONE** | | Mar 2026 | Mar 2026 |
| F-F10 | ✨ FEATURE | Instrument presets — MES, ES, MNQ, NQ with tick size, tick value, commission | **MED** | **DONE** | Custom instruments supported | Mar 2026 | Mar 2026 |
| F-F11 | ✨ FEATURE | Export/Import — JSON backup with schema versioning | **HIGH** | **DONE** | `safeSave()` wrapper on all localStorage writes | Mar 2026 | Mar 2026 |
| F-F12 | ✨ FEATURE | Storage Health — usage bar, per-key breakdown, runway estimate, archive system | **MED** | **DONE** | Settings card | Mar 2026 | Mar 2026 |

---

## Known Patterns to Avoid

### Pattern 1: `var` hoisting after IIFE
**What happens:** `var x = value` declared after the init IIFE gets hoisted as `undefined` during IIFE execution.
**Fix:** Declare all variables INSIDE or BEFORE the IIFE.
**Affected historically:** `selectedSetups`, `currentProc`, `hitLog`, `INSTRUMENT_PRESETS`, `SETUP_LABELS`

### Pattern 2: Raw JSON.parse on localStorage
**What happens:** Corrupt data in any key crashes the entire app silently.
**Fix:** Always use `_safeParse(key, fallback)` helper. `hitLog` specifically needs IIFE-wrapped init.

### Pattern 3: querySelectorAll('.tl-sf-btn') removing all active
**What happens:** Period/instrument button click strips `active` from the fee toggle button.
**Fix:** Always exclude fee toggle IDs: `if(b.id!=='anFeeToggle' && b.id!=='mtFeeToggle')`

### Pattern 4: Creating fresh objects instead of reading existing state
**What happens:** `var obj = { newStuff }` wipes fields that existed in the stored version.
**Fix:** Read with `JSON.parse(localStorage.getItem(key)||'{}')` first, then merge/add.

### Pattern 5: Division by zero in stats
**What happens:** `wins/n*100` crashes or returns NaN when n=0.
**Fix:** Every render function must guard `if(!n)` with early return.

### Pattern 6: Array index as object key
**What happens:** `custom_0`, `fuel_0` etc. shift when items are added/removed, breaking hitLog lookups.
**Fix:** Use stable identifiers: `custom_` + name, or timestamp-based IDs.

### Pattern 7: `const` not hoisted like `function`
**What happens:** Calling a function that references a `const` before the `const` is declared causes ReferenceError.
**Fix:** Declare `const` values BEFORE any code that calls functions referencing them.

### Pattern 8: `<details>` stays collapsed in edit mode
**What happens:** Form fields inside `<details>` (screenshots, errors, notes) are populated correctly by edit functions, but the collapsible stays closed so the user can't see or interact with the content.
**Fix:** Give the `<details>` element an ID, set `.open=true` in the edit function, and `removeAttribute('open')` in the clear function.

### Pattern 9: Fragile chip matching via `querySelectorAll` + text/attribute parsing
**What happens:** Edit functions try to restore chip selection state by parsing `onclick` attributes or matching `textContent`. Breaks when chips are dynamically rendered.
**Fix:** Set the selection state array first, then call the chip builder function. The builder reads the state and applies `.sel` class automatically.

### Pattern 10: AM/PM time not converted to 24-hour for math
**What happens:** `parseInt('1:30 PM'.split(':')[0])` returns `1`, not `13`. All PM trades get bucketed/filtered as early-morning times.
**Fix:** Use a shared helper that extracts hour and adds 12 for PM: `var h=parseInt(parts[0]); if(/PM/i.test(time)&&h<12) h+=12; if(/AM/i.test(time)&&h===12) h=0;`

---

## Regression Test Checklist

### Data Safety
- [ ] App loads without console errors
- [ ] Existing trades/sessions preserved after HTML file swap
- [ ] Export → Import cycle preserves all data
- [ ] v1.x backup imports successfully into v2.1
- [ ] v2.0 backup imports successfully into v2.1
- [ ] New day rollover clears levels but keeps trades/sessions

### Core Features
- [ ] Preflight: complete, reset, edit, all persist correctly
- [ ] Levels: standard + settlement + custom all save and load
- [ ] CSV import: mapped fields fill, unmapped auto-add as custom
- [ ] Live price: feed connects, levels tagged, proximity gradient works
- [ ] Trade log: save, edit, delete, screenshots attach
- [ ] Missed trades: save, period filter, instrument filter
- [ ] Missed trades: edit populates all fields (scales, reasons, screenshots, time)
- [ ] Missed trades: edit saves in-place, doesn't duplicate
- [ ] Missed trades: cancel edit resets form and banner
- [ ] Missed trades: screenshots textarea, previews, 📷 badge in list
- [ ] Custom labels: hide default → disappears from form, still in analytics
- [ ] Custom labels: add custom → appears in form chips and analytics
- [ ] Custom labels: hide custom → dimmed in settings, gone from form, still in analytics
- [ ] Custom labels: unhide → reappears in form immediately
- [ ] Custom labels: export includes customLabels, import restores them
- [ ] Custom labels: What-If Lab picks up label changes on tab open
- [ ] Journal: save session, edit past session, preflight editable

### Math & Analytics
- [ ] R-multiple: `totalPnlPts / (rPts × contracts)` — verified
- [ ] Fee toggle: ON shows net, OFF shows gross, goals tracker immune
- [ ] Equity curve: both lines render correctly
- [ ] Export CSV: computed stats match dashboard display
- [ ] What-If Lab: fees synced with global toggle

### Edge Cases
- [ ] Zero trades — all pages show placeholder, no div/0
- [ ] Custom level with no price — skipped by tracker, gold border shown
- [ ] Mid-session open — stale data protection accepts immediately
- [ ] App restart — levelHitState rebuilt from hitLog
- [ ] Multiple instruments — all filters chain correctly

### Custom Labels (v2.1.1)
- [ ] Hide a default error — disappears from trade form chips, still shows in analytics
- [ ] Add a custom emotion — appears in trade form, tag a trade, verify in analytics
- [ ] Hide a custom item — dimmed in Settings, gone from forms, label resolves in analytics
- [ ] Unhide an item — reappears in forms immediately
- [ ] Export → Import preserves customLabels (hidden + added)
- [ ] Fresh load with no tl_custom_labels key — all defaults show, no errors
- [ ] What-If Lab shows custom errors/emotions/triggers in filter chips
- [ ] AI Coach prompt includes custom label display names, not raw IDs
- [ ] CSV export uses display names for errors and emotions

### Media (v2.1.1)
- [ ] Paste image URL — thumbnail preview in form, thumbnail in list/detail
- [ ] Paste video URL — 🎬 link preview in form, 🎬 link in list/detail
- [ ] Mixed URLs — badge shows "📷 2 🎬 1" style counts
- [ ] imgur URL without extension — detected as image
- [ ] Edit trade with media — details section opens, URLs populated

---

## Version Summary

| Version | Bugs Fixed | Features Added | Schema |
|---------|-----------|----------------|--------|
| v1.1 | — | 12 (foundation) | 2 |
| v2.0 | 12 | 11 | 2 |
| v2.1 | 10 | 6 + 4 polish | 3 |
| v2.1.1 | 2 | 3 | 4 |
| **Total** | **24** | **32 + 4 polish** | **4** |

---

*TraderLab 101 Bug & Feature Tracker  •  v1.1 → v2.1.1 → v2.2  •  Private Developer Use*
