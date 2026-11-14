class player:
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

babar = player("P089", "Babar Azam", "BAT", "Peshawar Zalmi", 10.5)
Mohommad_Haris = player("P087", "Mohommad Haris", "WK", "Peshawar Zalmi", 7.5)
Iftikhar_Ahmed = player("PO94", "Iftikhar Ahmed", "AR", "Peshawar Zalmi" , 7.5)
Shaheen_Shah_Afridi = player("PO68", "Shaheen Shah Afridi", "BOWL", "Lahore Qalandars" , 10.5)
Shan_Masood = player("PO76", "Shan Masood", "BAT", "Multan Sultans" , 6.0)

for player in [babar,Mohommad_Haris,Iftikhar_Ahmed,Shaheen_Shah_Afridi,Shan_Masood]:
    print(player)


