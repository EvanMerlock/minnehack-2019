import Models.Crop
import csv
import database.db_access

class Analysis:
    def __init__(self):
        pass

    def est_yield(self):
        pass

    def est_cost(self):
        pass

    def get_yield_per_acre(self, crop_string):
        #finds the yeld per acre of the crop in input, and returns it



    def get_cost_per_ton(self, crop_string, search_string):
        pass
    # From the FAOSTAT file, gets the cost in usd per ton of the input crop string

        return self.stage_one_convert(crop_string, search_string)

    def create_crop (self, crop_string, search_string):
        #creates a new crop using the cost_per_ton and _yield_per_acre methods.
        #adds the crop to to database

        with crop_string as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:

                if row[7] == search_string:

                    country_name = row[3]
                    price = row[12]
                    cost_per_ton = self.get_cost_per_ton(crop_string, search_string)
                    yield_per_acre = self.get_yield_per_acre(crop_string)

        crop = Models.Crop.Crop(search_string, country_name, yield_per_acre, 0, cost_per_ton)

        database.db_access.add_crop(crop)

    def convert(self, database_handle, crop_string):
        pass
        # crop = Models.Crop.Crop(row[7], row[3], 0, 0, row[12])

    def stage_one_convert(self, crop_string, search_string):
        with crop_string as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")
            #line_count = 0

            for row in csv_reader:

                if row[7] == search_string:
                    return row[12]