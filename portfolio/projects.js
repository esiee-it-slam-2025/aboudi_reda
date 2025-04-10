const projects = [
    {
      title: "Yueii - Jeu en Python",
      description:
        "Créer un jeu en Python, où le joueur incarne un élève dans un lycée de héros. L’objectif est d’explorer différents lieux, d’interagir avec des personnages, de combattre un mannequin d’entraînement et de collecter des objets pour progresser.",
      missions:
        "Création du scénario, développement en Python, logique de combat, test utilisateur.",
      duree: "2 semaines",
      outils: "Python, VS Code",
      lecon: `
    <a href="https://github.com/esiee-it-slam-2025/aboudi_reda/tree/e1a8028c51bbaaa7456a92a2b28351674456a8f7/TP%20Yuei" 
       target="_blank" 
       style="color: #0066cc; text-decoration: underline;">
      🔗 Voir le code du projet sur GitHub
    </a>`,
      etapes: ["Analyse des besoins", "Développement de l'application", "Test et amélioration"],
      competences: [
        {
            titre: "Analyser les objectifs et les modalités d’organisation d’un projet",
            contenu: `
              J’ai listé tous les lieux, objets, combats et interactions dans un mini cahier des charges avant de coder.
              <br><br>
              <button onclick="togglePdf(this)">📄 Voir le cahier des charges</button>
              <div class="pdf-wrapper" style="display:none; margin-top: 10px;">
                <iframe src="docs/cahier-des-charges-yueii.pdf" width="100%" height="300px" style="border: 1px solid #ccc; border-radius: 8px;"></iframe>
                <br>
                <a href="docs/cahier-des-charges-yueii.pdf" target="_blank" class="pdf-btn">🔗 Ouvrir dans un nouvel onglet</a>
              </div>
            `
          },                   
          {
            titre: "Planifier les activités",
            contenu: `
              J’ai découpé les grandes étapes du jeu (combat, déplacement, dialogue, logique, tests...) pour les développer les unes après les autres. Pour organiser mon avancement, j’ai utilisé un tableau Trello avec plusieurs colonnes ("À faire", "En cours", "Bloqué", "Terminé") et fixé des dates limites pour chaque tâche.
              <br><br>
              <img src="docs/trelloYueii.png" alt="Trello projet Yueii" class="zoom-img" style="max-width:100%; border:1px solid #ccc; border-radius:8px; margin-bottom:10px; cursor: zoom-in;">
              <br>
              Chaque carte représente une fonctionnalité ou une tâche précise, me permettant de visualiser rapidement ce qu’il restait à faire. Le fait d'avoir tout planifié m'a permis d’avancer de manière fluide et de respecter mes objectifs.
            `
          },                            
          {
            titre: "Mettre en place son environnement d’apprentissage personnel",
            contenu: `
              J’ai utilisé Visual Studio Code avec le terminal intégré pour coder et tester le jeu en direct. J’ai aussi corrigé les erreurs au fur et à mesure en relançant fréquemment le script. Cela m’a permis de mieux comprendre Python.
              <br><br>
              <p style="margin-bottom: 10px;"><strong>🎥 Vidéo de démonstration :</strong> un aperçu du jeu en fonctionnement.</p>
              <video controls style="width: 100%; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <source src="docs/yueiivideo.mp4" type="video/mp4">
              </video>
            `
          }                   
      ]
    },
    {
      title: "JoTickets - Billetterie Olympique",
      description:
        "Développement d’un système de billetterie avec API, interface d’administration Django et deux applications front : achat de billets et scan QR Code.",
      missions:
        "Connexion API, gestion base de données, création des vues Django, implémentation de QR codes, sécurisation des accès.",
      duree: "3 mois",
      outils: "Django, Python, HTML, JS, QR Scanner, VS Code",
      lecon:
        "Compréhension des API REST, gestion de projet fullstack, sécurisation d’applications.",
      etapes: ["Développement de l'API", "Création des interfaces front", "Déploiement et test"],
      competences: [
        {
            titre: "Recenser et identifier les ressources numériques",
            contenu: `
              Pour démarrer le projet, j’ai listé tous les outils nécessaires :
              <ul style="margin-top: 8px;">
                <li><b>Django</b> pour l’API et l’administration</li>
                <li><b>SQLite</b> pour la base de données</li>
                <li><b>Django REST Framework</b> pour exposer les endpoints</li>
                <li><b>QR Scanner JS</b> pour lire les billets</li>
              </ul>
              <br>
              📌 Voici un aperçu de ma base de données :
              <div class="image-grid">
                <img src="docs/BDDJO.png" alt="Schéma BDD JoTickets" class="zoom-img" />
                <img src="docs/JOSTADIUM.png" alt="Table team" class="zoom-img" />
              </div>
            `
          },                           
          {
            titre: "Mettre en place et vérifier les niveaux d’habilitation associés à un service",
            contenu: `
              Pour sécuriser l’accès à certaines fonctionnalités, j’ai mis en place deux vérifications dans le back-end Django :
              <ul style="margin-top: 8px;">
                <li><b>1. Vérification de connexion</b> : une vue <code>check_auth</code> renvoie si un utilisateur est connecté ou non. Cela permet de contrôler l’affichage côté front et l'accès aux données.</li>
                <li><b>2. Vérification d’accès aux objets</b> : dans certaines vues, l’utilisateur ne peut interagir qu’avec ses propres données, grâce au filtre <code>user=request.user</code>.</li>
              </ul>
              <br>
              🔐 Voici les extraits de code :
              <div class="image-grid">
                <img src="docs/check_auth.png" alt="Vérification de connexion dans Django" class="zoom-img" />
                <img src="docs/request.user.png" alt="Restriction des objets à l'utilisateur courant" class="zoom-img" />
              </div>
            `
          },          
        {
          titre: "Planifier les activités",
          contenu: "Organisation du travail en plusieurs modules : interface d’admin, API, puis front-end en mobile et scan."
        }
      ]
    },
    {
      title: "GestEPI - Gestion des Équipements de Protection Individuelle",
      description:
        "Application de suivi des équipements de sécurité (EPI) pour cordistes : ajout, contrôles, alertes de maintenance, détails et historique.",
      missions:
        "Développement back-end Express/TS, front React/MUI, structuration des interfaces types, alerte de maintenance.",
      duree: "1 mois",
      outils: "React, TypeScript, Express, MariaDB, VS Code",
      lecon:
        "Renforcement en structuration d'app fullstack, typage et réutilisation de composants.",
      etapes: ["Architecture du projet", "Développement Front/Back", "Mise en place des alertes"],
      competences: [
        {
          titre: "Recenser et identifier les ressources numériques",
          contenu: "Analyse des EPI, types, états et périodicité de contrôle pour adapter les modèles de données."
        },
        {
          titre: "Planifier les activités",
          contenu: "Découpage en lots : BDD et API, puis front et alertes."
        },
        {
          titre: "Développer son projet professionnel",
          contenu: "Projet complexe en autonomie sur la durée, m’ayant permis de monter en compétences sur le développement React/TS."
        }
      ]
    },
    {
      title: "Billetterie métro Fukuoka",
      description:
        "Système de calcul de tarif de billets en ligne de métro avec distances, zones tarifaires et gestion des tarifs réduits.",
      missions:
        "Interaction utilisateur en ligne de commande, gestion des erreurs, logique tarifaire, affichage de l’itinéraire.",
      duree: "2 semaines",
      outils: "Python, Terminal",
      lecon:
        "Structuration de l’entrée utilisateur, fonctions, logique métier claire.",
      etapes: ["Création des règles de tarification", "Développement du terminal", "Test du script"],
      competences: [
        {
          titre: "Analyser les objectifs et les modalités d’organisation d’un projet",
          contenu: "J’ai commencé par identifier toutes les zones tarifaires et conditions à intégrer avant d’écrire le code."
        },
        {
          titre: "Planifier les activités",
          contenu: "Fonctions codées les unes après les autres pour garantir que chaque calcul marche avant d’aller plus loin."
        },
        {
          titre: "Gérer son identité professionnelle",
          contenu: "Projet réalisé seul en respectant une consigne réaliste, fidèle à une vraie demande d'entreprise."
        }
      ]
    },
    {
      title: "Gestion communication client par mail",
      description:
        "Réception et traitement des mails clients pour des demandes de projet. Transmission au responsable, rédaction de réponses, relance ou orientation.",
      missions:
        "Réponse aux mails, qualification des besoins, suivi de dossiers avec le responsable.",
      duree: "2 ans (ponctuel durant l'alternance)",
      outils: "Outlook, messagerie professionnelle",
      lecon:
        "Meilleure compréhension de la communication client et suivi de demandes techniques.",
      etapes: ["Lecture des demandes", "Transmission aux décideurs", "Réponse ou relance"],
      competences: [
        {
          titre: "Collecter, suivre et orienter des demandes",
          contenu: "Lecture des demandes entrantes, vérification de leur faisabilité et transmission aux bons interlocuteurs."
        },
        {
          titre: "Traiter des demandes concernant les services réseau et système, applicatifs",
          contenu: "Certains clients demandaient des sites ou des applis précises, que je relayais avec les infos nécessaires."
        }
      ]
    },
    {
      title: "Prototypage de pages web pour site de l’entreprise",
      description:
        "Observation du travail des développeurs, tests d’interface, proposition de modifications d’éléments UX/UI intégrés après validation.",
      missions:
        "Tests utilisateurs, maquettes de propositions, retours d’expérience clients, ajustements graphiques.",
      duree: "6 mois (ponctuel)",
      outils: "HTML, CSS, outils de maquettage, navigateur",
      lecon:
        "Approfondissement en accessibilité, ergonomie et accompagnement de l'utilisateur.",
      etapes: ["Test d'interfaces", "Prototypage de nouvelles idées", "Proposition à l’équipe"],
      competences: [
        {
          titre: "Participer à l’évolution d’un site Web exploitant les données de l’organisation.",
          contenu: "Ajout de petits modules ou améliorations de formulaires existants à partir d’observations terrain."
        },
        {
          titre: "Réaliser les tests d’intégration et d’acceptation d’un service",
          contenu: "Tests des sites terminés avant leur mise en ligne, validation UX et bugs mineurs."
        }
      ]
    }
  ];
  