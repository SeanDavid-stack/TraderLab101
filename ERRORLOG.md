# TraderLab 101 — Error & Bug Log

**Complete record of every bug found, fixed, and known pattern to avoid.**

---

## v2.3 Bugs Fixed

| # | Bug | Root Cause | Fix | Severity |
|---|-----|-----------|-----|----------|
| B-040 | Best Trade card shows `+$-10` green when all trades are losers | Display logic didn't handle all-loss scenario | Fixed display logic | 🟡 Display |
| B-041 | CSV direction export shows raw lowercase `long`/`short` | No capitalization before export | Capitalized for display | 🟢 Display |
| B-043 | Goals dropdown says "Only perfect process" | Stale "Process" label | → "Only perfect execution" | 🟢 Display |
| B-044 | Visual chart tab says "By Process" | Stale "Process" label | → "By Execution" | 🟢 Display |
| B-045 | Analytics mini-breakdown says "A-Process" | Stale "Process" label | → "A-Execution" | 🟢 Display |
| B-046 | Filter bar missing EXECUTION label | HTML missing the label span | Added with data-filter attrs | 🟡 UX |
| B-047 | Filter button logic uses fragile child-index counting | `querySelector` by child position | → data-filter/data-anf/data-jf attribute selectors | 🔴 Logic |
| B-048 | What-If Lab says "Minimum Process Rating" | Stale "Process" label | → "Minimum Execution Rating" | 🟢 Display |
| B-049 | AI Coach Full Review says "Process quality" | Stale "Process" label | → "Execution quality" | 🟢 Display |
| B-050 | AI Coach Error Audit says "Process rating impact" | Stale "Process" label | → "Execution rating impact" | 🟢 Display |
| B-051 | clearJFilters shows both form AND review | Hidden flag not restored | Always returns to form view | 🟡 UX |
| B-052 | Journal heatmap — click day with trades but no session → nothing | `openSessionReview` returned silently when no session found | Changed to `jGoToDate()` which navigates to any date | 🟡 UX |
| B-053 | clearTLFilters — `===All` doesn't match `All (220)` | Trade count badges changed button text from `All` to `All (N)` | → `startsWith('All')` | 🔴 Logic |
| B-054 | clearJFilters — same textContent match issue | Same root cause as B-053 | → `startsWith('All')` | 🔴 Logic |
| B-055 | `applyJournalDropdowns()` crashes on import with empty `journalDropdowns` | Direct `.map()` on undefined properties without fallback | Falls back to `DEFAULT_JOURNAL_DROPDOWNS` when properties missing | 🔴 Crash |
| B-056 | Import error shows generic "invalid file" with no detail | Catch block swallowed actual error message | Now shows `err.message` and logs to error log with stack trace | 🟡 UX |

### Pattern 11: Missed trade scales use `pts` not `pnlPts`
Regular trade scales: `{label, price, qty, pnlPts, r}`. Missed trade scales: `{label, price, qty, pts}`. Different formats! The rendering at `renderMTList()` line 9758 calls `s.pts.toFixed(2)`. If you generate demo data or import data with `pnlPts` instead of `pts`, the Missed Trades tab crashes.

---

## v2.2 Bugs Fixed

| # | Bug | Root Cause | Fix | Severity |
|---|-----|-----------|-----|----------|
| 1 | Direction case mismatch — Analytics "By Direction" showed 0 trades for all trade log entries | Trade Log saved `'long'` (lowercase), Missed Trades saved `'Long'` (capitalized). Comparisons used capitalized. | Standardized to lowercase. All comparisons use `.toLowerCase()` for legacy safety. | 🔴 Data |
| 2 | Direction dropdown missing onchange — changing direction didn't recalculate R/P&L/result | No `onchange` handler on `tl-dir` or `mt-dir` `<select>` elements | Added `onchange="calcTrade()"` and `onchange="calcMissed()"` | 🔴 UX |
| 3 | Missed trade log CSS class always "short" | Compared `t.dir==='Long'` but trades stored lowercase | Fixed with `.toLowerCase()` normalization | 🟡 Display |
| 4 | Hidden setup preserved on edit — editing wipes setup field | Edit populated dropdown but hidden value wasn't an option | Injects temporary "(hidden)" option | 🔴 Data |
| 5 | CSV export break-even count always 0 | Compared `'BE'` instead of `'Break Even'` | Fixed comparison string | 🟡 Data |
| 6 | Trade Log stats ignored fee toggle | Used gross P&L regardless of toggle | Shows net with gross/fee breakdown when ON | 🟡 Data |
| 7 | AM/PM time parsing — PM trades bucket as morning | `parseInt('1:30 PM')` returns `1`, not `13` | Shared `parseTradeHour()` helper, fixed 9 locations | 🟡 Data |
| 8 | Screenshot `#` in filenames breaks URL | `#` means fragment in URLs, SC uses `#` in filenames | `sanitizeMediaUrl()` encodes `#` to `%23` | 🟡 Data |
| 9 | Screenshot quoted paths fail to load | Windows paste wraps in `"quotes"` | `sanitizeMediaUrl()` strips outer quotes | 🟡 UX |
| 10 | AI Coach stale label variables | Custom labels showed raw IDs in prompts | Added `getAllLabels()` refresh on AI Coach tab open | 🟡 Data |
| 11 | CSV export raw IDs for errors/emotions | No label lookup before row generation | Added lookups in `exportAnalyticsCSV()` | 🟡 Data |
| 12 | What-If Lab missed reason filter key mismatch | Old presets stored display-string keys | `wiLoadPreset()` auto-migrates old keys | 🟡 Data |
| 13 | What-If Lab scroll jump | Any slider/chip interaction caused scroll to top | Saves and restores `.wi-scroll` position | 🟢 UX |
| 14 | Duplicate label addition | Could add same label twice (case-insensitive) | Blocked with toast message | 🟢 UX |
| 15 | Setup not required on Missed Trades | Setup field was optional | Now validated as required | 🟢 Data |
| 16 | Hide label without trade count warning | User could hide a label used by 50 trades without knowing | Confirm dialog shows trade count | 🟢 UX |

## v2.1.1 Bugs Fixed

| # | Bug | Root Cause | Fix | Severity |
|---|-----|-----------|-----|----------|
| 1 | AI Coach stale label variables — custom labels showed raw IDs in AI prompts | `WI_ERROR_LABELS`, `WI_EMO_LABELS`, `WI_TRIGGER_LABELS` only refreshed on What-If tab open, not AI Coach tab | Added same refresh (`getAllLabels()`) to `if(id==='aicoach')` block | 🟡 Data |
| 2 | CSV export used raw IDs for errors/emotions — `chased` instead of `Chased Entry` | `exportAnalyticsCSV()` pushed raw ID strings without label lookup | Added `getAllLabels('errors')` and `getAllLabels('emotions')` lookups before row generation | 🟡 Display |

## v2.1.1 Bugs Found (Fixed in v2.2)

| # | Bug | Root Cause | Status | Severity |
|---|-----|-----------|--------|----------|
| 1 | PM time parsing broken — all PM trades bucket into 09:30–10:00 | `parseInt('1:30 PM'.split(':')[0])` returns `1`, not `13`. No AM/PM conversion anywhere. | **FIXED v2.2** — shared `parseTradeHour()` helper. 9 locations fixed. | 🟡 Data |

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
**Fix:** Use shared `parseTradeHour()` helper. **FIXED in v2.2** — applied across 9 locations.

### Pattern 11: Direction case mismatch between forms
**What happens:** One form saves `'long'` (lowercase), another saves `'Long'` (capitalized). Downstream comparisons match only one case, silently dropping the other from analytics.
**Fix:** Standardize all dropdown `value` attributes to lowercase. All comparisons use `.toLowerCase()` for legacy data safety. Always add `onchange` to direction dropdowns so switching recalculates.

### Pattern 12: Special characters in file paths break URLs
**What happens:** `#` in filenames (common in Sierra Chart output) means "start of fragment" in URLs — everything after it is silently dropped. Outer `"quotes"` from Windows paste become part of the URL. Backslashes aren't valid in URLs.
**Fix:** Use `sanitizeMediaUrl()` helper: strip quotes, convert `\` to `/`, encode `#` `%` `?` and spaces, prepend `file:///` for local paths. Apply via `parseMediaUrls()` at all parse points.

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
