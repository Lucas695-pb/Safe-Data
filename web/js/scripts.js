document.addEventListener('DOMContentLoaded', () => {
    const learnMoreButton = document.getElementById('learn-more');
    const contactForm = document.getElementById('contact-form');

    learnMoreButton.addEventListener('click', () => {
        document.getElementById('services').scrollIntoView({ behavior: 'smooth' });
    });

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        if (name && email && message) {
            alert('Gracias por contactarnos, ' + name + '. Nos pondremos en contacto contigo pronto.');
            contactForm.reset();
        } else {
            alert('Por favor, complete todos los campos.');
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        autoplay: {
            delay: 3000, // Transición más rápida: 3 segundos
            disableOnInteraction: false,
        },
    });
});

// Validación del formulario de registro
document.querySelector("form[action='register.php']").addEventListener("submit", function(event) {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (username === "" || email === "" || password === "") {
        alert("Todos los campos son obligatorios");
        event.preventDefault();
    }
});

// Validación del formulario de inicio de sesión
document.querySelector("form[action='login.php']").addEventListener("submit", function(event) {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;

    if (username === "" || password === "") {
        alert("Por favor, ingrese su nombre de usuario y contraseña.");
        event.preventDefault();
    }
});

const passwordInput = document.getElementById("password");
const strengthDisplay = document.getElementById("password-strength");

passwordInput.addEventListener("input", function() {
    const strength = calculatePasswordStrength(passwordInput.value);
    strengthDisplay.textContent = `Fuerza de la contraseña: ${strength}`;
});

function calculatePasswordStrength(password) {
    // Implementar lógica para calcular la fuerza de la contraseña
    // Retornar "Débil", "Media", "Fuerte", etc.
    // Aquí puedes agregar tu lógica para calcular la fuerza de la contraseña
    if (password.length < 8) {
        return "Débil";
    } else if (password.length < 12) {
        return "Media";
    } else {
        return "Fuerte";
    }
}
