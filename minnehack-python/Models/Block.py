class Block:

    def __init__(self, bid, name, field, crop):
        self.__id = bid
        self.__crop = crop
        self.__field = field
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_farm(self):
        return self.get_field().get_farm()

    def get_field(self):
        return self.__field

    def get_crop(self):
        return self.__crop

    def get_crop(self):
        return self.__crop()


class BlockTemplate:
    def __init__(self, name, crop, field):
        self.__name = name
        self.__crop = crop
        self.__field = field

    def get_name(self):
        return self.__name

    def get_crop(self):
        return self.__crop

    def get_name(self):
        return self.__name

    def get_field(self):
        return self.__field
