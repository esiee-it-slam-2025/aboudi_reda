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
    quantite = int (input("Combien voulez-vous en ajouter ?"))
    liste_course[article] = quantite
    print (f"Vous avez ajouté {quantite} {article} à votre liste de course")
    affiche_maliste()

def affiche_maliste():
    print("Voici votre liste de course")
    for article,quantite in liste_course.items():
        print (f"{quantite} {article}")

def modifier_course(liste_course):
        article = input("Quel article voulez-vous modifier dans votre liste ? ")
        if article in liste_course:
            nouvelle_quantite = int(input(f"Nouvelle quantité pour {article} : "))
            liste_course[article] = nouvelle_quantite
            print(f"La quantité de {article} a été mise à jour.")
        else:
            print(f"L'article {article} n'est pas dans votre liste de course.")

def supprimer_article():
    article = input("Quel article voulez-vous supprimmer ?")
    if article in liste_course:
        del liste_course[article]
        print (f"L'article {article} à été supprimer de votre liste de course")
    else :
        print(f"L'article{article} n'est pas dans votre liste de course !")
  




def show_actions():
    print("1 - Ajouter")
    print("2 - Supprimer")
    print("3 - Afficher ma liste de course")
    print("4 - Modifier")
    print("5 - Quitter")


#########################
### Début du programe ###
#########################

print("Bienvenue dans la liste de courses.\n")
while True:
    print("Que voulez vous faire ?")
    show_actions()

    choix =  input("Quel est votre choix ?")
    if choix == "1":
        ajoute_course()
    elif choix == "2":
        supprimer_article()
    elif choix == "3":
        affiche_maliste()
    elif choix == "4":
        modifier_course(liste_course)
    elif choix == "5":
        print("Merci")
        break
    else : 
        print("Choix invalide !")




print("A bientot")