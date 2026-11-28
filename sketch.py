from Maliha_dugout.matches import load_match
from Maliha_dugout.tally import match_arrays
 
match = load_match('data/matches/match_07.json')
cards = match_arrays(match)
 
farhan = cards['Sahibzada Farhan']
print(farhan['runs_off_bat'])
print(farhan['legal_ball'].sum())
print(farhan['dismissed'])
