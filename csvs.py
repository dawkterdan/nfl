import nflgame


def home_passing_tds_in_year(year, player, team):
    avg = 0.0
    home_games = nflgame.games(year, home=team)
    players = nflgame.combine(home_games)
    this_player = players.name(player)
    avg += this_player.passing_tds
    print year, this_player, this_player.passing_tds, (avg / 8)

def home_passing_tds_in_range(start_year, end_year, player, team):
    for i in range(start_year, end_year):
        home_passing_tds_in_year(i, player, team)
        
def away_passing_tds_in_year(year, player, team):
    avg = 0.0
    away_games = nflgame.games(year, away=team)
    players = nflgame.combine(away_games)
    this_player = players.name(player)
    avg += this_player.passing_tds
    print year, this_player, this_player.passing_tds, (avg / 8)

def away_passing_tds_in_range(start_year, end_year, player, team):
    for i in range(start_year, end_year):
        away_passing_tds_in_year(i, player, team)

def home_rushing_tds_in_year(year, player, team):
    avg = 0.0
    home_games = nflgame.games(year, home=team)
    players = nflgame.combine(home_games)
    this_player = players.name(player)
    avg += this_player.rushing_tds
    print year, this_player, this_player.rushing_tds, (avg / 8)
    
def away_rushing_tds_in_year(year, player, team):
    avg = 0.0
    away_games = nflgame.games(year, home=team)
    players = nflgame.combine(away_games)
    this_player = players.name(player)
    avg += this_player.rushing_tds
    print year, this_player, this_player.rushing_tds, (avg / 8)

def home_rushing_tds_in_range(start_year, end_year, player, team):
    for i in range(start_year, end_year):
        home_rushing_tds_in_year(i, player, team)

def away_rushing_tds_in_range(start_year, end_year, player, team):
    for i in range(start_year, end_year):
        away_rushing_tds_in_year(i, player, team)

if __name__ == "__main__":
    
    print
    print "Flacco Home"
    print
    home_passing_tds_in_range(2009, 2015, "J.Flacco", "BAL")
    print
    print "Tannehill Home"
    print
    home_passing_tds_in_range(2012, 2015, "R.Tannehill", "MIA")
    print
    print "Wilson Home"
    print
    home_passing_tds_in_range(2012, 2015, "R.Wilson", "SEA")
    print
    print "Flacco Away"
    print
    away_passing_tds_in_range(2009, 2015, "J.Flacco", "BAL")
    print
    print "Tannehill Away"
    print
    away_passing_tds_in_range(2012, 2015, "R.Tannehill", "MIA")
    print
    print "Wilson Away"
    print
    away_passing_tds_in_range(2012, 2015, "R.Wilson", "SEA")
    print
    print "AP Home"
    print
    home_rushing_tds_in_range(2009, 2014, "A.Peterson", "MIN")
    print
    print "AP Away"
    print
    away_rushing_tds_in_range(2009, 2014, "A.Peterson", "MIN")
    print

    
