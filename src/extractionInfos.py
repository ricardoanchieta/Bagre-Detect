import requests
from constants import *
from bs4 import BeautifulSoup

def getSummonerInfo(summonerName):

    name = summonerName.replace(" ","+")
    url = BASE_URL + "br/" + name

    pageSummoner = requests.get(url, headers=HEADERS)
    parser = BeautifulSoup(pageSummoner.content,"html.parser")
    elo = parser.find("div",{"class": "leagueTier"}).text.strip()
    queue = parser.find("span",{"class": "queue"}).text.strip()

    containerTopChampion = parser.find("td",{"class": "champColumn"})
    topChampion = containerTopChampion.find("div",{"class": "name"}).text.strip()
    
    return elo, queue, topChampion 

def getChampionInfo(summonerName, championName):

    summonerName = summonerName.replace(" ","+")
    championName = (championName.replace(" ","")).lower()
    url = BASE_URL + "champions/"+ championName +"/br/" + summonerName

    pageChampion = requests.get(url, headers=HEADERS)
    parser = BeautifulSoup(pageChampion.content,"html.parser")

    try:
        numGames = parser.find("div",{"id":"graphDD55"}).text.strip()
        winrate = parser.find("div",{"id":"graphDD56"}).text.strip()
    except:
        numGames = parser.find("div",{"id":"graphDD56"}).text.strip()
        winrate = parser.find("div",{"id":"graphDD57"}).text.strip()

    avgKills = parser.find("span",{"class":"kills"}).text.strip()
    avgDeaths = parser.find("span",{"class":"deaths"}).text.strip()
    avgAssists = parser.find("span",{"class":"assists"}).text.strip()
    avgKDA = avgKills + "/" + avgDeaths + "/" + avgAssists

 #   print("Invocador nao encontrado")
 #   return None

    return numGames, winrate, avgKDA
   
