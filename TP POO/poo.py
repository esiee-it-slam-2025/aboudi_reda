import random

class Creature:
    def __init__(self, nom, pv, degats, etat=None):
        self.nom = nom
        self.pv = pv
        self.degats = degats
        self.etat = etat

    def rafale(self, cible):
        cible.pv -= self.degats
        print(f"{self.nom} attaque {cible.nom}.")

    def bombardement(self, cible):
        cible.etat = "explosé"
        print(f"{self.nom} utilise un bombardement sur {cible.nom}.")

class Hero(Creature):
    def __init__(self, nom, degats, pm):
        super().__init__(nom, 100, degats)
        self.pm = pm

    def missile(self, cible):
        if self.pm >= 1:
            cible.pv -= self.degats * 2
            self.pm -= 1
            print(f"{self.nom} lance un missile sur {cible.nom}.")
        else:
            print("Pas assez de roquets.")

# Init classes
armes = {
    1: {"nom": "ERYX", "degats": random.randint(9, 15)},
    2: {"nom": "SCAR-H PR", "degats": random.randint(5, 8)},
    3: {"nom": "MP-5", "degats": random.randint(12, 21)},
    4: {"nom": "AK-47", "degats": random.randint(22, 30)}
}

# Début du jeu
def intro():
    print("===============================================================")
    print("|| Bienvenue dans le système de combat POO (ARMÉE DE TERRE FRANÇAISE) ! ||")
    print("===============================================================")
    nom_hero = input("\nChoisissez le nom de votre militaire: ")
    print("Choisissez votre arme:")
    for numero, arme in armes.items():
        print(f"{numero}. {arme['nom']}")
    arme_choisie = input("Votre choix (entrez le numéro de l'arme): ")
    while not arme_choisie.isdigit() or int(arme_choisie) not in armes:
        print("Arme invalide.")
        arme_choisie = input("Choisissez votre arme (entrez le numéro de l'arme): ")

    # Récupération des informations sur l'arme choisie par ton joueur
    arme_infos = armes[int(arme_choisie)]
    # Création du militaire avec le prénom, les dégâts de l'arme choisie et 100 pv
    hero = Hero(nom_hero, arme_infos["degats"], 5)
    # Mise en place des usa avec une vie aléatoires entre 60 et 150
    monstre = Creature("USA", random.randint(60, 110), 15)

    combat(hero, monstre)

# Boucle de la guerre
def combat(hero, monstre):
    tour_hero = True
    print("La guerre commence!")

    while hero.pv > 0 and monstre.pv > 0:
        if tour_hero:
            print("\nTour des Français:")
            action = input("Choisissez votre action (rafale / missile): ")
            while action not in ["rafale", "missile"]:  
                print("Action invalide.")
                action = input("Choisissez votre action (rafale / missile): ")
                
            if action == "rafale":
                hero.rafale(monstre)
            elif action == "missile":
                hero.missile(monstre)
        else:
            print("\nTour des USA :")
            monstre.rafale(hero)

        tour_hero = not tour_hero

    if hero.pv <= 0:
        print("La France a été vaincue. Les USA gagne!")
    else:
        print("Les USA ont été vaincus. La France gagne!")

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")