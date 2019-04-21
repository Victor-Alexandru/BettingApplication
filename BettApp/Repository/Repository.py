from Domain.Match import Match

class Repository:
    def __init__(self):
        self.__All_Matches = set([])
        self.betting_odds = ["1", "X", "2", "1X", "X2", "12", "first_half_or_final 1", "first_half_or_final X",
                             "first_half_or_final 2"]
        self.read_from_file()

    def updateMatches(self):
        """
        We update the Repository List
        We can  have the matches hard-coded
        stored in a file or in a database
        """
        pass

    def read_from_file(self):
        count = 0
        # making an auxilliary match object

        input_match = Match("default", "default", "default", "Friday 15.02.2019")

        with open("input.txt") as file:
            for line in file:

                if count % 3 == 0:
                    input_match.set_home_team(line.strip())
                elif count % 3 == 1:
                    input_match.set_away_team(line.strip())
                elif count % 3 == 2:
                    match_odds = line.strip().split()
                    for i in range(0, len(match_odds)):
                        match_odds[i] = match_odds[i].replace(",", ".")
                        match_odds[i] = '1' if match_odds[i] == '-' else match_odds[i]


                    auxiliary_odds = {
                        "1": match_odds[0],
                        "X": match_odds[1],
                        "2": match_odds[2],
                        "1X": match_odds[3],
                        "X2": match_odds[4],
                        "12": match_odds[5],
                        "first_half_or_final 1": match_odds[10],
                        "first_half_or_final X": match_odds[11],
                        "first_half_or_final 2": match_odds[12],

                    }
                    input_match.set_odds(auxiliary_odds)
                    self.add_Match(input_match)
                    input_match = Match("default", "default", "default", "Friday 15.02.2019")
                count += 1

    def add_Match(self, match):
        """
        Adding a match into the storage list
        """
        self.__All_Matches.add(match)

    def getStorage(self):
        return self.__All_Matches

    def print_all_storage(self):
        for match in self.getStorage():
            print(match)
