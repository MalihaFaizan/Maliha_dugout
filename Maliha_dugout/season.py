"""Asking questions of a whole season with pandas.

DELIVERABLE 3. Every function here is yours to write.

The data is data/deliveries.csv: last season's PSL, every ball of it, one row
per ball, 7,672 rows. It is last season rather than this one on purpose. This
season is still being played and the leaderboard would be spoiled; last season
is finished, which is exactly what you want when you are looking for the
players who are worth their credits.

The columns, once:

    match_id        M01 to M34
    date            the day it was played
    venue           one of four grounds
    innings         1 or 2
    batting_team, bowling_team
    over            0 to 19. Cricsheet numbers overs from 0, not 1
    ball_in_over    1, 2, 3 ... and more than 6 when there were wides
    batter, bowler, non_striker
    runs_off_bat    runs the bat scored
    extras          every extra on that ball added together
    wides, noballs, byes, legbyes    the extras, split out
    total_runs      runs_off_bat + extras: what went on the scoreboard
    legal_ball      1 if the ball counted, 0 for a wide or a no-ball
    wicket_kind     "bowled", "caught", "run out" ... empty if nobody was out
    player_out      who was out, empty if nobody was
    fielder         the fielder credited, empty if there was none

Most rows have nothing in wicket_kind, player_out and fielder, so pandas reads
those three as missing values. That is correct and you should expect it.

Run
    python season.py
to see your answers. The expected answers are in the handout, section 3.7.
"""

import pandas as pd


def load_deliveries(path="data/deliveries.csv"):
    """Return the deliveries file as a DataFrame.

    One line. The three text columns that are usually empty should come back as
    empty strings rather than missing values, because every function below asks
    questions like wicket_kind != "", and a missing value answers no question
    truthfully. Fill them when you load, not later, in every function.
    """

    pass


def add_flags(deliveries):
    """Return the DataFrame with four new True/False columns added.

        is_four     the ball went for four off the bat
        is_six      the ball went for six off the bat
        is_wicket   somebody was out on that ball
        is_dot      nothing at all was scored off that ball

    A dot ball is one where total_runs is 0, not where runs_off_bat is 0: a ball
    that went for a leg bye was not a dot. Getting this wrong changes the answer
    to question 2 by about four hundred.

    Add the columns to a copy and return it, so that calling this function twice
    cannot do anything strange.
    """

    pass


def most_sixes(deliveries, how_many=5):
    """Return the batters who hit the most sixes, as a Series of name -> count.

    Highest first, how_many of them. Two lines: pick the rows that were sixes,
    then count the values in the batter column.
    """

    pass


def most_dot_balls(deliveries, how_many=5):
    """Return the bowlers who bowled the most dot balls, as a Series.

    Same shape as most_sixes, one column different. Bowling dots is the whole
    job of a death bowler and it is worth no fantasy points at all, which is
    worth saying out loud in class.
    """

    pass


def highest_scoring_venue(deliveries):
    """Return a DataFrame of venue -> runs, matches and runs per match.

    Four grounds, so four rows. Index by venue, with these columns:

        total_runs      every run scored there, extras included
        matches         how many matches were played there
        runs_per_match  total_runs divided by matches, rounded to 1 decimal

    Sort by runs_per_match, highest first. The total on its own is not an
    answer: one ground hosted far more matches than the others, so of course it
    has more runs. This is the function where that lesson lands.
    """

    pass


def run_rate_by_phase(deliveries):
    """Return the run rate in each phase of the innings, as a Series.

        powerplay   overs 0 to 5
        middle      overs 6 to 14
        death       overs 15 to 19

    Run rate is runs per over: total_runs added up, divided by the legal balls,
    times six. Round to 2 decimals. Index the Series with those three names in
    that order, so it prints in the order the innings is actually played.

    Remember that overs are numbered from 0, so the powerplay is over < 6.
    """

    pass


def strike_rates(deliveries, min_balls=200):
    """Return a DataFrame of batter -> runs, balls faced and strike rate.

    Only batters who faced at least min_balls, so that a number eleven who hit
    one six off his only ball does not come top with a strike rate of 600.
    Sort by strike rate, highest first, and round it to 2 decimals.

    Columns: runs, balls_faced, strike_rate.
    """

    pass


def wickets_by_bowler(deliveries, how_many=5):
    """Return the leading wicket-takers, as a Series of name -> wickets.

    Only the dismissals the laws credit to the bowler count, and the list of
    those is dugout.tally.BOWLER_WICKETS. Import it rather than typing the six
    strings again: it is one fact and it should live in one place.

    A run out is in the file as a wicket and must not be in your answer.
    """

    pass


def main():
    """Print the answer to each question, with a heading, so the output reads.

    Load the file once at the top and pass it down. Loading a 7,672-row CSV
    eight times is not slow enough to notice here, and it is still the wrong
    habit.
    """

    pass


if __name__ == "__main__":
    main()
