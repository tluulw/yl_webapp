let more = document.getElementsByClassName("menu-categories__label")[0];
let hidden = document.getElementsByClassName("menu-categories__hidden-wrap")[0];
let inHidden = false;

more.addEventListener("mouseover", function (event) {
    hidden.classList.add('not-hidden');
});

more.addEventListener("mouseleave", function (event) {
    hidden.classList.remove('not-hidden');
});

hidden.addEventListener("mouseover", function (event) {
    hidden.classList.add('not-hidden');
});

hidden.addEventListener("mouseleave", function (event) {
    hidden.classList.remove('not-hidden');
});