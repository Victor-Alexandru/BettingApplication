from Repository.Repository import Repository
from Domain.Bet_Ticket import Bet_Ticket
from Domain.Selected_Match import Selected_Match

from decimal import Decimal
import copy


class Controller:
    # we hold a storage reference
    # and we also make a list with the Bet_Tickets
    def __init__(self):
        self.__repo = Repository()
        self.__resulting_tickets = []
        self.init_Strategies()

    def init_Strategies(self):
        # this function will add into the resulting_tickets the tickets
        # which are obtained following the strategies
        self.trebleStrategy()

    def get_storage(self):
        return self.__repo.getStorage()

    def preety_print(self):
        self.__repo.print_all_storage()

    def trebleStrategy(self):
        # we make the list for the trebleStrategy 1/4 1/5 1/6
        one_to_six = []
        one_to_five = []
        one_to_four = []
        for item in self.get_storage():
            # print(item.get_odds())
            for key, value in item.get_odds().items():
                selected_match = Selected_Match(item.toString(), key, value)
                if Decimal(float(value)) == 1.17:
                    one_to_six.append(selected_match)

                elif Decimal(float(value)) == 1.20:
                    one_to_five.append(selected_match)

                elif Decimal(float(value)) == 1.25:
                    one_to_four.append(selected_match)

        for index in range(0, min(len(one_to_six), len(one_to_five), len(one_to_four))):
            current_ticket = Bet_Ticket()
            current_ticket.addMatch(one_to_four[index])
            current_ticket.addMatch(one_to_five[index])
            current_ticket.addMatch(one_to_six[index])

            self.__resulting_tickets.append(current_ticket)

    def get_Betting_Tickets(self):
        return self.__resulting_tickets
