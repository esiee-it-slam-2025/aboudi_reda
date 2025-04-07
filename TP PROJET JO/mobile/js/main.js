// ================== CONFIG ===================

// Récupère le token CSRF depuis les cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// ================== LANCEMENT ===================

window.addEventListener("DOMContentLoaded", () => {
    checkAuth();
    loadEvents();

    // Affiche la modale de connexion
    document.getElementById("loginBtn").addEventListener("click", () => {
        document.getElementById("loginModal").classList.remove("hidden");
    });

    // Fermer toutes les modales
    document.querySelectorAll(".closeModal").forEach(btn =>
        btn.addEventListener("click", () => {
            document.querySelectorAll(".modal-overlay").forEach(modal => modal.classList.add("hidden"));
        })
    );

    document.getElementById("loginForm").addEventListener("submit", loginUser);
    document.getElementById("buyTicketForm").addEventListener("submit", buyTicket);
    document.getElementById("myTicketsBtn").addEventListener("click", loadUserTickets);
    document.getElementById("logoutBtn").addEventListener("click", logoutUser);
    document.getElementById("registerBtn").addEventListener("click", () => {
    document.getElementById("registerModal").classList.remove("hidden");
      });
      
    document.getElementById("registerForm").addEventListener("submit", registerUser);
      
});

// ================== AUTH ===================

async function loginUser(e) {
    e.preventDefault();
    const form = e.target;
    const data = {
        username: form.username.value,
        password: form.password.value,
    };

    const res = await fetch("http://127.0.0.1:8000/api/login/", {
        method: "POST",
        credentials: "include",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
    });

    const json = await res.json();

    if (res.ok) {
        showToast("✅ Connexion réussie", "success");
        document.getElementById("username").textContent = json.user.username;
        document.getElementById("loginModal").classList.add("hidden");
        document.getElementById("authButtons").classList.add("hidden");
        document.getElementById("userInfo").classList.remove("hidden");
    } else {
        showToast(json.message || "Erreur de connexion", "error");
    }
}

async function checkAuth() {
    const res = await fetch("http://127.0.0.1:8000/api/check-auth/", {
        credentials: "include"
    });

    if (res.ok) {
        const json = await res.json();
        document.getElementById("username").textContent = json.username || "Connecté";
        document.getElementById("authButtons").classList.add("hidden");
        document.getElementById("userInfo").classList.remove("hidden");
    } else {
        document.getElementById("authButtons").classList.remove("hidden");
        document.getElementById("userInfo").classList.add("hidden");
    }
}

function logoutUser() {
    fetch("http://127.0.0.1:8000/api/logout/", {
        credentials: "include"
    }).then(() => {
        showToast("Déconnexion réussie", "success");
        location.reload();
    });
}
// inscripiton 
async function registerUser(e) {
    e.preventDefault();
    const form = e.target;
  
    const data = {
      username: form.username.value,
      email: form.email.value,
      password: form.password.value,
    };
  
    const res = await fetch("http://127.0.0.1:8000/api/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });
  
    const json = await res.json();
  
    if (res.ok) {
      showToast("✅ Inscription réussie ! Vous pouvez vous connecter.", "success");
      document.getElementById("registerModal").classList.add("hidden");
    } else {
      showToast(json.message || "Erreur à l'inscription", "error");
    }
  }
  
// ================== MATCHS ===================

function safeTeamName(name) {
    return name === null || name === "null" ? "TBD" : name;
}

async function loadEvents() {
    const container = document.getElementById("matchList");
    container.innerHTML = "";

    const res = await fetch("http://127.0.0.1:8000/api/events/");
    const events = await res.json();

    events.forEach(event => {
        const home = safeTeamName(event.home_team);
        const away = safeTeamName(event.away_team);

        const card = document.createElement("div");
        card.className = "bg-white p-4 rounded shadow";

        card.innerHTML = `
            <h3 class="text-xl mb-2">${home} vs ${away}</h3>
            <p class="text-sm text-gray-600">${event.stadium}</p>
            <p class="text-sm text-gray-600">${new Date(event.start).toLocaleString()}</p>
            <button class="bg-yellow-500 hover:bg-yellow-600 text-white mt-3 px-4 py-2 rounded w-full font-semibold"
                onclick="openBuyModal(${event.id}, '${home} vs ${away}')">
                🎟️ Acheter un billet
            </button>
        `;

        container.appendChild(card);
    });
}

function openBuyModal(eventId, matchName) {
    document.getElementById("eventId").value = eventId;
    document.getElementById("matchInfo").textContent = matchName;
    document.getElementById("buyTicketModal").classList.remove("hidden");
}

// ================== BILLETS ===================

async function buyTicket(e) {
    e.preventDefault();
    const form = e.target;

    const res = await fetch("http://127.0.0.1:8000/api/tickets/", {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            event_id: form.eventId.value,
            category: form.category.value
        })
    });

    const json = await res.json();

    if (res.ok) {
        showToast("🎟️ Billet acheté avec succès !", "success");
        document.getElementById("buyTicketModal").classList.add("hidden");
    } else {
        showToast(json.message || "Erreur lors de l'achat", "error");
    }
}

async function loadUserTickets() {
    const container = document.getElementById("ticketsList");
    container.innerHTML = "";
    document.getElementById("loader")?.classList.remove("hidden");

    try {
        const res = await fetch("http://127.0.0.1:8000/api/my-tickets/", {
            credentials: "include"
        });

        const json = await res.json();

        Object.entries(json.tickets).forEach(([match, tickets]) => {
            tickets.forEach(ticket => {
                const card = document.createElement("div");
                card.className = "bg-white p-4 rounded shadow flex flex-col justify-between";

                card.innerHTML = `
                    <p class="font-semibold text-lg text-gray-800 mb-1">${match}</p>
                    <p class="text-sm text-gray-600">Catégorie : <span class="font-medium">${ticket.category}</span></p>
                    <p class="text-sm text-gray-600">Prix : ${ticket.price} €</p>
                    <div id="qrcode-${ticket.ticket_id}" class="mt-2"></div>
                    <button onclick="cancelTicket('${ticket.ticket_id}')" class="mt-4 bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm">
                        ❌ Annuler / Rembourser
                    </button>
                `;

                container.appendChild(card);

                new QRCode(document.getElementById(`qrcode-${ticket.ticket_id}`), {
                    text: ticket.ticket_id,
                    width: 128,
                    height: 128
                });
            });
        });

        document.getElementById("ticketsModal").classList.remove("hidden");
    } catch (err) {
        showToast("Erreur lors du chargement des billets", "error");
        console.error(err);
    } finally {
        document.getElementById("loader")?.classList.add("hidden");
    }
}

async function cancelTicket(ticketId) {
    if (!confirm("Confirmer l'annulation de ce billet ?")) return;

    const res = await fetch(`http://127.0.0.1:8000/api/tickets/${ticketId}/cancel/`, {
        method: "DELETE",
        credentials: "include"
    });

    const json = await res.json();

    if (res.ok) {
        showToast("🎫 Billet annulé et remboursé", "success");
        loadUserTickets();
    } else {
        showToast(json.message || "Erreur lors de l'annulation", "error");
    }
}

// ================== TOAST NOTIFICATIONS ===================

function showToast(message, type = "success") {
    const toast = document.createElement("div");
    toast.className = `
        px-4 py-2 rounded shadow text-white animate-slide-in
        ${type === "success" ? "bg-green-600" : "bg-red-600"}
    `;
    toast.textContent = message;

    const container = document.getElementById("toast-container");
    container.appendChild(toast);

    setTimeout(() => {
        toast.classList.add("opacity-0");
        setTimeout(() => toast.remove(), 500);
    }, 3000);
}
