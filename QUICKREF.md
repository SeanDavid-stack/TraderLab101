# TraderLab 101 — Quick Reference

**v2.2 · Keep this open alongside the tool**

---

## Daily Workflow (7-Step Stepper)

```
1. PREFLIGHT    → Answer 8 questions → ✅ Complete (↺ Reset & Redo if needed)
2. PRE-MARKET   → Import or enter levels → Add custom levels → Set bias → Map fuel
3. OPEN CONTEXT → Opening print auto-detects or use ⚡ estimate → Confirm open type → Follow tree
4. LIVE PRICE   → Monitor levels → Review tag log → IB auto-fills at 10:30
5. TRADE        → Log entries → Tag targets, errors, emotions → 📎 Attach media
6. MISSED       → Log trades you didn't take → Edit later if needed
7. JOURNAL      → Edit preflight answers → Save session → Notes, lessons, media
```

---

## Opening Print

| Context | Button | What Happens |
|---------|--------|-------------|
| Pre-RTH, no estimate | ⚡ Use [price] as Estimate | Gold preview — OT preview active, not committed |
| Pre-RTH, has estimate | ⚡ Update Estimate | Refreshes with current price |
| RTH, no real open | 📌 Set Opening Print | Captures live price as confirmed |
| RTH, has estimate | 📌 Confirm Opening Print | Replaces estimate with real value |
| Feed delivers open | Auto | Replaces estimate silently (alerts if OT changed) |
| Manual entry | Type in field | Overrides everything, clears estimate |

Live Tracking header shows: ⚡ live · 📌 captured · manual

---

## Pre-Market Levels

| Field | Section |
|-------|---------|
| pHigh, pLow, pClose, pVPOC, Settlement | Prior Day |
| pVAH, pVAL | Value Area |
| ONH, ONL, ON/VPOC, Today's Open | Overnight |
| Any name + price | Custom Levels (purple card) |

### Custom Levels
- Name only → Enter (fill price later, gold border = needs price)
- CSV import auto-adds unmapped labels as custom levels
- Settings → CSV Column Mapping → ★ Custom targets + ★ + New Custom Level

---

## Preflight Checklist

| Action | What Happens |
|--------|-------------|
| ✅ Complete Preflight | Locks answers, snapshots to journal, shows ↺ Reset |
| ↺ Reset & Redo | Keeps answers, unlocks form for editing |
| Edit after completing | Answers update live, completion preserved |
| 📋 Journal section | Same answers editable in Journal form, syncs both ways |

---

## Media Attachments

- 📎 Media section in trade form, missed trade form, and journal (after Notes)
- Paste URLs or local file paths — one per line, supports multiple
- **Image URLs** (`.png/.jpg/.gif/.webp/.svg`, imgur) → thumbnails
- **Local file paths** — auto-strips quotes, encodes `#` and spaces, converts to `file:///`
- **Video/other URLs** → 🎬 clickable links with domain preview
- Smart badge: 📷 2 🎬 1 for mixed media
- Populated when editing trades or missed trades
- Local file display works best when TraderLab is opened as a local HTML file

---

## Custom Labels

Settings → Labels. Five categories:

| Category | Default Count | Used In |
|----------|--------------|---------|
| Trade Setups | 7 | Trade form, missed trades, journal, analytics, What-If, AI Coach |
| Trigger Types | 4 | Trade form, analytics, What-If |
| Execution Errors | 12 | Trade form, analytics, What-If, AI Coach |
| Emotional States | 10 | Trade form, analytics, What-If, AI Coach |
| Missed Trade Reasons | 10 | Missed trade form, reason breakdown |

- 👁 Hide defaults you don't use (unhide anytime)
- \+ Add your own custom items
- Hidden items still appear in analytics for historical trades
- Nothing is ever deleted — hide/show only
- "↺ Reset" button per category — unhides defaults, removes custom items

---

## Level Tracker

| Badge | Source |
|-------|--------|
| ✓ tagged | Live detection (~5s checks) |
| ✓ tagged ◈ | Reconciled from session range |
| ✓ tagged ✎ | Manual (⊕ button, cyan badge) |

IB auto-fills from session range at 10:30 ET. Manual entry pauses auto-fill. Click Clear to resume.

---

## Fee Toggle

One button syncs: Analytics ↔ Trade Log ↔ Missed Trades ↔ What-If Lab.
Daily goals tracker is **immune** — always shows real fees.

---

## Analytics Cards (Configurable in Settings → Goals)

| Card | Default Green | Your Strategy May Differ |
|------|--------------|------------------------|
| Win Rate | >55% | A 30% WR with 3:1 R is profitable |
| Profit Factor | >1.5 | Depends on R:R and win rate |
| Risk Neutral Rate | >50% | Scale plan dependent |
| Full Stop Rate | <20% | Lower = better risk management |
| A-Process Win Rate | >60% | Measures process, not P&L |
| Break Even Rate | <15% | High BE may indicate hesitation |

---

## Open Types

| Code | Meaning |
|------|---------|
| HOR | Gap up — above prior high |
| LOR | Gap down — below prior low |
| HIR | Higher open, in range |
| LIR | Lower open, in range |
| IR-IV | In value area |

---

## Terminology

| Term | Context |
|------|---------|
| **Tagged** | Level detection — price touched a pre-market level |
| **Hit** | Trade target outcome — your target was reached |

---

## Process Ratings

| Grade | Meaning |
|-------|---------|
| A | Perfect — followed every rule |
| B | Minor deviation |
| C | Off plan |
| F | Broke the rules |

---

## BMBridge Setup

| Feed | Purpose |
|------|---------|
| ◎ Levels Feed | Pre-market level imports |
| ⚡ Live Price Feed | Near real-time price data |

Fallback chain: Price feed → Levels feed → Yahoo Finance

---

## Import Sources

| Source | How |
|--------|-----|
| BMBridge | Settings → Levels Feed URL → Import |
| CSV File | Choose file → auto-maps + auto-adds custom |
| Google Sheet | Publish as CSV → paste URL |
| Manual | Type into fields |

---

## Data Safety

- Export regularly: Settings → Export Backup
- Old backups (v1.x, v2.0, v2.1, v2.1.x) import cleanly — auto-migrated
- Schema v5 — migrations only ADD, never delete
- Always export before updating to a new version

---

## Settings Checklist

- [ ] Instrument preset selected
- [ ] Commission set
- [ ] BMBridge URLs configured (if using)
- [ ] CSV column mapping set up for your source
- [ ] Custom Labels reviewed — hide unused, add your own
- [ ] Daily goals configured
- [ ] First backup exported

---

*"If this — then that. If not — then what?"*
