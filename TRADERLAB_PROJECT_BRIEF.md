# TraderLab 101 — Project Brief

**v2.1.1 · Schema Version 4 · ~12,740 lines · ~350 functions**
Single-file HTML trading journal + analytics tool for ES/MES futures traders.
Built on Market Auction Theory (AMT) and Tom B.'s Traders Lab methodology.

---

## Purpose & Context

Sean is a futures trader and developer building TraderLab 101 for himself and his community, distributed free via GitHub + Discord. The tool runs entirely in the browser using localStorage — no server, no accounts. Sean trades ES/MES and NQ/MNQ futures using Sierra Chart with BMBridge for live market data, and IRT (Investor/RT) for pre-market level exports.

---

## Architecture

### Single-File Structure
Everything is in `TraderLab101.html`:
- Lines 1–800: HTML structure, CSS, splash screen
- Lines 800–3450: HTML panels (levels, trades, analytics, journal, settings)
- Lines 3450–3470: Constants, SCHEMA_VERSION, _safeParse, migrateLocalStorage() call
- Lines 3470–3560: State initialization (sessions, pmData, tradeLog, etc.)
- Lines 3560–9300: Core JavaScript (all features)
- Lines 9300–9500: DATA SCHEMA & MIGRATION block, export/import
- Lines 9500–11000: What-If Lab, AI Coach
- Lines 11000–12100: Level tracker, reconciliation, session UI

### Data Storage
All data in browser `localStorage`. Key constants defined at line ~3458:
```
KS='tl_sessions', KC='tl_checks', KP='tl_pm', KPF='tl_preflight',
KST='tl_st_checks', KBM='tl_bmurl', KBMP='tl_bmurl_price',
KTL='tl_trades', KCS='tl_custom_setups', KIS='tl_instrument',
KJD='tl_journal_dropdowns', KBMM='tl_bmmap', KMT='tl_missed',
KCL='tl_custom_labels'
```

Other keys: `tl_goals`, `tl_an_fees`, `tl_an_toggles`, `tl_an_collapse`, `tl_an_order`, `tl_hits`, `tl_schema_version`, `tl_rth_buffer`, `tl_splash_seen`, `tl_an_card_toggles`, `tl_an_card_order`, `tl_tl_card_toggles`, `tl_tl_card_order`

### Startup Order (CRITICAL)
```
SCHEMA_VERSION = 4          ← const, defined first
DEFAULT_ERRORS/EMOTIONS/... ← const arrays for label defaults
_safeParse()                ← utility function
migrateLocalStorage()       ← patches localStorage IN PLACE (function hoisted)
sessions = _safeParse(...)  ← reads already-migrated data
tradeLog = _safeParse(...)  ← already-migrated
missedTrades = _safeParse(...)
customLabels = _safeParse(KCL, {...})  ← label customizations
```
`migrateLocalStorage()` is defined later (~line 9530) but `function` declarations are hoisted, so calling it early works. `SCHEMA_VERSION` must be a `const` defined BEFORE the call.

---

## 🔴 SACRED DATA RULE

**User trade data and session data are SACRED.**

Every schema update must:
1. Increment `SCHEMA_VERSION` (currently 4)
2. Add a migration step in BOTH `migrateLocalStorage()` AND `migrateImport(d)`
3. ONLY add missing fields with safe defaults
4. NEVER delete, rename, or overwrite existing data
5. Migrations must be idempotent (safe to run unlimited times)
6. Document in the `DATA SCHEMA & MIGRATION` comment block (~line 9500)

### Schema History
| Schema | Version | Changes |
|--------|---------|---------|
| 1 | v1.x | Original |
| 2 | v1.1 | pmData date field, trade normalization |
| 3 | v2.1 | Settlement, custom levels, screenshots, dual feeds, RTH buffer, fee toggle, analytics state |
| 4 | v2.1.1 | Missed trade screenshots, custom labels support |

---

## Known Bug Patterns (Avoid These)

### #1: `var` declarations after init IIFE
`var` declarations appearing after the init IIFE cause hoisting as `undefined`. All declarations must be inside or before the IIFE. Has affected: `selectedSetups`, `currentProc`, `hitLog`, `INSTRUMENT_PRESETS`, `SETUP_LABELS`.

### #2: Raw `JSON.parse` on localStorage
Corrupt data in any key (especially `tl_hits`) silently crashes the app. Always use `_safeParse` helper. `hitLog` requires IIFE-wrapped initialization.

### #3: `</div><!-- /content -->` placement
The closing tag must enclose all panels — placing it too early leaves panels outside the scroll container.

### #4: `panel.scrollTop = 0` wrong target
`.content` is the scrollable container, not `.panel`.

### #5: Period/instrument button deselects fee toggle
Any `querySelectorAll('.tl-sf-btn').forEach(remove active)` must exclude `id!=='anFeeToggle'` and `id!=='mtFeeToggle'`.

### #6: Division by zero in stats
All render functions must guard `n=0` with early return. `wiCalcStats` already does.

### #7: `savePreflight()` must preserve completion state
Was creating a fresh object on every keystroke, wiping `_completed`. Fixed: now reads existing state first.

### #8: `<details>` stays collapsed in edit mode
Form fields inside `<details>` (media, errors, notes) are populated by edit functions, but the collapsible stays closed. Fix: give the element an ID, set `.open=true` in edit, `removeAttribute('open')` in clear.

### #9: Fragile chip matching via querySelector
Edit functions that parse `onclick` attributes or match `textContent` to restore chip state break when chips are dynamically rendered. Fix: set the selection state array first, then call the chip builder function which reads state and applies `.sel` automatically.

### #10: AM/PM time not converted to 24-hour
`parseInt('1:30 PM'.split(':')[0])` returns `1`, not `13`. All PM trades get bucketed as early-morning. Fix: shared `parseTradeHour()` helper. **Queued for v2.2.**

---

## Key Conventions

### Terminology
- **"Tagged"** = level detection (price touched a pre-market level)
- **"Hit"** = trade target outcome (your trade target was reached)
- These are distinct concepts used consistently throughout the UI

### Field Names
- `t.proc` = process rating (NOT `t.process`)
- `t.screenshots` = array of URL strings (renamed to "Media" in UI, but field name is SACRED)
- `t.emotion` = array (was string in v1, migrated)
- `t.rPts` = risk in points (per contract)
- `t.totalR` = `totalPnlPts / (rPts × contracts)` — per-contract basis
- Commission stored as round-trip — do NOT double-charge

### Custom Labels System
- `customLabels` stored in `tl_custom_labels`: `{errors:{hidden:[],added:[]}, emotions:{...}, reasons:{...}, triggers:{...}}`
- `DEFAULT_ERRORS`, `DEFAULT_EMOTIONS`, `DEFAULT_REASONS`, `DEFAULT_TRIGGERS` — const arrays, never modified
- `getActiveItems(cat)` — defaults minus hidden, plus added minus hidden (forms use this)
- `getAllLabels(cat)` — full id→label map including hidden (analytics/export use this)
- `LABEL_DEFAULTS` — map of category → default array
- Chips are built dynamically by `buildErrorChips()`, `buildEmotionChips()`, `buildReasonChips()`, `buildTriggerChips()`
- WI_ERRORS, WI_ERROR_LABELS, WI_EMOTIONS, WI_EMO_LABELS, WI_TRIGGER_LABELS — refreshed on tab open via `getAllLabels()`

### Custom Level Keys
Use `custom_` + level name (NOT array index). Example: `custom_VWAP`, `custom_WeeklyHigh`. Prevents key mismatch when levels are reordered/removed.

### biasLog
Should contain only mid-session changes. An empty array means bias held all day.

### Fee Toggle
Single source of truth: `anShowFees` variable + `localStorage('tl_an_fees')`. Default ON.
- `getCommissionForTrades()` returns 0 when toggle is OFF
- Daily goals tracker is IMMUNE — always shows real fees
- What-If Lab syncs bidirectionally with global toggle
- `wiState.feesEnabled` reads from localStorage on init

### Filter Bar Style
All four pages use `wi-filter-bar` class: Analytics, Trade Log, Missed Trades, What-If Lab. Period row + instrument row (auto-appears with 2+ instruments).

---

## Feature Inventory (v2.1.1)

### Pre-Market
- Standard fields: pHigh, pLow, pClose, pVPOC, Settlement, pVAH, pVAL, ONH, ONL, ONVPOC, todayOpen
- Custom Levels: name + optional price, tracked/tagged/reconciled, purple theme
- Fuel Map: buyers/sellers/stops with price + notes
- Bias: Long/Short/Neutral with change logging
- Import: BMBridge, CSV file, Google Sheets, IRT auto-detection
- CSV Column Mapping: user-configurable, ★ Custom targets, ★ + New Custom Level

### Opening Print System
- Pre-RTH estimate: `_preliminaryOpen` stored separately, gold border preview
- Auto-confirm from feed: replaces estimate, alerts if OT classification changed
- Manual capture: 📌 button during RTH
- Layered button states: pre-RTH → estimate workflow, RTH → confirm workflow
- Live Tracking header: source badges (⚡ live, 📌 captured, ⚠ estimate, manual)

### Preflight
- 8 research questions, minimum 3 required
- ✅ Complete + ↺ Reset & Redo
- Editable after completion (preserves state)
- 📋 Preflight Answers section in Journal form (syncs bidirectionally)

### Level Tracking
- Near real-time (~2-10s) live detection
- Three tag sources: live (✓), reconciled (✓ ◈), manual (✓ ✎)
- Proximity gradient (5 intensity levels, pulse at ≤1pt)
- RTH stale data protection with configurable buffer
- `levelHitState` rebuilt from hitLog on startup
- IB auto-fill at 10:30 ET with 1.5× and 2.0× extensions
- Manual IB override with Clear to resume auto-fill

### Trade Log
- 3 scale-outs + runner, R-multiple tracking
- 📎 Media: images as thumbnails, video/links as 🎬 (schema field: `screenshots`)
- Customizable execution errors, emotions, triggers (Settings → Custom Labels)
- 4 entry triggers (expandable), ideal exit, trend alignment
- Smart defaults (entry price from feed, direction from bias)
- Edit any trade (✎ → full form population → Update)
- Daily goals tracker (immune to fee toggle)

### Missed Trades
- Full edit support: ✎ → populate form → Update (edit banner + cancel)
- Period filter (All/1W/1M/3M/6M/YTD) + instrument filter
- Media attachments (same as trade log)
- What-if impact with top 3 costliest reasons
- Fee-aware calculations

### Journal
- Session snapshots: levels, custom levels, fuel, bias log, hits, preflight
- Custom levels displayed as purple ★ pills
- Editable preflight answers
- Media attachments (images + video links)
- Edit past sessions (✎ button loads all fields)

### Analytics
- 30+ overview metrics, 6 SVG charts
- 15+ collapsible/reorderable sections with persistent state
- ⚙ Sections dropdown with ✕ Close button
- Global fee toggle synced across all pages
- Period + instrument filters
- CSV export (computed stats, 10 breakdown tables, dynamic label names)

### What-If Lab
- 10 simulation panels
- Edge Optimizer (15+ dimensions, ranked by P&L impact)
- Presets (save/load)
- Fee toggle synced with global state
- Dynamic label lookups for errors/emotions/triggers (refreshed on tab open)

### AI Trade Coach
- Mode 1: clipboard prompt for any AI
- Mode 2: Anthropic API key, in-app (~$0.03/call)
- Three types: Full Review, Error Audit, Setup Analysis
- Dynamic label names in prompts (refreshed on tab open)

### Custom Labels System
- 4 categories: errors (12), emotions (10), reasons (10), triggers (4)
- Settings UI: hide defaults (👁 toggle), add custom items, hide custom items
- Nothing ever deleted — hide/show only
- `getAllLabels()` always returns full map (analytics safe)
- Export/import includes `customLabels`

### BMBridge
- Dual feeds: ◎ Levels Feed (tl_bmurl) + ⚡ Live Price Feed (tl_bmurl_price)
- `getPriceFeedUrl()` tries KBMP → KBM → Yahoo
- Auto-test on Settings open
- `_cl:` field mappings for custom levels in BMBridge import

### Media Rendering
- `isImageUrl()` detects image extensions + imgur domains
- `renderMediaItem(url, w, h)` — thumbnails for images, 🎬 links for video/other
- `renderMediaBadge(urls)` — smart counts: 📷 2 🎬 1
- Used in all 8 rendering locations (trade list, missed list, journal cards, session review, session cards, 3 form previews)

---

## Tools & Resources

- **Sierra Chart** — trading platform, CSV export source for BMBridge
- **BMBridge** — Sean's tool, localhost level distribution to Bookmap
- **IRT / Investor/RT** — pre-market level exports (Symbol/Price/Note format)
- **Bookmap** — heatmap visualization
- **GitHub + Discord** — distribution channels

---

## Approach & Patterns

- Sean communicates in ALL CAPS and prefers direct, concise responses
- Asks conceptual/architectural questions before implementation
- Works iteratively: confirms fixes work before moving on
- Uploads the current HTML file at start of sessions — always read it before making changes
- Separate Claude chats handle different concerns — do not cross-modify
- Uses the What-If Lab visual format as reference standard for filter bars

---

## Files in This Project

| File | Purpose |
|------|---------|
| `TraderLab101_v2_1_1.html` | The app — always upload latest version at session start |
| `TRADERLAB_PROJECT_BRIEF.md` | This file — project context for Claude |
| `CHANGELOG.md` | Version history |
| `README.md` | GitHub front page |
| `QUICKREF.md` | One-page daily reference card |
| `USERGUIDE.md` | Full user manual |
| `ERRORLOG.md` | Bug log with patterns to avoid |
| `TraderLab101_Bug_Feature_Tracker.md` | Active bug/feature tracker |
| `CONTRIBUTING.md` | Dev rules + SACRED rule |
| `SECURITY.md` | Privacy policy |
| `LICENSE` | MIT |

### Methodology PDFs (reference)
- `Opening_Context_Alignment.pdf`
- `Trader_Lab_Glossary.pdf`
- `Stats_by_Target.pdf`
- `VHVN__VPOC.pdf`
- `MID_to_VWAP_to_VPOC.pdf`
- `BAR_break_and_retest.pdf`
- `VPOC_SHIFT.pdf`
- `IBC.pdf`
- `IBF.pdf`
- `MR_mean_reversion.pdf`
