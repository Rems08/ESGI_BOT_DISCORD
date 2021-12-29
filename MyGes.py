#!/usr/bin/env python3

import requests
from urllib.parse import urlsplit, parse_qs
import base64
import json
import time
import discord
from datetime import datetime
logo_thumbnail = "https://www.ican-design.fr/ecole-infographie/ESGI_logo_web_blanc.png"
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

    def unregister(self):
        users = open('users.json', 'r')
        jsonusers = json.load(users)
        if self.is_registered():
            for user in jsonusers:
                if user["DiscordId"] == self.discordid:
                    for i, user in enumerate(jsonusers):
                        jsonusers.pop(i)
            usersout = open('users.json', 'w')
            json.dump(jsonusers, usersout, indent=4, separators=(',',': '))
            return True
        else:
            return False
    
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
    

    def get_agenda(self, start, end):
        return requests.get(f"{self.actionurl}/me/agenda?start={start}&end={end}", headers=self.token).json()["result"]

    def get_profil(self):
        return requests.get(f"{self.actionurl}/me/profile", headers=self.token).json()["result"]

    def get_absences(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/absences", headers=self.token).json()

    def get_agenda(self, start, end):
        return requests.get(f"{self.actionurl}/me/agenda?start={start}&end={end}", headers=self.token).json()["result"]
        
    def get_grades(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/grades", headers=self.token).json()

    def get_students(self, year):
        return requests.get(requests.get(f"{self.actionurl}/me/{year}/classes", headers=self.token).json()["result"][0]["links"][1]["href"], headers=self.token).json()["result"]

    def get_news(self):
        return requests.get(f"{self.actionurl}/me/news", headers=self.token).json()["result"]


    async def print_absences(self, ctx, year="2021"):
        """Permet d'afficher les absence de l'utilisateur"""
        jsondata = self.get_absences(year)

        ###EMBED###
        embed=discord.Embed(title=f"absence de {ctx.author}", url="https://myges.fr/student/marks", description="Ici apparaissent vos absence", color=0x1f6e9e)
        embed.set_author(name="ESGI | !mes_absences", icon_url="https://zupimages.net/up/21/49/73pj.png")
        embed.set_thumbnail(url=logo_thumbnail)
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
        embed.set_thumbnail(url=logo_thumbnail)
        embed.set_footer(text="Made by DAVE")
        ###EMBED###

        jsondata = self.get_grades(year)
        print(ctx.author)
        for row in jsondata["result"]: #Parcours le fichier JSON
            nom_cours = row["course"] #Nom du cours
            nom_prof = row["teacher_last_name"] # Nom du prof
            grades = f"{(str(row['grades'])[1:-1])} / 20" if row["grades"] else "Vous n'avez pas encore de note dans cette matière"
            print(f'{nom_cours}\t{nom_prof}\t{grades}') 
            embed.add_field(name=f"{nom_cours}: {nom_prof}", value=f"**{grades}**", inline=True)
            print("____________________") 
        await ctx.send(embed=embed)



    async def print_profil(self, ctx):
        embed=discord.Embed(title=f"Profil de {ctx.author}", url="https://myges.fr/student/marks", description="Ici apparaissent vos informations personnelles", color=0x1f6e9e)
        embed.set_author(name="ESGI | !profil", icon_url="https://zupimages.net/up/21/49/us0q.png")
        embed.set_thumbnail(url=logo_thumbnail)
        embed.set_footer(text="Made by DAVE")
        data = self.get_profil()
        for key in data:
            if key == 'mailing':
                break
            embed.add_field(name=f"{key}", value=f"{data[key]}", inline=True)
        await ctx.send(embed=embed)

    async def print_agenda(self, ctx, start, end):
        data = self.get_agenda(start, end)
        for row in data:
            ###EMBED###
            embed=discord.Embed(title=f"Prochains cours de {ctx.author}", url="https://myges.fr/student/marks", description="Ici apparaissent vos prochains cours", color=0x1f6e9e)
            embed.set_author(name="ESGI | !prochains_cours", icon_url="https://zupimages.net/up/21/50/9bk1.png")
            embed.set_thumbnail(url=logo_thumbnail)
            embed.set_footer(text="Made by DAVE")
            ###EMBED###
            ctr = ''
            debut_du_cours = datetime.fromtimestamp(row["start_date"] / 1000)
            date = debut_du_cours.strftime("%d/%m/%Y")
            debut_du_cours = debut_du_cours.strftime("%HH%M")
            fin_du_cours = datetime.fromtimestamp(row["end_date"] / 1000)
            fin_du_cours = fin_du_cours.strftime("%HH%M")
            
            prof = row["teacher"]
            matiere = row["name"]
            type_de_cours = row["modality"]
            room_info = row['rooms']
            if room_info ==None:
                room_number = "Informations indisponibles"
                etage = "Informations indisponibles"
                campus = "Informations indisponibles"
                return False
            else:
                for key in room_info:
                    room_number = key['name']
                    etage = key['floor']
                    campus = key['campus']
            if type_de_cours == "Présentiel":
                embed.add_field(name=f"Catégorie de présence", value=f"**{type_de_cours}**", inline=True)
                embed.add_field(name=f"Lieu", value=f"Au campus**{campus}**, au **{etage}**, salle numéro **{room_number}**", inline=True)
                embed.add_field(name=f"Horaire", value=f"Le cours débutera à **{debut_du_cours}** et finira à **{fin_du_cours}** le **{date}**", inline=True)
                embed.add_field(name=f"Professeur.e", value=f"**{prof}**", inline=True)
                embed.add_field(name=f"Cours", value=f"Cours de **{matiere}**", inline=True)
 
            else:
                embed.add_field(name=f"Catégorie de présence", value=f"**{type_de_cours}**", inline=True)
                embed.add_field(name=f"Horaire", value=f"Le cours débutera à **{debut_du_cours}** et finira à **{fin_du_cours}** le **{date}**", inline=True)
                embed.add_field(name=f"Professeur.e", value=f"**{prof}**", inline=True)
                embed.add_field(name=f"Cours", value=f"Cours de **{matiere}**", inline=True)
            await ctx.send(embed=embed)


    async def print_students(self,ctx, eleve=False, year="2021"):
        liste_info_nul = ["profile_type", "uid", "links", "civility"] #Liste des informations qui ne seront pas affichées
        dico_trad = { #Traduction des libellés
                    "firstname": "Prénom", 
                    "lastname": "Nom de famille",
                    "email": "Adresse e-mail",
                    }
        data = self.get_students(year)
        for classes in data:
            embed=discord.Embed(title=f"Profil de {classes['firstname']} {classes['lastname']}", url="https://myges.fr/student/marks", description="Ici apparaissent les informations de vos camarades de classe", color=0x1f6e9e)
            embed.set_author(name="ESGI | !ma_classe", icon_url="https://zupimages.net/up/21/49/9lc8.png")
            embed.set_thumbnail(url=logo_thumbnail)
            embed.set_footer(text="Made by DAVE")
            ctr = ''
            if eleve == False:
                for key in classes:
                    if f"{ctr}{key}" in liste_info_nul:
                        pass
                    else:
                        if f"{ctr}{key}" == "uid":
                            inline = False
                        else:
                            inline = True
                        embed.add_field(name=f"{ctr}{dico_trad[key]}", value=f"{classes[key]}", inline=inline)
            else:
                embed.add_field(name=f"{ctr}{dico_trad[key]}", value=f"{classes['firstname']}", inline=inline)
                embed.add_field(name=f"{ctr}{dico_trad[key]}", value=f"{classes['lastname']}", inline=inline)
                embed.add_field(name=f"{ctr}{dico_trad[key]}", value=f"{classes['email']}", inline=inline)
            await ctx.send(embed=embed)
    async def print_news(self, ctx):
        data = self.get_news()
        for key in data:
            news_info = data['content']
        for info in data['content']:
            for row in info:
                title_news = info['title']
                author_news = info['author']
                date_news = datetime.fromtimestamp(info["date"] / 1000)
                date_news = date_news.strftime("%d/%m/%Y")

                for i in info['links']:
                    if "https://www.myges.fr/#/actualites" in i['href']:
                        link_news = i['href']
                    #else:
                        #link_news = "https://www.myges.fr/#/actualites"
                ###EMBED###
                embed=discord.Embed(title=title_news, url=link_news, description=f"Voici l'article concernant: {title_news}", color=0x1f6e9e)
                embed.set_author(name="ESGI | !news", icon_url="https://zupimages.net/up/21/51/wv0u.png")
                embed.set_thumbnail(url=logo_thumbnail)
                embed.set_footer(text="Made by DAVE")
                embed.add_field(name=f"Auteur", value=f"{author_news}", inline=True)
                embed.add_field(name=f"Publié le", value=f"{date_news}", inline=True)
                embed.add_field(name=f"Lien vers l'article", value=f"{link_news}", inline=True)
                embed.add_field(name=f"Autres articles", value=f"https://www.myges.fr/#/actualites", inline=False)
                ###EMBED###
        await ctx.send(embed=embed)        
        print(f"L'article a pour titre {title_news}, il a été écrit par {author_news} et a été publié le {date_news}. Lien de l'article ici:{link_news}")


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