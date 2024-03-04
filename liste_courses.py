# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py liste_courses.py"

# Variables
liste_course = {
    "pates": 2,
    "sauce tomate": 1,
    "parmesan": 1
}

# Fonctions L'utilisateur peut ajouter des articles à sa liste

def  ajoute_course():
    article = input("Quel article voulez-vous ajouter à votre liste ?")
    quantite = input("Combien voulez-vous en ajouter ?")
    liste_course[article] = quantite
    print ("Vous avez ajouté (quantite)(article) à votre liste de course")



def show_actions():
    print("1 - Ajouter")
    print("2 - Supprimer")
    print("3 - Modifier")
    print("4 - Quitter")


#########################
### Début du programe ###
#########################

print("Bienvenue dans la liste de courses.\n")
print("Que voulez vous faire ?")
show_actions()


print("A bientot")