
class Livre:
    def __init__(self,id,titre,Auteur ):
        self.id = id # identifiant univique du livre
        self.titre = titre # titre du livre
        self.Auteur = [] # Auteur du livre
        self.disponible = True # Par défaut disponible

