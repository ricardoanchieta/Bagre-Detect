from ..extractionInfos import *

class Summoner:
    def __init__(self, summonerName):
        self.name = summonerName
        self.elo, self.queue, self.topChampion = getSummonerInfo(summonerName)

    def getChampion(self): 
        pass

