# Cahier des charges – Billetterie métro Fukuoka

## Objectif principal

Programme en Python permettant de calculer le tarif d’un billet de métro à Fukuoka, en fonction :

- Stations de départ et d’arrivée,
- Afiichage de la distance parcourue (zones tarifaires A, B, C),
- Prix si réduction spécial ou pas

---

## Fonctionnalités attendues

- Entrée utilisateur : station de départ et d’arrivée
- Affichage du tarif (plein ou si réduction)
- Validation du trajet (éviter stations inconnues)

---

## Règles tarifaires (exemple fictif)

- Zone A (1–3 stations) : 120¥
- Zone B (4–7 stations) : 200¥
- Zone C (8+ stations) : 300¥
- Tarif réduit : -50% (enfants, seniors)

---

## Données externes utilisées

- Plan du métro de Fukuoka
- Liste des stations et zones 

---

## Contraintes techniques

- Script Python
- Affichage en ligne de commande