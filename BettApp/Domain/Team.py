class Team:
    def __init__(self, name, ratio):
        self.__name = name
        self.__ratio = ratio
        self.__form = self.get_form()

    def get_name(self):
        return self.__name

    def get_form(self):
        return self.__ratio[-1] + self.__ratio[-2] + self.__ratio[-3]

    def get_ration(self):
        return self.__ratio
