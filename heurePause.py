# on importe le module discord.py pour utiliser la bibliothèque qui nous permet de contrôler le servuer
from discord import channel
from random import*
from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands
import time, calendar, asyncio, datetime, discord, requests #On importe le module time pour la commande sleep
bot = commands.Bot(command_prefix='!') #Permettra au bot de savoir quand est-ce qu'on lui parle grâce au str de command_prefix
async def pause():
    print("Ce programme est fait pour combler les lacunes de la PTN d'ESGI de merde qui ne sait pas faire son taff")
    channel = bot.get_channel(903609266072600629) #defini le channel Général du discord
    async def wait_until(dt):
        # sleep until the specified datetime
        now = datetime.datetime.now()
        await asyncio.sleep((dt - now).total_seconds())

    async def run_at(dt, coro):
        await wait_until(dt)
        return await coro
    # datetime.datetime.today().weekday() renvoie un entier: 0 = Lundi, 1 = Mardi, 2 = Mercredi, 3 = Jeudi, 4 = Vendredi, 5 = Samedi, 6 = Dimanche.
    async def advertising():
        if (("9:30" in time.strftime('%X')) or ("11:15" in time.strftime('%X')) or ("15:30" in time.strftime('%X')) or ("18:34²" in time.strftime('%X'))) and ((datetime.datetime.today().weekday() == 0 or datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 2 or datetime.datetime.today().weekday() == 3 or datetime.datetime.today().weekday() == 4)):
            await channel.send(f"ATTENTION IL EST {time.strftime('%X')} ET C'EST LA PAUSE ! Oubliez pas de signer la feuille d'émargement.")
            print(f"ATTENTION IL EST {time.strftime('%X')} ET C'EST LA PAUSE !")
            await asyncio.sleep(60) #Faire attendre le programme 60 secondes
            loop.create_task(advertising()) #Relance la fonction advertising
        else:
            await asyncio.sleep(5) #Faire attendre le programme 5 secondes
            loop.create_task(advertising()) #Relance la fonction advertising


    loop = asyncio.get_event_loop()
    # Lance la fonction d'avertissement
    loop.create_task(advertising())
    loop.run_forever()