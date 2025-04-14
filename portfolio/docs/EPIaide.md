# GestEPI – Suivi des Équipements de Protection Individuelle

---

## Stack utilisée

- Backend : Node.js, Express, Sequelize
- Base de données : MariaDB
- Frontend : React + Material UI
- Langage : TypeScript

> À retenir : TypeScript doit m'aider à structurer le code et éviter les erreurs dès le développement.

---

## Fonctionnalités

- Création, édition et suppression d’équipements (EPI)
- Liaison des contrôles à chaque EPI (suivi, remarques…)
- Gestion des utilisateurs avec rôles (admin / gestionnaire)
- Système d’alerte pour les équipements à contrôler

---

## Authentification et sécurité

- JWT pour les connexions utilisateur
- Middleware d’authentification pour protéger certaines routes
- Accès restreint selon le rôle utilisateur

> À revoir : la sécurisation des tokens côté front.

---

## Organisation du projet

J’ai découpé le projet en 4 grandes étapes :

1. Modélisation de la base de données avec Sequelize
2. Développement des routes et contrôleurs Express
3. Création de l’interface React
4. Ajout du système d’alerte de maintenance

> J’ai tout organisé dans un Trello : “à faire”, “en cours”, “terminé”.

---

## Difficultés rencontrées

- Liaison des modèles avec clés étrangères

> J’ai réussi à m’en sortir en lisant la doc et en testant beaucoup, beaucoup trop...

---

## Améliorations possibles

- Mon interface
- Meilleure gestion des erreurs côté back

---

## Bilan personnel

J’ai progressé sur :

- La structuration d’un projet fullstack
- L’organisation de mon code
- L’usage de TypeScript de manière concrète
