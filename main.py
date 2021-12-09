# on importe le module discord.py pour utiliser la bibliothèque qui nous permet de contrôler le servuer
import discord
from discord import *
from discord.ext import commands
from discord.ext.commands.errors import NoEntryPointError
from discord.utils import *
from random import*
# ajouter un composant de discord.py
import time, calendar, asyncio, datetime, discord, requests
import MyGes #On importe le module time pour la commande sleep
import heurePause
import requests #Enable HTTP requests
from requests import*
from bs4 import BeautifulSoup #Find Elements on website
import welcome
import embed


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
    global ESGI_BOT_ART
    ESGI_BOT_ART= '''

    88888888b .d88888b   .88888.  dP     888888ba   .88888.  d888888P    dP .d88888b      888888ba   88888888b  .d888888  888888ba  dP    dP    dP    
    88        88.    "' d8'   `88 88     88    `8b d8'   `8b    88       88 88.    "'     88    `8b  88        d8'    88  88    `8b Y8.  .8P    88    
   a88aaaa    `Y88888b. 88        88    a88aaaa8P' 88     88    88       88 `Y88888b.    a88aaaa8P' a88aaaa    88aaaaa88a 88     88  Y8aa8P     88    
    88              `8b 88   YP88 88     88   `8b. 88     88    88       88       `8b     88   `8b.  88        88     88  88     88    88       dP    
    88        d8'   .8P Y8.   .88 88     88    .88 Y8.   .8P    88       88 d8'   .8P     88     88  88        88     88  88    .8P    88             
    88888888P  Y88888P   `88888'  dP     88888888P  `8888P'     dP       dP  Y88888P      dP     dP  88888888P 88     88  8888888P     dP       oo    
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    ESGI discord: https://discord.gg/8ZkXxzm5s6
    '''
    print(ESGI_BOT_ART)
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("#ESGI | !help"))
    #await heurePause.pause() #Lance la fonction qui permet de gérer les pauses 
# phrase
print("Lancement de ESGI...")

#Action quand un user arrive dans le serveur
@bot.event
async def on_member_join(member):
    print(member)
    await member.send('''
    ```yaml
    /$$      /$$ /$$$$$$$$ /$$        /$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$$       /$$$$$$ /$$   /$$       /$$      /$$            /$$$$$$  /$$$$$$$$  /$$$$$$ 
    | $$  /$ | $$| $$_____/| $$       /$$__  $$ /$$__  $$| $$$    /$$$| $$_____/      |_  $$_/| $$$ | $$      | $$$    /$$$           /$$__  $$| $$_____/ /$$__  $$
    | $$ /$$$| $$| $$      | $$      | $$  \__/| $$  \ $$| $$$$  /$$$$| $$              | $$  | $$$$| $$      | $$$$  /$$$$ /$$   /$$| $$  \__/| $$      | $$  \__/
    | $$/$$ $$ $$| $$$$$   | $$      | $$      | $$  | $$| $$ $$/$$ $$| $$$$$           | $$  | $$ $$ $$      | $$ $$/$$ $$| $$  | $$| $$ /$$$$| $$$$$   |  $$$$$$ 
    | $$$$_  $$$$| $$__/   | $$      | $$      | $$  | $$| $$  $$$| $$| $$__/           | $$  | $$  $$$$      | $$  $$$| $$| $$  | $$| $$|_  $$| $$__/    \____  $$
    | $$$/ \  $$$| $$      | $$      | $$    $$| $$  | $$| $$\  $ | $$| $$              | $$  | $$\  $$$      | $$\  $ | $$| $$  | $$| $$  \ $$| $$       /$$  \ $$
    | $$/   \  $$| $$$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$$       /$$$$$$| $$ \  $$      | $$ \/  | $$|  $$$$$$$|  $$$$$$/| $$$$$$$$|  $$$$$$/
    |__/     \__/|________/|________/ \______/  \______/ |__/     |__/|________/      |______/|__/  \__/      |__/     |__/ \____  $$ \______/ |________/ \______/ 
                                                                                                                            /$$  | $$                              
                                                                                                                        |  $$$$$$/                              
                                                                                                                            \______/                                         
    ```
    ''')
    await member.send(welcome.welcome()) #Envoie un message de bienvenue aux utilisateurs rejoignant le serveur


@bot.command()
async def membres(ctx): 
    """Fonction qui permet de lister le nombre de membre présent sur le serveur"""
    member_count = 0
    for member in ctx.guild.members:
       member_count += 1
    await ctx.send(f"Le serveur comptabilise {member_count} utilisateur à son actif !")
    print(ctx.guild)

@bot.command()
async def test(ctx): # Commande de test pour vérifier que le bot est bien en Etat de répondre 
    '''Commande inutile pour le moment'''
    embed_test = embed.EMBED("title", "description", "!nom_fonction", "https://www.supersoluce.com/sites/default/files/styles/picto_soluce/interrogation.png")
    embed_test.create()
    embed_test.add_field("Test1", "Value1")
    embed_test.add_field("Test2", "Value2")
    await ctx.send(embed=embed_test)

@bot.command()
async def nul(ctx): # Commande qui envoie la photo de mathis qui dit "Nul ce cours"
    '''Envoie Commande qui envoie la photo de mathis qui dit "Nul ce cours"'''
    await ctx.message.delete() #Supprime le message de la personne ayant rentré la commande
    await ctx.send("https://cdn.discordapp.com/attachments/889481646221430794/903662315340173352/unknown.png")

@bot.command()
async def help(ctx): #Affiche une liste structurées des différentes commandes
    '''Cette commande permet de tester le bot'''
    embed=discord.Embed(title="Liste des commandes", description="**Voici la liste des commandes du bot ESGI:**", color=0x9e0cbb)
    embed.set_author(name="ESGI | !help", icon_url="https://www.supersoluce.com/sites/default/files/styles/picto_soluce/interrogation.png")
    embed.add_field(name="- !connexion", value="**!connexion** {user MyGES} {Password MyGES} connecte l'utilisateur à son compte MyGES", inline=True)
    embed.add_field(name="- !mes_notes", value="Permet d'afficher les notes de l'utilisateur", inline=True)
    embed.add_field(name="- !mes_absences", value="Permet d'afficher les absences de l'utilisateur", inline=True)
    embed.add_field(name="- !membres", value="Permet d'afficher le nombre de membre du serveur discord", inline=True)
    embed.set_footer(text="#Rems")
    try:
        right_channel = discord.utils.get(ctx.guild.channels, name="🔎cmd-bot🔎")
        if right_channel == ctx.channel:
            await ctx.send(embed=embed)
        else:
            await ctx.message.delete() #Supprime le message de la personne ayant rentré la commande
            await ctx.author.send("Vous écrivez dans le mauvais channel.")
    except:
        await ctx.send(embed=embed)

@bot.command()
@commands.dm_only()
async def connexion(ctx, user, password): # Commande de test pour vérifier que le bot est bien en Etat de répondre 
    '''Permet à l'utilisateur de se connecter à son profil MyGES à l'aide de son id et de son mdp'''
    myges = MyGes.MYGES(ctx.author.id ,user, password)
    await ctx.send("✅**Félicitation votre connexion a bien aboutie merci de votre confiance**✅")

@bot.command()
async def deconnexion(ctx): # Commande de test pour vérifier que le bot est bien en Etat de répondre 
    '''Permet à l'utilisateur de se déconnecter de son profil MyGES'''
    myges = MyGes.MYGES(ctx.author.id)

    if myges.unregister():
        await ctx.send("✅**Félicitation vous vous êtes déconnecté avec succès !**✅")
    else:
        await ctx.send("Malhereusement vous n'êtes pas enregistré dans notre base de donnée vous pouvez vous connecter avec !connexion user mdp")

@bot.command()
async def mes_notes(ctx, user=None, password=None): 
    """Fonction qui permet à un utilisateur de visualiser ses notes à l'aide d'un identifiant et d'un mdp"""
    myges = MyGes.MYGES(ctx.author.id ,user, password)
    await myges.print_grades(ctx, "2021")

@bot.command()
async def mes_absences(ctx, user=None, password=None): 
    """Fonction qui permet à un utilisateur de visualiser ses notes à l'aide d'un identifiant et d'un mdp"""
    myges = MyGes.MYGES(ctx.author.id ,user, password)
    await myges.print_absences(ctx, "2021")
    
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("**Erreur:** Un argument est manquant. !help pour plus d'information sur les commandes.")
    elif isinstance(error,commands.CommandNotFound):
        await ctx.send("**Erreur:** Il semblerait que votre commande soit mauvaise, !help pour la liste des commandes.")
    elif isinstance(error,commands.CommandInvokeError):
        await ctx.send("**Erreur:** Il semblerait que je n'arrive pas à me connecter à votre compte. Entrez la commande !deconnexion puis réitérer la connexion")
    elif isinstance(error,commands.PrivateMessageOnly):
        await ctx.author.send("⚠️ATTENTION⚠️ n'envoyez jamais votre mot de passe en publique ! Pour vous connectez envoyez le moi en message privé (ici).")
        await ctx.message.delete()
    else:
        raise error

#Partie lancement du bot
token = open("../token.txt", "r").read() #Renseignez le chemin du token ici
# connecter au serveur
bot.run(token) #Mettre "Token pour lancer le bot"