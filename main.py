# on importe le module discord.py pour utiliser la bibliothèque qui nous permet de contrôler le servuer
from discord import channel
from random import*
from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands
import time, calendar, asyncio, datetime, discord, requests
import MyGES #On importe le module time pour la commande sleep
import heurePause
import requests #Enable HTTP requests
from requests import*
from bs4 import BeautifulSoup #Find Elements on website 



# créer le bot
bot = commands.Bot(command_prefix='!') #Permettra au bot de savoir quand est-ce qu'on lui parle grâce au str de command_prefix
client = discord.Client()
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
    ESGI discord: https://discord.gg/qmSVQedGek
    """)
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("#ESGI | !help"))
    #await heurePause.pause() #Lance la fonction qui permet de gérer les pauses 
# phrase
print("Lancement de ESGI...")

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
        embed=discord.Embed(title="Liste des commandes", description="**Voici la liste des commandes du bot ESGI:**", color=0x1f6e9e)
        embed.set_author(name="ESGI bot", icon_url="https://www.sciences-u-lyon.fr/images/2020/03/myges.png")
        embed.add_field(name="- !regles", value="Permet d'afficher les règles du serveur", inline=False)
        embed.add_field(name="- !signes", value="Permet d'afficher la liste des signes disponible à utiliser avec la commande horoscope", inline=True)
        embed.add_field(name="- !horoscope", value="Permet d'afficher votre horoscope grâce à la commande !horoscope (votre signe)", inline=True)
        embed.add_field(name="- !clash", value="Permet de clasher un membre du discord grâce à la commande !clash (mention d'un autre membre)", inline=True)
        embed.add_field(name="- !disquettePrive", value="Permet d'envoyer un message privé à un autre membre grâce à la commande !disquettePrive (mention d'un autre membre)", inline=True)
        embed.add_field(name="!comp", value="Compare deux utilisateurs entre eux pour vérifier si ils sont compatible utilisez !comp (mention du permier utilisateur) (mention du deuxième utilisateur)", inline=True)
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