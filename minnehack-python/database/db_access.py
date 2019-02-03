import psycopg2
import functools

from Models.Block import Block
from Models.Crop import Crop
from Models.CropEvent import CropEvent
from Models.Farm import Farm
from Models.Field import Field


class Database():
    def __init__(self, connection_object):
        self.__connection = connection_object

    def add_farm(self, farm_template):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.insert_farm(1,%s,%s)", (farm_template.get_name(), farm_template.get_location()))

    def add_field(self, field_template):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.insert_field(1, %s, %s)", (field_template.get_farm_id(), field_template.get_name()))

    def add_block(self, block_template):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.insert_block(1, %s, %s, %s", (block_template.get_field(), block_template.get_name(), block_template.get_crop()))

    def add_crop(self, crop_template):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.insert_crop(1, %s, %s, %s, %s, %s)",
                       (crop_template.get_name(), crop_template.get_market_value_per_unit(), crop_template.get_yield_time(), crop_template.get_cost_per_unit(), crop_template.get_country_name()))

    def add_crop_event(self, crop_event_template):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.insert_crop_swap_event(1, %s, %s, %s)",
                       (crop_event_template.get_old_crop(), crop_event_template.get_new_crop(), crop_event_template.get_date()))

    def remove_farm(self, farm_id):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.remove_farm(%s)", (farm_id))

    def remove_field(self, field_id):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.remove_field(%s)", (field_id))

    def remove_block(self, block_id):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.remove_block(%s)", (block_id))

    def remove_crop(self, crop_id):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.remove_crop(%s)", (crop_id))

    def remove_crop_event(self, crop_event_id):
        cursor = self.__connection.cursor()
        cursor.execute("orange_produce.remove_crop_swap_event(%s)", (crop_event_id))

    def update_farm(self, farm_id, farm):
        pass

    def update_field(self, field_id, field):
        pass

    def update_block(self, block_id, block):
        pass

    def update_crop(self, crop_id, crop):
        pass

    def update_crop_event(self, crop_event_id, crop_event):
        pass

    def get_farm(self, farm_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM orange_produce.farms WHERE id = %s", (farm_id))
        items = cursor.fetch_all()
        if len(items) == 1:
            return self.convert_farm(items[0])
        else:
            raise KeyError(farm_id)

    def get_field(self, field_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM orange_produce.fields WHERE id = %s", (field_id))
        items = cursor.fetch_all()
        if len(items) == 1:
            return self.convert_field(items[0])
        else:
            raise KeyError(field_id)

    def get_block(self, block_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM orange_produce.blocks WHERE id = %s", (block_id))
        items = cursor.fetch_all()
        if len(items) == 1:
            return self.convert_block(items[0])
        else:
            raise KeyError(block_id)

    def get_crop(self, crop_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM orange_produce.crops WHERE id = %s", (crop_id))
        items = cursor.fetch_all()
        if len(items) == 1:
            return self.convert_crop(items[0])
        else:
            raise KeyError(crop_id)

    def get_crop_event(self, crop_event_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM orange_produce.crop_swap_event WHERE id = %s", (crop_event_id))
        items = cursor.fetch_all()
        if len(items) == 1:
            return self.convert_crop_event(items[0])
        else:
            raise KeyError(crop_event_id)

    def get_fields_from_farm(self, farm_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM orange_produce.fields WHERE contained_in = %s", (farm_id))
        items = cursor.fetch_all()
        return items

    def get_blocks_from_field(self, field_id):
        cursor = self.__connection.cursor()
        cursor.execute("SELECT * FROM orange_produce.blocks WHERE contained_in = %s", (field_id))
        items = cursor.fetch_all()
        return items

    def convert_farm(self, tuple_item):
        print(tuple_item)
        return Farm(tuple_item[2], tuple_item[1], tuple_item[3], functools.partial(self.get_fields_from_farm, tuple_item[1]))

    def convert_field(self, tuple_item):
        print(tuple_item)
        return Field(tuple_item[1], tuple_item[2], tuple_item[3], functools.partial(self.get_blocks_from_field, tuple_item[1]))

    def convert_block(self, tuple_item):
        print(tuple_item)
        return Block(tuple_item[1], tuple_item[2], functools.partial(self.get_field, tuple_item[3]), functools.partial(self.get_crop, tuple_item[4]))

    def convert_crop(self, tuple_item):
        print(tuple_item)
        return Crop(tuple_item[1], tuple_item[2], tuple_item[3], tuple_item[4], tuple_item[5], tuple_item[6])

    def convert_crop_event(self, tuple_item):
        print(tuple_item)
        return CropEvent(tuple_item[1], functools.partial(self.get_crop, tuple_item[2]), functools.partial(self.get_crop, tuple_item[3]), tuple_item[4])
