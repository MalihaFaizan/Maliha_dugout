"""Tell me which of my points.py functions are right yet.

    python check_points.py

Run it after every two or three functions. A function you have not started
reports "not written yet", which is not a failure, just a fact. Nothing in this
file is marked; it is here so that you are never guessing.
"""

import csv

import numpy as np

from Maliha_dugout.loader import load_players, load_teams
from Maliha_dugout.matches import load_match
from Maliha_dugout.tally import match_arrays, player_roles
import Maliha_dugout.points as pts

PASS, FAIL, TODO = "  ok  ", " WRONG", "  --  "
results = []


def check(name, got, want, note=""):
    """Compare one answer with the expected one and remember the verdict."""

    if got is None:
        results.append((TODO, name, "not written yet"))
        return
    try:
        if isinstance(want, float):
            ok = abs(float(got) - want) < 0.005
        elif isinstance(want, np.ndarray):
            ok = np.array_equal(np.asarray(got), want)
        else:
            ok = got == want
    except Exception as error:
        results.append((FAIL, name, f"raised {type(error).__name__}: {error}"))
        return
    if ok:
        results.append((PASS, name, note))
    else:
        results.append((FAIL, name, f"got {got!r}, expected {want!r}"))


def rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def arrays_for(innings_rows):
    """Turn the rows of one worked innings into the arrays points.py expects."""

    return (
        np.array([int(r["runs_off_bat"]) for r in innings_rows]),
        np.array([int(r["legal_ball"]) for r in innings_rows]),
        any(int(r["wicket"]) for r in innings_rows),
        innings_rows[0]["role"],
    )


def spell_arrays(spell_rows):
    return (
        np.array([int(r["runs_conceded"]) for r in spell_rows]),
        np.array([int(r["legal_ball"]) for r in spell_rows]),
        np.array([int(r["over"]) for r in spell_rows]),
    )


def safe(fn, *args):
    """Call a function; return None if it is still a stub or it blew up."""

    try:
        return fn(*args)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Session 9
# ---------------------------------------------------------------------------
innings = {}
for row in rows("data/worked_innings.csv"):
    innings.setdefault(row["innings_id"], []).append(row)
keys = {r["innings_id"]: r for r in rows("data/worked_innings_key.csv")}

runs, legal, out, role = arrays_for(innings["I1"])

check("total_runs", safe(pts.total_runs, runs), 106)
check("count_boundaries (fours)", safe(pts.count_boundaries, runs, 4), 7)
check("count_boundaries (sixes)", safe(pts.count_boundaries, runs, 6), 8)
check("balls_faced", safe(pts.balls_faced, legal), 56)
check("strike_rate", safe(pts.strike_rate, runs, legal), 189.29)
check("highest_bonus (106)", safe(pts.highest_bonus, 106, pts.RUNS_BONUS), 32)
check("highest_bonus (50)", safe(pts.highest_bonus, 50, pts.RUNS_BONUS), 16,
      "a 50 collects 16 and not 24")
check("highest_bonus (29)", safe(pts.highest_bonus, 29, pts.RUNS_BONUS), 0)

worm = safe(pts.innings_worm, runs)
check("innings_worm (last value)", None if worm is None else int(worm[-1]), 106)
check("innings_worm (length)", None if worm is None else len(worm), len(runs))

for iid in ("I4", "I5"):
    r, l, o, ro = arrays_for(innings[iid])
    want = iid == "I4"
    check(f"is_duck ({keys[iid]['batter']}, {ro})", safe(pts.is_duck, r, l, o, ro), want,
          "a bowler's duck is free" if iid == "I5" else "")

for iid in sorted(innings):
    r, l, o, ro = arrays_for(innings[iid])
    card = {"runs_off_bat": r, "legal_ball": l, "dismissed": o}
    check(f"batting_points ({iid} {keys[iid]['batter']})",
          safe(pts.batting_points, card, ro), int(keys[iid]["batting_points"]))

spells = {}
for row in rows("data/worked_spells.csv"):
    spells.setdefault(row["spell_id"], []).append(row)
skeys = {r["spell_id"]: r for r in rows("data/worked_spells_key.csv")}

for sid in sorted(spells):
    conceded, bowl_legal, bowl_over = spell_arrays(spells[sid])
    key = skeys[sid]
    card = {
        "conceded": conceded,
        "bowl_legal": bowl_legal,
        "bowl_over": bowl_over,
        "wickets_credited": int(key["wickets"]),
        "bowled_or_lbw": int(key["bowled_or_lbw"]),
    }
    check(f"overs_bowled ({sid})", safe(pts.overs_bowled, bowl_legal), float(key["overs_bowled"]))
    check(f"economy ({sid})", safe(pts.economy, conceded, bowl_legal), float(key["economy"]))
    check(f"maiden_overs ({sid} {key['bowler']})",
          safe(pts.maiden_overs, conceded, bowl_legal, bowl_over), int(key["maidens"]))
    check(f"bowling_points ({sid} {key['bowler']})",
          safe(pts.bowling_points, card), int(key["bowling_points"]))

check("fielding_points (2 catches, 1 run out)",
      safe(pts.fielding_points, {"catches": 2, "stumpings": 0, "run_outs": 1}), 22)

# ---------------------------------------------------------------------------
# Session 10
# ---------------------------------------------------------------------------
players = load_players("data/players.csv")
roles = player_roles(players)
expected = rows("data/expected_points.csv")

wrong = 0
checked = 0
first_bad = ""
scored_any = False

for number in range(5, 10):
    name = f"match_{number:02d}"
    match = load_match(f"data/matches/{name}.json")
    got = safe(pts.score_match, match, roles)
    if not got:
        continue
    scored_any = True
    for row in expected:
        if row["match"] != name:
            continue
        checked += 1
        mine = got.get(row["player"])
        want = int(row["total_points"])
        if mine is None or int(mine.get("total", -1)) != want:
            wrong += 1
            if not first_bad:
                have = "missing" if mine is None else mine.get("total")
                first_bad = f"{name} {row['player']}: got {have}, expected {want}"

if not scored_any:
    results.append((TODO, "score_match (matches 5-9)", "not written yet"))
elif wrong:
    results.append((FAIL, "score_match (matches 5-9)",
                    f"{wrong} of {checked} players wrong. First: {first_bad}"))
else:
    results.append((PASS, "score_match (matches 5-9)", f"all {checked} players correct"))

teams = safe(load_teams, "data/class_teams.csv", players)
season = [load_match(f"data/matches/match_{n:02d}.json") for n in range(1, 13)]
official = {r["owner"]: float(r["total_points"]) for r in rows("data/leaderboard_after_match12.csv")}

if teams:
    for team in teams:
        got = safe(pts.team_season_points, team, season, roles)
        total = None if not isinstance(got, dict) else got.get("total")
        check(f"team_season_points ({team.owner})", None if total is None else round(float(total), 1),
              official[team.owner])

# ---------------------------------------------------------------------------
print()
print("  Session 9 and 10 self-check")
print("  " + "-" * 68)
for verdict, name, note in results:
    print(f"  [{verdict}] {name}" + (f"   <- {note}" if note else ""))
print("  " + "-" * 68)
ok = sum(1 for v, _, _ in results if v == PASS)
bad = sum(1 for v, _, _ in results if v == FAIL)
todo = sum(1 for v, _, _ in results if v == TODO)
print(f"  {ok} right, {bad} wrong, {todo} not written yet, out of {len(results)}")
print()
