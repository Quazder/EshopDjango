/*Zrušení možností kliknout na dropdown menu - nefunguje tak jak by měl*/

/*Funkce pro změnění fotky při hover efektu*/
window.onload = function() {
    var dropdown = document.getElementById('navbarDropdown');
    if (dropdown) {
        dropdown.addEventListener('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
        }, true); // Add true to make the event handler execute in the capturing phase
    }

    var cards = document.querySelectorAll('.card.h-100');
    cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            var imgOriginal = card.querySelector('.product-image.original');
            var imgCloseup = card.querySelector('.product-image.closeup');
            if (imgOriginal && imgCloseup) {
                imgOriginal.style.opacity = 0;
                imgCloseup.style.opacity = 1;
            }
        });
        card.addEventListener('mouseleave', function() {
            var imgOriginal = card.querySelector('.product-image.original');
            var imgCloseup = card.querySelector('.product-image.closeup');
            if (imgOriginal && imgCloseup) {
                imgOriginal.style.opacity = 1;
                imgCloseup.style.opacity = 0;
            }
        });
    });
};


/*ZOOM FOTKY*/
document.addEventListener('DOMContentLoaded', function() {
    const img = document.querySelector('.zoomable');
    img.addEventListener('mousemove', function(e) {
        const x = e.clientX - e.target.offsetLeft;
        const y = e.clientY - e.target.offsetTop;
        e.target.style.transformOrigin = `${x}px ${y}px`;
    });
    img.addEventListener('mouseleave', function(e) {
        e.target.style.transformOrigin = 'center center';
    });
});