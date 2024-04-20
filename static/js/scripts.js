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

/*Funkce pro zobrazování underline-text podtržení podle toho jak široký je text - název kategorie brandu*/
window.addEventListener('load', function() {
    // Najděte elementy na stránce
    var brandElements = document.querySelectorAll('.aer h5');
    var underlineElements = document.querySelectorAll('.underline-text2');

    // Pro každý element brand a underline
    for (var i = 0; i < brandElements.length; i++) {
        // Nastavte šířku podtržení na šířku textu
        underlineElements[i].style.width = brandElements[i].offsetWidth + 'px';
    }
});


document.addEventListener('DOMContentLoaded', function() {
    let priceElement = document.getElementById('total-price');
    if (priceElement) {
        let price = priceElement.textContent.replace(',', '.');
        price = parseFloat(price);
        priceElement.textContent = price.toString().replace('.', ',') + " Kč";
    }
});


function calculateArea() {
    const xValue = parseFloat(document.getElementById('x-value').value);
    const yValue = parseFloat(document.getElementById('y-value').value);
    let result = xValue * yValue;

    // Get the package size and price per package from the hidden elements
    const packageSize = parseFloat(document.getElementById('package-size').textContent);
    const pricePerPackage = parseFloat(document.getElementById('price-per-package').textContent);

    let packagesNeeded = Math.round( result / packageSize); // Use Math.round to round to the nearest whole number

    // Calculate the cost
    let cost = result * pricePerPackage;

    // Update the area, package results and cost separately
    document.getElementById('area-result').textContent = result.toFixed(2);
    document.getElementById('package-result').textContent = packagesNeeded;
    document.getElementById('cost-result').textContent = cost.toFixed(2);

    // Display the "Add to Cart" button
    document.getElementById('add-to-cart').style.display = 'inline-block';
}