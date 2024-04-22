/*Zrušení možností kliknout na dropdown menu - nefunguje tak jak by měl*/

/*Funkce pro změnění fotky při hover efektu*/
window.onload = function() {
    // Najde dropdown menu
    var dropdown = document.getElementById('navbarDropdown');
    if (dropdown) {
        // Přidá event listener, který zruší defaultní chování při kliknutí
        dropdown.addEventListener('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
        }, true); // Add true to make the event handler execute in the capturing phase
    }

    // Najde všechny karty produktů
    var cards = document.querySelectorAll('.card.h-100');
    cards.forEach(function(card) {
        // Přidá event listener pro změnu obrázku při najetí myši
        card.addEventListener('mouseenter', function() {
            var imgOriginal = card.querySelector('.product-image.original');
            var imgCloseup = card.querySelector('.product-image.closeup');
            if (imgOriginal && imgCloseup) {
                imgOriginal.style.opacity = 0;
                imgCloseup.style.opacity = 1;
            }
        });
        // Přidá event listener pro změnu obrázku při odjetí myši
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
    // Najde obrázek, na který se má aplikovat zoom
    const img = document.querySelector('.zoomable');
    img.addEventListener('mousemove', function(e) {
        // Vypočítá souřadnice kurzoru vůči obrázku
        const x = e.clientX - e.target.offsetLeft;
        const y = e.clientY - e.target.offsetTop;
        // Nastaví transform-origin na souřadnice kurzoru
        e.target.style.transformOrigin = `${x}px ${y}px`;
    });
    img.addEventListener('mouseleave', function(e) {
        // Nastaví transform-origin zpět na střed obrázku
        e.target.style.transformOrigin = 'center center';
    });
});

/*Funkce pro zobrazování underline-text podtržení podle toho jak široký je text - název kategorie brandu*/
window.addEventListener('load', function() {
    // Najde elementy značky a podtržení na stránce
    var brandElements = document.querySelectorAll('.aer h5');
    var underlineElements = document.querySelectorAll('.underline-text2');

    // Pro každý element značky a podtržení
    for (var i = 0; i < brandElements.length; i++) {
        // Nastaví šířku podtržení na šířku textu
        underlineElements[i].style.width = brandElements[i].offsetWidth + 'px';
    }
});


function calculateArea(xValueElement, yValueElement, areaResultElement, costResultElement, pricePerPackageElement, packageSizeElement, packagesNeededElement) {
    // Převede hodnoty na čísla
    const xValue = parseFloat(xValueElement.value);
    const yValue = parseFloat(yValueElement.value);

    // Kontroluje, zda jsou vstupy neprázdné
    if (isNaN(xValue) || isNaN(yValue)) {
        alert('Prosím vyplňte pole před výpočtem.');
        return;
    }

    // Vypočítá plochu
    let result = xValue * yValue;

    // Získá cenu za balení z hidden elementu
    const pricePerPackage = parseFloat(pricePerPackageElement.textContent);

    // Vypočítá cenu
    let cost = result * pricePerPackage;

    // Vypočítá počet potřebných balení
    const packageSize = parseFloat(packageSizeElement.textContent);
    let packagesNeeded = Math.ceil(result / packageSize);

    // Aktualizuje plochu, cenu a počet balení
    areaResultElement.textContent = result.toFixed(2);
    costResultElement.textContent = cost.toFixed(2);
    packagesNeededElement.textContent = packagesNeeded;
}

document.addEventListener('DOMContentLoaded', function() {
    // Najde všechna tlačítka pro výpočet
    const calculateButtons = document.querySelectorAll('.calculate-button');
    const resetButtons = document.querySelectorAll('.reset-button'); // Najde všechna tlačítka pro reset

    // Přidá event listener pro každé tlačítko pro výpočet
    calculateButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Najde rodičovskou kartu produktu
            const productCard = button.closest('.product-card');

            // Najde elementy
            const xValueElement = productCard.querySelector('.x-value');
            const yValueElement = productCard.querySelector('.y-value');
            const areaResultElement = productCard.querySelector('.area-result');
            const costResultElement = productCard.querySelector('.cost-result');
            const pricePerPackageElement = productCard.querySelector('.price-per-package');
            const packageSizeElement = productCard.querySelector('#package-size');
            const packagesNeededElement = productCard.querySelector('.packages-needed');

            // Vypočítá plochu
            calculateArea(xValueElement, yValueElement, areaResultElement, costResultElement, pricePerPackageElement, packageSizeElement, packagesNeededElement);
        });
    });

    // Přidá event listener pro každé tlačítko pro reset
    resetButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            // Najde rodičovskou kartu produktu
            const productCard = button.closest('.product-card');

            // Najde elementy
            const xValueElement = productCard.querySelector('.x-value');
            const yValueElement = productCard.querySelector('.y-value');
            const areaResultElement = productCard.querySelector('.area-result');
            const costResultElement = productCard.querySelector('.cost-result');
            const packagesNeededElement = productCard.querySelector('.packages-needed');

            // Resetuje vstupy a výsledky
            xValueElement.value = '';
            yValueElement.value = '';
            areaResultElement.textContent = '0';
            costResultElement.textContent = '0';
            packagesNeededElement.textContent = '0';
        });
    });

    // Najde všechny vstupy pro hodnoty x a y
    const xValueInputs = document.querySelectorAll('.x-value');
    const yValueInputs = document.querySelectorAll('.y-value');

    // Přidá event listener pro každý vstup pro hodnoty x a y
    xValueInputs.forEach(function(input) {
        input.addEventListener('keydown', function(event) {
            // Kontroluje, zda byla stisknuta klávesa Enter
            if (event.key === 'Enter') {
                // Zabrání odeslání formuláře
                event.preventDefault();

                // Klikne na tlačítko pro výpočet
                const calculateButton = input.closest('.product-card').querySelector('.calculate-button');
                calculateButton.click();
            }
        });
    });
    yValueInputs.forEach(function(input) {
        input.addEventListener('keydown', function(event) {
            // Kontroluje, zda byla stisknuta klávesa Enter
            if (event.key === 'Enter') {
                // Zabrání odeslání formuláře
                event.preventDefault();

                // Klikne na tlačítko pro výpočet
                const calculateButton = input.closest('.product-card').querySelector('.calculate-button');
                calculateButton.click();
            }
        });
    });
});

window.onload = function() {
    let reviews = document.querySelectorAll('.review');
    let loadMoreButton = document.getElementById('loadMore');
    let loadPreviousButton = document.getElementById('loadPrevious');
    let currentReviewIndex = 0;

    // Skryje tlačítko "Zpět" na začátku
    loadPreviousButton.style.display = 'none';

    function showReviews() {
        // Skryje všechny recenze
        for (let i = 0; i < reviews.length; i++) {
            reviews[i].style.display = 'none';
        }

        // Zobrazí další tři recenze
        let nextReviewIndex = currentReviewIndex + 3;
        for (; currentReviewIndex < nextReviewIndex && currentReviewIndex < reviews.length; currentReviewIndex++) {
            reviews[currentReviewIndex].style.display = 'block';
        }

        // Skryje tlačítko, pokud nejsou k dispozici žádné další recenze
        if (currentReviewIndex >= reviews.length) {
            loadMoreButton.style.display = 'none';
        }

        // Zobrazí tlačítko "Zpět", pokud jsou k dispozici předchozí recenze
        if (currentReviewIndex > 3) {
            loadPreviousButton.style.display = 'block';
        } else {
            loadPreviousButton.style.display = 'none';
        }
    }

    function showPreviousReviews() {
        // Skryje všechny recenze
        for (let i = 0; i < reviews.length; i++) {
            reviews[i].style.display = 'none';
        }

        // Zobrazí předchozí tři recenze
        currentReviewIndex -= 6;
        if (currentReviewIndex < 0) {
            currentReviewIndex = 0;
        }
        let nextReviewIndex = currentReviewIndex + 3;
        for (; currentReviewIndex < nextReviewIndex && currentReviewIndex < reviews.length; currentReviewIndex++) {
            reviews[currentReviewIndex].style.display = 'block';
        }

        // Skryje tlačítko "Zpět", pokud nejsou k dispozici předchozí recenze
        if (currentReviewIndex <= 3) {
            loadPreviousButton.style.display = 'none';
        }

        // Zobrazí tlačítko "Další", pokud jsou k dispozici další recenze
        if (currentReviewIndex < reviews.length) {
            loadMoreButton.style.display = 'block';
        }
    }

    loadMoreButton.addEventListener('click', showReviews);
    loadPreviousButton.addEventListener('click', showPreviousReviews);
    showReviews();
};
