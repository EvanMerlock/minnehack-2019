class Farm:
    def __init__(self, name, id, loc, fields):
        self.__name = name
        self.__id = id
        self.__loc = loc
        self.__fields = fields

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


class FarmTemplate:
    def __init__(self, name, loc):
        self.__name = name
        self.__loc = loc

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__loc
