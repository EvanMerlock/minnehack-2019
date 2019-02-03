class Farm:
    def __init__(self, name, ID, loc, fields, profitable, profit):
        self.__name = name
        self.__ID = ID
        self.__loc = loc
        self.__fields = fields
        self.__profitable = profitable
        self.__profit = profit

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_loc(self):
        return self.__loc

    def get_fields(self):
        return self.__fields

    def get_profitable(self):
        return self.__profitable

    def get_profit(self):
        return self.__profit

    def get_croptypes(self):
        pass