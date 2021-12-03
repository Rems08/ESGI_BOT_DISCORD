import requests #Enable HTTP requests
from requests import*
from bs4 import BeautifulSoup #Find Elements on website 
import mechanize #Permet de remplir les formulaires automatiquement
def afficher_notes():
    url = "https://myges.fr/student/home;jsessionid=BE1E52FB1A10F454DFE273F0388E54A1" #URL du site à parcourir
    user = ""
    mdp = ""
    page = requests.get(url, auth=('user', 'mdp'))
    code_connexion = str(page.status_code)
    if code_connexion == "200":
        print("Connexion success")
        print("Status code: ", page.status_code)
    else:
        print("Connexion failed")
        print(f"ERROR: {code_connexion}")
        exit()
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title) #Permet d'afficher toute la page
    print("Récupération de vos notes en cours...")
    liste = soup.find_all("span", class_="ui-column-title")
    div_notes = soup.find_all("tr", role="row")
    for i in liste:
        if i == None:
            print("La case est vide")
        else:
            print(i.string, end=" ")
    
def mist(): #Affiche les ABSENCES ET les RETARDS
    print("test")
afficher_notes()

