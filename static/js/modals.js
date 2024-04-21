const body = document.querySelector('body');

const innerTimeout = 800;
const outerTimeout = 400;

var unlock = true;

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

function popupOpen(currentPopup, currentButton) {
    if (currentPopup && unlock) {

        const popupActive = document.querySelector('.modal.open');

        if (popupActive) {

            popupClose(popupActive, false);

        } else {

            bodyLock();
        }

        currentPopup.classList.add('open');

        offButton();

        currentPopup.addEventListener('click', function (e) {
            if (!e.target.closest('.modal__box')) {
                popupClose(document.querySelector('.modal.open'));
            }
        });

        window.addEventListener('keydown', (e) => {
            if (e.key == "Escape") {
                popupClose(document.querySelector('.modal.open'));
            }
        });

        $(currentButton).unbind('click').click(function() {
            popupClose(document.querySelector('.modal.open'));
            addItem(currentButton.replace('__button', "").replace('modal-item', "").replace('#', ""));
            showButton();
        });
    }
}

function popupClose(popupActive, doUnlock = true) {
    if (unlock) {

        popupActive.classList.remove('open');

        if (doUnlock) {

            bodyUnlock();
            showButton();
        }
    }
}

function modalsScript() {
    var popupLinks = document.querySelectorAll(".popup-link");

    if (popupLinks.length > 0) {
        for (let index = 0; index < popupLinks.length; index++) {

            const popupLink = popupLinks[index];

            popupLink.addEventListener("click", function (e) {

                const popupName = popupLink.getAttribute("href").replace('#', "");
                const currentPopup = document.getElementById(popupName);
                const currentButton = '#' + popupName + '__button'
                popupOpen(currentPopup, currentButton) ;
                e.preventDefault();
            });
        }
    }

    var popupCloseIcon = document.querySelectorAll('.close-popup');

    if (popupCloseIcon.length > 0) {
        for (let index = 0; index < popupCloseIcon.length; index++) {
            const el = popupCloseIcon[index];

            el.addEventListener('click', function (e) {
                popupClose(el.closest('.modal'));
                e.preventDefault();
            });
        }
    }
}

modalsScript();