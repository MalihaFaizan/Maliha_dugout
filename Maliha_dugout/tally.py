"""Walking a match file and tallying what each player did.

GIVEN TO YOU. You do not write this module and it is not part of Deliverable 3.

Everything in here is the skill you already proved in Session 6: open a match
file, loop through innings, overs and deliveries, and pull out what you need.
There is nothing new in it. It is long because a cricket match has a lot of
corners, not because it is hard.

What it gives you is one dict per player, holding plain NumPy arrays and a few
counts. Your job in points.py is to turn those numbers into fantasy points.

    from dugout.tally import match_arrays
    from dugout.matches import load_match

    match = load_match("data/matches/match_07.json")
    cards = match_arrays(match)
    farhan = cards["Sahibzada Farhan"]
    print(farhan["runs_off_bat"])      # array([0, 4, 1, 6, ...])
    print(farhan["runs_off_bat"].sum())

Every key is described in blank_card() below. Read that first.
"""

import numpy as np

# The dismissals the laws credit to the bowler. A run out is nobody's wicket,
# which is the mistake that costs the most marks in Deliverable 3.
BOWLER_WICKETS = {
    "bowled",
    "caught",
    "caught and bowled",
    "lbw",
    "stumped",
    "hit wicket",
}


def blank_card():
    """One player's record for one match, before anything has been added.

    Batting, one entry per ball bowled to this player:
        runs_off_bat   runs the bat scored off that ball (extras are not here)
        legal_ball     1 if the ball counts as a ball faced, 0 for a wide or no-ball
        dismissed      True if this player was out in this match

    Bowling, one entry per ball this player bowled:
        conceded       runs charged to the bowler off that ball
                       (off the bat, plus wides and no-balls; byes and leg byes
                        are the keeper's fault, not the bowler's)
        bowl_legal     1 if the ball was legal, 0 for a wide or no-ball
        bowl_over      which over the ball belonged to, so maidens can be found

    Bowling counts:
        wickets_credited   wickets the laws give this bowler
        bowled_or_lbw      how many of those were bowled or lbw

    Fielding counts:
        catches, stumpings, run_outs
    """

    return {
        "runs_off_bat": [],
        "legal_ball": [],
        "dismissed": False,
        "conceded": [],
        "bowl_legal": [],
        "bowl_over": [],
        "wickets_credited": 0,
        "bowled_or_lbw": 0,
        "catches": 0,
        "stumpings": 0,
        "run_outs": 0,
    }


def match_arrays(match):
    """Return a dict of player name -> card, with the list fields as NumPy arrays.

    Super overs are skipped: the league rules do not count them.
    """

    cards = {}

    def card(name):
        """Return this player's card, creating a blank one the first time."""

        if name not in cards:
            cards[name] = blank_card()
        return cards[name]

    for innings in match["innings"]:
        if innings.get("super_over"):
            continue

        for over in innings["overs"]:
            for delivery in over["deliveries"]:
                extras = delivery.get("extras", {})
                wides = extras.get("wides", 0)
                noballs = extras.get("noballs", 0)
                is_legal = 1 if (wides == 0 and noballs == 0) else 0

                off_the_bat = delivery["runs"]["batter"]

                # --- the batter ---
                batter = card(delivery["batter"])
                batter["runs_off_bat"].append(off_the_bat)
                batter["legal_ball"].append(is_legal)

                # --- the bowler ---
                bowler = card(delivery["bowler"])
                bowler["conceded"].append(off_the_bat + wides + noballs)
                bowler["bowl_legal"].append(is_legal)
                bowler["bowl_over"].append(over["over"])

                # --- anything that fell ---
                for wicket in delivery.get("wickets", []):
                    kind = wicket["kind"]
                    card(wicket["player_out"])["dismissed"] = True

                    if kind in BOWLER_WICKETS:
                        bowler["wickets_credited"] += 1
                        if kind in ("bowled", "lbw"):
                            bowler["bowled_or_lbw"] += 1

                    fielders = [
                        f["name"] for f in wicket.get("fielders", []) if "name" in f
                    ]

                    if kind in ("caught", "caught and bowled"):
                        # A caught and bowled has no fielder listed: it is the bowler
                        catcher = fielders[0] if fielders else delivery["bowler"]
                        card(catcher)["catches"] += 1
                    elif kind == "stumped" and fielders:
                        card(fielders[0])["stumpings"] += 1
                    elif kind == "run out" and fielders:
                        # The league rules credit one fielder, so take the first named
                        card(fielders[0])["run_outs"] += 1

    # Lists were easy to build one ball at a time. Arrays are what you want to
    # do maths on, so convert them once, here, at the end.
    for record in cards.values():
        for field in ("runs_off_bat", "legal_ball", "conceded", "bowl_legal", "bowl_over"):
            record[field] = np.array(record[field], dtype=int)

    return cards


def player_roles(players):
    """Return a dict of player name -> role, built from the loaded player pool.

    score_match() needs this because the duck penalty does not apply to bowlers,
    and the player pool is keyed by id while a match file names people.
    """

    return {player.name: player.role for player in players.values()}
