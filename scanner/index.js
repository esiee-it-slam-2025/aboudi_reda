const result = document.getElementById("result");

function showResult(data, success = true) {
    const result = document.getElementById("result");
  
    if (!success || !data) {
      result.innerHTML = `
        <div class="bg-red-100 text-red-700 p-4 rounded shadow text-center space-y-4">
          <p>❌ Billet invalide</p>
          <button onclick="restartScan()" class="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded">
            Scanner un autre billet
          </button>
        </div>
      `;
      return;
    }
  
    result.innerHTML = `
      <div class="bg-green-100 text-green-800 p-4 rounded shadow text-left space-y-2">
        <p class="font-bold text-lg">✅ Billet valide</p>
        <p><strong>Nom d'utilisateur :</strong> ${data.user}</p>
        <p><strong>Match :</strong> ${data.event}</p>
        <p><strong>Catégorie :</strong> ${data.category}</p>
        <button onclick="restartScan()" class="mt-4 bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded w-full">
          Scanner un autre billet
        </button>
      </div>
    `;
  }
  
  function restartScan() {
    document.getElementById("result").innerHTML = "";
  
    scanner.start(
      { facingMode: "environment" },
      { fps: 10, qrbox: 250 },
      (decodedText) => {
        scanner.stop().then(() => {
          validateTicket(decodedText);
        });
      },
      (errorMessage) => {
        // Ignore les erreurs
      }
    );
  }
  
  
  
  
  function validateTicket(uuid) {
    fetch(`http://127.0.0.1:8000/api/tickets/${uuid}/validate/`, {
      method: "POST",
      credentials: "include"
    })
      .then(res => res.json())
      .then(data => {
        if (data.status === "success") {
          showResult({
            user: data.user,
            event: data.event,
            category: data.category
          }, true);
        } else {
          showResult(null, false);
        }
      })
      .catch(() => showResult(null, false));
  }
   

const scanner = new Html5Qrcode("reader");

scanner.start(
  { facingMode: "environment" }, // utilise caméra arrière si dispo
  { fps: 10, qrbox: 250 },
  (decodedText) => {
    scanner.stop().then(() => {
      validateTicket(decodedText);
    });
  },
  (errorMessage) => {
    // erreur de scan non bloquante
  }
  
);
