class Block:

    def __init__(self, estimateYield, workHours):

        self.__estimateYield = estimateYield
        self.__workHours = workHours

    def getEstimateYield(self):
        return self.__estimateYield

    def getWorkHours(self):
        return self.__workHours

    def yieldPerHour(self):
        return self.__estimateYield/self.__workHours