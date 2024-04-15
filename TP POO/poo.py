# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py entrainement_poo.py"

# Init variables
hero = None
monstre = None

armes = {"Epée": 5, "Arc": 4, "Couteau à beurre": 1}


# Init classes


class Creature():
    # Ajouter les autres attributs
    degats = 0

    def __init__(self, degats):
        self.degats = degats

    def attaque(self, cible):
        # Ici les concéquences de l'attaque
        pass  # A supprimer quand la fonction sera écrite

# Ajouter les autres classes

# Début du jeu


def intro():
    print("===============================================================")
    print("|| Bienvenue dans le système de combat POO (Punch Out Out) ! ||")
    print("===============================================================")
    print("\nQuel est le nom de ton héros.")
    # Choix du nom, choix de l'arme

    # Création des instances

    # Attention pour modifier les variables globales dans une fonction en python vous devez d'abord utiliser cette ligne
    global heros, monstre

    combat()

# Boucle de combat


def combat():
    tourHeros = True
    print("Bagarre")
    # Créer la boucle de combat


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")