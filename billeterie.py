"""
Cours "Introduction 1" - Exercice "Billetterie"
"""

# Variables
stations = {
    "Meinohama": 1.5,
    "Muromi": 0.8,
    "Fujisaki": 1.1,
    "Nishijin": 1.2,
    "Tojinmachi": 0.8,
    "Ohorikoen (Ohori Park)": 1.1,
    "Akasaka": 0.8,
    "Tenjin": 0.8,
    "Nakasu-Kawabata": 1.0,
    "Gion": 0.7,
    "Hakata": 1.2,
    "Higashi-Hie": 2.1,
    "Fukuokakuko (Airport)": 0.0,
}
stations_names = list(stations.keys())
stations_distances = list(stations.values())
nb_billets_adulte = 0
has_reduit = False

# Introduction
print("           /////// ")
print("         ///       ")
print("  //////////////   ")
print("      ///          ")
print("///////            ")
print("\nBienvenue sur la billetterie du métro municipal de Fukuoka.")

# Questions à l'utilisateur
nb_billets_adulte = int(input("Combien de billet adulte voulez-vous prendre ?"))
reponse = input("Voulez-vous des billets réduits ? (oui/non) ").lower()
if reponse == "oui":
    has_reduit = True
    nb_billets_reduit = int(input("Combien de billets réduits souhaitez-vous acheter ? "))
else:
    has_reduit = False

# Liste des stations avec leurs index
for index, station in enumerate(stations_names, start=1):
    print(f"{index}. {station}")

# Demander à l'utilisateur de sélectionner le numéro de la station de départ jusqu'à ce que la saisie soit cohérente
while True:
    try:
        depart_index = int(input("Veuillez sélectionner le numéro de la station de départ : "))
        if depart_index < 1 or depart_index > len(stations_names):
            raise ValueError
        break  
    except ValueError:
        print("La gare saisie n'eexiste pas. Veuillez taper un numéro de station valide.")
while True:
    try:
        arrivee_index = int(input("Veuillez sélectionner le numéro de la station d'arrivée : "))
        if arrivee_index < 1 or arrivee_index > len(stations_names):
            raise ValueError
        break 
    except ValueError:
        print("La gare saisie n'existe pas1. Veuillez taper un numéro de station valide.")


# Conversion des indices en noms de station
depart = stations_names[depart_index - 1]
arrivee = stations_names[arrivee_index - 1]

# Calcul de la distance parcourue
if depart_index < arrivee_index:
    distance_parcourue = sum(stations_distances[depart_index:arrivee_index])
else:
    distance_parcourue = sum(stations_distances[arrivee_index:depart_index])

# Choix de la bonne zone tarifaire
if distance_parcourue <= 3:
    zone_tarifaire = 1
elif distance_parcourue <= 7:
    zone_tarifaire = 2
elif distance_parcourue <= 11:
    zone_tarifaire = 3
else:
    zone_tarifaire = 4

# Calcul du coût total
tarif_plein = {1: 210, 2: 260, 3: 300, 4: 340}
tarif_reduit = {1: 110, 2: 130, 3: 150, 4: 170}

total_adulte = nb_billets_adulte * tarif_plein[zone_tarifaire]
total_reduit = nb_billets_reduit * tarif_reduit[zone_tarifaire]

# Affichage des détails du voyage et du tarif
print("\nDétails du voyage :")
print("Station de départ :",depart)
print("Station d'arrivée :", arrivee)
print("Distance parcourue :", distance_parcourue, "km")
print("Zone tarifaire :", zone_tarifaire)

# Affichage du tarif
print("\nTarif :")
print("Total adulte :", total_adulte, "yen")
if has_reduit:
    print("Total réduit :", total_reduit, "yen")

# Affichage de la voie du train à emprunter
if depart_index < arrivee_index:  
    print("\nVeuillez emprunter la voie 1.")
elif depart_index > arrivee_index:  
    print("\nVeuillez emprunter la voie 2.")
else:
    print("\nVous êtes déjà à destination.")

