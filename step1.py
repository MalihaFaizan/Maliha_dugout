
from Maliha_dugout.loader import load_players
from Maliha_dugout.models import find_player
 
players = load_players("data/players.csv")
 
print(find_player(players, "P089"))
print(find_player(players, "P999"))
