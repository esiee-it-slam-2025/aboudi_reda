






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
    "Invocation des Ombres Primordiales"
]

plats = "Ramen,Onigiri,Udon,Curry"  # À transformer en liste

plats_stock = {}  # À remplir avec les plats

objets_cles = ["smartphone"]
inventaire = {}

# ********************************************************************************
# FONCTIONS UTILITAIRES
# ********************************************************************************


def proposer_lieux(mots_cles):
    message = "│[Lieux] "
    # A remplir ici
    print(message)


def proposer_actions(actions):
    message = "│[Actions] "
    # A remplir ici
    print(message)

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
    print("===============================")
    print("Commençons par créer ton personnage.")
    print("\nQuel âge as-tu ?")

    # Demander un âge et écrire cette information dans le dictionnaire "personnage"

prenom = input (" quel est ton prénom ? ")
personnage["prenom"] = prenom
age = input(" Quel age avez-vous ? ")
personnage["Age"] = age

    # Afficher la liste des pouvoirs (avec leur position) et demander d'en choisir un
print("Voici la liste des pouvoirs disponibles :")
for i, pouvoir in enumerate(pouvoirs, 1):
    print(f"{i}. {pouvoir}")


    # Stocker le nom du pouvoir choisi dans le dictionnaire "personnage"
pouvoir_index = int(input("Choisissez un pouvoir en saisissant son numéro : "))
while pouvoir_index < 1 or pouvoir_index > len(pouvoirs):
    print("Ton pouvoir n'existe pas.")
    pouvoir_index = int(input("Choisissez un pouvoir en saisissant son numéro dans la liste: "))
personnage["Pouvoir"] = pouvoirs[pouvoir_index - 1]
    # Afficher tout le contenu (clé et valeur) du dictionnaire "personnage"
print("\nよくやった ! Voici les informations de ton héro :")
for cle, valeur in personnage.items():
    print(f"{cle}: {valeur}")




# ********************************************************************************
# LIEUX
# ********************************************************************************

lieu_hall()

def lieu_hall():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

    while True:
        print("┌────────────────────────────────────────")
        proposer_actions(["quitter"])  # À compléter
        proposer_lieux(["couloir1"])  # À compléter
        reponse = input("├─> ")
        print("└────────────────────────────────────────")

        # Gérer ici toutes les réponses possibles, qu'elles soient correctes ou non
def Hall_entree_rdc():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans le hall d'entrée de l'école.")
    print("On peut aller à de nombreux endroits d'ici.")

def Couloir_du_rdc():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans les couloirs de l'école.")
    print("Tu peux aller en classe 1A, dans le hall du rdc, ou monter au 1er étage.")

def Classe_1A_rdc():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans la classe 1A de l'école.")
    print("Tu peux aller dans les couloirs du rdc, ou dans le hall du rdc.")

def Couloir_du_1er_étage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans les couloirs du 1er étage de l'école.")
    print("Tu peux aller dans la salle d'entrainement, à la caféteria, ou descendre au rdc.")

def Caféteria_1er_etage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans la caféteria de l'école.")
    print("Tu peux aller dans la salle d'entrainement, ou dans les couloirs du 1ère étage.")

def Salle_entraînement_1er_étage():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("Tu es dans la salle d'entrainement de l'école.")
    print("Tu peux aller dans les couloirs du 1ère étage, ou à la caféteria.")    






def lieu_couloir_rdc():
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("\nC'est le couloir du rez de chaussé.")
    print("On y trouve entre autres la classe 1-A.")

# ********************************************************************************
# EXECUTION
# ********************************************************************************


# Pour lancer le jeu, on appelle la fonction d'introduction
if __name__ == "__main__":
    intro()
    print("Fin du jeu.")