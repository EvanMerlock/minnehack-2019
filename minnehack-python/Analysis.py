import Models.Crop
import csv


class Analysis:
    def __init__(self):
        pass

    def est_yield(self):
        pass

    def est_cost(self):
        pass

    def est_yield_peracre(self):
        pass

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