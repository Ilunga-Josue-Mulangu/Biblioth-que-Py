from Livre import Livre
from Emprunteur import Emprunteur
from Auteur import Auteur

class Bibliothèque :

    def __init__(self):
        self.Auteur = []
        self.Livre = []
        self.Emprunteur = []

        # la methode qui permet d'ajouter un livre
        def ajouter_livre(id_livre,titre,auteur):
            self.livres.append(Livre(id_livre,titre,auteur))
            print ("Livre" +self.Livre + " ajouté à la bibliothèque")
            return Livre


        # la methode qui permet de rechercher un livre
        def rechercher_livre(titre,auteur):
            for livre in self.livres:
                if livre.titre == titre:
                    if livre.auteur == auteur:
                     return livre


        # la methode qui permet d'emprunter un livre'
        def emprunter_livre(id_livre,id_emprunteur):
            for livre in self.livres:
                if livre.id == id_livre:
                    if livre.disponible :
                        livre.id_emprunteur (id_emprunteur.nom_emprunteur)
                        id_emprunteur.livres_empruntees.append(livre)
                        print(f"{id_emprunteur.nom_emprunteur} a emprunter {livre.titre}")
                        return True
                    else:
                        print("Le livre" + livre.titre + "  est déjà emprunté. ")
                        return False
            print ("Livre avec id " + {id_livre} + " non trouvé.")
            return False

        # la methode qui permet de retourne un livre
        def retourner_livre(id_livre , id_emprunteur):

            livre_Disponible = None
            for livre in self.livres:
                if livre.id == id_livre:
                    livre_Disponible = livre
                    break


            if livre_Disponible is None:
                print (f"Erreur: Livre avec l'id {id_livre} introuvable.")
                return False

            # Rechercher l'emprunteur
            emprunteur_trouve = None
            for emprunteur in self.emprunteurs:
                if emprunteur.id == id_emprunteur:
                    emprunteur_trouve = emprunteur
                    break


            if emprunteur_trouve is None:
                print(f"Erreur: Emprunteur avec l'id {id_emprunteur} introuvable.")
                return False

            if livre_Disponible not in emprunteur_trouve.livres_empruntes:
                print(f"Erreur :{emprunteur_trouve.nom_emprunteur} n'a pas emprunter le livre {livre_Disponible.titre}.")
                return False

            livre_Disponible.disponible = True
            emprunteur_trouve.livres_empruntees.remove(livre_Disponible)
            print(f"{emprunteur_trouve.nom_emprunteur} a retourné '{livre_Disponible.titre}'")
            return True

