# Copiez ce fichier dans votre repo PERSONNEL
# Tapez votre code ci dessous
# puis executer ce fichier dans un terminal avec la commande "py ex_basic1_1.py"

# Init variables
teams_points = {
    "Paris SG": 85,
    "Lens": 84,
    "Marseille": 73,
    "Rennes": 68,
    "Lille": 67,
    "Monaco": 65,
    "Lyon": 62,
}

classement_Ligue1 = ["Paris SG", "Lens", "Marseille", "Rennes", "Lille", "Monaco", "Lyon"]

ligue_champions = []
ligue_europa = []
autres = []

# Parcourir le classement pour déterminer les équipes qualifiées pour chaque compétition
for i, equipe in enumerate(classement_Ligue1):
    if i < 2:  
        ligue_champions.append(equipe)
    elif i < 5:  
        ligue_europa.append(equipe)
    else:  
        autres.append(equipe)

print("Équipes qualifiées pour la Ligue des Champions :", ligue_champions)
print("Équipes qualifiées pour la Ligue Europa :", ligue_europa)
print("Équipes ne jouant pas de compétition supplémentaire :", autres)

#Demander à l'utilisateur si il souhaite des info sur une équipe ou sur une compétition (demander de choisir entre 1 et 2).

choix_utilisateur = input("Que souhaitez-vous obtenir?\n1. Informations sur une équipe\n2. Informations sur une compétition\nChoix : ")

if choix_utilisateur == "1":
    equipe_choisi = input("Entrez le nom de l'équipe : ")
    if equipe_choisi in classement_Ligue1:
        print(f"{equipe_choisi} a terminé à la {classement_Ligue1.index(equipe_choisi) + 1}ème place.")
elif choix_utilisateur == "2":
    # Choix compétition
# -- Demande user quelle compétition
# -- Afficher les équipes de la compétition
    competition_demandee = input("Entrez le code de la compétition (UCL pour Ligue des Champions, EL pour Ligue Europa) : ")
    if competition_demandee == "UCL":
        print("Les équipes qualifiées pour la Ligue des Champions sont :", ligue_champions)
    elif competition_demandee == "EL":
        print("Les équipes qualifiées pour la Ligue Europa sont :", ligue_europa)
    else:
        print("Le code de la compétition choisi est invalide.")
else:
    print("Votre choix est invalide. Veuillez choisir entre 1 et 2.")

# Choix équipe
    
# -- Afficher les équipes
# -- Demande user quelle équipe
# -- Affiche les infos de l'équipe