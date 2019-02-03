class Field:
    def __init__(self, name, farm, blocks):
        self.__name = name
        self.__farm = farm
        self.__blocks = blocks

    def get_name(self):
        return self.__name

    def get_farm(self):
        return self.__farm

    def get_blocks(self):
        return self.__blocks()


class FieldTemplate:
    def __init__(self, name, farm_id):
        self.__name = name
        self.__farm_id = farm_id

    def get_name(self):
        return self.__name

    def get_farm_id(self):
        return self.__farm_id
