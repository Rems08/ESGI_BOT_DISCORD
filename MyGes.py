#!/usr/bin/env python3

import requests
from urllib.parse import urlsplit, parse_qs
import base64
import json
import time
import discord

class MYGES:
    def __init__(self, discordid, username=None, password=None):
        self.actionurl = "https://api.kordis.fr"
        self.discordid = discordid
        if username!=None and password!=None:
            self.username = username; self.password = password
            self.register()
            
        if self.is_registered():
            self.userobj = self.get_userbydiscordid()
            self.token = self.get_token(self.userobj["BasicToken"])
        
    def is_registered(self):
        users = open('users.json', 'r')
        jsonusers = json.load(users)        
        for user in jsonusers:
            if user["DiscordId"] == self.discordid:
                return True

        return False

    def register(self):
        users = open('users.json', 'r')
        jsonusers = json.load(users)
        if self.is_registered():
            return

        jsonusers.append({
            "DiscordId": self.discordid,
            "BasicToken" : self.get_basictoken()
        })

        usersout = open('users.json', 'w')
        json.dump(jsonusers, usersout, indent=4, separators=(',',': '))
    
    def get_userbydiscordid(self):
        users = open('users.json', 'r')
        jsonusers = json.load(users)        
        for user in jsonusers:
            if user["DiscordId"] == self.discordid:
                return user
        
    def get_basictoken(self):
        token = base64.b64encode(f"{self.username}:{self.password}".encode()).decode('UTF-8')
        return {"Authorization": f"Basic {token}"}

    def get_token(self, token):
        urltoken = 'https://authentication.kordis.fr/oauth/authorize?response_type=token&client_id=skolae-app'
        try:
            r = requests.get(urltoken, headers=token)
        except requests.exceptions.InvalidSchema as e:
            urltokenreturn = repr(e).split("'")[1].replace("#", '?')
        
        tokenret = {k: v[0] for k, v in parse_qs(urlsplit(urltokenreturn).query).items()}
        return {"Authorization" : f"{tokenret['token_type']} {tokenret['access_token']}"}
    



    def get_absences(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/absences", headers=self.token).json()

    def get_agenda(self, start, end):
        return requests.get(f"{self.actionurl}/me/agenda?start={start}&end={end}", headers=self.token)
        
    def get_grades(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/grades", headers=self.token).json()

    async def print_absences(self, ctx, year="2021"):
        """Permet d'afficher les absence de l'utilisateur"""
        jsondata = self.get_absences(year)

        ###EMBED###
        embed=discord.Embed(title=f"absence de {ctx.author}", url="https://myges.fr/student/marks", description="Ici apparaissent vos absence", color=0x1f6e9e)
        embed.set_author(name="ESGI | !mes_absences", icon_url="https://zupimages.net/up/21/49/73pj.png")
        embed.set_thumbnail(url="https://www.sciences-u-lyon.fr/images/2020/03/myges.png")
        embed.set_footer(text="Made by DAVE")
        ###EMBED###

        print(ctx.author)
        for row in jsondata["result"]:
            date = time.strftime('%d-%m-%Y %H:%M', time.localtime(int(str(row['date'])[:-3])))
            just = "Jusitifiée" if row["justified"] else "Non justifiée"
            course_name = row["course_name"]
            print(f'{date}\t{just}\t{row["course_name"]}')
            embed.add_field(name=f"{date}: {just}", value=f"{course_name}", inline=True)
        await ctx.send(embed=embed)
    
    async def print_grades(self, ctx, year="2021"):
        """Permet d'afficher les notes de l'utilisateur"""

        ###EMBED###
        embed=discord.Embed(title=f"Notes de {ctx.author}", url="https://myges.fr/student/marks", description="Ici apparaissent vos notes", color=0x1f6e9e)
        embed.set_author(name="ESGI | !mes_notes", icon_url="https://zupimages.net/up/21/49/i5w7.png")
        embed.set_thumbnail(url="https://www.sciences-u-lyon.fr/images/2020/03/myges.png")
        embed.set_footer(text="Made by DAVE")
        ###EMBED###

        jsondata = self.get_grades(year)
        print(ctx.author)
        for row in jsondata["result"]: #Parcours le fichier JSON
            nom_cours = row["course"] #Nom du cours
            nom_prof = row["teacher_last_name"] # Nom du prof
            grades = f"{(str(row['grades'])[1:-1])} / 20" if row["grades"] else "Vous n'avez pas encore de note dans cette matière"
            print(f'{nom_cours}\t{nom_prof}\t{grades}') 
            embed.add_field(name=f"{nom_cours}: {nom_prof}", value=f"{grades}", inline=True)
            print("____________________") 
        await ctx.send(embed=embed)


#    def main():
#        myges = MYGES("", "")
#        print("""
#        88888888b .d88888b   .88888.  dP     888888ba   .88888.  d888888P 
#        88        88.    "' d8'   `88 88     88    `8b d8'   `8b    88    
#       a88aaaa    `Y88888b. 88        88    a88aaaa8P' 88     88    88    
#        88              `8b 88   YP88 88     88   `8b. 88     88    88    
#        88        d8'   .8P Y8.   .88 88     88    .88 Y8.   .8P    88    
#        88888888P  Y88888P   `88888'  dP     88888888P  `8888P'     dP    
#        ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#        """)
#        myges.print_absences("2021")
#        myges.print_grades("2021")
#    if __name__ == '__main__':
#        main()