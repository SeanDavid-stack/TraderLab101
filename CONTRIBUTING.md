# Contributing to TraderLab 101

Thanks for your interest in contributing! TraderLab 101 is a community tool built for the Traders Lab methodology.

---

## How to Contribute

### Reporting Bugs
1. Check [existing issues](../../issues) for duplicates
2. Open a new issue with: what happened, steps to reproduce, expected behavior, browser, screenshot

### Requesting Features
Open an issue with the `enhancement` label. Describe the feature and which workflow step it relates to.

### Submitting Code
1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Make changes to `TraderLab101.html`
4. Test in Chrome + at least one other browser
5. Submit a pull request

---

## The SACRED Rule

**User trade data and session data must NEVER be lost.**

If your change modifies the data schema:

1. **Increment `SCHEMA_VERSION`** (currently 4)
2. **Add migration** in BOTH `migrateLocalStorage()` AND `migrateImport(d)`
3. **ONLY add** fields with safe defaults
4. **NEVER delete, rename, or overwrite** existing data
5. **Migrations must be idempotent** (safe to run unlimited times)
6. **Document** in the `DATA SCHEMA & MIGRATION` comment block

---

## Code Style

- Single-file HTML app — keep it that way
- No external dependencies (except Google Fonts)
- All data in `localStorage`
- Use CSS variables for theming (`var(--green)`, `var(--text)`, etc.)
- `function name(){}` syntax (hoistable)

---

## Key Conventions

| Convention | Rule |
|-----------|------|
| "Tagged" | Level detection (price touched level) |
| "Hit" | Trade target outcome |
| `t.proc` | Process rating field (not `t.process`) |
| `t.screenshots` | Array of URL strings (UI says "Media" but field name is SACRED) |
| Custom level keys | `custom_` + level name (not index) |
| Fee toggle | Single source: `anShowFees` + `localStorage('tl_an_fees')` |
| Label chips | Dynamic — built by `buildErrorChips()` etc., not hardcoded HTML |

---

## Testing Checklist

- [ ] No console errors on load
- [ ] Existing data preserved (no loss)
- [ ] Export → Import cycle works
- [ ] New day rollover correct
- [ ] Empty state (0 trades) works
- [ ] Fees ON and OFF both work
- [ ] Multiple instruments work
- [ ] Analytics math correct
- [ ] Chrome + one other browser

---

## Architecture

Everything in `TraderLab101_v2.1.1.html` (~12,740 lines):
- HTML/CSS: lines 1–3450
- State + defaults + migration call: lines 3450–3570
- Core JS: lines 3570–9400
- Migration + export/import: lines 9400–9800
- What-If Lab + AI: lines 9800–11200
- Level tracker + session UI: lines 11200–12740

### Key localStorage Keys

`tl_sessions`, `tl_trades`, `tl_missed`, `tl_pm`, `tl_schema_version`, `tl_bmurl`, `tl_bmurl_price`, `tl_bmmap`, `tl_an_fees`, `tl_instrument`, `tl_goals`, `tl_hits`, `tl_preflight`, `tl_custom_labels`, `tl_custom_setups`, `tl_journal_dropdowns`
