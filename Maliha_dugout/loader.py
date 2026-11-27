import csv
import json 

from Maliha_dugout.models import FantasyTeam, Player


def load_players(path):
    """Read a player CSV and return the players indexed by ID."""
    players = {}
    with open(path, newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players


def team_from_row(row, players):
    team = FantasyTeam(row["team_name"], row["owner"])
    for player_id in row["players"].split(";"):
        team.add_player(players[player_id.strip()])

    team.set_captain(
        players[row["captain"].strip()],
        players[row["vice_captain"].strip()],
    )
    return team


def load_team(path, players):
    """Return the first team in a team CSV, or None if it has no rows."""
    with open(path, newline="", encoding="utf-8-sig") as file:
        for row in csv.DictReader(file):
            return team_from_row(row, players)
    return None


def load_teams(path, players):
    """Return every team in a team CSV."""
    with open(path, newline="", encoding="utf-8-sig") as file:
         return [team_from_row(row, players) for row in csv.DictReader(file)]
    

def read_team_rows(path):
    """Return the raw rows of a teams CSV file, without building any teams."""
 
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def read_team_entries(path):
    """Return the raw entries of a teams JSON file, without building any teams."""

    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_teams_json(path, teams):
    """Write a list of FantasyTeams to a JSON file."""

    data = [team.to_dict() for team in teams]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_teams_json(path, players):
    """Return a list of FantasyTeams read from a JSON file."""

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return [FantasyTeam.from_dict(entry, players) for entry in data]

