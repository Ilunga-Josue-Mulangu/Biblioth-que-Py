class Emprunteur:
    def __init__(self,id_emprunteur,nom_emprunteur):
        self.id = id_emprunteur # identifiant univique de l'emprunteur'
        self.nom = nom_emprunteur # nom de l'emprunteur'
        self.livres_empruntees = [] # liste des livres empruntes