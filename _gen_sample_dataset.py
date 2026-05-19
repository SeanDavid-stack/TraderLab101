"""
Generate a fresh, fully-shaped TraderLab 101 v2.3.15 demo backup.

Goal: a slightly-profitable trader, ~300 trades over the past 6 months across
MES/ES/MNQ/NQ, plus matching Journal sessions and missed trades — built to the
EXACT current schema so importing triggers ZERO migration recalculation.

Zero-migration requirements (verified against migrateImport + importData):
  - schemaVersion: 7  -> every versioned migration branch is skipped
  - Only the "Always: Normalize" block runs. Every field it would touch is
    pre-set with the correct type so the value is returned unchanged.
  - totalR uses the CURRENT formula totalPnlPts/(rPts*contracts). The R-fix
    sub-block only rewrites totalR when it matches the OLD formula
    (totalPnlPts/rPts) AND contracts>1 — by using the new formula we never
    collide with that, so totalR is left untouched.
  - emotion is an array, scales/errors/targets/screenshots are arrays,
    sessions carry hitsSnap [] / preflightSnap null / levelSnap null,
    missed trades carry reasons [] / scales null / screenshots [].

Deterministic: fixed seed so re-running yields an identical file.
"""

import json
import random
from datetime import date, timedelta

SEED = 20260519
random.seed(SEED)

OUT = r"D:\SDES Current Program Stack 4.8.26\TraderLab101\traderlab-sample-300.json"

# ── Exact preset table (from INSTRUMENT_PRESETS, line 4118) ──────────────
PRESETS = {
    "MES": {"name": "MES", "tickSize": 0.25, "tickValue": 1.25,  "commission": 0.62, "yahooTicker": "ES=F"},
    "ES":  {"name": "ES",  "tickSize": 0.25, "tickValue": 12.50, "commission": 2.32, "yahooTicker": "ES=F"},
    "MNQ": {"name": "MNQ", "tickSize": 0.25, "tickValue": 0.50,  "commission": 0.62, "yahooTicker": "NQ=F"},
    "NQ":  {"name": "NQ",  "tickSize": 0.25, "tickValue": 5.00,  "commission": 2.32, "yahooTicker": "NQ=F"},
}
INSTR_WEIGHTS = [("MES", 45), ("MNQ", 25), ("ES", 18), ("NQ", 12)]

SETUPS = ["opening", "cont", "mr", "ibf", "vpoc", "bar", "midvpoc", "vhvn"]
TRIGGERS = {
    "1": "Type 1 — Break High ↑",
    "2": "Type 2 — Break Low ↓",
    "3": "Type 3 — Sweep Low → Long ↑",
    "4": "Type 4 — Sweep High → Short ↓",
}
LONG_TRIGGERS = ["1", "3"]
SHORT_TRIGGERS = ["2", "4"]
ERRORS = ["chased", "early-entry", "late-entry", "moved-stop", "early-exit",
          "no-setup", "wrong-size", "fomo", "revenge", "overtrading",
          "no-plan", "widened-stop"]
EMO_POS = ["confident", "patient", "focused", "neutral"]
EMO_NEG = ["anxious", "frustrated", "greedy", "fearful", "revenge", "bored"]
REASONS = ["fear", "uncertainty", "hesitation", "distraction", "not-at-desk",
           "didnt-see", "overtrading", "recent-loss", "conditions", "other"]
OPEN_TYPES = ["HOR", "LOR", "HIR", "LIR", "IR-IV", "HIR-IV", "LIR-IV"]
DAY_TYPES = [
    "Trend Day — Strong directional, one timeframe participant",
    "Normal Variation — Overlapping, two-sided with mild range extension",
    "Neutral / Rotational — Two-sided, balanced, no clear winner",
    "Outside Day — Traded both above and below prior range",
    "Gap and Go — Gap held, trend continued in gap direction",
    "Gap Fill — Gap faded, price returned into prior range",
]

# US market holidays in the window (no trades on these)
HOLIDAYS = {
    date(2025, 11, 27), date(2025, 12, 25), date(2026, 1, 1),
    date(2026, 1, 19), date(2026, 2, 16), date(2026, 4, 3),
}

START = date(2025, 11, 19)
END = date(2026, 5, 19)


def trading_days():
    days, d = [], START
    while d <= END:
        if d.weekday() < 5 and d not in HOLIDAYS:
            days.append(d)
        d += timedelta(days=1)
    return days


def weighted(pairs):
    pool = []
    for v, w in pairs:
        pool += [v] * w
    return random.choice(pool)


def price_region(instr, d):
    """Approx contract price, gently trending up over the 6 months + daily noise."""
    frac = (d - START).days / (END - START).days
    if instr in ("MES", "ES"):
        base = 5760 + 320 * frac + random.uniform(-45, 45)
        return round(base / 0.25) * 0.25
    base = 20250 + 1250 * frac + random.uniform(-220, 220)
    return round(base / 0.25) * 0.25


def risk_points(instr):
    if instr in ("MES", "ES"):
        return round(random.uniform(2.5, 8.0) / 0.25) * 0.25
    return round(random.uniform(18, 60) / 0.25) * 0.25


def contracts_for(instr):
    if instr == "MES":
        return random.randint(2, 8)
    if instr == "MNQ":
        return random.randint(2, 6)
    if instr == "ES":
        return random.randint(1, 3)
    return random.randint(1, 2)  # NQ


def round_tick(p):
    return round(p / 0.25) * 0.25


def split_contracts(n, parts):
    """Split n contracts into `parts` positive integers summing to n."""
    if parts <= 1 or n <= 1:
        return [n]
    cuts = sorted(random.sample(range(1, n), min(parts - 1, n - 1)))
    out, prev = [], 0
    for c in cuts:
        out.append(c - prev)
        prev = c
    out.append(n - prev)
    return out


def build_trade(tid, d, instr):
    p = PRESETS[instr]
    tick, tv, comm = p["tickSize"], p["tickValue"], p["commission"]
    dollar_per_pt = tv / tick
    n = contracts_for(instr)
    rpts = risk_points(instr)
    is_long = random.random() < 0.52
    entry = round_tick(price_region(instr, d))
    stop = round_tick(entry - rpts) if is_long else round_tick(entry + rpts)
    rpts = abs(entry - stop)
    if rpts == 0:
        stop = stop - tick if is_long else stop + tick
        rpts = abs(entry - stop)

    # Outcome model tuned for "slightly profitable":
    #   win ~50%, BE ~3%, loss ~47%; avg win ~+1.2R, avg loss ~-0.95R
    roll = random.random()
    scales = []
    if roll < 0.50:                      # WIN
        result_kind = "win"
        # Slightly-profitable scalper: average win ≈ average loss in R terms.
        # Most wins are small (RN + a scratch), rare modest runner. Mean ~0.80R.
        target_r = max(0.2, random.gauss(0.72, 0.32))
        if random.random() < 0.08:       # rare runner
            target_r += random.uniform(0.5, 1.5)
        target_r = round(min(target_r, 3.5), 2)
        nparts = 1 if n <= 2 else random.choice([2, 2, 3])
        qtys = split_contracts(n, nparts)
        # per-scale rMults: first ~1R (RN), later scales larger; tune mean→target
        rmults = []
        for i in range(len(qtys)):
            if i == 0:
                rmults.append(round(random.uniform(0.85, 1.15), 2))
            elif i == len(qtys) - 1:
                rmults.append(round(random.uniform(target_r + 0.3, target_r + 1.8), 2))
            else:
                rmults.append(round(random.uniform(1.4, 2.4), 2))
        # rescale so contract-weighted mean ≈ target_r
        wmean = sum(rm * q for rm, q in zip(rmults, qtys)) / n
        if wmean > 0:
            rmults = [round(rm * target_r / wmean, 2) for rm in rmults]
    elif roll < 0.535:                   # BREAK EVEN
        result_kind = "be"
        qtys = [n]
        rmults = [0.0]
    else:                                # LOSS
        result_kind = "loss"
        if random.random() < 0.70:       # clean full stop = -1R
            qtys = [n]
            rmults = [-1.0]
        else:                            # partial: small lock then stopped
            a = max(1, int(n * random.uniform(0.2, 0.35)))
            qtys = [a, n - a]
            rmults = [round(random.uniform(0.3, 0.7), 2), -1.0]

    # Build scale objects with app-faithful labels and exact price math
    total_pnl_pts = 0.0
    for i, (q, rm) in enumerate(zip(qtys, rmults)):
        pnl_pts_per = rpts * rm
        price = round_tick(entry + pnl_pts_per) if is_long else round_tick(entry - pnl_pts_per)
        # recompute from the tick-rounded price so the stored math is exact
        pnl_pts_per = (price - entry) if is_long else (entry - price)
        rm_exact = pnl_pts_per / rpts if rpts else 0.0
        if result_kind == "loss" and len(qtys) == 1 and rmults == [-1.0]:
            label = "Full Stop"
        elif i == 0:
            label = "Scale 1 (RN)"
        elif i == len(qtys) - 1:
            label = "Runner"
        else:
            label = "Scale " + str(i + 1)
        scales.append({
            "label": label,
            "price": round(price, 2),
            "qty": q,
            "pnlPts": round(pnl_pts_per, 2),
            "r": round(rm_exact, 4),
        })
        total_pnl_pts += pnl_pts_per * q

    total_pnl_pts = round(total_pnl_pts, 2)
    total_pnl_dollars = round(total_pnl_pts * dollar_per_pt)  # parseFloat(toFixed(0))
    total_r = round(total_pnl_pts / (rpts * n), 2) if rpts else 0.0
    result = "Win" if total_pnl_pts > 0.01 else ("Loss" if total_pnl_pts < -0.01 else "Break Even")
    got_rn = bool(scales) and scales[0]["r"] >= 0.9

    # session timing
    hh = random.choice([9, 9, 10, 10, 10, 11, 11, 12, 13, 14, 14, 15])
    mm = random.randint(0, 59)
    ampm = "AM" if hh < 12 else "PM"
    h12 = hh if hh <= 12 else hh - 12
    if h12 == 0:
        h12 = 12
    t_str = f"{h12}:{mm:02d} {ampm}"
    dur = random.choice([4, 7, 11, 14, 18, 23, 31, 42, 55, 68])
    em = (hh * 60 + mm) + dur
    eh, emin = (em // 60) % 24, em % 60
    e_ampm = "AM" if eh < 12 else "PM"
    eh12 = eh if eh <= 12 else eh - 12
    if eh12 == 0:
        eh12 = 12
    exit_t = f"{eh12}:{emin:02d} {e_ampm}"

    if result_kind == "win":
        proc = random.choice(["A", "A", "B", "B", "C"])
        srate = random.choice(["A", "A", "B", "B", "C"])
        emo = [random.choice(EMO_POS)]
        errs = [] if random.random() < 0.85 else [random.choice(["early-exit", "late-entry"])]
    elif result_kind == "loss":
        proc = random.choice(["B", "C", "C", "F"])
        srate = random.choice(["B", "C", "C", "F"])
        emo = [random.choice(EMO_NEG)] if random.random() < 0.6 else [random.choice(EMO_POS)]
        errs = [] if random.random() < 0.55 else random.sample(ERRORS, random.randint(1, 2))
    else:
        proc = random.choice(["B", "C"])
        srate = random.choice(["B", "C"])
        emo = [random.choice(EMO_POS + EMO_NEG)]
        errs = []

    dir_s = "long" if is_long else "short"
    bias = random.choice(["long", "short", "neutral"])
    trig = random.choice(LONG_TRIGGERS if is_long else SHORT_TRIGGERS)
    if bias == "neutral":
        trend_align = "neutral"
    elif bias == dir_s:
        trend_align = "with"
    else:
        trend_align = "counter"

    return {
        "id": tid,
        "date": d.isoformat(),
        "time": t_str,
        "setup": random.choice(SETUPS),
        "dir": dir_s,
        "entry": round(entry, 2),
        "stop": round(stop, 2),
        "contracts": n,
        "rPts": round(rpts, 2),
        "scales": scales,
        "totalPnlPts": total_pnl_pts,
        "totalPnlDollars": total_pnl_dollars,
        "totalR": total_r,
        "gotRN": got_rn,
        "result": result,
        "proc": proc,
        "setupRating": srate,
        "notes": "",
        "instrument": instr,
        "commission": comm,
        "tickValue": tv,
        "tickSize": tick,
        "openType": random.choice(OPEN_TYPES),
        "bias": bias,
        "trendAlign": trend_align,
        "trendContext": "",
        "triggerType": trig,
        "triggerLabel": TRIGGERS[trig],
        "errors": errs,
        "idealExit": None,
        "emotion": emo,
        "exitTime": exit_t,
        "duration": dur,
        "targets": [],
        "screenshots": [],
    }


def build_missed(tid, d, instr):
    p = PRESETS[instr]
    tick, tv, comm = p["tickSize"], p["tickValue"], p["commission"]
    dollar_per_pt = tv / tick
    n = contracts_for(instr)
    rpts = risk_points(instr)
    is_long = random.random() < 0.5
    entry = round_tick(price_region(instr, d))
    stop = round_tick(entry - rpts) if is_long else round_tick(entry + rpts)
    rpts = abs(entry - stop) or tick

    # A missed trade is a setup you didn't take — its hypothetical outcome must
    # follow a realistic distribution, NOT always a winner. Mix:
    #   ~48% would have won  (regret — should have taken it)
    #   ~7%  scratch / near-flat
    #   ~45% would have lost (good skip — dodged a stop-out)
    roll = random.random()
    if roll < 0.48:                       # missed a WINNER
        outcome_r = max(0.2, random.gauss(0.85, 0.45))
        if random.random() < 0.10:        # rare runner you missed
            outcome_r += random.uniform(0.5, 1.8)
        outcome_r = round(min(outcome_r, 4.0), 2)
        reason_pool = ["fear", "uncertainty", "hesitation", "distraction",
                       "not-at-desk", "didnt-see", "other"]
    elif roll < 0.55:                     # scratch
        outcome_r = round(random.uniform(-0.12, 0.15), 2)
        reason_pool = REASONS
    else:                                 # missed a LOSER (correctly skipped)
        if random.random() < 0.65:        # would have hit full stop
            outcome_r = -1.0
        else:                             # would have bled out partially
            outcome_r = round(random.uniform(-0.85, -0.4), 2)
        reason_pool = ["conditions", "overtrading", "recent-loss",
                       "uncertainty", "other"]

    # App-faithful missed-trade math (saveMissedTrade): totals are across ALL
    # contracts; missedR is the R-multiple; dollars use tickValue/tickSize.
    per_contract_pts = rpts * outcome_r
    target = (round_tick(entry + per_contract_pts) if is_long
              else round_tick(entry - per_contract_pts))
    per_contract_pts = (target - entry) if is_long else (entry - target)
    total_pts = round(per_contract_pts * n, 2)
    rs = random.sample(reason_pool, min(random.randint(1, 2), len(reason_pool)))
    hh = random.choice([9, 10, 10, 11, 13, 14])
    mm = random.randint(0, 59)
    ampm = "AM" if hh < 12 else "PM"
    h12 = hh if hh <= 12 else hh - 12
    return {
        "id": tid,
        "date": d.isoformat(),
        "time": f"{h12}:{mm:02d} {ampm}",
        "setup": random.choice(SETUPS),
        "dir": "long" if is_long else "short",
        "entry": round(entry, 2),
        "actual": None,
        "stop": round(stop, 2),
        "contracts": n,
        "scales": None,
        "missedPnlPts": total_pts,
        "missedPnlDollars": round(total_pts * dollar_per_pt),
        "missedR": round(total_pts / (rpts * n), 2) if rpts else 0.0,
        "reason": rs[0],
        "reasons": rs,
        "notes": "",
        "screenshots": [],
        "instrument": instr,
        "commission": comm,
        "tickValue": tv,
        "tickSize": tick,
        "bias": random.choice(["long", "short", "neutral"]),
        "openType": random.choice(OPEN_TYPES),
    }


def build_session(d, day_trades):
    net = sum(t["totalPnlDollars"] for t in day_trades)
    if net > 1:
        res = "Win"
    elif net < -1:
        res = "Loss"
    else:
        res = "Break Even"
    setups = sorted({t["setup"] for t in day_trades})
    bias = day_trades[0]["bias"]
    ot = day_trades[0]["openType"]
    proc = sorted([t["proc"] for t in day_trades])[len(day_trades) // 2]
    lessons = [
        "Stuck to the plan on the A setups; the C-rated entries are where the bleed is.",
        "Patience on the open paid off. Forced one mid-session trade that didn't need taking.",
        "Let a runner go further than usual and it worked. Keep trusting structure.",
        "Cut a loser fast instead of widening the stop. That is the habit to keep.",
        "Overtraded the chop after lunch. One and done would have been better.",
        "Bias was right but entry timing was late on two of these.",
    ]
    return {
        "date": d.isoformat(),
        "openType": ot,
        "bias": bias,
        "biasLog": [],
        "dayType": random.choice(DAY_TYPES),
        "result": res,
        "processRating": proc,
        "setups": setups,
        "responsive": random.choice([
            "Yes — Faded back into balance (responsive)",
            "No — Continued impulsive (non-responsive)",
            "N/A — In Range Open",
        ]),
        "ib": random.choice([
            "IBC Up — IBH extension, continuation higher",
            "IBF Down — Broke IBL, failed, came back inside",
            "In Balance — No IB extension either side",
        ]),
        "biasChange": "No — Bias held all day",
        "riskNeutral": random.choice([
            "Yes — Scaled to RN, held runner",
            "No — Full stop taken",
        ]),
        "checklistUsed": "Yes — All 7 conditions met before entry",
        "preflightDone": "Yes — All 8 questions answered",
        "levels": "",
        "notes": f"{len(day_trades)} trade(s). Net ${net:.0f}. Open read as {ot}.",
        "lesson": random.choice(lessons),
        "screenshots": [],
        "levelSnap": None,
        "hitsSnap": [],
        "preflightSnap": None,
        "savedAt": f"{d.isoformat()}T21:30:00.000Z",
    }


def main():
    days = trading_days()
    tid = 1763600000000  # base id (ms-ish), strictly increasing
    trades, sessions, missed = [], [], []

    # distribute ~300 trades across a subset of days (1–5 per active day)
    active_days = []
    while sum(c for _, c in active_days) < 300:
        d = random.choice(days)
        active_days.append((d, random.choice([1, 1, 2, 2, 3, 3, 4, 5])))
    # trim to exactly 300
    by_day = {}
    count = 0
    for d, c in sorted(active_days, key=lambda x: x[0]):
        if count >= 300:
            break
        take = min(c, 300 - count)
        by_day[d] = by_day.get(d, 0) + take
        count += take

    for d in sorted(by_day):
        day_trades = []
        for _ in range(by_day[d]):
            instr = weighted(INSTR_WEIGHTS)
            tid += random.randint(40000, 900000)
            tr = build_trade(tid, d, instr)
            trades.append(tr)
            day_trades.append(tr)
        sessions.append(build_session(d, day_trades))

    # ~40 missed trades on random trading days
    for _ in range(40):
        d = random.choice(days)
        instr = weighted(INSTR_WEIGHTS)
        tid += random.randint(40000, 900000)
        missed.append(build_missed(tid, d, instr))

    trades.sort(key=lambda t: (t["date"], t["id"]))
    sessions.sort(key=lambda s: s["date"], reverse=True)
    missed.sort(key=lambda m: (m["date"], m["id"]))

    backup = {
        "schemaVersion": 7,
        "logName": "Sample_Trader_2026",
        "sessions": sessions,
        "pmData": {"date": END.isoformat(), "customLevels": []},
        "checks": {},
        "fuelItems": [],
        "tradeLog": list(reversed(trades)),  # app stores newest-first
        "customSetups": [],
        "instrumentSettings": {"name": "MES", "tickSize": 0.25, "tickValue": 1.25, "commission": 0.62, "yahooTicker": "ES=F"},
        "journalDropdowns": None,
        "preflight": {},
        "stChecks": {},
        "bmMap": {
            "P Low": "pLow", "P High": "pHigh", "P VPOC": "pVPOC", "VAH": "pVAH",
            "VAL": "pVAL", "P Close": "pClose", "OP": "todayOpen", "ONH": "ONH",
            "ONL": "ONL", "ON POC": "ONVPOC", "IBH": "IBH_bm", "IBL": "IBL_bm",
            "Last": "_price", "Session High": "_high", "Session Low": "_low",
            "Session Open": "_open", "Prior Close": "_prevClose",
        },
        "bmUrl": "",
        "bmPriceUrl": "",
        "rthBuffer": 3,
        "missedTrades": missed,
        "dailyGoals": {"maxLoss": 500, "maxTrades": 6, "minProc": "B", "commission": 0},
        "customLabels": {
            "errors": {"hidden": [], "added": []},
            "emotions": {"hidden": [], "added": []},
            "reasons": {"hidden": [], "added": []},
            "triggers": {"hidden": [], "added": []},
            "setups": {"hidden": [], "added": []},
        },
        "perfThresholds": {},
        "exportedAt": END.isoformat() + "T22:00:00.000Z",
        "_sig": "sample-dataset-gen",
        "_app": "TraderLab101",
    }

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(backup, f, indent=2)

    wins = sum(1 for t in trades if t["result"] == "Win")
    losses = sum(1 for t in trades if t["result"] == "Loss")
    be = sum(1 for t in trades if t["result"] == "Break Even")
    gross_win = sum(t["totalPnlDollars"] for t in trades if t["totalPnlDollars"] > 0)
    gross_loss = sum(-t["totalPnlDollars"] for t in trades if t["totalPnlDollars"] < 0)
    fees = sum(t["commission"] * t["contracts"] for t in trades)
    net = sum(t["totalPnlDollars"] for t in trades)
    instr_mix = {}
    for t in trades:
        instr_mix[t["instrument"]] = instr_mix.get(t["instrument"], 0) + 1

    print(f"OUT: {OUT}")
    print(f"trades={len(trades)} sessions={len(sessions)} missed={len(missed)}")
    print(f"win/loss/be = {wins}/{losses}/{be}  win-rate={wins/len(trades)*100:.1f}%")
    print(f"gross win=${gross_win:,.0f}  gross loss=${gross_loss:,.0f}  "
          f"profit factor={gross_win/gross_loss:.2f}" if gross_loss else "n/a")
    print(f"gross net=${net:,.0f}  est fees=${fees:,.0f}  net after fees=${net-fees:,.0f}")
    print(f"instrument mix: {instr_mix}")
    print(f"date span: {trades[0]['date']} -> {trades[-1]['date']}")
    print(f"unique ids: {len(set(t['id'] for t in trades))}/{len(trades)}")
    mw = sum(1 for m in missed if m["missedPnlDollars"] > 0)
    ml = sum(1 for m in missed if m["missedPnlDollars"] < 0)
    ms = len(missed) - mw - ml
    mnet = sum(m["missedPnlDollars"] for m in missed)
    print(f"missed: would-win={mw} would-lose={ml} scratch={ms}  "
          f"net-if-all-taken=${mnet:,.0f}")


if __name__ == "__main__":
    main()
