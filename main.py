class Player:
    # constructor
    def __init__(self, player_id, name, role, franchise, credits):
        self.player_id = player_id
        self.name = name
        self.role = role            # WK, AT, AR or BOWL
        self.franchise = franchise  # price in the fantasy game
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits}cr)"

#Creating the 5 players including Babar

babar = Player("P089", "Babar Azam", "BAT", "Peshawar Zalmi", 10.5)
Mohommad_Haris = Player("P087", "Mohommad Haris", "WK", "Peshawar Zalmi", 7.5)
Iftikhar_Ahmed = Player("PO94", "Iftikhar Ahmed", "AR", "Peshawar Zalmi" , 7.5)
Shaheen_Shah_Afridi = Player("PO68", "Shaheen Shah Afridi", "BOWL", "Lahore Qalandars" , 10.5)
Shan_Masood = Player("PO76", "Shan Masood", "BAT", "Multan Sultans" , 6.0)
             
class FantasyTeam:
    """A fantasy XI picked by one person"""

    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None

    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
        total=0
        for p in self.players:
            total = total + p.credits
        return total

    def count_by_role(self):
        counts = {"WK" :0, "BAT": 0, "AR": 0, "BOWL":0}
        for p in self.players:
            counts[p.role] = counts[p.role] + 1
        return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain

    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"

    # Create your 11 players
rizwan = Player("P122", "Mohammad Rizwan", "WK", "Rawalpindiz", 10.5)
babar = Player("P089", "Babar Azam", "BAT", "Peshawar Zalmi", 10.5)
warner= Player("P037", "DA Warner",  "BAT", "Karachi Kings", 9.5)
shan = Player("P076", "Shan Masood", "BAT", "Multan Sultans", 6.0)
haider = Player("P021", "Haider Ali", "BAT", "Islamabad United", 6.0)
iftikhar = Player("P094", "Iftikhar Ahmed", "AR", "Peshawar Zalmi", 7.5)
shadab = Player("P029", "Shadab Khan", "AR", "Islamabad United", 10.5)
shaheen = Player("P068", "Shaheen Shah Afridi", "BOWL", "Lahore Qalandars", 10.5)
haris = Player("P066", "Haris Rauf", "BOWL", "Lahore Qalandars", 7.5)
naseem = Player("P140", "Naseem Shah", "BOWL", "Rawalpindiz", 8.0)
hasnain = Player("P031", "Mohammad Hasnain", "BOWL", "Islamabad United", 6.0)

    # Build your team
team=FantasyTeam("YorkerKings", "Maliha")
team.add_player(rizwan)
team.add_player(babar)
team.add_player(warner)
team.add_player(shan)
team.add_player(haider)
team.add_player(iftikhar)
team.add_player(shadab)
team.add_player(shaheen)
team.add_player(haris)
team.add_player(naseem)
team.add_player(hasnain)

    # Set Captain and Vice_Captain
team.set_captain(babar, shaheen)

    # Print output
print(team)
print("Roles:" , team.count_by_role())
print("Captain:", team.captain)