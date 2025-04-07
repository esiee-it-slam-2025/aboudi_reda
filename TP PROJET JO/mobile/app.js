// Configuration de base
const API_BASE_URL = 'http://127.0.0.1:8000/api';

// Fonction utilitaire pour les requêtes fetch
async function apiFetch(endpoint, options = {}) {
    const defaultOptions = {
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    };
    
    const mergedOptions = { ...defaultOptions, ...options };
    
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, mergedOptions);
        return await response.json();
    } catch (error) {
        console.error('Erreur API:', error);
        return null;
    }
}

// Récupérer le cookie CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Gestion de l'affichage des sections
function showSection(sectionId) {
    // Masquer toutes les sections
    ['matches-section', 'login-section', 'register-section', 'tickets-section']
        .forEach(id => document.getElementById(id).classList.add('hidden'));
    
    // Afficher la section demandée
    document.getElementById(sectionId).classList.remove('hidden');
}

// Chargement des matchs
async function loadMatches() {
    const matchesList = document.getElementById('matches-list');
    matchesList.innerHTML = 'Chargement des matchs...';

    try {
        const matches = await apiFetch('/events/');
        
        // Vider la liste avant de remplir
        matchesList.innerHTML = '';

        matches.forEach(match => {
            const matchElement = document.createElement('div');
            matchElement.classList.add('match-card');
            matchElement.innerHTML = `
                <h3>${match.home_team || 'Équipe non définie'} vs ${match.away_team || 'Équipe non définie'}</h3>
                <p>Stade : ${match.stadium}</p>
                <p>Date : ${new Date(match.start).toLocaleString()}</p>
                <button class="buy-ticket-btn" data-match-id="${match.id}">Acheter un billet</button>
            `;
            matchesList.appendChild(matchElement);
        });
    } catch (error) {
        matchesList.innerHTML = 'Erreur de chargement des matchs.';
    }
}

// Gestion de la connexion
async function handleLogin(event) {
    event.preventDefault();
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;

    try {
        const result = await apiFetch('/login/', {
            method: 'POST',
            body: JSON.stringify({ username, password })
        });

        if (result.status === 'success') {
            alert('Connexion réussie !');
            showSection('matches-section');
            loadMatches();
        } else {
            alert('Échec de la connexion : ' + result.message);
        }
    } catch (error) {
        console.error('Erreur de connexion:', error);
    }
}

// Gestion de l'inscription
async function handleRegister(event) {
    event.preventDefault();
    const username = document.getElementById('register-username').value;
    const email = document.getElementById('register-email').value;
    const password = document.getElementById('register-password').value;

    try {
        const result = await apiFetch('/register/', {
            method: 'POST',
            body: JSON.stringify({ username, email, password })
        });

        if (result.status === 'success') {
            alert('Inscription réussie ! Vous pouvez maintenant vous connecter.');
            showSection('login-section');
        } else {
            alert('Échec de l\'inscription : ' + result.message);
        }
    } catch (error) {
        console.error('Erreur d\'inscription:', error);
    }
}

// Événements de navigation
document.getElementById('login-btn').addEventListener('click', () => showSection('login-section'));
document.getElementById('register-btn').addEventListener('click', () => showSection('register-section'));

// Événements de formulaire
document.getElementById('login-form').addEventListener('submit', handleLogin);
document.getElementById('register-form').addEventListener('submit', handleRegister);

// Événement de chargement initial
document.addEventListener('DOMContentLoaded', () => {
    // Vous pouvez ajouter des actions initiales ici si nécessaire
});