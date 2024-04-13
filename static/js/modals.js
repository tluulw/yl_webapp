const popupLinks = document.querySelectorAll(".popup-link");

const body = document.querySelector('body');

const innerTimeout = 800;
const outerTimeout = 400;

let unlock = true;

if (popupLinks.length > 0) {
    for (let index = 0; index < popupLinks.length; index++) {

        const popupLink = popupLinks[index];

        popupLink.addEventListener("click", function (e) {

            const popupName = popupLink.getAttribute("href").replace('#', "");
            const curentPopup = document.getElementById(popupName);
            popupOpen(curentPopup) ;
            e.preventDefault();
        });
    }
}

const popupCloseIcon = document.querySelectorAll('.close-popup');

if (popupCloseIcon.length > 0) {
    for (let index = 0; index < popupCloseIcon.length; index++) {
        const el = popupCloseIcon[index];

        el.addEventListener('click', function (e) {
            popupClose(el.closest('.modal'));
            e.preventDefault();
        });
    }
}

function popupOpen(currentPopup) {
    if (currentPopup && unlock) {

        const popupActive = document.querySelector('.modal.open');

        if (popupActive) {

            popupClose(popupActive, false);

        } else {

            bodyLock();
        }

        currentPopup.classList.add('open');

        currentPopup.addEventListener('click', function (e) {
            if (!e.target.closest('.modal__box')) {
                popupClose(currentPopup);
            }
        });

        window.addEventListener('keydown', (e) => {
            if (e.key == "Escape") {
                popupClose(currentPopup);
            }
        });
    }
}

function popupClose(popupActive, doUnlock = true) {
    if (unlock) {

        popupActive.classList.remove('open');

        if (doUnlock) {

            bodyUnlock();
        }
    }
}

function bodyLock() {
    if (document.body.offsetHeight > window.innerHeight) {
        body.style.paddingRight = '5px';
    } else {
        body.style.paddingRight = '0px';
    }

    body.classList.add('lock');

    unlock = false;

    setTimeout(function () {
        unlock = true;
    }, innerTimeout);
}


function bodyUnlock() {
    setTimeout(function () {
        body.style.paddingRight = '0px';
        body.classList.remove('lock');

    }, outerTimeout);

    unlock = false;

    setTimeout(function () {
        unlock = true;
    }, outerTimeout);
}