document.getElementById('navbarDropdown').addEventListener('click', function (event) {
    event.preventDefault();
});

window.onload = function() {
    var cards = document.querySelectorAll('.card.h-100');
    cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            var imgOriginal = card.querySelector('.product-image.original');
            var imgCloseup = card.querySelector('.product-image.closeup');
            imgOriginal.style.opacity = 0;
            imgCloseup.style.opacity = 1;
        });
        card.addEventListener('mouseleave', function() {
            var imgOriginal = card.querySelector('.product-image.original');
            var imgCloseup = card.querySelector('.product-image.closeup');
            imgOriginal.style.opacity = 1;
            imgCloseup.style.opacity = 0;
        });
    });
};