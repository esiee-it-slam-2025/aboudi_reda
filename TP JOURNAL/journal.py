"""
Cours "Advanced 2" - Exercice "Journal"
Réalisé par Xxxxx XXXXX
"""

import argparse
import random


articles = [
    {
        "date": "2021-04-06",
        "edition": "national",
        "auteur": "Météo Nationale",
        "titre": "Vague de froid sur le pays",
        "contenu": "Après quelques jours avec des températures supérieures aux normales de saison, un soudain retour à la neige",
    },
    {
        "date": "2021-04-07",
        "edition": "national",
        "auteur": "Agence Presse de France",
        "titre": "Des français dehors car il fait beau",
        "contenu": "Conséquence inattendue du beau temps, les citoyens ont un peu plus envie de sortir dehors par rapport à la normale",
    },
    {
        "date": "2021-04-07",
        "edition": "paca",
        "auteur": "Correspondant à Marseille",
        "titre": "Le bruit des criquets désormais protégés par les droits d'auteurs",
        "contenu": "Toute reproduction artificielle de leur chant dans un magasin nécessitera de financer les associations de protection des criquets du sud",
    },
    {
        "date": "2021-04-06",
        "edition": "idf",
        "auteur": "Rive-Gauche Médias",
        "titre": "Une sixième marque de trotinettes électriques arrive à Paris",
        "contenu": "Par sécurité et pour se démarquer de ses concurrents, le klaxon pourra jouer des mélodies polyphoniques rigolotes",
    },
    {
        "date": "2021-04-06",
        "edition": "paca",
        "auteur": "Léna NICES",
        "titre": "Conséquence du Brexit, la Promenade des Anglais de Nice bientôt renommée",
        "contenu": "La mairie ouvre un vote citoyen pour choisir entre la Promenade de la Pluie ou la Promenade du Pudding",
    },
    {
        "date": "2021-04-06",
        "edition": "idf",
        "auteur": "Colin PERDU",
        "titre": "Jugée irrécupérable, une partie du RER A laissera sa place à un aérotrain",
        "contenu": "Cette idée abandonnée des années 1970 a été jugée plus simple à faire que de réparer toutes les voies entre Cergy et la Défense",
    },
        {
        "date": "2021-04-07",
        "edition": "paca",
        "auteur": "Armand PACHERE",
        "titre": "L'OM va réaliser au Japon un match amical avec le tenant en titre de la J.League 1",
        "contenu": "Le club cite une volonté de resserrer ses liens avec ses fans Japonais, et l'occasion d'y vendre également le premier béret officiel de l'OM",
    },
]

interviews = [
    {
        "date": "2021-04-06",
        "edition": "national",
        "auteur": "test",
        "invite": "Pierre REPUBLICAIN",
        "contenu": "La troisième raison de son retour en politique va vous étonner !",
    },
    {
        "date": "2021-04-06",
        "edition": "idf",
        "auteur": "Léon CULTURA",
        "invite": "Poire",
        "contenu": "Découvrez cette nouvelle chanteuse du Val-de-Marne qui truste le top France du site de streaming Spotizeer",
    },
    {
        "date": "2021-04-07",
        "edition": "national",
        "auteur": "Marcel GASTROMEO",
        "invite": "Léo DIVINCI",
        "contenu": "L'un des plus grands chefs de Bordeaux récompensé pour ses étonnantes et audacieuses ravioles à l'ananas",
    },
]
class ElementJournal:
    def __init__(self, date, edition, auteur, contenu):
        self.date = date
        self.edition = edition
        self.auteur = auteur
        self.contenu = contenu

class Article(ElementJournal):
    def __init__(self, date, edition, auteur, titre, contenu):
        super().__init__(date, edition, auteur, contenu)
        self.titre = titre

class Interview(ElementJournal):
    def __init__(self, date, edition, auteur, invite, contenu):
        super().__init__(date, edition, auteur, contenu)
        self.invite = invite

class Generateur:
    def importer(self, articles, interviews):
        instances_articles = [Article(**article_data) for article_data in articles]
        random.shuffle(interviews)
        instances_interviews = [Interview(**interview_data) for interview_data in interviews]
        return instances_articles, instances_interviews

    # Ajoutez également la méthode filtrer_elements ici
    def filtrer_elements(self, elements, date, edition):
        filtered_elements = []
        for element in elements:
            if element.date == date and element.edition == edition:
                filtered_elements.append(element)
        return filtered_elements

    def afficher(self, elements):
        print(f"==================================")
        print(f"*-*-*-*-*-* LeLutécien *-*-*-*-*-*")
        print(f"==================================")
        random.shuffle(elements)
        for element in elements:
            if isinstance(element, Article):
                print(f"Article: {element.titre}\nAuteur: {element.auteur}\nDate: {element.date}\nContenu: {element.contenu}\n")
            elif isinstance(element, Interview):
                print(f"Interview avec: {element.invite}\nAuteur: {element.auteur}\nDate: {element.date}\nContenu: {element.contenu}\n")
       






if __name__ == "__main__":
    # On crée l'instance de ce qui nous permets d'accepter des arguments à l'aide de la bibliothèque argparse
    parser = argparse.ArgumentParser(description="Génère le journal du jour selon une date et une région.")
    # On demande deux arguments positionnels (obligatoires) lors de l'appel de ce script
    parser.add_argument("date", help="Date du journal à générer, sous le format 'annee-mois-jour'")
    parser.add_argument("edition", help="Édition du journal à générer", choices=["national", "idf", "paca"])
    # Argparse nous renvoie ensuite un objet contenant les valeurs des arguments
    args = parser.parse_args()

    # On crée une instance de Générateur
    generateur = Generateur()
    
    # On appelle la méthode du générateur en lui passant les articles et interviews (importés au tout début de ce fichier)
    articles_filtres, interviews_filtres = generateur.importer(articles, interviews)
    
    # On filtre les éléments selon la date et l'édition spécifiées dans les arguments
    elements = generateur.filtrer_elements(articles_filtres + interviews_filtres, args.date, args.edition)
    
    # On affiche les éléments filtrés
    generateur.afficher(elements)
    with open("credit.txt", "r") as file:
        credit_content = file.read()
        print("\n--- Crédits ---")
        print(credit_content)

