from Maliha_dugout.loader import (
    load_players,
    load_team,
    save_teams_json,
    load_teams_json,
)

players = load_players("data/players.csv")
team = load_team("data/my_team.csv", players)

save_teams_json("data/teams.json", [team])

# now pretend the program closed and started again
again = load_teams_json("data/teams.json", players)[0]
print(again.team_name, again.total_credits(), len(again.players))