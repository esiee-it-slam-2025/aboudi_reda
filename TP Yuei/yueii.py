import time


personnage = {
    "PV": 70
}

pouvoirs = [
    "Un pour Tous",
    "Contrôler la gravité",
    "Faire des explosions",
    "Être une grenouille",
    "Créer des objets",
    "Mi-chaud mi-froid",
    "Aller très vite",
    "Fléau des Âmes Errantes",
    "Bannissement vers le Néant",
    "Éclat de l'Aurore Éternelle"
]
pouvoir_degats = {
    "Un pour Tous": 12,
    "Contrôler la gravité": 8,
    "Faire des explosions": 13,
    "Être une grenouille": 4,
    "Créer des objets": 9,
    "Mi-chaud mi-froid": 13,
    "Aller très vite": 11,
    "Fléau des Âmes Errantes": 16,
    "Bannissement vers le Néant": 100000,
    "Éclat de l'Aurore Éternelle": 19
}


plats = {
    "Ramen": {"Nouilles": 1, "Bouillon": 1, "Oeuf": 1, "Viande": 1},
    "Onigiri": {"Riz": 1, "Algues": 1, "Saumon": 1},
    "Udon": {"Nouilles": 1, "Bouillon": 1, "Poulet": 1, "Oignon": 1},
    "Curry": {"Riz": 1, "Curry": 1, "Poulet": 1, "Carottes": 1}
}  # Liste des plats et de leur ingrédients

plats_liste = list(plats.keys())  # Liste des noms de plats
plats_stock = {plat: 2 for plat in plats_liste}  # Initialisation du stock de chaque plat
argent = 10000  # Argent du joueur pour manger à la cafeteria


objets_cles = []
objets_badge = []
inventaire = {}

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************


def proposer_lieux(mots_cles):
    message = "│[Lieux] "
    for lieu in mots_cles:
        message += lieu + ", "
    print(message[:-2])


def proposer_actions(actions):
    message = "│[Actions] "
    for i, action in enumerate(actions, 1):
        message += f"{i}. {action}, "
    print(message[:-2])

def recuperer_objet_special(): # Création de trois objet qui servent à donner des boost au joueur --> voir def_combat 
    objet_special = random.choice(["Livre ancien", "Amulette mystique", "Cristal magique"])
    print(f"Vous avez trouvé un objet spécial : {objet_special} !")
    objets_cles.append(objet_special)

# ********************************************************************************
# INTRODUCTION
# ********************************************************************************

def intro():
    print("      ////////    ///  ///")
    print("      ///  ///    ///  ///")
    print("      ////////    ///  ///")
    print("      ///  ///    ////////")
    print("===============================")
    print("|| Bienvenue au lycée A.U. ! ||")
    time.sleep(1)
    print("Le monde est en proie au chaos, ravagé par les forces du mal. À Yuei, l'école des héros, votre mission commence. Devenez le héros que le monde attend, combattez les ténèbres et ramenez la lumière.")
    print("===============================")
    time.sleep(1)
    print("Commençons par créer ton personnage.")

    prenom = input("Quel est ton prénom ? ")
    personnage["prénom"] = prenom
    age = input("Quel âge as-tu ? ")
    personnage["Age"] = age


    # Afficher la liste des pouvoirs disponibles avec leur position dans la liste
    print("Voici la liste des pouvoirs disponibles :")
    for i, pouvoir in enumerate(pouvoirs, 1):
        print(f"{i}. {pouvoir}")

    # Demander au joueur de choisir un pouvoir en saisissant son numéro
    pouvoir_index = int(input("Choisissez un pouvoir en saisissant son numéro : "))
    while pouvoir_index < 1 or pouvoir_index > len(pouvoirs):
        print("Numéro de pouvoir invalide.")
        pouvoir_index = int(input("Choisissez un pouvoir en saisissant son numéro : "))
    personnage["Pouvoir"] = pouvoirs[pouvoir_index - 1]

    # Afficher les informations du personnage créé
    print("\nFélicitations ! Voici les informations de ton personnage :")
    for cle, valeur in personnage.items():
        print(f"{cle}: {valeur}")

    lieu_hall()

# ********************************************************************************
# LIEUX
# ********************************************************************************


def lieu_hall():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Vous êtes dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["Quitter", "Observer", "Aller dans la classe 1-A", "Aller dans le couloir du rdc"])
        proposer_lieux(["couloir du RDC"])
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

        if reponse.lower() == "1" or reponse.lower() == "quitter":
            print("Vous avez quitté le jeu.")
            break
        elif reponse.lower() == "2" or reponse.lower() == "observer":
            observer()
            if random.random() < 0.9:  # Probabilité de 70% de trouver un objet spécial
                recuperer_objet_special()
        elif reponse.lower() == "3" or reponse.lower() == "aller dans la classe 1-a":
            lieu_classe_1a()
        elif reponse.lower() == "4" or reponse.lower() == "aller dans le couloir du rdc":
            lieu_couloir_rdc()
            break

def observer():
    print("Vous observez une jeune fille magnifique devant vous...")
    print("Voulez-vous aller lui parler? (oui/non)")
    reponse = input("├─> ").lower()

    if reponse == "oui":
        parler_a_fille()
    elif reponse == "non":
        print("Vous décidez de ne pas aller lui parler pour le moment.")
    else:
        print("Réponse invalide. Veuillez répondre 'Oui' ou 'Non'.")

def parler_a_fille():
    print("Vous: Bonjour, je suis", personnage["prénom"], "Comment tu t'appelles?")
    print("Fille: Bonjour", personnage["prénom"], "Je m'appelle Orihime. Tu viens d'intégrer l'école ?")
    reponse = input("├─> ").lower()
    if reponse == "oui":
        parler_a_fille1(personnage["PV"])  # Passer player_pv en argument
    elif reponse == "non":
        print("Orihime vous regarde bizarrement")
    else:
        print("Réponse invalide. Veuillez répondre 'Oui' ou 'Non'.")

def parler_a_fille1(player_pv):  # Utilisation de player pour jouer sur la vie du perso
    print("Vous: Enchanté, Orihime. Pourrais-tu m'indiquer la salle de classe 1-A ?")
    print("Orihime: Pardon ? Tu fais partie de cette classe.... ?")
    print("oui/non")
    reponse = input("├─> ").lower()

    if reponse == "oui":
        player_pv = la_gifle(player_pv)
    elif reponse == "non":
        print("Mmmmh, rattrape-toi")
    else:
        print("Réponse invalide. Veuillez répondre 'Oui' ou 'Non'.")
    return player_pv

def la_gifle(player_pv): # Le joueur perd 10pv avec cette fonction
    print("Orihime s'enfuit et vous bouscule viollement, vous perdez 10 points de vie.")
    player_pv -= 10
    print("Je devrais surement aller la chercher !")
    print("Elle semblait s'en aller vers le 1ère étage...")
    return player_pv


def lieu_couloir_rdc():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est le couloir du rez-de-chaussée.")
    print("On y trouve la classe 1-A, et le hall de l'école.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["Observer", "Aller dans la classe 1-A", "Aller dans le hall", "Aller au couloir du 1ère étage"])
        proposer_lieux(["couloir du RDC"])
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

        if reponse.lower() == "1" or reponse.lower() == "observer":
            print("Vous voyez Orihime dans un coin du couloir...")
            print("Vous allez à sa rencontre...")
            time.sleep(2) # Mise en place d'un délai pour l'affichage à l'écran
            print("Elle s'enfuit au première étage...")
        elif reponse.lower() == "2" or reponse.lower() == "aller dans la classe 1-a":
            lieu_classe_1a()
        elif reponse.lower() == "3" or reponse.lower() == "aller dans le hall":
            lieu_hall()
        elif reponse.lower() == "4" or reponse.lower() == "aller au couloir du 1ère étage":
            lieu_couloir_1er_etage()
        
def lieu_classe_1a():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la classe 1-A.")
    
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["Sortir dans le hall", "Sortir dans le couloir", "Étudier les matières scolaires", "Demander le badge de combat", "Montrer ces badges de combats"])
        reponse = input("├─> ")
        print("└────────────────────────────────────────")
        
        if reponse.lower() == "1" or reponse.lower() == "sortir dans le hall":
            lieu_hall()
        elif reponse.lower() == "2" or reponse.lower() == "sortir dans le couloir":
            lieu_couloir_rdc()
        elif reponse.lower() == "3" or reponse.lower() == "étudier les matières scolaires":
            etudier_matiere()
        elif reponse.lower() == "4" or reponse.lower() == "Demander le badge au professeur":
            demander_passe()
        elif reponse.lower() == "5" or reponse.lower() == "Montrer ces badges au professeur":
            montrer_badges()

def montrer_badges():
    nb_badges = len(objets_badge) # permet de savoir le nombre de badge dans l'inventaire
    print(f"Vous montrez au professeur que vous avez {nb_badges} badges.")

    if "passe" in objets_badge:
        print("Félicitations ! Vous avez collecté trois badges et réussi le jeu.")
        print("Fin du jeu.")
        exit()
    else:
        print("Vous n'avez pas encore suffisamment de badges pour réussir le jeu.")

        
def demander_passe():
    print("Vous demandez le passe au professeur.")
    if "passe" not in objets_badge:
        print("Le professeur vous remet le passe.")
        objets_badge.append("passe")
        # Ajoutez le badge dans les objets clés
        objets_badge.append("badge")
    else:
        print("Vous avez déjà reçu le passe.")


class Matiere: # Création de matiere pour les cours 
    def __init__(self, nom):
        self.nom = nom
anglais = Matiere("Anglais")
japonais = Matiere("Japonais")
combat = Matiere("Combat")
camouflage = Matiere("Camouflage")

def etudier_matiere():
    print("Quelle matière souhaitez-vous étudier?")
    print("1. Anglais")
    print("2. Japonais")
    print("3. Combat")
    print("4. Santé des héros")
    choix = input("├─> ")
    
    if choix == "1":
        print("In this English course, you'll enhance your language skills through practical exercises and discussions on various topics, enabling you to communicate confidently and accurately in English..")
    elif choix == "2":
        print("この日本語コースでは、インタラクティブなアクティビティやケーススタディを通じて、言語スキルと日本文化の理解を深めます。")
    elif choix == "3":
        print("Dans notre cours sur le combat rapproché à l'école Yuei, nous étudierons les techniques de base telles que les coups de poing, les coups de pied, les blocages et les esquives, ainsi que l'adaptation des pouvoirs individuels à ce style de combat. Les étudiants apprendront également l'importance de la discipline mentale et de la pratique régulière pour devenir des combattants compétents et efficaces.")
    elif choix == "4":
        print("Souhaitez-vous suivre le cours de santé des héros ? (oui/non)")
        choix_sante = input("├─> ").lower()
        if choix_sante == "oui":
            print("Vous choisissez de suivre le cours de santé des héros.")
            personnage["PV"] += 20  # Ajout des 20 points de vie
            print("Bravo ! Vous maîtrisez le cours de santé des héros. Vous gagnez 20 points de vie !")
            print(f"Points de vie actuels : {personnage['PV']}")
        elif choix_sante == "non":
            print("Vous décidez de ne pas suivre ce cours pour le moment.")
        else:
            print("Réponse invalide. Veuillez répondre 'oui' ou 'non'.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["Sortir dans le hall", "Sortir dans le couloir", "Étudier les matières scolaires", "Demander le badge au professeur", "Montrer ces badges de combats"])
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

        if reponse.lower() == "1" or reponse.lower() == "sortir dans le hall":
            lieu_hall()
        elif reponse.lower() == "2" or reponse.lower() == "sortir dans le couloir":
            lieu_couloir_rdc()
        elif reponse.lower() == "3" or reponse.lower() == "étudier les matières scolaires":
            etudier_matiere()
        elif reponse.lower() == "4" or reponse.lower() == "Demander le badge au professeur":
            demander_passe()
        elif reponse.lower() == "5" or reponse.lower() == "Montrer ces badges de combats":
            montrer_badges()


def lieu_couloir_1er_etage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est le couloir du premier étage.")
    print("On peut aller à la cafétéria ou à la salle d'entraînement depuis ici.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["Observer", "Aller à la cafétéria", "Aller à la salle d'entraînement", "Aller dans le couloir du rdc", "Aller à la tambola"])
        proposer_lieux(["cafétéria", "salle d'entraînement", "Tambola"])
        reponse = input("├─> ")
        print("└────────────────────────────────────────")
        pere_confirme = False  # Variable vérifier si c'est bien le père du joueur
        if reponse.lower() == "1" or reponse.lower() == "observer":
                print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("\nC'est le couloir du premier étage.")
                print("Orihime vous remarque et s'approche de vous...")
                print("Orihime: Ah, c'est toi,", personnage["prénom"], ".")
                print("Orihime: Laisse-moi tranquille.")
                print("1. D'accord, je ne voulais pas te déranger.")
                print("2. Pourquoi cet accueil glacial ?")
                choix = input("├─> ")

                if choix == "1":
                    print("Vous: D'accord, je ne voulais pas te déranger.")
                    print("Orihime: Bien.")
                elif choix == "2":
                    print("Vous: Pourquoi cet accueil glacial ?")
                    print("Orihime: Ton pouvoir me fait peur. Mon frère est mort à cause d'un homme qui avait le même pouvoir.")
                    print("Orihime: C'était ton père, n'est-ce pas ?")
                    print("1. Non, ce n'était pas mon père.")
                    print("2. Je ne sais pas de qui tu parles.")
                    choix = input("├─> ")

                    if choix == "1":
                        print("Vous: Non, ce n'était pas mon père.")
                        print("Orihime: Oh, je vois... Désolée pour la confusion.")
                    elif choix == "2":
                        print("Vous: Je ne sais pas de qui tu parles.")
                        print("Orihime: Il était grand, avec des cheveux noirs et des yeux perçants... Tu es sûr de ne pas le connaître ?")
                        print("1. Oui, je suis sûr.")
                        print("2. Attends... cette description correspond à mon père.")
                        choix = input("├─> ")

                        if choix == "1":
                            print("Vous: Oui, je suis sûr.")
                            print("Orihime: Hmm, alors je me suis trompée.")
                        elif choix == "2":
                            if not pere_confirme:  
                                print("Vous: Attends... cette description correspond à mon père.")
                                print("Orihime: Je le savais ! C'est bien lui !")
                                pere_confirme = True  
                            else:
                                print("Vous avez déjà confirmé que c'est votre père.")
                        else:
                            print("Réponse invalide.")
                    else:
                        print("Réponse invalide.")
                else:
                    print("Réponse invalide.")

        elif reponse.lower() == "2" or reponse.lower() == "aller à la cafétéria":
                            lieu_cafeteria()
        elif reponse.lower() == "3" or reponse.lower() == "aller à la salle d'entraînement":
                            lieu_salle_entrainement()
        elif reponse.lower() == "4" or reponse.lower() == "aller au couloir du rdc":
            lieu_couloir_rdc()
        elif reponse.lower() == "5" or reponse.lower() == "aller à la tambola yueii":
            lieu_tambola()
            break

def lieu_tambola():
    print("\nBienvenue à la tambola Yueii !")  # Fonction pour la tambola
    print("Vous pouvez jouer à notre jeu de numéro ici.")
    while True:
        print("┌───────────────────────────────────────")
        proposer_actions(["Jouer au jeu de numéro", "Quitter la tambola"])
        reponse = input("├─> ").lower()
        print("└───────────────────────────────────────")
        if reponse.lower() == "1" or reponse.lower() == "jouer au jeu de numéro":
            jouer_jeu_tambola()
        elif reponse.lower() == "2" or reponse.lower() == "quitter la tambola":
            print("Vous quittez la tambola.")
            break

def jouer_jeu_tambola():
    global argent
    print("Bienvenue au jeu de numéro !")
    print("Choisissez un numéro entre 1 et 3 inclus.")
    numero_choisi = int(input("├─> "))
    if 1 <= numero_choisi <= 3:  # Vérifier si le numéro choisi est valide
        print("Le croupier lance les dés...")
        numero_gagnant = random.randint(1, 3)  # Numéro gagnant aléatoire
        if numero_choisi == numero_gagnant:
            gain = random.randint(500, 2000)  # Gain aléatoire entre 500 et 2000 yen
            argent += gain  # Le joueur gagne de l'argent
            print(f"Félicitations ! Le numéro gagnant est le {numero_gagnant}. Vous gagnez {gain} yen.")
        else:
            print(f"Dommage ! Le numéro gagnant est le {numero_gagnant}. Vous perdez votre mise.")
        print(f"Vous avez maintenant {argent} yen.")
    else:
        print("Numéro invalide. Veuillez choisir un numéro entre 1 et 3.")

def lieu_cafeteria():
    print("\nC'est la cafétéria.") # Fonction pour la cafétéria
    print("On peut accéder à la salle d'entraînement et au couloir du 1er étage depuis ici.")
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["Sortir dans le couloir", "Aller à la salle d'entraînement", "Manger"])
        reponse = input("├─> ").lower()
        print("└────────────────────────────────────────")
        if reponse.lower() == "1" or reponse.lower() == "sortir dans le couloir":
            lieu_couloir_1er_etage()
        elif reponse.lower() == "2" or reponse.lower() == "aller à la salle d'entraînement":
            lieu_salle_entrainement()
        elif reponse.lower() == "3" or reponse.lower() == "manger":
            manger()

def choisir_ingredients(plat):
    print(f"Voulez-vous ajouter des ingrédients à votre {plat}? (oui/non)")
    reponse = input("├─> ").lower()
    if reponse == "oui":
        ingredients_plat = plats[plat]
        tous_ingredients_non = True
        for ingredient, quantite in ingredients_plat.items():
            print(f"Voulez-vous ajouter {quantite} {ingredient} à votre {plat}? (oui/non)")
            reponse_ing = input("├─> ").lower()
            if reponse_ing == "oui":
                print(f"Vous avez ajouté {quantite} {ingredient} à votre {plat}.")
                tous_ingredients_non = False
                # Ajoutez votre logique pour gérer l'ajout d'ingrédients ici
            elif reponse_ing == "non":
                print(f"Vous ne pouvez pas manger de {plat} sans {ingredient}.")
            else:
                print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
                return choisir_ingredients(plat)
        if tous_ingredients_non:
            print(f"Vous ne pouvez pas manger de {plat} sans ingrédients.")
            return False
    elif reponse == "non":
        print(f"D'accord, vous ne pouvez pas manger de {plat} sans ingrédients.")
        return False
    else:
        print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")
        return choisir_ingredients(plat)
    return True

def manger():
    global argent
    print("Quel plat voulez-vous manger?") # Fonction pour manger un plat
    print("Plats disponibles : Ramen, Onigiri, Udon, Curry")
    plat_demande = input("├─> ").capitalize()
    prix_repas = 500  # Prix de chaque repas en yen
    if plat_demande in plats_stock and plats_stock[plat_demande] > 0:
        if choisir_ingredients(plat_demande) is False:
            return
        if argent >= prix_repas:  # Vérifier si le joueur a assez d'argent
            print(f"Vous avez choisi de manger {plat_demande}.")
            plats_stock[plat_demande] -= 1
            argent -= prix_repas  # Déduire le prix du repas de l'argent du joueur
            personnage["PV"] += 10
            print("Vous avez récupéré 10 points de vie.")
            print(f"Il vous reste {argent} yen.")
        else:
            print("Désolé, vous n'avez pas assez d'argent pour acheter ce plat.")
    elif plat_demande in plats_stock and plats_stock[plat_demande] == 0:
        print(f"Désolé, on a plus de {plat_demande} !")
    else:
        print("Ce plat n'existe pas. Veuillez choisir parmi les plats disponibles.")
        manger()




def lieu_salle_entrainement():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la salle d'entraînement.")
    if "badge" not in objets_badge:
        print("Vous ne pouvez pas entrer dans la salle d'entraînement sans le badge.")
        print("Revenez une fois que vous l'avez obtenu.")
        return
    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["Sortir dans le couloir", "Combattre le mannequin,", "Aller à la salle du coffre"])  # Ajout d'un choix pour combattre le mannequin
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

        if reponse.lower() == "1" or reponse.lower() == "sortir dans le couloir":
            lieu_couloir_1er_etage()
            break
        elif reponse.lower() == "2" or reponse.lower() == "combattre le mannequin":
            combattre()
        elif reponse.lower() == "3" or reponse.lower() == "Aller à la salle du coffre":
            salle_coffre()
            break

import random

def combattre():
    mannequin_pv = 50
    player_pv = 70
    print("Prêt à combattre !")
    bonus_attaque = 0  # Initialisation du bonus d'attaque à 0

    if "Cristal magique" in objets_cles:
        bonus_attaque += 15  # Augmentation des attaques de 15 points
        print("Vous sentez le pouvoir du cristal magique augmenter vos attaques !")

    if "Amulette mystique" in objets_cles:
        bonus_attaque += 10
        print("Vous sentez émerger en vous, le pouvoir de l'amulette mystique")

    if "Livre ancien" in objets_cles:
        player_pv += 30
        print("Vous sentez votre vie augmenter...")


    while mannequin_pv > 0:
        print("Que voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Fuir")
        if "potion" in inventaire:
            print("3. Utiliser une potion")

        action = input("├─> ").lower()
        
        if action == "1" or action == "attaquer":
            if personnage["Pouvoir"] == "Bannissement vers le Néant":
                print("Vous invoquez le pouvoir du Bannissement vers le Néant...")
                print("L'école entière est engloutie dans les ténèbres, détruite par votre puissance...")
                print("Vous avez vaincu le mannequin d'entraînement, mais à quel prix...")
                print("Fin du jeu.")
                exit()
            else:
                print("Vous attaquez le mannequin d'entraînement.")
                degats = pouvoir_degats[personnage["Pouvoir"]]  
                mannequin_pv -= degats
                if mannequin_pv < 0:
                    mannequin_pv = 0  # Si la vie du mannequin est négative, elle passe à zéro
                print(f"Le mannequin d'entraînement a maintenant {mannequin_pv} PV.")

                if mannequin_pv <= 0:
                    print("Vous avez vaincu le mannequin d'entraînement !")
                    print("Vous recevez un badge en récompense.")
                    objets_badge.append("badge")
                    break

                print("Le mannequin d'entraînement riposte !")
                degats_mannequin = random.randint(6, 30)  # Dégâts aléatoires du mannequin
                player_pv -= degats_mannequin
                if player_pv < 0:
                    player_pv = 0  # Si la vie du joueur est négative, la fixer à zéro
                print(f"Le mannequin d'entraînement vous inflige {degats_mannequin} dégâts.")
                print(f"Vous avez maintenant {player_pv} PV.")

                if player_pv <= 0:
                    print("Vous avez été vaincu par le mannequin d'entraînement.")
                    print("Fin du jeu.")
                    exit()
        
        elif action == "2" or action == "fuir":
            print("Vous fuyez comme un lâche.")
            break
        elif action == "3" or action == "utiliser une potion":
            if "potion" in inventaire:
                utiliser_potion()
            else:
                print("Vous n'avez pas de potion dans votre inventaire.")
        else:
            print("Choisissez une action valide.")


def salle_coffre():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est la salle du coffre.")
    print("Vous pouvez échanger vos badges contre des objets ici.")

    # Définir les objets disponibles à l'achat en fonction des badges
    objets_disponibles = {
        "potion": {"prix": 1, "description": "Une potion de guérison pour restaurer 20 PV."},
        "élixir": {"prix": 2, "description": "Un élixir de liquide divin pour restaurer 40 PV."}
    }

    print("\nVoici les objets disponibles à l'achat :")
    for objet, details in objets_disponibles.items():
        print(f"{objet.capitalize()} - Prix: {details['prix']} badges - Description: {details['description']}")

    while True:
        choix = input("\nQue souhaitez-vous acheter ? (Tapez 'quitter' pour sortir) : ").lower()
        if choix == "quitter":
            break
        elif choix in objets_disponibles:
            if choix in objets_cles and objets_cles.count(choix) >= 3:
                print("Désolé, vous avez déjà le maximum d'objets de ce type.")
            elif "badge" not in objets_cles or objets_cles.count("badge") < objets_disponibles[choix]["prix"]:
                print("Vous n'avez pas assez de badges pour acheter cet objet.")
            else:
                objets_cles.append(choix)
                print(f"Vous avez acheté un(e) {choix} !")
                # Rajouter les effets de l'élixir sur les points de vie du personnage
                if choix == "potion":
                    personnage["PV"] += 20
                    print("Vous avez consommé votre potion et gagné 20 points de vie !")
                    print(f"Points de vie actuels : {personnage['PV']}")
                # Retirer le nombre de badges utilisés pour l'achat
                for _ in range(objets_disponibles[choix]["prix"]):
                    objets_cles.remove("badge")
        else:
            print("Cet objet n'est pas disponible à l'achat dans la salle du coffre.")
               # Rajouter les effets de l'élixir sur les points de vie du personnage
            if choix == "élixir":
                    personnage["PV"] += 40
                    print("Vous avez consommé l'élixir et gagné 40 points de vie !")
                    print(f"Points de vie actuels : {personnage['PV']}")
                # Retirer le nombre de badges utilisés pour l'achat
            for _ in range(objets_disponibles[choix]["prix"]):
                    objets_cles.remove("badge")
            else:
                print("Cet objet n'est pas disponible à l'achat dans la salle du coffre.")

    # Utiliser les objets achetés
    while objets_cles:
        utiliser = input("\nVoulez-vous utiliser un objet ? (oui/non) : ").lower()
        if utiliser == "non":
            break
        elif utiliser == "oui":
            print("\nVoici les objets que vous avez :")
            for objet in objets_cles:
                print(objet.capitalize())
            objet_utiliser = input("Quel objet voulez-vous utiliser ? : ").lower()
            if objet_utiliser in objets_cles:
                # Effets de l'élixir sur les points de vie du personnage
                if objet_utiliser == "élixir":
                    personnage["PV"] += 20
                    print("Vous avez consommé l'élixir et gagné 20 points de vie !")
                    print(f"Points de vie actuels : {personnage['PV']}")
                objets_cles.remove(objet_utiliser)
            else:
                print("Vous n'avez pas cet objet.")
        else:
            print("Choix invalide.")

def utiliser_potion():
    if "potion" in inventaire and inventaire["potion"] > 0:
        # Restaurer 20 points de vie
        personnage["PV"] += 20
        print("Vous avez utilisé une potion et restauré 20 points de vie.")
        print(f"Points de vie actuels : {personnage['PV']}")
        # Réduire le nombre de potions dans l'inventaire
        inventaire["potion"] -= 1
    else:
        print("Vous n'avez pas de potion dans votre inventaire.")
  






# ********************************************************************************
# EXECUTION
# ********************************************************************************

# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")
