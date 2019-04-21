class Bet_Ticket:
    # Bet_Ticket holds the Selected matches and total odd of the Ticket
    def __init__(self):
        self.__ticket_matches = []
        self.__ticket_odd = self.set_ticket_odd()

    def addMatch(self, match):
        self.__ticket_matches.append(match)
        self.set_ticket_odd()

    def set_ticket_odd(self):
        if not self.__ticket_matches:
            self.__ticket_odd = 1
        else:
            result_odd = 1
            for match in self.__ticket_matches:
                result_odd *= float(match.getOddNumber())

            self.__ticket_odd = result_odd

    def __str__(self):
        pString = "\n"
        for match in self.__ticket_matches:
            pString += match.toString() + "\n"
        pString += str(self.__ticket_odd)
        return pString
