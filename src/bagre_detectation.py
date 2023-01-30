from suspect import Suspect
from view import printBagreCard

def bagreDetector(summonerName, championName):
    bagre = False
    message = ""

    suspect = Suspect(summonerName,championName)

    kills, deaths, assists = suspect.avgKDA.split("/")
    
    numberKDA = (float(kills) + float(assists))/ float(deaths)
    winrate = suspect.winrate.replace("%", "")
    if(float(winrate) < 50 and numberKDA <= 1.9):
        bagre = True
        message = "BAGRE DETECTADO"
    elif(float(winrate) >= 50 and numberKDA <= 2.5):
        message = "POSSIVEL BAGRE, AINDA PODE FAZER ALGO"
    else:
        message = "GENIO DO LOL"
        
    dictResp = {
        "message": message,
        "nome": suspect.nome,
        "games": suspect.numGames,
        "winrate": suspect.winrate,
        "kda": suspect.avgKDA
    }
    printBagreCard(message,suspect.nome,suspect.numGames,suspect.winrate, suspect.avgKDA)
    
    return dictResp


if __name__ == "__main__":
    nomeJogador = input("Insira o invocador:")
    nomeBoneco = input("qual o boneco?")
    bagreDetector(nomeJogador, nomeBoneco)