# TraderLab 101 — Error & Bug Log

**Complete record of every bug found, fixed, and known pattern to avoid.**

---

## v2.1.1 Bugs Fixed

| # | Bug | Root Cause | Fix | Severity |
|---|-----|-----------|-----|----------|
| 1 | AI Coach stale label variables — custom labels showed raw IDs in AI prompts | `WI_ERROR_LABELS`, `WI_EMO_LABELS`, `WI_TRIGGER_LABELS` only refreshed on What-If tab open, not AI Coach tab | Added same refresh (`getAllLabels()`) to `if(id==='aicoach')` block | 🟡 Data |
| 2 | CSV export used raw IDs for errors/emotions — `chased` instead of `Chased Entry` | `exportAnalyticsCSV()` pushed raw ID strings without label lookup | Added `getAllLabels('errors')` and `getAllLabels('emotions')` lookups before row generation | 🟡 Display |

## v2.1.1 Bugs Found (Pre-existing, Queued for v2.2)

| # | Bug | Root Cause | Status | Severity |
|---|-----|-----------|--------|----------|
| 1 | PM time parsing broken — all PM trades bucket into 09:30–10:00 | `parseInt('1:30 PM'.split(':')[0])` returns `1`, not `13`. No AM/PM conversion anywhere. | **OPEN** — need shared `parseTradeHour()` helper. 6+ locations affected: CSV export, AI Coach, What-If cutoff, ETH filter | 🟡 Data |

---

## v2.1 Bugs Fixed

| # | Bug | Root Cause | Fix | Severity |
|---|-----|-----------|-----|----------|
| 1 | `testBMBridge` crash when status element null | `if(status) status.textContent='...'; status.style.color='...'` — semicolon made second statement run unconditionally | Wrapped in proper braces `if(status){ ... }` | 🔴 Crash |
| 2 | `setAnPeriod` deselects fee toggle button | `querySelectorAll('.tl-sf-btn').forEach(remove active)` hit fee toggle too | Added `if(b.id!=='anFeeToggle')` guard | 🟡 Visual |
| 3 | `setAnInstr` same issue | Same root cause as #2 | Same fix | 🟡 Visual |
| 4 | What-If Lab fees independent from global toggle | `wiState.feesEnabled` hardcoded to `false`, never synced | Three fixes: default reads localStorage, tab open syncs, toggle writes back | 🟡 Data |
| 5 | `clearPM()` missing `settle` and `customPMLevels` | Clear function didn't know about new fields | Added `settle` to field list, `customPMLevels=[]` | 🟡 State |
| 6 | Custom level keys used array index | `custom_0`, `custom_1` shifted on remove, mismatching hitLog | Changed to `custom_` + level name | 🔴 Data |
| 7 | Custom level null price crash | `isNaN(null)` behavior varies, `parseFloat(null)` issues | Added explicit `cl.price == null` guard | 🔴 Crash |
| 8 | `getMTFilteredTrades` fell back to unfiltered data | Period filter used `missedTrades` instead of instrument-filtered `trades` | Changed to `return trades.filter(...)` | 🟡 Data |
| 9 | `savePreflight()` wiped completion state | Created fresh object on every keystroke, losing `_completed` | Reads existing state first, preserves flags | 🔴 Data loss |
| 10 | Goals tracker affected by fee toggle | Used `getCommissionForTrades()` which respects toggle | Inline fee calculation, immune to toggle | 🟡 Display |

---

## v2.0 Bugs Fixed

| # | Bug | Root Cause | Fix | Severity |
|---|-----|-----------|-----|----------|
| 1 | FS + Error reduction overwrite | Error loss reduction read from original trade, not post-FS-modified | Reads from modified trade | 🟡 Data |
| 2 | Error loss reduction didn't sync pts/R | Only cut dollars, didn't recalculate points and R | Recalculates using per-trade instrument tick value | 🟡 Data |
| 3 | Winner R boost didn't sync pts | Scaled dollars but not points/R | Scales all three uniformly | 🟡 Data |
| 4 | Fee 2× discrepancy | Commission was already round-trip, got doubled | Removed erroneous ×2, rewrote `wiCalcStats` | 🔴 Data |
| 5 | `avgRiskDollars` used global instrument | Mixed ES/MES accounts calculated wrong | Per-trade instrument tick value lookup | 🟡 Data |
| 6 | Missed trade defaults hardcoded | Used 3 rPts and 1 contract instead of actual averages | Reads from trade data | 🟡 Data |
| 7 | Daily loss limit ignored fees | Accumulated gross P&L, not net | Subtracts per-trade commission | 🟡 Data |
| 8 | Optimizer Apply All crash | Nullified results then tried to read them | Saves recommendations before reset | 🔴 Crash |
| 9 | `apply` property name conflict | Collided with `Function.prototype.apply` | Renamed to `applyFn` | 🔴 Crash |
| 10 | Slider drag killed by DOM rebuild | `oninput` triggered full re-render, destroying the slider | `oninput` → display update only, `onchange` → full render | 🟡 UX |
| 11 | Stat card coloring by direction of change | Positive delta colored green even when value was negative | Colored by what the value IS (positive=green) | 🟡 Visual |
| 12 | Format types wrong on some cards | Trades showed $ sign, drawdown showed ± | Trades=count, Avg=abs, P&L=signed dollar | 🟡 Visual |

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
**Fix:** Every render function must guard `if(!n)` with early return. `wiCalcStats` already does this.

### Pattern 6: Array index as object key
**What happens:** `custom_0`, `fuel_0` etc. shift when items are added/removed, breaking hitLog lookups.
**Fix:** Use stable identifiers: `custom_` + name, or timestamp-based IDs.

### Pattern 7: `const` not hoisted like `function`
**What happens:** Calling a function that references a `const` before the `const` is declared causes ReferenceError.
**Fix:** Declare `const` values BEFORE any code that calls functions referencing them. `SCHEMA_VERSION` must be declared before `migrateLocalStorage()` is called.

### Pattern 8: `<details>` stays collapsed in edit mode
**What happens:** Form fields inside `<details>` (screenshots, errors, notes) are populated correctly by edit functions, but the collapsible stays closed so the user can't see or interact with the content.
**Fix:** Give the `<details>` element an ID, set `.open=true` in the edit function, and `removeAttribute('open')` in the clear function.

### Pattern 9: Fragile chip matching via `querySelectorAll` + text/attribute parsing
**What happens:** Edit functions try to restore chip selection state by parsing `onclick` attributes or matching `textContent`. Breaks when chips are dynamically rendered.
**Fix:** Set the selection state array (e.g. `selectedErrors`, `mtSelectedReasons`) first, then call the chip builder function (e.g. `buildErrorChips()`). The builder reads the state and applies `.sel` class automatically.

### Pattern 10: AM/PM time not converted to 24-hour for math
**What happens:** `parseInt('1:30 PM'.split(':')[0])` returns `1`, not `13`. All PM trades get bucketed/filtered as early-morning times.
**Fix:** Use a shared helper that extracts hour and adds 12 for PM: `var h=parseInt(parts[0]); if(/PM/i.test(time)&&h<12) h+=12; if(/AM/i.test(time)&&h===12) h=0;`

---

## Regression Test Checklist

Run these checks after any significant code change:

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
- [ ] Hide default → gone from form, still in analytics
- [ ] Add custom → appears in form, works in analytics
- [ ] Hide custom → dimmed in Settings, gone from forms, label resolves in analytics
- [ ] Export → Import preserves customLabels
- [ ] What-If + AI Coach show custom labels correctly
- [ ] CSV export uses display names

### Media (v2.1.1)
- [ ] Image URL → thumbnail; video URL → 🎬 link
- [ ] Mixed badge: "📷 2 🎬 1"
- [ ] Edit trade with media opens details section
