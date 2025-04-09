document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('nav ul li a');
    for (const link of links) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            target.scrollIntoView({ behavior: 'smooth' });
        });
    }

    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
            rect.top >= 0 &&
            rect.left >= 0 &&
            rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
            rect.right <= (window.innerWidth || document.documentElement.clientWidth)
        );
    }

    const paragraphs = document.querySelectorAll('section p');
    function checkParagraphs() {
        paragraphs.forEach(paragraph => {
            if (isInViewport(paragraph)) {
                paragraph.classList.add('animate');
            }
        });
    }

    window.addEventListener('scroll', checkParagraphs);
    window.addEventListener('resize', checkParagraphs);
    checkParagraphs();

    // Effet de frappe pour le message de bienvenue
    const welcomeMessage = document.getElementById('welcome-message');
    const messageText = welcomeMessage.textContent;
    let index = 0;

    function typeWriter() {
        if (index < messageText.length) {
            welcomeMessage.textContent += messageText.charAt(index);
            index++;
            setTimeout(typeWriter, 100); // Ajustez la vitesse en modifiant la valeur du délai
        } else {
            setTimeout(() => {
                welcomeMessage.textContent = '';
                index = 0;
                typeWriter();
            }, 2000); // Pause avant de recommencer l'animation
        }
    }

    welcomeMessage.textContent = '';
    typeWriter();
});
