class Selected_Match:
    def __init__(self,match_string,odd_type,odd_number):
        self.__name = match_string
        self.__odd_type = odd_type
        self.__odd_number= odd_number

    def getName(self):
        return  self.__name

    def getOddType(self):
        return self.__odd_type


    def getOddNumber(self):
        return self.__odd_number

    def toString(self):
        return self.__name + " " + self.__odd_type + " " + self.__odd_number

    def __str__(self):
        return self.__name + " " + self.__odd_type + " " + self.__odd_number
