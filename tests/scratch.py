import json

team = {
    "name": "Lahore Strikers",
    "owner": "Maliha",
    "player_ids": ["P1", "P2", "P3"],
}

text = json.dumps(team, indent=2)
print(text)

back_to_dict = json.loads(text)
print(len(back_to_dict["player_ids"]))  # Should print 3

from Maliha_dugout.matches import load_match, batter_runs

captain = "Babar Azam"       # Replace with your captain's exact name in the match data
vice_captain = "Shaheen Afridi"  # Replace with your vice-captain's name

for number in range(1, 5):
    match = load_match(f"data/matches/match_{number:02d}.json")
    cap_runs = batter_runs(match, captain)
    vc_runs = batter_runs(match, vice_captain)
    print(f"Match {number:02d} -> {captain}: {cap_runs} | {vice_captain}: {vc_runs}")