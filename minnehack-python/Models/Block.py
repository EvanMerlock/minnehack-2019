class Block:

    def __init__(self, crop):
        self.__crop = crop

    def get_farm(self):
        return self.__field.get_farm()

    def get_field(self):
        return self.__field

    def get_blocks(self):
        return self.__blocks


    def __init__(self, estimateYield, workHours):

        self.__estimateYield = estimateYield
        self.__workHours = workHours

    def getEstimateYield(self):
        return self.__estimateYield

    def getWorkHours(self):
        return self.__workHours

    def yieldPerHour(self):
        return self.__estimateYield/self.__workHours

