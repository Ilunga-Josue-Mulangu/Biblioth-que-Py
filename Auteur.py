class Auteur:
    def __init__(self,nom,nationalite):
        self.nom = nom # nom de l'auteur'
        self.nationalite = nationalite # nationalite de l'auteur'
        self.oeuvres =  [] # liste des oeuvres de l'auteur'

    def __str__(self):
        if self.oeuvres:
            titres = ", ".join([oeuvre.titre for oeuvre in self.oeuvres])
            return f"{self.nom} ({self.nationalite}) - Oeuvres: {titres}"
        else:
            return f"{self.nom} ({self.nationalite}) - Aucune oeuvre "









