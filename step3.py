from Maliha_dugout.errors import InvalidTeamError
from Maliha_dugout.loader import load_players, load_teams
 
players = load_players("data/players.csv")
 
for team in load_teams("data/sample_teams.csv",
                       players):
    try:
        team.validate()
        print(f"{team.team_name}: LEGAL")
    except InvalidTeamError as error:
        print(f"{team.team_name}: {error}")
