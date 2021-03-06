import requests #Enable HTTP requests
from requests import*
from bs4 import BeautifulSoup #Find Elements on website 
import mechanize #Permet de remplir les formulaires automatiquement
def afficher_notes():
    #Partie connexion
    url = "https://myges.fr/student/student-teacher-directory;jsessionid=F02C85E333FEC9828E3291323220168C" #URL du site à parcourir
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


    #Partie scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title) #Permet d'afficher toute la page
    print("Récupération de vos notes en cours...")
    matrice_notes = []
    #Récupération des titres
    liste_titres = soup.find_all("span", class_="ui-column-title")
    div_notes = soup.find_all("tr", role="row")
    for i in liste_titres:
        if i == None:
            print("La case est vide")
        else:
            print(i.string, end=" ")

    print("\nSTOP TITRE\n")
    #Recuperation des matieres
    notes = soup.find_all("tr", class_="ui-widget-content")
    for i in notes:
        
        if i == None:
            print("La case est vide")
        else:
            print(i.td.string)

def mist(): #Affiche les ABSENCES ET les RETARDS
    print("test")

def infos_profs():
    #Partie connexion
    url = "https://myges.fr/student/student-teacher-directory;jsessionid=F02C85E333FEC9828E3291323220168C" #URL du site à parcourir
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


    #Partie scrapping
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title) #Permet d'afficher toute la page
    print("Récupération du nom de vos profs en cours...")
    matrice_notes = []
    #Récupération des titres
    liste_profs = soup.find_all("div", class_="ui-outputpanel ui-widget")
    for i in liste_profs:
        print(i.string)
infos_profs()

#Notes <tr data-ri="0" class="ui-widget-content ui-datatable-even odd-row" role="row">
#Abscences s<tr data-ri="1" class="ui-widget-content ui-datatable-odd even-row" role="row">