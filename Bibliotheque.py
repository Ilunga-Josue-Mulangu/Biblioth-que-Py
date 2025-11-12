from Livre import Livre


class Bibliotheque :

        def __init__(self):
          self.auteurs = []
          self.livres= []
          self.emprunteurs = []

        # la methode qui permet d'ajouter un livre
        def ajouter_livre(self, id_livre, titre, auteur):
            nouveau_livre = Livre(id_livre, titre, auteur)
            self.livres.append(nouveau_livre)
            auteur.oeuvres.append(nouveau_livre) # permet d'ajouter le livere aux oeuvres de l'auteur'
            print(f"Livre '{titre}' a été ajouté à la bibliothèque ")
            return nouveau_livre


            # la methode qui permet de rechercher un livre
        def rechercher_livre(self,titre, auteur):
                for livre in self.livres:
                    if livre.titre == titre:
                        if livre.auteur == auteur:
                             return livre

                return None


        # la methode qui permet d'emprunter un livre
        def emprunter_livre(self,id_livre,id_emprunteur):
            for livre in self.livres:
                if livre.id == id_livre:
                    if livre.disponible :
                        livre.disponible = False
                        id_emprunteur.livres_empruntees.append(livre)
                        print(f"{id_emprunteur.nom_emprunteur} a emprunté {livre.titre}")
                        return True
                    else:
                        print(f"{id_emprunteur.nom_emprunteur} Le livre {livre.titre} est déjà emprunté.")

                        return False
            print(f"Livre avec id {id_livre} non trouvé.")
            return False



        # la methode qui permet de retourne un livre
        def retourner_livre(self,id_livre , id_emprunteur):

            livre_Disponible = None
            for livre in self.livres:
                if livre.id == id_livre:
                    livre_Disponible = livre
                    break

            if livre_Disponible is None:
                print (f"Erreur: Livre avec l'id {id_livre} introuvable.")
                return False

            #  La methode qui permet de Rechercher l'emprunteur
            emprunteur_trouve = None
            for emprunteur in self.emprunteurs:
                if emprunteur.id == id_emprunteur:
                    emprunteur_trouve = emprunteur
                    break

            if emprunteur_trouve is None:
                print(f"Erreur: Emprunteur avec l'id {id_emprunteur} introuvable.")
                return False

            if livre_Disponible not in emprunteur_trouve.livres_empruntees:
                print(f"Erreur :{emprunteur_trouve.nom_emprunteur} n'a pas emprunter le livre {livre_Disponible.titre}.")
                return False

            livre_Disponible.disponible = True
            emprunteur_trouve.livres_empruntees.remove(livre_Disponible)
            print(f"{emprunteur_trouve.nom_emprunteur} a retourné '{livre_Disponible.titre}'")
            return True

