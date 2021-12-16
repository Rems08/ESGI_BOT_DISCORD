#!/usr/bin/env python3

import requests
from urllib.parse import urlsplit, parse_qs
import base64
import time
import json
from datetime import datetime

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
    
    def get_info(self):
        return requests.get(f"{self.actionurl}/me/profile", headers=self.token).json()["result"]
    def get_agenda(self, start, end):
        return requests.get(f"{self.actionurl}/me/agenda?start={start}&end={end}", headers=self.token).json()["result"]
    
    def get_absences(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/absences", headers=self.token).json()["result"]

    def get_courses(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/courses", headers=self.token).json()["result"]

    def get_grades(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/grades", headers=self.token).json()["result"]

    def get_partners(self):
        return requests.get(f"{self.actionurl}/me/partners", headers=self.token).json()["result"]

    def get_school(self):
       return requests.get(f"{self.actionurl}/me/schools", headers=self.token).json()["result"][0]

    def get_students(self, year):
        return requests.get(requests.get(f"{self.actionurl}/me/{year}/classes", headers=self.token).json()["result"][0]["links"][1]["href"], headers=self.token).json()["result"]

    # All method used for display api informations
    def print_info(self):
        data = self.get_info()
        for key in data:
            if key == 'mailing':
                break
            print(f"{key} : {data[key]}")

    def print_agenda(self, start, end):
        data = self.get_agenda(start, end)
        for row in data:
            ctr = ''
            debut_du_cours = datetime.fromtimestamp(row["start_date"] / 1000)
            fin_du_cours = datetime.fromtimestamp(row["end_date"] / 1000)
            prof = row["teacher"]
            matiere = row["name"]
            type_de_cours = row["modality"]
            room_info = row['rooms']
            for key in room_info:
                room_number = key['name']
                etage = key['floor']
                campus = key['campus']
            print(f"Le prochain cours aura lieu au campus {campus}, à l'étage {etage} salle numéro {room_number}")
            print(f"Il commencera à {debut_du_cours} et finira à {fin_du_cours}, il sera dirigé par {prof} qui vous enseignera {matiere}")

    def print_absences(self, start, end):
        for row in self.get_absences(start, end):
            date = time.strftime('%d-%m-%Y %H:%M', time.localtime(int(str(row['date'])[:-3])))
            just = "Jusitifiée" if row["justified"] else "Non justifiée"
            print(f'{date}\t{just}\t{row["course_name"]}')

    def print_courses(self, year):
        data = self.get_courses(year)
        for classes in data:
            ctr = ''
            for key in classes:
                print(f"{ctr}{key} : {classes[key]}")
                ctr = '\t'
            print()

    def print_grades(self, year):
        data = self.get_grades(year)
        for classes in data:
            ctr = ''
            for key in classes:
                print(f"{ctr}{key} : {classes[key]}")
                ctr = '\t'
            print()

    def print_partners(self):
        data = self.get_partners()
        for row in data:
            ctr = ''
            for key in row:
                print(f"{ctr}{key} : {row[key]}")
                ctr = '\t'
            print()

    def print_school(self):
        data = self.get_school()
        for row in data:
            print(f"{row}: {data[row]}")

    def print_students(self, year):
        data = self.get_students(year)
        for classes in data:
            ctr = ''
            for key in classes:
                print(f"{ctr}{key} : {classes[key]}")
                ctr = '\t'
            print()

def main():
    myges = MYGES("6666", "rmassiet", "x1oypZ9L$^9aj8XwFDslUF0zs" )
    print("""
    88888888b .d88888b   .88888.  dP     888888ba   .88888.  d888888P 
    88        88.    "' d8'   `88 88     88    `8b d8'   `8b    88    
   a88aaaa    `Y88888b. 88        88    a88aaaa8P' 88     88    88    
    88              `8b 88   YP88 88     88   `8b. 88     88    88    
    88        d8'   .8P Y8.   .88 88     88    .88 Y8.   .8P    88    
    88888888P  Y88888P   `88888'  dP     88888888P  `8888P'     dP    
    ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
    """)
    myges.print_agenda("1633071600000", "1633107600000")
    #myges.print_info()
if __name__ == '__main__':
    main()