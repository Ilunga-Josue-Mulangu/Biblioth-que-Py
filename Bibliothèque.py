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


    Bibliothèque = Bibliothèque()

    B1 = Auteur("Josue", "Zambien", "Bernard")
    B2 = Auteur("Joshe", "Congolais", "BYPYTHON")
    B3 = Auteur("Joseph", "Americain", "Cycy")
    B4 = Auteur("Joy", "Marocain", "Au paysical")
    B5 = Auteur("Josephine", "Congolais", "Python")
    B6 = Livre("FAB123","La vie est belle",B1)
    B7 = Livre("FAB456","La vie au pays de blancs",B2)
    B8 = Livre("FAB789","La vie au pays de geants",B3)
    B9 = Livre("FAB1011","La vie au pays de Mzee",B4)
    B10 = Livre("FAB1213","La vie au pays de blancs",B5)
    B11 = Livre("FAB1415","La vie au pays de lumumba",B6)
    B12 = Livre("FAB1617","La vie au pays de kasavubu",B7)

    B13 = Emprunteur("P001A","josue","La vie est belle")
    B14 = Emprunteur("P002B","josh","La vie au pays de blancs")
    B15 = Emprunteur("P003C","joseph","La vie au pays de geants")
    B16 = Emprunteur("P004D","josephine","La vie au pays de lumumba")
    B17 = Emprunteur("P005E","joshe","La vie au pays de kasavubu")
    B18 = Emprunteur("P006F","joy","La vie au pays de Mzee")
    Bibliothèque.ajouter_livre(203,"La vie est belle",B1)
    Bibliothèque.ajouter_livre(204,"La vie au pays de blancs",B2)
    Bibliothèque.ajouter_livre(205,"La vie au pays de geants ",B3)
    Bibliothèque.ajouter_livre(206,"La vie au pays de blancs",B4)

