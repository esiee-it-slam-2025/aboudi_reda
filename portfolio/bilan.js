const bilanOutput = document.getElementById("bilan-output");

const contenus = {
  appris:`
  Pendant ces deux années, j’ai vraiment appris à coder – mais pas juste à taper des lignes. J’ai appris à organiser mes idées, à comprendre des systèmes, à réfléchir avant d’écrire, à chercher des solutions (même si parfois c'était juste une virgule manquante).
  
  🛠️ Langages & outils que j’ai appris :
  - HTML / CSS / JavaScript
  - Python, Django
  - React, TypeScript
  - Node.js, Express
  - SQL / Sequelize / MariaDB
  - IntelliJ IDEA, Postman, Docker, MAMP, Git, Trello
  
  Mais surtout :
  - À chercher une erreur pendant 3h... ou à la corriger en 1 min avec ChatGPT 😅
  - À comprendre que coder c’est aussi se tromper, souvent.
  - À devenir autonome, poser les bonnes questions, m’améliorer sans attendre qu’on me dise quoi faire.
  
  Et même si j’ai galéré parfois, je me suis surpris à comprendre des trucs tout seul. Et ça, ça fait plaisir.
  `,
  aime: `
  Découvrir du code, me demander comment ça fonctionne… et réussir à le faire marcher. Ce sentiment de fierté quand quelque chose bloque pendant des heures, puis d’un coup tout s’éclaire. J’ai appris à aimer cette logique, cette recherche, cette satisfaction d’avoir trouvé par moi-même.
  
  Ce que j’ai aimé aussi, c’est voir un projet évoluer. Commencer avec une idée, poser les premières lignes, tester, corriger, améliorer... et finir par dire "c'est moi qui l’ai fait". C’est motivant de voir son travail grandir avec soi.
  
  Et surtout : l’ambiance dans ma classe. Le soutien, les fous rires, les profs qui prennent le temps de nous parler, de nous aider, sans jugement. J’ai grandi à leurs côtés. Et je les remercie pour ça.
  
  ⚠️ Et pour les employeurs qui liront ce bilan : les alternants ne sont pas juste “des juniors” à former. Ce sont des personnes qui veulent apprendre, qui donnent tout, qui cherchent juste leur place. Donnez-leur leur chance, et vous serez surpris.
  `,
  apres: `
J’aimerais devenir chef de projet. Pas juste pour piloter des équipes, mais pour faire le lien entre les besoins du client, les idées de l’équipe, et les solutions à livrer. J’aime organiser, anticiper, rendre les choses claires et concrètes.

Je ne sais pas encore exactement quelle spécialisation je vais suivre, mais une chose est sûre : je veux continuer à coder. Garder les mains dans le code, comprendre les enjeux techniques, et ne jamais être "le chef qui ne sait pas ce que fait son équipe". 💡

Côté études, je vise une licence dans la gestion de projet ou une alternance qui me permette de grandir dans ce rôle tout en restant proche du développement.

Et pourquoi pas à l’étranger 🌏 ? L’Asie m’attire énormément : le Japon, la Corée, Singapour... des pays où l’innovation et le respect du métier sont au cœur de tout. Travailler là-bas serait une vraie aventure.

Ah, et si un jour je perds confiance, je relirai cette phrase :
> "Même quand t’as le seum, t’as pas le temps, t’as des deadlines." ⏳
Bref, la suite s’annonce intense, mais j’suis prêt.
`,
  retiens: `
Ce que je retiens, c’est que dans cette filière SLAM, on apprend pas juste à coder — on apprend à galérer proprement. J’ai compris qu’un bon dev, c’est pas celui qui sait tout… c’est celui qui sait où chercher (merci Google, StackOverflow… et ChatGPT 👀).

J’ai aussi compris l’importance d’écrire du code lisible, de commenter (même si on le fait tous à la fin quand on a plus le temps), et surtout de garder une logique dans ce qu’on fait.

Mais ce que je retiens surtout, c’est l’ambiance qu’on a eue : une classe soudée, des profs investis (vraiment !), toujours prêts à prendre le temps d’expliquer, même quand on demandait “juste une dernière chose” à la fin du cours. Franchement, j’ai eu de la chance.

Alors merci à cette filière, à l’ESIEE IT, à ceux qui nous ont poussés, conseillés, motivés... et surtout, à ceux qui nous ont appris à apprendre.

Et si je devais résumer ces 2 ans :
> Coder, c’est 10% d’inspiration… et 90% de “mais pourquoi ça fait ça ?” 🤣🤯
`,
  debut: `
  Quand j’ai commencé, j’avais juste envie d’apprendre à coder, sans trop savoir où je mettais les pieds. J’étais curieux, motivé, mais un peu paumé.
  
  J’ai vite découvert que coder, c’est souvent chercher pendant des heures... ou tomber sur la bonne réponse en 1 minute grâce à ChatGPT 😅
  
  Mais au-delà des bugs et des erreurs incompréhensibles, j’ai appris à réfléchir, à me poser, à décomposer un problème et à m’auto-corriger.
  
  Et surtout, j’ai jamais été seul. Les profs m’ont soutenu, mes camarades aussi. C’est ce mélange d’entraide, de doutes et de progrès qui rend l’expérience marquante.
  
  Aujourd’hui, je suis fier du chemin parcouru. Et je sais que ce n’est que le début.
  `
};

function showBilan(type) {
  const texte = contenus[type] || "Contenu indisponible.";
  bilanOutput.innerHTML = "";

  // Nouveau span pour écrire caractère par caractère
  const span = document.createElement("span");
  bilanOutput.appendChild(span);

  let i = 0;
  const typingSpeed = 5; // Moins = plus rapide

  function typeWriter() {
    if (i < texte.length) {
      // Gère les sauts de ligne manuellement
      const char = texte[i];
      if (char === '\n') {
        span.appendChild(document.createElement('br'));
      } else {
        span.innerHTML += char;
      }
      i++;
      setTimeout(typeWriter, typingSpeed);
    } else {
      // Curseur après le texte
      const cursor = document.createElement("span");
      cursor.classList.add("cursor");
      bilanOutput.appendChild(cursor);
    }
  }

  typeWriter();
}