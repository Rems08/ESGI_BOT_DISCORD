# on importe le module discord.py pour utiliser la bibliothèque qui nous permet de contrôler le servuer
import discord
from discord import *
from discord.ext import commands
from discord.utils import *
from random import*
# ajouter un composant de discord.py
import time, calendar, asyncio, datetime, discord, requests
import MyGES #On importe le module time pour la commande sleep
import heurePause
import requests #Enable HTTP requests
from requests import*
from bs4 import BeautifulSoup #Find Elements on website
import welcome


intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True
# créer le bot
bot = commands.Bot(command_prefix='!', intents=intents) #Permettra au bot de savoir quand est-ce qu'on lui parle grâce au str de command_prefix
#client = discord.Client() inutile à priori

bot.remove_command('help') #Supprime la commande help afin de créer note propre commande
# détecter quand le bot est pret ("allumé")
@bot.event
async def on_ready():
    print("""

    88888888b .d88888b   .88888.  dP     888888ba   .88888.  d888888P    dP .d88888b      888888ba   88888888b  .d888888  888888ba  dP    dP    dP    
    88        88.    "' d8'   `88 88     88    `8b d8'   `8b    88       88 88.    "'     88    `8b  88        d8'    88  88    `8b Y8.  .8P    88    
   a88aaaa    `Y88888b. 88        88    a88aaaa8P' 88     88    88       88 `Y88888b.    a88aaaa8P' a88aaaa    88aaaaa88a 88     88  Y8aa8P     88    
    88              `8b 88   YP88 88     88   `8b. 88     88    88       88       `8b     88   `8b.  88        88     88  88     88    88       dP    
    88        d8'   .8P Y8.   .88 88     88    .88 Y8.   .8P    88       88 d8'   .8P     88     88  88        88     88  88    .8P    88             
    88888888P  Y88888P   `88888'  dP     88888888P  `8888P'     dP       dP  Y88888P      dP     dP  88888888P 88     88  8888888P     dP       oo    
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    ESGI discord: https://discord.gg/8ZkXxzm5s6
    """)
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("#ESGI | !help"))
    #await heurePause.pause() #Lance la fonction qui permet de gérer les pauses 
# phrase
print("Lancement de ESGI...")

#Action quand un user arrive dans le serveur
@bot.event
async def on_member_join(member):
    print(member)
    await member.send(welcome.welcome())

@bot.command()
async def membres(ctx): 
    """Fonction qui permet à un utilisateur de visualiser ses notes à l'aide d'un identifiant et d'un mdp"""
    member_count = 0
    for member in ctx.guild.members:
       member_count += 1
    await ctx.send(f"Le serveur comptabilise {member_count} utilisateur à son actif !")

@bot.command()
async def test(ctx): # Commande de test pour vérifier que le bot est bien en Etat de répondre 
    '''Commande inutile pour le moment'''
    channel = bot.get_channel(908037516945403974)
    await channel.send("Le bot est en Etat de fonctionner ^^")

@bot.command()
async def nul(ctx): # Commande qui envoie la photo de mathis qui dit "Nul ce cours"
    '''Envoie Commande qui envoie la photo de mathis qui dit "Nul ce cours"'''
    await ctx.message.delete() #Supprime le message de la personne ayant rentré la commande
    await ctx.send("https://cdn.discordapp.com/attachments/889481646221430794/903662315340173352/unknown.png")

@bot.command()
async def help(ctx): #Affiche une liste structurées des différentes commandes
    '''Cette commande permet de tester le bot'''
    right_channel = discord.utils.get(ctx.guild.channels, name="🔎cmd-bot🔎")
    if right_channel == ctx.channel:
        embed=discord.Embed(title="Liste des commandes", description="**Voici la liste des commandes du bot ESGI:**", color=0x9e0cbb)
        embed.set_author(name="ESGI bot !help", icon_url="https://www.supersoluce.com/sites/default/files/styles/picto_soluce/interrogation.png")
        embed.add_field(name="- !mes_notes", value="Permet d'afficher les notes de l'utilisateur", inline=True)
        embed.add_field(name="- !mes_absences", value="Permet d'afficher les absences de l'utilisateur", inline=True)
        embed.add_field(name="- !membres", value="Permet d'afficher le nombre de membre du serveur discord", inline=True)
        embed.set_footer(text="#Rems")
        await ctx.send(embed=embed)
    else:
        await ctx.message.delete() #Supprime le message de la personne ayant rentré la commande
        await ctx.author.send("Vous écrivez dans le mauvais channel.")

@bot.command()
async def mes_notes(ctx, user, password): 
    """Fonction qui permet à un utilisateur de visualiser ses notes à l'aide d'un identifiant et d'un mdp"""
    myges = MyGES.MYGES(user, password)
    await myges.print_grades(ctx, "2021")

@bot.command()
async def mes_absences(ctx, user, password): 
    """Fonction qui permet à un utilisateur de visualiser ses notes à l'aide d'un identifiant et d'un mdp"""
    myges = MyGES.MYGES(user, password)
    await myges.print_absences(ctx, "2021")
    
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("**Erreur:** Un argument est manquant. !help pour plus d'information sur les commandes.")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("**Erreur:** Il semblerait que votre commande soit mauvaise, !help pour la liste des commandes.")
    else:
        raise error

#Partie lancement du bot
token = open("../token.txt", "r").read() #Renseignez le chemin du token ici
# connecter au serveur
bot.run(token) #Mettre "Token pour lancer le bot"