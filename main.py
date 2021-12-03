# on importe le module discord.py pour utiliser la bibliothèque qui nous permet de contrôler le servuer
from discord import channel
from random import*
from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands
import time, calendar, asyncio, datetime, discord, requests #On importe le module time pour la commande sleep
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
     _____ _____ _____ _____  ______  _____ _____   _____ _____  ______ _____  ___ ________   __
    |  ___/  ___|  __ \_   _| | ___ \|  _  |_   _| |_   _/  ___| | ___ \  ___|/ _ \|  _  \ \ / /
    | |__ \ `--.| |  \/ | |   | |_/ /| | | | | |     | | \ `--.  | |_/ / |__ / /_\ \ | | |\ V / 
    |  __| `--. \ | __  | |   | ___ \| | | | | |     | |  `--. \ |    /|  __||  _  | | | | \ /  
    | |___/\__/ / |_\ \_| |_  | |_/ /\ \_/ / | |    _| |_/\__/ / | |\ \| |___| | | | |/ /  | |  
    \____/\____/ \____/\___/  \____/  \___/  \_/    \___/\____/  \_| \_\____/\_| |_/___/   \_/

    ESGI discord: https://discord.gg/vSqxvdaBVY

    
__/\\\\\\\\\\\\________/\\\\\\\\\_____/\\\________/\\\__/\\\________/\\\___________                                                                                       
 _\/\\\////////\\\____/\\\\\\\\\\\\\__\/\\\_______\/\\\_\///\\\____/\\\/____________                                                                                      
  _\/\\\______\//\\\__/\\\/////////\\\_\//\\\______/\\\____\///\\\/\\\/______________                                                                                     
   _\/\\\_______\/\\\_\/\\\_______\/\\\__\//\\\____/\\\_______\///\\\/________________                                                                                    
    _\/\\\_______\/\\\_\/\\\\\\\\\\\\\\\___\//\\\__/\\\__________\/\\\_________________                                                                                   
     _\/\\\_______\/\\\_\/\\\/////////\\\____\//\\\/\\\___________\/\\\_________________                                                                                  
      _\/\\\_______/\\\__\/\\\_______\/\\\_____\//\\\\\____________\/\\\_________________                                                                                 
       _\/\\\\\\\\\\\\/___\/\\\_______\/\\\______\//\\\_____________\/\\\_________________                                                                                
        _\////////////_____\///________\///________\///______________\///__________________                                                                               
_________/\\\_______________________________________________/\\\\\\_______________________________________________________________________________________________        
 ________\/\\\______________________________________________\////\\\_______________________________________________________________________________________________       
  ________\/\\\_________________________________________________\/\\\____________________/\\\\\\\\\_______________________________________________________/\\\______      
   ________\/\\\______/\\\\\\\\___/\\\____/\\\_____/\\\\\\\\_____\/\\\________/\\\\\_____/\\\/////\\\____/\\\\\__/\\\\\_______/\\\\\\\\___/\\/\\\\\\____/\\\\\\\\\\\_     
    ___/\\\\\\\\\____/\\\/////\\\_\//\\\__/\\\____/\\\/////\\\____\/\\\______/\\\///\\\__\/\\\\\\\\\\___/\\\///\\\\\///\\\___/\\\/////\\\_\/\\\////\\\__\////\\\////__    
     __/\\\////\\\___/\\\\\\\\\\\___\//\\\/\\\____/\\\\\\\\\\\_____\/\\\_____/\\\__\//\\\_\/\\\//////___\/\\\_\//\\\__\/\\\__/\\\\\\\\\\\__\/\\\__\//\\\____\/\\\______   
      _\/\\\__\/\\\__\//\\///////_____\//\\\\\____\//\\///////______\/\\\____\//\\\__/\\\__\/\\\_________\/\\\__\/\\\__\/\\\_\//\\///////___\/\\\___\/\\\____\/\\\_/\\__  
       _\//\\\\\\\/\\__\//\\\\\\\\\\____\//\\\______\//\\\\\\\\\\__/\\\\\\\\\__\///\\\\\/___\/\\\_________\/\\\__\/\\\__\/\\\__\//\\\\\\\\\\_\/\\\___\/\\\____\//\\\\\___ 
        __\///////\//____\//////////______\///________\//////////__\/////////_____\/////_____\///__________\///___\///___\///____\//////////__\///____\///______\/////____
    
    """)
    await bot.change_presence(status=discord.Status.online,
            activity=discord.Game("#ESGI | !help"))
    await heurePause.pause() #Lance la fonction qui permet de gérer les pauses 
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
    right_channel = discord.utils.get(ctx.guild.channels, name="🔎cmd-bot🔎")
    if right_channel == True:
        '''Cette commande permet de tester le bot'''
        embed=discord.Embed(title="Liste des commandes", description="**Voici la liste des commandes du bot ESGI:**", color=0x8a00bd)
        embed.set_author(name="ESGI bot", icon_url="https://i.ytimg.com/vi/q906x1vjeSI/mqdefault.jpg")
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
async def mes_notes(ctx): #ATTENTION RISQUE DE POSER DES PB
        url = "https://myges.fr/student/marks;jsessionid=B08F28A8171E158FDA6EB8B9E7383F4E" #URL du site à parcourir
        user = "rmassiet"
        mdp = "ta3JHeK8"
        page = requests.get(url, auth=('user', 'mdp'))
        code_connexion = str(page.status_code)
        if code_connexion == "200":
            print("Connexion réussite")
            print("Status code: ", page.status_code)
        else:
            print("Connexion failed")
            print(f"ERROR: {code_connexion}")
            exit()
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.title) #Permet d'afficher toute la page
        print("Récupération de vos notes en cours...")
        liste = soup.find_all("td", role="gridcell")
        for i in liste:
            print(i.string)
            if i.string == None:
                await ctx.send("Case vide comme le cerveau de Villain")
            else:
                await ctx.send(i.string)

#Partie lancement du bot
token = open("../token.txt", "r").read() #Renseignez le chemin du token ici
# connecter au serveur
bot.run(token) #Mettre "Token pour lancer le bot"