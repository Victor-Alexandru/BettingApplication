class Match:
    def __init__(self, h_team, a_team, odds, date):
        self.__h_team = h_team
        self.__a_team = a_team
        self.__odds = odds
        self.__date = date

    def set_home_team(self, h_team):
        self.__h_team = h_team

    def set_away_team(self, a_team):
        self.__a_team = a_team

    def set_odds(self, odds):
        self.__odds = odds

    def get_odds(self):
        return self.__odds

    def get_home_team(self):
        return self.__h_team

    def get_away_team(self):
        return self.__a_team

    def get_match_date(self):
        return self.__date

    def toString(self):
        return self.__h_team + " vs " + self.__a_team

    def __str__(self):
        return self.__h_team + " vs " + self.__a_team  # +  # "  ODDS:  " + str(self.__odds)

    def __repr__(self):
        return self.__h_team + " vs " + self.__a_team  # +  # "  ODDS:  " + str(self.__odds)

# return ' '.join([num for num in dir(self)])
