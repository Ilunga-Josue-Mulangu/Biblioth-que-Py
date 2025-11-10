from Livre import Livre
from Emprunteur import Emprunteur
from Auteur import Auteur


class Bibliothèque :
    def __init__(self):
        self.Auteur = []
        self.Livre = []
        self.Emprunteur = []


        def ajouter_livre(id,titre,Auteur):
            self.livres.append(Livre(id,titre,Auteur)) # la methode qui permet d'ajouter un livre



        # la methode qui permet de rechercher un livre
        def rechercher_livre(titre,Auteur):
            for livre in self.livres:
                if livre.titre == titre:
                    if livre.Auteur == Auteur:

                     return livre


        # la methode qui permet d'emprunter un livre'
        def emprunter_livre(id_livre,id_emprunteur):
            for livre in self.livres:
                if livre.id == id_livre:
                    livre.disponible = False
                    self.Emprunteur.append(id_emprunteur)

        # la methode qui permet de retourne un livre
        def retourner_livre(id_livre, id_emprunteur):
            for id_livre in self.Livre:
                if (Livre.id_livre == id_livre and Emprunteur.id_emprunteur == id_emprunteur):
                    Livre.disponible = True
                    return Livre




