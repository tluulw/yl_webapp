function modalsScript() {

    var popupLinks = document.querySelectorAll(".popup-link");

    var body = document.querySelector('body');

    var innerTimeout = 800;
    var outerTimeout = 400;

    var unlock = true;

    if (popupLinks.length > 0) {
        for (let index = 0; index < popupLinks.length; index++) {

            const popupLink = popupLinks[index];

            popupLink.addEventListener("click", function (e) {

                const popupName = popupLink.getAttribute("href").replace('#', "");
                const currentPopup = document.getElementById(popupName);
                popupOpen(currentPopup) ;
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

    function popupOpen(currentPopup) {
        if (currentPopup && unlock) {

            const popupActive = document.querySelector('.modal.open');

            if (popupActive) {

                popupClose(popupActive, false);

            } else {

                bodyLock();
            }

            currentPopup.classList.add('open');

            const addButtons = document.querySelectorAll(".modal__add-button")

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

            for (let index = 0; index < addButtons.length; index++) {

                const addButton = addButtons[index];

                addButton.addEventListener("click", function (e) {
                    popupClose(document.querySelector('.modal.open'));
                });
            }
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
}

modalsScript();