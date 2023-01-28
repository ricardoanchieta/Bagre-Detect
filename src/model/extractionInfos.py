import requests
from constants import *
from bs4 import BeautifulSoup

def formatName(name):
    name = name.replace(" ","+")
    return name

def getSummonerInfo(summonerName):

    name = formatName(summonerName)
    url = BASE_URL + "br/" + name

    pageSummoner = requests.get(url, headers=HEADERS)
    parser = BeautifulSoup(pageSummoner.content,"html.parser")
    elo = parser.find("div",{"class": "leagueTier"}).text.strip()
    
    x = 2


if __name__ == "__main__":

    getSummonerInfo("Augustus GIoop")
