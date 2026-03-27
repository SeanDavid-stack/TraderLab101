# TraderLab 101 — Quick Reference

**v2.1 · Keep this open alongside the tool**

---

## Daily Workflow (7-Step Stepper)

```
1. PREFLIGHT    → Answer 8 questions → ✅ Complete (↺ Reset & Redo if needed)
2. PRE-MARKET   → Import or enter levels → Add custom levels → Set bias → Map fuel
3. OPEN CONTEXT → Confirm open type → Follow decision tree
4. LIVE PRICE   → Monitor levels → Review tag log → Manual tag if needed
5. TRADE        → Log entries → Tag targets, errors, emotions → 📷 Attach charts
6. MISSED       → Log trades you didn't take with reasons
7. JOURNAL      → Edit preflight answers → Save session → Notes, lessons, screenshots
```

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

## Trade Screenshots

- 📷 Screenshots section in trade form (after Notes)
- Paste image URLs — one per line, supports multiple
- Live previews while typing
- Purple 📷 badge on trade card shows count
- Thumbnails in expanded detail + journal review
- Populated when editing trades

---

## Level Tracker

| Badge | Source |
|-------|--------|
| ✓ tagged | Live detection (~5s checks) |
| ✓ tagged ◈ | Reconciled from session range |
| ✓ tagged ✎ | Manual (⊕ button, cyan badge) |

---

## Fee Toggle

One button syncs: Analytics ↔ Trade Log ↔ Missed Trades ↔ What-If Lab.
Daily goals tracker is **immune** — always shows real fees.

---

## Analytics Cards

| Card | Target |
|------|--------|
| Win Rate | >55% |
| Profit Factor | >1.5 |
| Avg R | >0.2R |
| Risk Neutral Rate | >50% |
| Full Stop Rate | <20% |
| Recovery Factor | >2.0 |

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
- Old backups (v1.x, v2.0) import cleanly — auto-migrated
- Schema v3 — migrations only ADD, never delete
- Always export before updating to a new version

---

## Settings Checklist

- [ ] Instrument preset selected
- [ ] Commission set
- [ ] BMBridge URLs configured (if using)
- [ ] CSV column mapping set up for your source
- [ ] Daily goals configured
- [ ] First backup exported

---

*"If this — then that. If not — then what?"*
