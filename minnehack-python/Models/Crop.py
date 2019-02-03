class crop :

    def __init__(self, marketValuePerBlock, YieldTime, costPerBlock):

        self.__marketValuePerBlock = marketValuePerBlock
        self.__YieldTime = YieldTime
        self.__costPerBlock = costPerBlock

    def getMarketValuePerBlock(self):
        return self.__marketValuePerBlock

    def getYieldTime(self):
        return self.__YieldTime

    def getCostPerBlock(self):
        return self.__costPerBlock

    def getFields(self):
        pass

    def getFarms(self):
        pass

    def getCropRotation(self):
        pass

    def getBlock(self):
        pass

    def calcProfit(self):
        return self.__marketValuePerBlock - self.__costPerBlock

    def calcProfitPerSecond(self):
        return self.calcProfit()/self.__YieldTime

