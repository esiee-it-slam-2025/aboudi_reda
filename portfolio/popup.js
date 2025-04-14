const popup = document.getElementById("popup");
const title = document.getElementById("popup-title");
const desc = document.getElementById("popup-description");
const missions = document.getElementById("popup-missions");
const duree = document.getElementById("popup-duree");
const outils = document.getElementById("popup-outils");
const lecon = document.getElementById("popup-lecon");
const etapesList = document.getElementById("popup-etapes");
const competencesContainer = document.getElementById("popup-competences");

function openPopupByIndex(index) {
  const project = projects[index];
  if (!project) return;

  title.textContent = project.title;
  desc.textContent = project.description;
  missions.textContent = project.missions;
  duree.textContent = project.duree;
  outils.textContent = project.outils;
  lecon.innerHTML = project.lecon;

  // Étapes du projet
  etapesList.innerHTML = "";
  project.etapes.forEach((etape) => {
    const li = document.createElement("li");
    li.textContent = etape;
    etapesList.appendChild(li);
  });

  // Compétences
  competencesContainer.innerHTML = "";
  if (Array.isArray(project.competences)) {
    project.competences.forEach((comp) => {
      const container = document.createElement("div");
      container.className = "competence-item";

      const toggle = document.createElement("div");
      toggle.className = "competence-toggle";
      toggle.innerHTML = `
        <span>${comp.titre}</span>
        <span class="arrow">▼</span>
      `;

      const content = document.createElement("div");
      content.className = "competence-content";
      content.innerHTML = comp.contenu;

      toggle.addEventListener("click", () => {
        const isVisible = content.style.display === "block";
        content.style.display = isVisible ? "none" : "block";
        toggle.querySelector(".arrow").textContent = isVisible ? "▼" : "▲";
      });

      container.appendChild(toggle);
      container.appendChild(content);
      competencesContainer.appendChild(container);
    });
    popup.style.display = "flex";
    Prism.highlightAll(); // ✅ colorisation syntaxique
  }

  popup.style.display = "flex";
}

function closePopup() {
  popup.style.display = "none";
}
function togglePdf(button) {
    const pdfWrapper = button.nextElementSibling;
    if (pdfWrapper.style.display === "none") {
      pdfWrapper.style.display = "block";
      button.textContent = "❌ Fermer le PDF";
    } else {
      pdfWrapper.style.display = "none";
      button.textContent = "📄 Voir le cahier des charges";
    }
  }
  

window.addEventListener("click", function (e) {
  if (e.target === popup) {
    closePopup();
  }
});
window.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closePopup();
    }
  });

// Zoom image on click
const zoomModal = document.getElementById("zoom-modal");
const zoomedImg = document.getElementById("zoomed-img");

document.addEventListener("click", function (e) {
  if (e.target.classList.contains("zoom-img")) {
    e.preventDefault(); // Empêche comportement par défaut
    e.stopPropagation(); // Empêche d'autres handlers
    zoomedImg.src = e.target.src;
    zoomModal.style.display = "flex";
  } else if (e.target === zoomModal) {
    zoomModal.style.display = "none";
  }
});

function openReadmePopup() {
  document.getElementById("readme-popup").style.display = "flex";
}

function closeReadmePopup() {
  document.getElementById("readme-popup").style.display = "none";
}

window.addEventListener("click", function (e) {
  const readmePopup = document.getElementById("readme-popup");
  if (e.target === readmePopup) {
    closeReadmePopup();
  }
});
function openChargeFukuoka() {
  document.getElementById("charge-fukuoka-popup").style.display = "flex";
}

function closeChargeFukuoka() {
  document.getElementById("charge-fukuoka-popup").style.display = "none";
}

window.addEventListener("click", function (e) {
  const popupFukuoka = document.getElementById("charge-fukuoka-popup");
  if (e.target === popupFukuoka) {
    closeChargeFukuoka();
  }
});