
class Livre:
    def __init__(self,id_livre,titre,Auteur ):
        self.id = id_livre # identifiant univique du livre
        self.titre = titre # titre du livre
        self.Auteur = [] # Auteur du livre
        self.disponible = True # Par défaut disponible

