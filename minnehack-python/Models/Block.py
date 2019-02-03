class Block:
    def __init__(self, crop):
        self.__crop = crop

    def get_farm(self):
        return self.__field.get_farm()

    def get_field(self):
        return self.__field

    def get_blocks(self):
        return self.__blocks