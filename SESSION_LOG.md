# TraderLab 101 — Session Log

A rolling, chronological log of substantive work sessions. Newest at the top. Use this to get oriented quickly on what's been done, why, and what's still open.

---

## 2026-05-13 — v2.3.14 → v2.3.15

### What shipped

**One user-visible feature plus a housekeeping cleanup.**

#### 1. Journal Session draft persistence

User pain: closing the browser mid-entry on a long journal write (Trade Notes / Lesson) loses everything. Now those entries auto-save as you type and restore on next open.

- 350ms-debounced save on every field change in the journal form
- Captures all 12 form fields (selects, textareas, input) plus the Process Rating button state and Setup chip selections
- **"✓ Draft saved"** indicator in the Session Entry form header
- **"✕ discard"** link next to the indicator — manual abandon with a confirm prompt; reverts to the saved session if one exists, or empties the form
- Restore only applies when the draft is newer than the saved session for the same date (avoids stale overrides)
- Clears on Save / Cancel Edit / Discard Draft / Clear Everything

**Scope decision discussed and rejected during the session:** add the same draft persistence to the Trade Log and Missed Trade forms. Rejected because (1) those are rapid fill-and-save flows where typing time at risk is seconds not minutes, and (2) the surface area to capture full state (dynamic scale rows, multi-select chip arrays, target arrays) wasn't justified by the small UX win. Also considered and rejected: a `beforeunload` warning for those forms — too unreliable across browser engines and can't be fully verified programmatically (the actual browser prompt fires from user gesture, not script).

**Implementation:**
- New additive key: `tl_draft_journal`
- New JS identifier: `KJDR` (NOT `KJD` — that's already taken by `tl_journal_dropdowns`; caught this mid-session as a parse error that broke the entire script, fixed before push)
- New functions: `_captureJournalDraft`, `_draftHasContent`, `saveJournalDraft`, `clearJournalDraft`, `restoreJournalDraft`, `discardJournalDraft`, `updateJournalDraftIndicator`
- Wired via event delegation on `#panel-journal` (input/change/click), plus explicit hooks in `_doSaveSession`, `cancelJEdit`, `loadJDate`
- Indicator placed in the Session Entry header between the title and the Cancel Edit button

#### 2. SCHEMA_VERSION migration gap closed

Pre-existing inconsistency: `SCHEMA_VERSION = 7` (used by the exporter, set when multi-symbol per-trade fields landed in v2.3.10) but `migrateImport` topped out at v6. Every export-import round-trip silently bumped the value by 1 because of the always-run "Normalize" block but the migration ladder never explicitly handled it. Added a no-op v6→v7 branch so the ladder matches the constant. No data shape change.

### Files changed
- `TraderLab101.html` (v2.3.14 → v2.3.15, 7 in-file version refs)
- `CHANGELOG.md`, `README.md`, `QUICKSTART.md`, `QUICKREF.md`, `USERGUIDE.md`
- `_build_pdfs.py` (cover version string)
- `USERGUIDE.pdf`, `QUICKSTART.pdf`, `MULTI_SYMBOL_NOTES.pdf` (regenerated)
- `SESSION_LOG.md` — this entry

### Testing performed
- Programmatic end-to-end via headless preview: type → save → reload → restore → save again → draft clears (all clean)
- Manual smoke test in real Chrome via the Chrome MCP: same flow plus visual confirmation of the indicator and discard link
- Discard button verified both scenarios: with saved session (reverts) and without (empties)
- Schema migration verified: v2 → 7 and v6 → 7 both land at schemaVersion 7
- Zero JS console errors at any point
- 220-trade v1.0-era demo still loads cleanly

### Failures / lessons from this session (Rule 12)
- **`KJD` identifier collision broke ALL JS.** I declared `var KJD = 'tl_draft_journal'` without first grepping the file. Existing `const KJD = 'tl_journal_dropdowns'` on line 3918 made the duplicate declaration a SyntaxError. The whole script failed to execute, and **the preview console showed no error** because pre-execution syntax errors don't always surface to dev tools. Caught it via Rule 4 "loop until verified" — first programmatic check was `TL_VERSION` and it was undefined. Fix: renamed to `KJDR`. Lesson reinforced: **Rule 8 — read before write.** Grep the file for any identifier name before declaring a new global.
- **`beforeunload` was started and then dropped.** Initial plan was Option A (journal draft) + Option C (beforeunload warning for trade/missed). User questioned whether C was worth shipping given (a) browser-side prompt is unverifiable programmatically, (b) inconsistent browser behavior, and (c) the parse error showed any silent JS failure also kills the protection. Agreed and removed C entirely. Lesson: an unverifiable safety net might be worse than no safety net because it creates false confidence.

### Open items NOT done
- **Manual smoke test screenshot review.** I verified the smoke test programmatically through the Chrome MCP, including a screenshot showing all the right elements rendered. User has the file open in real Chrome at `http://localhost:8765/TraderLab101.html` and can interact directly if they want additional eyes-on.
- **Trade Log and Missed Trade forms still have no draft protection.** Documented in the changelog under "What is NOT covered (by design)." If user pain comes up here, revisit in a future release.

---

## 2026-05-12 — v2.3.13 → v2.3.14

### What shipped

**Two user-visible features + one set of legal/business changes.**

#### 1. Dynamic scale-outs in the Trade Log

- New **+ Add Scale** button below the Risk Neutral / Target / Runner block.
- Click to insert an additional Target leg *between Scale 2 and the Runner row*.
- Each user-added row has its own **✕ Remove** button. Labels auto-renumber on add/remove (`Scale 3 — Target 2`, `Scale 4 — Target 3`, …).
- Runner always stays as the final exit row regardless of how many extras are added.
- No upper limit on how many scales a trade can have.

**Why this was a small surface change but big-feeling code change:** the data model (`trade.scales[]`) was *already* a variable-length array on disk, so old 3-scale trades load unchanged. The hard-coded "3" only lived in:
- The HTML form (3 fixed scale blocks)
- `calcTrade()` (3-entry scales config)
- `saveTradeEntry()` (3-entry tuple loop)
- `clearTradeForm()` (`[1,2,3].forEach`)
- `editTradeEntry()` (used position-based IDs)

All five replaced with class-based DOM walks via `#tl-scales-list .tl-scale-row`. Added `addScaleRow()`, `removeScaleRow()`, `renumberScaleLabels()`.

#### 2. Mandatory Service & Support Terms splash

New one-time disclaimer splash that gates the app on first load. Four sections:

- **Bug Fixes Are at the Developer's Discretion** — reviewed/fixed at sole discretion, no obligation, no timeline guarantee.
- **Classification Is at the Developer's Discretion** *(added later in v2.3.14 as a text-only amendment — commit `7fefadf`)* — what counts as a bug, an enhancement, or a feature request is determined solely by the developer. The classification is final and governs whether work is free (standard release) or billable (custom request). Closes the gray area between "I think this is a bug, fix it free" vs "I consider this a feature request, $100".
- **Custom Requests & Add-Ons Require a Service Fee** — the tool itself is free; the developer's time is not. **Minimum $100.00 USD per request.** Each fee covers that one request only (no future versions, ongoing maintenance, priority support, or credit toward future requests). Scope agreed in writing first.
- **Your Trading Decisions Are Your Own** — standard "not advice" framing.

UX gating:
- Checkbox + disabled-by-default **Continue** button. Button only enables once the box is ticked.
- Cannot be ESC-dismissed.
- `showDisclaimer()` resets the checkbox state every time it opens (so a same-session re-show after Clear Everything doesn't appear pre-ticked).
- New additive localStorage key `tl_disclaimer_agreed` — appears in the Clear Everything key list so a full reset re-prompts.
- New users see welcome splash → dismissal chains to disclaimer. Existing users (already past welcome) see the disclaimer alone on next load.

#### 3. Contact info added across the project

- Website: **https://sdes.dev**
- Email: **sean@sdes.dev** (rendered as `mailto:` links)

Placed in: welcome splash signature, disclaimer splash signature, Settings credits footer, disclaimer's "Custom Requests" contact line, README, USERGUIDE, QUICKSTART, MULTI_SYMBOL_NOTES.

### Files changed

| File | What changed |
|---|---|
| `TraderLab101.html` | v2.3.13 → v2.3.14 (6 in-file version refs); dynamic scales (HTML form + 6 JS sections); new disclaimer splash (HTML + 3 JS functions); contact info in 4 spots |
| `CHANGELOG.md` | Full rewrite — added v2.3.14 entry, bridge note for v2.3.x intermediate versions, kept original v1.0 entry |
| `README.md` | Version badge v1.0 → v2.3.14; Trade Log blurb updated; new "Feedback & Service Terms" section; contact lines |
| `QUICKSTART.md` | v2.3.13 → v2.3.14; Step 1 documents both splashes; Step 6 documents + Add Scale; help-table row for custom requests |
| `QUICKREF.md` | v1.0 → v2.3.14; scale-out table includes + Add Scale row |
| `USERGUIDE.md` | v2.3.13 → v2.3.14; Getting Started covers Service Terms splash; Scale-Outs section rewritten for variable length |
| `MULTI_SYMBOL_NOTES.md` | Contact line + signature updated (file otherwise left as the historical v2.3.9 → v2.3.11 release notes) |

### Testing performed

Full end-to-end test via a local HTTP server + Claude Preview MCP. All zero-error.

- ✅ Static audit: no stale `tl-s[1-3]-` IDs, no positional `scales[0/1/2]` access, no fixed-count assumptions
- ✅ Migration: demo JSON (`schemaVersion: 2`, 220 trades / 61 sessions / 41 missed) loads cleanly into v2.3.14
- ✅ Render after import: Trade Log (220 rows), Analytics, What-If, Journal, Missed Trades — all OK
- ✅ Dynamic scales: add → 5 rows, remove → 4 rows, labels auto-renumber, Runner stays last
- ✅ Save 5-scale trade: R values 1/2/3/4/5, total +60 pts / +3R / Win, `gotRN: true`, commission stamped
- ✅ Edit 5-scale trade: form auto-expands to 5 rows, all data restored
- ✅ Edit old 3-scale demo trade: exactly 3 rows, no spurious extras
- ✅ Export round-trip: 5-scale trade preserved through JSON export → re-parse
- ✅ Disclaimer flow: welcome → chain → disclaimer; premature agree blocked; tick → enable → agree → key stored
- ✅ Bug found and fixed mid-test: `showDisclaimer()` now resets checkbox state on every open
- ✅ Final verification: zero JS console errors across the entire test run

### Known items NOT done

1. **PDFs not regenerated.** The `*.pdf` files (`USERGUIDE.pdf`, `QUICKSTART.pdf`, `MULTI_SYMBOL_NOTES.pdf`) still reflect the v2.3.13 Markdown. Run `_build_pdfs.py` to regenerate. Did not run it without confirmation.

2. **Pre-existing `SCHEMA_VERSION` gap (not a regression).** `SCHEMA_VERSION = 7` (used on export) but `migrateImport` tops out at `v6`. Harmless because the v6→v7 bump (commission/tickValue/tickSize per trade from the multi-symbol work) was purely additive and the always-run "Normalize" block at the bottom of `migrateImport` handles all data-shape concerns. Could be cleaned up with one line: `if(d.schemaVersion < 7){ d.schemaVersion = 7; }` after the v5→v6 block.

3. **Splash not showing for the user after reopening (open thread).** User reported the Service & Support Terms splash didn't appear after a close-and-reopen even though they never agreed. Init code at line 4226 looks correct. Most likely cause: browser served a cached old file, or user opened a different copy. Diagnostic snippet was provided to run in DevTools console. **Awaiting user feedback to confirm root cause** — may or may not be a code bug.

### Architectural / standing rules reinforced

1. **Backwards data compatibility is non-negotiable.** Every change here was additive — new localStorage key (`tl_disclaimer_agreed`), no field renames, no shape changes. `trade.scales[]` was already an array on disk; we just exercise the existing flexibility.
2. **Filename stays `TraderLab101.html`.** Version lives inside the file (6 spots).
3. **Single-file app.** All HTML / CSS / JS in one file (~15k lines, ~915 KB).

### Working state of localStorage keys

| Key | Purpose | Notes |
|---|---|---|
| `tl_splash_seen` | Welcome splash dismissed flag | Existing |
| `tl_disclaimer_agreed` | Service & Support Terms agreed flag | **New in v2.3.14** |
| `tl_trades` (`KTL`) | Trade log | Existing |
| ... | (full list in the `clearEverything` keys array) | |

---

## How to pick up in a future session

1. **Read this file first.** Most recent entry = current state.
2. **Read `MEMORY.md`** in the Claude project folder for the standing rules (backwards compat, versioning, GitHub repo, sdes.dev contact).
3. **Confirm in-file version:** `<title>` and `TL_VERSION` should match. If they don't, something's mid-migration.
4. **The "what to verify in browser" recipe:** spin up a local server (`python -m http.server 8765` from the project folder), open `http://localhost:8765/TraderLab101.html`, then in DevTools run `({version: TL_VERSION, splashSeen: localStorage.getItem('tl_splash_seen'), disclaimerAgreed: localStorage.getItem('tl_disclaimer_agreed')})`.
