The Dugout — Deliverable 1
Student: Maliha
Batch: LiveX Nano Degree, Batch 3
Course: Advanced Python for AI, Week 1

Overview
This project loads 142 PSL 2026 players from CSV, models players and fantasy teams with Python classes, checks league rules, and ranks teams by credits. It completes Part A and the B1–B4 programming tasks.

Run
Install Python 3, then from the repository root run:

python main.py
No third-party packages required.

Example output
Player pool: 142 players
Summary: 2 legal, 6 illegal out of 8 teams
LEAGUE TABLE (cheapest first)
Files
dugout/models.py: Player, FantasyTeam, League
dugout/rules.py: league limits, five original checks, duplicate check (B1)
dugout/loader.py: CSV loaders
data/players.csv: 142 player records
data/sample_teams.csv: 6 class teams and 2 deliberately invalid teams (B2)
data/my_team.csv: example XI for now; replace with the exact XI from your submitted form (B3)
main.py: output, rule checks, and cheapest-first league table (B4)
Important before submission
Replace data/my_team.csv with the XI you submitted on the class form. The current Aiza XI is a provisional example, not verified as your actual submission. Ensure your final XI is legal.
Confirm your name in this README and your team owner name.
Create a public GitHub repository and make at least 8 genuine commits over at least 2 different days with meaningful messages. This ZIP does not and cannot establish that history.
Push, clone the public repo into a fresh folder, run python main.py, and submit the repository URL via LiveX by Friday, 20 November 2026 at 11:59 pm PKT.
Be ready to explain selected lines of code at the demonstration.
# Week 2 data pack

Four new data files for Week 2. Unzip this folder and copy everything inside
`data/` into the `data/` folder of your own Dugout repository, next to
`players.csv`. Nothing here replaces a Week 1 file.

| File | First used in | What it holds |
|---|---|---|
| `data/bad_teams.csv` | Session 5 | Six teams, each breaking exactly one league rule |
| `data/bad_teams.json` | Session 6 | The same six teams, written as JSON |
| `data/good_teams.json` | Session 6 | Three legal teams, for testing the API |
| `data/matches/match_01.json` to `match_04.json` | Session 6 | Matches 1 to 4 of PSL 2026, ball by ball |

After copying, your `data/` folder should look like this:

```
data/
    players.csv
    my_team.csv
    sample_teams.csv
    bad_teams.csv
    bad_teams.json
    good_teams.json
    matches/
        match_01.json
        match_02.json
        match_03.json
        match_04.json
```

Then commit them:

```
git add data
git commit -m "Add Week 2 data: bad teams and the first four match files"
```

## About the match files

Each file is one complete PSL 2026 match as Cricsheet publishes it: the match
details, then every innings, over and delivery. The files are named by match
number; Cricsheet names them by its own match id.

## Data source

Match data from [Cricsheet](https://cricsheet.org), used under the Open Data
Commons Attribution License. Credit Cricsheet in your README.
