class CropEvent():
    def __init__(self, old_crop, new_crop, date):
        self.__old_crop = old_crop
        self.__new_crop = new_crop
        self.__date = date

    def get_old_crop(self):
        return self.__old_crop()

    def get_new_crop(self):
        return self.__new_crop()

    def get_date(self):
        return self.__date


class CropEventTemplate:
    def __init__(self, oc_id, nc_id, date):
        self.__oc_id = oc_id
        self.__nc_id = nc_id
        self.__date = date

    def get_old_crop(self):
        return self.__oc_id

    def get_new_crop(self):
        return self.__nc_id

    def get_date(self):
        return self.__date
