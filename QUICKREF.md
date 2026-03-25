# TraderLab 101 — Quick Reference

**v1.1 · Keep this open alongside the tool**

---

## Daily Workflow

```
1. PREFLIGHT    → Answer 8 questions → Click ✅ Complete Preflight
2. PRE-MARKET   → Import or enter levels → Set bias (Long/Short/Neutral)
3. OPEN CONTEXT → Confirm open type → Follow decision tree
4. TRADE        → Log entries in Trade Log → Tag targets, errors, emotions
5. MISSED       → Log trades you didn't take with reasons
6. JOURNAL      → Save session → Notes, lessons, screenshots
7. REVIEW       → Analytics → Filter by date/instrument → Study your edge
```

---

## Keyboard Shortcuts

| Action | How |
|--------|-----|
| Add custom target | Type name → Enter |
| Add custom setup | Type name → Enter (in Settings) |
| Quick date nav | ◄ ► buttons in Journal |
| Save trade | Click "Log Trade" button |
| Edit trade | Click ✎ Edit on any trade → modify → Update Trade |

---

## Trade Form Fields

| Field | What to Enter |
|-------|---------------|
| Setup | Opening, IBC, IBF, MR, VPOC Shift, BAR, MID>VWAP>VPOC, VHVN>VPOC, or custom |
| Direction | Long or Short |
| Entry/Stop | Price levels (0.25 increments for ES/MES) |
| Scale 1 | Risk Neutral exit — price + contracts |
| Scale 2 | Target exit — price + contracts |
| Scale 3/Runner | Final exit or trail — price + contracts |
| Targets | Click chips → set price → mark Hit/Bailed/Missed |
| Process | A = perfect, B = minor deviation, C = off plan, F = broke rules |
| Exit Time | Optional — enables duration tracking |

---

## Analytics Cards

| Card | What It Measures | Good |
|------|-----------------|------|
| Win Rate | Wins ÷ total trades | >55% |
| Net P&L | Total profit/loss after fees | Green |
| Profit Factor | Gross wins ÷ gross losses | >1.5 |
| Expectancy | Avg $ per trade | Positive |
| Avg R | Average R-multiple | >0.2R |
| Risk Neutral Rate | % reaching RN | >50% |
| Full Stop Rate | % taking full -1R loss | <20% |
| Recovery Factor | Net P&L ÷ max drawdown | >2.0 |
| First Trade WR | Win rate on 1st trade of day | Above overall WR |
| After Loss WR | Win rate following a loss | Near overall WR |
| Break Even Rate | % scratch trades | <10% |

---

## Open Types

| Code | Meaning | Market State |
|------|---------|-------------|
| HOR | High Out of Range | Gap up — above prior high |
| LOR | Low Out of Range | Gap down — below prior low |
| HIR | High In Range | Higher open, inside prior range |
| LIR | Low In Range | Lower open, inside prior range |
| IR-IV | In Range, In Value | Opened inside prior value area |

---

## Alignment Badges

| Badge | Meaning |
|-------|---------|
| ▶ In Play (green) | Setup conditions met |
| ◆ Waiting (gold) | Partial conditions, needs confirmation |
| ⚠ Not In Play (red) | Conditions not met |

---

## Target Outcomes

| Outcome | When to Use |
|---------|-------------|
| ✓ Hit | Price reached your target level |
| ↩ Bailed | Exited before target — select a reason |
| ✗ Missed | Target was valid but never reached |

**Bail Reasons:** Price Action Change · Market Structure Shift · News · Fear/Emotion · Protecting P&L · Time · Other

---

## Import Levels

| Source | Steps |
|--------|-------|
| BMBridge | Enter URL → Click Import |
| CSV File | Click Choose CSV File → select file |
| Google Sheet | Publish sheet as CSV → paste content in textarea |

Column format: Level name in column 1, price in column 2 or 3. Configure mapping in Settings → CSV Column Mapping.

---

## Process Ratings

| Grade | Meaning | Use When |
|-------|---------|----------|
| A | Perfect process | Followed every rule, regardless of outcome |
| B | Good, minor deviation | Mostly followed plan, small adjustment |
| C | Off plan | Significant deviation from methodology |
| F | Broke the rules | Revenge trade, no setup, ignored stops |

---

## Emotional States

😎 Confident · 🧘 Patient · 🎯 Focused · 😰 Anxious · 😤 Frustrated · 🤑 Greedy · 😨 Fearful · 🔥 Revenge · 😴 Bored · 😐 Neutral

Multi-select — tag all that apply to a trade.

---

## Data Safety

- **Export regularly:** Settings → Export Backup → saves JSON file
- **Import to restore:** Settings → Import Backup → merges with existing data
- Data lives in browser localStorage — cleared if you clear browser data
- No cloud sync, no server, no accounts

---

## Settings Checklist

- [ ] Instrument preset selected (MES/ES/MNQ/NQ/custom)
- [ ] Commission set per instrument
- [ ] BMBridge URL configured (if using Sierra Chart)
- [ ] CSV column mapping matches your data source
- [ ] Daily goals set (max loss, max trades, min process)
- [ ] First backup exported

---

*"If this — then that. If not — then what?"*
