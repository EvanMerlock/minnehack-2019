class Crop:
    def __init__(self, name, countryName, marketValuePerBlock, YieldTime, costPerBlock):
        self.__name = name
        self.__countryName = countryName
        self.__marketValuePerBlock = marketValuePerBlock
        self.__YieldTime = YieldTime
        self.__costPerBlock = costPerBlock

    def getName(self):
        return self.__name

    def getCountryName(self):
        return self.__countryName

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


class CropTemplate:
    def __init__(self, name, country_name, market_value_per_unit, yield_time, cost_per_unit):
        self.__name = name
        self.__country_name = country_name
        self.__mkpu = market_value_per_unit
        self.__yield_time = yield_time
        self.__cpu = cost_per_unit

    def get_name(self):
        return self.__name

    def get_country_name(self):
        return self.__country_name

    def get_market_value_per_unit(self):
        return self.__mkpu

    def get_yield_time(self):
        return self.__yield_time

    def get_cost_per_unit(self):
        return self.__cpu


