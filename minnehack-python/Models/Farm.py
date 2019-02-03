class Farm:
    def __init__(self, name, ID, loc, fields):
        self.__name = name
        self.__ID = ID
        self.__loc = loc
        self.__fields = fields

    def get_name(self):
        return self.__name

    def get_ID(self):
        return self.__ID

    def get_loc(self):
        return self.__loc

    def get_fields(self):
        return self.__fields

    def get_croptypes(self):
        pass



