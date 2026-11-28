"""Fantasy scoring with NumPy.

DELIVERABLE 3. Every function in this file is yours to write. They arrive with
their name, their docstring and the word pass, and pass is the only line you
have to delete.

Work down the file in order. Each function is small, each one has an expected
answer you can check, and each one is used by the one below it. Run
    python check_points.py
after every two or three functions. It tells you which ones are right.

The scoring rules are the frozen course rules. They are on the Fantasy rules
sheet and repeated here so you never have to go and look:

    Batting   1 point per run
              +1 per four, +2 per six
              bonus +8 at 30 runs, +16 at 50, +32 at 100 (the highest one only)
              -2 for a duck, unless the player's role is BOWL
    Bowling   25 per wicket (run outs are not the bowler's wicket)
              +8 if the wicket was bowled or lbw
              +12 per maiden over
              haul bonus +4 at 3 wickets, +8 at 4, +16 at 5 (the highest only)
    Fielding  8 per catch, 12 per stumping, 6 per run out
    Captain   points x 2        Vice-captain   points x 1.5
    Excluded  super overs; wides and no-balls are not balls faced
"""

import numpy as np

# The bonus tables, biggest first, so the first one that fits is the highest.
RUNS_BONUS = [(100, 32), (50, 16), (30, 8)]
HAUL_BONUS = [(5, 16), (4, 8), (3, 4)]

CAPTAIN_MULTIPLIER = 2.0
VICE_CAPTAIN_MULTIPLIER = 1.5


# ---------------------------------------------------------------------------
# Session 9, part 1: four things an array can tell you
# ---------------------------------------------------------------------------

def total_runs(runs_off_bat):
    """Return the total runs scored off the bat."""
    return int(np.asarray(runs_off_bat).sum())


def count_boundaries(runs_off_bat, value):
    """Return how many balls went for exactly `value` runs off the bat."""
    return int((np.asarray(runs_off_bat) == value).sum())


def balls_faced(legal_ball):
    """Return the number of balls faced."""
    return int(np.asarray(legal_ball).sum())


def strike_rate(runs_off_bat, legal_ball):
    """Return runs per 100 balls faced, rounded to 2 decimal places."""
    faced = balls_faced(legal_ball)
    if faced == 0:
        return 0.0
    runs = total_runs(runs_off_bat)
    return round((runs / faced) * 100, 2)


# ---------------------------------------------------------------------------
# Session 9, part 2: the batting rules
# ---------------------------------------------------------------------------

def highest_bonus(value, table):
    """Return the largest bonus the value has earned, or 0 if it earned none."""
    for threshold, bonus in table:
        if value >= threshold:
            return bonus
    return 0


def is_duck(runs_off_bat, legal_ball, dismissed, role):
    """Return True if this innings is a duck that costs the player 2 points."""
    return bool(
        dismissed
        and total_runs(runs_off_bat) == 0
        and balls_faced(legal_ball) >= 1
        and role != "BOWL"
    )


def batting_points(card, role):
    """Return the batting points in one tally card."""
    runs_off_bat = card["runs_off_bat"]
    legal_ball = card["legal_ball"]
    dismissed = card["dismissed"]

    runs = total_runs(runs_off_bat)
    fours = count_boundaries(runs_off_bat, 4)
    sixes = count_boundaries(runs_off_bat, 6)
    bonus = highest_bonus(runs, RUNS_BONUS)
    duck_penalty = -2 if is_duck(runs_off_bat, legal_ball, dismissed, role) else 0

    return runs + fours + (2 * sixes) + bonus + duck_penalty


# ---------------------------------------------------------------------------
# Session 9, part 3: the bowling rules
# ---------------------------------------------------------------------------

def overs_bowled(bowl_legal):
    """Return the number of overs bowled, as a number such as 3.5."""
    return np.asarray(bowl_legal).sum() / 6


def economy(conceded, bowl_legal):
    """Return runs conceded per over, rounded to 2 decimal places."""
    legal = int(np.asarray(bowl_legal).sum())
    if legal == 0:
        return 0.0
    overs = legal / 6
    runs_conceded = int(np.asarray(conceded).sum())
    return round(runs_conceded / overs, 2)


def maiden_overs(conceded, bowl_legal, bowl_over):
    """Return how many maiden overs this bowler bowled."""
    conceded_arr = np.asarray(conceded)
    legal_arr = np.asarray(bowl_legal)
    over_arr = np.asarray(bowl_over)

    maidens = 0
    for over_num in np.unique(over_arr):
        mask = over_arr == over_num
        if conceded_arr[mask].sum() == 0 and legal_arr[mask].sum() >= 6:
            maidens += 1
    return maidens


def bowling_points(card):
    """Return the bowling points in one tally card."""
    wickets = int(np.asarray(card["wickets_credited"]).sum())
    bowled_lbw = int(np.asarray(card["bowled_or_lbw"]).sum())
    maidens = maiden_overs(
        card["conceded"], card["bowl_legal"], card["bowl_over"]
    )
    haul = highest_bonus(wickets, HAUL_BONUS)

    return (25 * wickets) + (8 * bowled_lbw) + (12 * maidens) + haul


def fielding_points(card):
    """Return the fielding points in one tally card."""
    catches = card.get("catches", 0)
    stumpings = card.get("stumpings", 0)
    run_outs = card.get("run_outs", 0)
    return (8 * catches) + (12 * stumpings) + (6 * run_outs)


def innings_worm(runs_off_bat):
    """Return the running total of the innings, ball by ball, as an array."""
    return np.cumsum(np.asarray(runs_off_bat))


# ---------------------------------------------------------------------------
# Session 10: the points engine
# ---------------------------------------------------------------------------

def card_points(card, role):
    """Return everything one player earned in one match, as a dict."""
    bat_pts = batting_points(card, role)
    bowl_pts = bowling_points(card)
    field_pts = fielding_points(card)
    total = bat_pts + bowl_pts + field_pts

    return {
        "batting": bat_pts,
        "bowling": bowl_pts,
        "fielding": field_pts,
        "total": total,
        "role": role,
    }


def score_match(match, roles):
    """Return a dict of player name -> the dict that card_points returns."""
    from Maliha_dugout.tally import match_arrays

    cards = match_arrays(match)
    result = {}
    for player_name, card in cards.items():
        role = roles.get(player_name, "BAT")
        result[player_name] = card_points(card, role)
    return result


def multiplier_for(player, team):
    """Return 2.0 if this player is the team's captain, 1.5 if vice, else 1.0."""
    player_name = getattr(player, "name", player)
    captain_name = getattr(team.captain, "name", team.captain) if team.captain else None
    vice_name = (
        getattr(team.vice_captain, "name", team.vice_captain)
        if team.vice_captain
        else None
    )

    if captain_name is not None and player_name == captain_name:
        return CAPTAIN_MULTIPLIER
    if vice_name is not None and player_name == vice_name:
        return VICE_CAPTAIN_MULTIPLIER
    return 1.0


def team_match_points(team, match, roles):
    """Return what one fantasy team scored in one match."""
    match_scores = score_match(match, roles)
    players_out = []
    total_points = 0.0

    for player in team.players:
        name = getattr(player, "name", player)
        base = match_scores[name]["total"] if name in match_scores else 0
        mult = multiplier_for(player, team)
        pts = base * mult
        total_points += pts
        players_out.append({
            "name": name,
            "base": base,
            "multiplier": mult,
            "points": pts,
        })

    return {
        "total": total_points,
        "players": players_out,
    }


def team_season_points(team, matches, roles):
    """Return what one fantasy team has scored across several matches."""
    per_match = [
        team_match_points(team, match, roles)["total"] for match in matches
    ]
    return {
        "total": sum(per_match),
        "per_match": per_match,
    }
