# Multi-Symbol Support in TraderLab 101

**Version 2.3.11 · April 2026**

A reference for users who want to track multiple instruments — and a peek under the hood for anyone curious about what changed across the v2.3.9 → v2.3.11 releases to make symbol support correct end-to-end.

---

## What's new

### Live price feed follows your instrument

Set your instrument in **Settings → Instrument** and the Yahoo Finance fallback now pulls data for that symbol instead of the hardcoded ES feed it used in earlier versions. Built-in mappings:

| Selected | Yahoo ticker fetched |
|---|---|
| **MES** | `ES=F` |
| **ES** | `ES=F` |
| **MNQ** | `NQ=F` |
| **NQ** | `NQ=F` |

Micros track the parent contract on Yahoo because Yahoo's micro feeds can be sparse or stale.

For any **custom contract** outside the four presets, there's a new optional **Yahoo Symbol** field in Settings → Instrument. Enter your Yahoo ticker (e.g. `YM=F`, `RTY=F`, `CL=F`, `GC=F`, `BTC-USD`, `^GSPC`) or leave blank — TraderLab will auto-derive `<Symbol>=F` from the symbol name as a sensible default. The status line under the live price shows which symbol is being fetched at a glance.

### Per-trade commission, tick value, tick size

Every trade now stamps these three fields onto its own record at save time:

- `t.commission` — the per-contract round-trip cost active when you saved
- `t.tickValue` — the dollar value of one tick
- `t.tickSize` — the point size of one tick

This is the foundation of correct multi-symbol analytics. Before, calculations would re-derive these from the *currently active* instrument settings — so if you traded MES in the morning, switched to ES in the afternoon, and viewed analytics, your morning MES trades would be silently revalued at ES point values. Now they hold their own truth.

Old trades from before v2.3.10 don't have these fields, and that's fine — TraderLab falls back to the preset / active-instrument lookup in those cases. **No migration. No data loss.**

### Multi-symbol UX in the Trade Log

When your log contains 2+ distinct instruments, two new affordances appear:

1. **Soft info banner** — explains what's happening and points at the **Analytics → Instrument filter**, which scopes the entire dashboard to one symbol at a time. Dismissible; reappears only if your symbol count later grows.
2. **Per-symbol summary chips** above the trade list:

   `ES 80 · 55% · +$3,400` &nbsp;&nbsp;&nbsp; `NQ 40 · 60% · +$1,800` &nbsp;&nbsp;&nbsp; `MES 12 · 50% · +$210`

   Click any chip to filter the trade list to that symbol; click "All" to restore.

This is *deliberately* not a "single-symbol mode" toggle. The Instrument filter is already strictly more flexible than a binary mode (per-symbol or aggregate or any subset), and adding a mode would double the testing surface and hide aggregate analytics from users who sometimes want them.

### Custom-symbol commission validation

The four presets ship with sensible default commissions; for any other symbol there's no sensible default — your broker rate is yours alone. So **Settings → Custom Symbol** now blocks the Save button if a non-preset symbol is saved with commission `0` or empty:

> *Commission required for custom symbol "XYZ" — enter your broker RT cost.*

This prevents the silent failure mode where a custom symbol gets saved with `commission: 0` and propagates `$0` fees through analytics, daily goals, and What-If forever.

### Edit-trade dropdown handles historical symbols

If you trade YM in the morning, switch to ES in the afternoon, and open to **edit** that morning YM trade, the trade form's instrument dropdown now auto-injects YM as an option instead of silently falling back. Same fix applied to Missed Trades.

---

## Best practice — one log per instrument

TraderLab's analytics, win rate, expectancy, and R-multiple math read cleanest when the log is scoped to a single symbol. The simplest pattern for a multi-symbol trader:

1. **One JSON backup per symbol.** Name them `Sean_NQ_2026.json`, `Sean_ES_2026.json`, etc.
2. **Switch between them** with Settings → DATA → Export / Import.
3. **Settings → Log Name** keeps the file name in sync.

If you'd rather keep multiple symbols in one log, that works too — TraderLab v2.3.10+ persists tick value, tick size, and commission per trade so historical numbers stay accurate even if you change your active instrument later. The summary chips and Instrument filter make per-symbol analysis a click away.

---

## Under the hood — what had to change

This is the map for anyone who wants to modify the source. **TraderLab is one ~15,000-line single-file app**, and what looks like a small change usually has a longer pipeline than expected. Symbol support touched eight distinct paths:

### 1. Yahoo Finance fetch URLs (3 sites)
The live-price fallback uses three resolution strategies for CORS reasons — direct fetch, AllOrigins proxy, and corsproxy.io fallback. All three were hardcoded to `ES%3DF` regardless of the user's instrument. Now they all call `getYahooTicker()`.

### 2. `getYahooTicker()` — new resolution helper
Priority order:
1. Explicit override on `instrumentSettings.yahooTicker`
2. Preset mapping (`INSTRUMENT_PRESETS[name].yahooTicker`)
3. Sensible guess: `<name>=F`
4. Safe fallback: `ES=F`

### 3. Trade dropdown injection
`syncTradeFormInstrument()` already inserted the *currently active* custom symbol as an option. But editing a trade with a *different* historical symbol (e.g. you traded YM yesterday but now you're active on ES) still left the dropdown without YM. New `ensureInstrumentOption(selectEl, name)` helper adds historical symbols on demand from `editTradeEntry` and `editMissedTrade`.

### 4. Per-trade fee calculation (6 sites)
The codebase has six places that compute commission for a trade — daily goals tracker, analytics `getCommissionForTrades`, equity curve `cumNet`, missed-trade `getMTFee`, AI Coach `buildAIPrompt`, What-If per-trade fee. All six now prefer `t.commission` when present, falling back to preset / active-instrument lookup for old trades.

### 5. What-If risk math (2 sites)
- Risk per-contract loop in `wiGetBaseTrades` (line ~12570)
- Improvement loop in `wiRunOptimizer` (line ~12719)

Both now prefer `t.tickValue` / `t.tickSize` when present, with the same fallback chain.

### 6. Yahoo ticker input sanitization
The new override field strips whitespace, uppercases, and rejects characters Yahoo doesn't use (`A-Z 0-9 . - = ^` only). Toast surfaces the cleaned value if the input changed.

### 7. Multi-symbol UX components
- `getDistinctTradeInstruments()` — pure helper
- `renderMixedInstrumentBanner()` — soft banner with dismissable count
- `renderSymbolSummary()` — per-symbol chip row with click-to-filter
- `filterTradeListByInstrument(symbol)` — wires `tlInstrFilter` into the trade list filter pipeline
- All called from `renderTradeLog()`

### 8. Commission validation in Settings
`saveCustomInstrument()` now blocks save with red-border + focus + toast when a non-preset symbol has commission ≤ 0 or empty. Other validation errors (missing name, bad tick size, bad tick value) also highlight their fields in red for consistent feedback.

### Why each fix was its own
Each calculation lives in a different code path and they don't all reach back to one source of truth. The cleanest way to make them reach the same answer was to **persist on the trade record itself** at save time, then have every path prefer the persisted value. That's why a "small symbol fix" turned into eight changes — every path that recomputes anything needed to know which source of truth to trust.

---

## Modifying the source

The license is **PolyForm Noncommercial 1.0.0**. Personal modifications are explicitly allowed — for learning, your own workflow, or hobby use. You may NOT sell modified versions, redistribute them commercially, or include any portion of the source in a competing product. See `LICENSE` for full terms.

If you do modify the source, the cascade map above is your starting point. The single biggest pitfall is assuming any one calculation has a single source for tick / commission data — there are eight, and they need to stay in sync.

---

## Backwards data compatibility

Every release in the v2.3.9 → v2.3.11 chain is **100% backwards-compatible** with prior versions:

- All new fields (`t.commission`, `t.tickValue`, `t.tickSize`, `instrumentSettings.yahooTicker`, `tl_mixed_instr_dismissed_count`) are purely additive.
- Old trades without the new fields use the existing fallback chain.
- No localStorage key was renamed or reshaped.
- JSON imports preserved as-is.

Verified by a 6-stage smoke test against the v2.3 demo dataset (220 trades / 61 sessions / 41 missed — all old format) plus an export → wipe → re-import round-trip that confirmed identical state on both sides. Zero JS console errors.

---

*If you have questions or hit something unexpected, open an issue on the [GitHub repository](https://github.com/SeanDavid-stack/TraderLab101) or reach out via the Traders Lab Discord.*

— SeanDavid
