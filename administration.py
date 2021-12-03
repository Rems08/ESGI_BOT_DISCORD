
class Eleve:

    def __init__(self, nom, prenom, age, classe, school, delegue=False):
        self.nom = nom #nom de famille de l'eleve
        self.prenom = prenom #Prenom de l'eleve
        self.age = age #Age de l'eleve
        self.classe = classe #Classe de l'eleve exemple: ESGI1
        self.school = school #nom de l'ecole exemple ESGI
        self.delegue = delegue #Statut de delegue ou pas

class Prof:

    def __init__(self, nom, prenom, age=None):
        self.nom = nom #nom de famille de l'enseignant 
        self.prenom = prenom #Prenom de l'enseignant
        self.age = age #Age de l'enseignant (facultatif)
        self.classes = [] #Liste des classes que gèrent les profs