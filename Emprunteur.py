class Emprunteur:
    def __init__(self,id_emprunteur,nom_emprunteur):
        self.id = id_emprunteur # identifiant univique de l'emprunteur'
        self.nom_emprunteur = nom_emprunteur # nom de l'emprunteur'
        self.livres_empruntees = [] # liste des livres empruntes

    def __str__(self):
        nb_livres = len(self.livres_empruntees)
        return f"{self.nom_emprunteur} (ID: {self.id}) - {nb_livres} livre(s) emprunté(s)"
