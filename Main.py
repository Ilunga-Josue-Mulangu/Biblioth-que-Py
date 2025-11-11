from Bibliotheque import Bibliotheque
from Auteur import Auteur
from Emprunteur import Emprunteur

#  # Créer une bibliothèque
ma_biblio = Bibliotheque()


# Créer des auteurs



auteur1 = Auteur("Victor Hugo", "Française")
auteur2 = Auteur("Albert Camus", "Française")
auteur3 = Auteur("Sony Labou Tansi","Congolaise")

# Ajouter des livres à la bibliothèque

print("\n------Ajouter des livres à la bibliothèque--------\n")
livre1 = ma_biblio.ajouter_livre(1, "Les Misérables", auteur1)
livre2 = ma_biblio.ajouter_livre(2, "L'Étranger", auteur2)
livre3 = ma_biblio.ajouter_livre(3, "Notre-Dame de Paris", auteur1)
livre4 = ma_biblio.ajouter_livre(4,"La vie et demie",auteur3)
livre5 = ma_biblio.ajouter_livre(3, "Notre-Dame de Paris", auteur1)

# Créer des emprunteurs


emprunteur1 = Emprunteur(101, "Alice Dupont")
emprunteur2 = Emprunteur(102, "Bob Martin")
emprunteur3 = Emprunteur(103, "Charlie Dumont")

# Ajouter les emprunteurs à la bibliothèque

ma_biblio.emprunteurs.append(emprunteur1)
ma_biblio.emprunteurs.append(emprunteur2)
ma_biblio.emprunteurs.append(emprunteur3)

# Afficher les livres disponibles
print("\n-----------Livres dans la bibliothèque -----------\n")
for livre in ma_biblio.livres:
    print(livre)

# Emprunter un livre
print("\n------ Emprunts ------\n")
ma_biblio.emprunter_livre(1, emprunteur1)
ma_biblio.emprunter_livre(2, emprunteur2)
ma_biblio.emprunter_livre(1, emprunteur2)
ma_biblio.emprunter_livre(3, emprunteur3)

# Afficher l'état des livres
print("\n------État des livres ------\n")
for livre in ma_biblio.livres:
    print(livre)

# Afficher les emprunteurs
print("\n------ Emprunteurs ------\n")
for emprunteur in ma_biblio.emprunteurs:
    print(emprunteur)

# Rechercher un livre
print("\n------ Recherche ------\n")
livre_trouve = ma_biblio.rechercher_livre("L'Étranger", auteur2)
if livre_trouve:
    print(f"Trouvé: {livre_trouve}")



# Retourner un livre
print("\n------ Retours ------\n")


ma_biblio.retourner_livre(3, 103)




# Afficher l'état final
print("\n------- État final ------\n")
for livre in ma_biblio.livres:
    print(livre)













