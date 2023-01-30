from extractionInfos import getChampionInfo
class Suspect:
    def __init__(self, summonerName, championName):
        self.nome = summonerName
        self.champion = championName
        self.numGames, self.winrate, self.avgKDA = getChampionInfo(summonerName,championName)



if __name__ == "__main__":
    Suspect("Augustus GIoop", "Jax")