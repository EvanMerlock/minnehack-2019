class CropEvent():
    def __init__(self, old_crop, new_crop, date):
        self.__old_crop = old_crop
        self.__new_crop = new_crop
        self.__date = date

    def get_old_crop(self):
        return self.__old_crop

    def get_new_crop(self):
        return self.__new_crop

    def get_date(self):
        return self.__date
