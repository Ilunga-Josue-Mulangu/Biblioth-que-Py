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


        if __name__ == "__main__":
            biblio = Bibliothèque

            print("CREATION DES AUTEURS")

            # Créer des auteurs
            auteur1=Auteur("Josue","Congolais")
            auteur2 = Auteur("George Orwell", "Britannique")
            auteur3= Auteur("Victor Hugo", "Français")
            auteur4 = Auteur("Antoine de Saint-Exupéry", "Français")


            print("CREATION DES LIVRES")
            biblio.ajouter_livre("L001", "1984", auteur1)
            biblio.ajouter_livre("L002", "La Ferme des animaux", auteur4)
            biblio.ajouter_livre("L003", "Les Misérables", auteur2)
            biblio.ajouter_livre("L004", "Notre-Dame de Paris", auteur2)
            biblio.ajouter_livre("L005", "Le Petit Prince", auteur3)

            print("--- Ajouter un livre avec ID existant ---")
            biblio.ajouter_livre("L001", "Autre livre", auteur1)

            print("\n" + "=" * 60)
            print("CRÉATION DES EMPRUNTEURS")
            print("=" * 60)

            # Créer et ajouter des emprunteurs
            emprunteur1 = Emprunteur("E001", "Alice Dupont")
            emprunteur2 = Emprunteur("E002", "Bob Martin")
            emprunteur3 = Emprunteur("E003", "Charlie Lefebvre")

            biblio.emprunteurs.append(emprunteur1)
            biblio.emprunteurs.append(emprunteur2)
            biblio.emprunteurs.append(emprunteur3)

            print(f" {emprunteur1.nom} ajouté")
            print(f" {emprunteur2.nom} ajouté")
            print(f" {emprunteur3.nom} ajouté")

        print("\n" + "=" * 60)
        print("RECHERCHE DE LIVRES")
        print("=" * 60)

        print("\n--- Recherche: 'vie' ---")
        resultats = biblio.rechercher_livre("vie")
        for livre in resultats:
            print(f"  {livre}")

        print("\n--- Recherche: 'Hugo' ---")
        resultats = biblio.rechercher_livre("Hugo")
        for livre in resultats:
            print(f"  {livre}")

        print("\n--- Recherche: 'Python' (aucun résultat) ---")
        biblio.rechercher_livre("Python")

        print("\n" + "=" * 60)
        print("EMPRUNTS DE LIVRES")
        print("=" * 60)

        # Emprunts normaux
        biblio.emprunter_livre("L001", "E001")  # Alice emprunte 1984
        biblio.emprunter_livre("L003", "E001")  # Alice emprunte Les Misérables
        biblio.emprunter_livre("L002", "E002")  # Bob emprunte La Ferme des animaux

        print("\n--- Test: Emprunter un livre déjà emprunté ---")
        biblio.emprunter_livre("L001", "E002")  # Bob essaie d'emprunter 1984

        print("\n--- Test: Emprunter un livre inexistant ---")
        biblio.emprunter_livre("L999", "E001")

        print("\n--- Test: Emprunteur inexistant ---")
        biblio.emprunter_livre("L005", "E999")

        print("\n" + "=" * 60)
        print("AFFICHAGE DES EMPRUNTS")
        print("=" * 60)
        print(emprunteur1)
        print(f"  Livres: {[livre.titre for livre in emprunteur1.livres_empruntes]}")

        print("\n" + "=" * 60)
        print("RETOUR DE LIVRES")
        print("=" * 60)

        # Retour normal
        biblio.retourner_livre("L001", "E001")  # Alice retourne 1984

        print("\n--- Test: Retourner un livre non emprunté ---")
        biblio.retourner_livre("L005", "E001")  # Alice n'a pas emprunté Le Petit Prince

        print("\n--- Test: Retourner un livre inexistant ---")
        biblio.retourner_livre("L999", "E001")

        print("\n" + "=" * 60)
        print("CATALOGUE FINAL")
        print("=" * 60)
        for livre in biblio.livres:
            print(livre)

        print("\n" + "=" * 60)
        print("AUTEURS ET LEURS OEUVRES")
        print("=" * 60)
        for auteur in biblio.auteurs:
            print(auteur)

