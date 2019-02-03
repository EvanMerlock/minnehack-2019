import Models.Crop
import csv


class Analysis:
    def __init__(self):
        pass

    def est_yield(self):
        pass

    def est_cost(self):
        pass

    def get_yield_per_acre(self, cropt_string):
        #finds the yeld per acre of the crop in input, and returns it

    def get_cost_per_ton(self, crop_string):
        pass
    # From the FAOSTAT file, gets the cost in usd per ton of the input crop string

    def create_crop (self, crop_string):
        #creates a new crop using the cost_per_ton and _yield_per_acre methods.
        #adds the crop to to database



    def convert(self, database_handle, crop_string):
        pass
        # crop = Models.Crop.Crop(row[7], row[3], 0, 0, row[6])

    def stage_one_convert(self, crop_string, search_string):
        with crop_string as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")
            #line_count = 0

            for row in csv_reader:

                if row[7] == search_string:
                    return row[6]