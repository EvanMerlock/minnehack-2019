class Farm:
    def __init__(self, name, id, loc, fields, profit):
        self.__name = name
        self.__id = id
        self.__loc = loc
        self.__fields = fields
        self.__profit = profit

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_loc(self):
        return self.__loc

    def get_fields(self):
        return self.__fields()

    def get_crop_types(self):
        pass

    def get_profit(self):
        return self.__profit


class FarmTemplate:
    def __init__(self, name, loc):
        self.__name = name
        self.__loc = loc

    def get_name(self):
        return self.__name

    def get_location(self):
        return "(" + self.__loc[0] + ", " + self.__loc[1] + ")1"
