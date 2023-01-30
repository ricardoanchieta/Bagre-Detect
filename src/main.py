import discord
from discord import app_commands
from discord.ext import commands
import json
from bagre_detectation import bagreDetector
# IMPORT THE OS MODULE.
import os


# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents= intents)

@bot.command()
async def detectar(ctx):
    def check(msg):
        return True

    await ctx.channel.send("Qual o nome do suspeito?")
    msg = await bot.wait_for("message",timeout=30)
    summonerName = msg.content
    await ctx.channel.send("Qual o boneco?")
    msg = await bot.wait_for("message",timeout=30)
    championName = msg.content
    resp = bagreDetector(summonerName,championName)
    await ctx.channel.send(f'{resp["message"]} \n Nome: {resp["nome"]}  \n Jogos com o boneco: {resp["games"]}  \n Winrate: {resp["winrate"]}  \n KDA: {resp["kda"]}')


with open("credencials.json", encoding='utf-8') as meu_json:
    credencials = json.load(meu_json)

bot.run(credencials["token"])