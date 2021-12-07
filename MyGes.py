#!/usr/bin/env python3

import requests
from urllib.parse import urlsplit, parse_qs
import base64
import json
import time


class MYGES:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.actionurl = "https://api.kordis.fr"
        self.token = self.get_token()

    def get_token(self):
        urltoken = 'https://authentication.kordis.fr/oauth/authorize?response_type=token&client_id=skolae-app'
        token = base64.b64encode(f"{self.username}:{self.password}".encode()).decode('UTF-8')
        headers = {"Authorization": f"Basic {token}"}
        try:
            r = requests.get(urltoken, headers=headers)
        except requests.exceptions.InvalidSchema as e:
            urltokenreturn = repr(e).split("'")[1].replace("#", '?')

        tokenret = {k: v[0] for k, v in parse_qs(urlsplit(urltokenreturn).query).items()}
        return {"Authorization" : f"{tokenret['token_type']} {tokenret['access_token']}"}
    
    def get_absences(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/absences", headers=self.token).json()
        

    def print_absences(self, year):
        jsondata = self.get_absences(year)
        for row in jsondata["result"]:
            date = time.strftime('%d-%m-%Y %H:%M', time.localtime(int(str(row['date'])[:-3])))
            just = "Jusitifiée" if row["justified"] else "Non justifiée"
            print(f'{date}\t{just}\t{row["course_name"]}')
    
    def get_agenda(self, start, end):
        return requests.get(f"{self.actionurl}/me/agenda?start={start}&end={end}", headers=self.token)

    def get_grades(self, year):
        return requests.get(f"{self.actionurl}/me/{year}/grades", headers=self.token).json()
    
    def print_grades(self, year):
         jsondata = self.get_grades(year)
         for row in jsondata["result"]:
            nom_cours = row["course"]
            nom_prof = row["teacher_last_name"]
            grades = row["grades"] if row["grades"] else "Pas de note"
            print(f'{nom_cours}\t{nom_prof}\t{grades}')

def main():
    myges = MYGES("", "")
    myges.print_absences("2021")
    myges.print_grades("2021")
if __name__ == '__main__':
    main()
