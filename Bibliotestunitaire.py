import unittest
from Bibliotheque import Bibliotheque
from Auteur import Auteur
from Emprunteur import Emprunteur



class BibliothequeTestCase(unittest.TestCase):
        def setUp(self):
            """Initialisation avant chaque test"""
            self.ma_biblio = Bibliotheque()
            self.auteur = Auteur("Victor Hugo", "Française")
            self.emprunteur = Emprunteur(101, "Alice Dupont")
            self.ma_biblio.emprunteurs.append(self.emprunteur)

        def test_ajouter_livre(self):
            """Test d'ajout d'un livre"""
            livre = self.ma_biblio.ajouter_livre(1, "Les Miserables", self.auteur)
            self.assertIsNotNone(livre)
            self.assertEqual(len(self.ma_biblio.livres), 1)
            self.assertTrue(livre.disponible)

        def test_emprunter_livre(self):
            """Test d'emprunt d'un livre"""
            livre = self.ma_biblio.ajouter_livre(1, "Les Misérables", self.auteur)
            resultat = self.ma_biblio.emprunter_livre(1, self.emprunteur)
            self.assertTrue(resultat)
            self.assertFalse(livre.disponible)
            self.assertIn(livre, self.emprunteur.livres_empruntees)

        def test_retourner_livre(self):
            """Test de retour d'un livre"""
            livre = self.ma_biblio.ajouter_livre(1, "Les Misérables", self.auteur)
            self.ma_biblio.emprunter_livre(1, self.emprunteur)
            resultat = self.ma_biblio.retourner_livre(1, 101)
            self.assertTrue(resultat)
            self.assertTrue(livre.disponible)
            self.assertNotIn(livre, self.emprunteur.livres_empruntees)



if __name__ == '__main__':
   unittest.main()
