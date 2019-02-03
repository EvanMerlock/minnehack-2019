class Field:
    def __init__(self, farm, blocks):
        self.__farm = farm
        self.__blocks = blocks



    def get_farm(self):
        return self.__farm

    def get_blocks(self):
        return self.__blocks