function buildHTML(category, products) {
    var html = "";
    var index = 0;

    products.forEach(function(item) {
        html += `
            <li title="${item['title']}" class="catalog-product base-grid-item popup-link" href='#modal-item${index}'>
                <div class="catalog-product__link-image">
                    <figure class="base-image catalog-product__image">
                        <img src="${item['src']}" width="100%" height="100%" loading="lazy" alt="${item['title']}" class="base-image__img" style="width: 100%; height: 100%"/>
                    </figure>
                    ${item['is_new'] == 1 && category == 'is_new' ? `
                    <ul class="catalog-product-labels catalog-product__labels">
                        <li class="catalog-product-labels__label catalog-product-labels__label_red">Новинка</li>
                    </ul>` : ''}
                    ${item['is_popular'] == 1 && category == 'is_popular' ? `
                    <ul class="catalog-product-labels catalog-product__labels">
                        <li class="catalog-product-labels__label catalog-product-labels__label_purple">Популярно</li>
                    </ul>` : ''}
                </div>
                <div class="catalog-product__content">
                    <div class="catalog-product__info">
                        <div class="catalog-product-title">${item['title']} ${item['size'] != 'Обычный' ? `${item['size']}` : ''}</div>
                    </div>
                </div>
            </li>
            <li class="modal" id="modal-item${index}">
                <div class="modal__box">
                    <a class="modal__close-btn close-popup" id="close-modal__item">
                        <svg
                          width="23"
                          height="25"
                          viewBox="0 0 23 25"
                          fill="none"
                          xmlns="http://www.w3.org/2000/svg"
                        >
                          <path
                            d="M2.09082 0.03125L22.9999 22.0294L20.909 24.2292L-8.73579e-05 2.23106L2.09082 0.03125Z"
                            fill="#333333"
                          />
                          <path
                            d="M0 22.0295L20.9091 0.0314368L23 2.23125L2.09091 24.2294L0 22.0295Z"
                            fill="#333333"
                          />
                        </svg>
                    </a>
                    <img src="${item['src']}">
                    <h2>${item['title']} ${item['size'] != 'Обычный' ? `${item['size']}` : ''}</h2>
                    <p>${item['about']}</p>
                    <p>${item['price']}₽</p>
                    <button class='modal__add-button'>Добавить в корзину</button>
                </div>
            </li>`;
        index++;
    });

    return html;
}

$(document).ready(function() {
            document.getElementById("new").classList.add('menu-categories__item_selected');
            showProducts("is_new");

            $("#new").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("new").classList.add('menu-categories__item_selected');
                showProducts("is_new");
            });

            $("#popular").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("popular").classList.add('menu-categories__item_selected');
                showProducts('is_popular');
            });

            $("#drinks").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("drinks").classList.add('menu-categories__item_selected');
                showProducts("is_drink");
            });

            $("#combo").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("combo").classList.add('menu-categories__item_selected');
                showProducts("combo");
            });

            $("#burgers").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("burgers").classList.add('menu-categories__item_selected');
                showProducts("is_burger");
            });

            $("#snacks").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("snacks").classList.add('menu-categories__item_selected');
                showProducts("is_snack");
            });

            $("#cafe").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("cafe").classList.add('menu-categories__item_selected');
                showProducts("is_cafe");
            });

            $("#breakfast").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("breakfast").classList.add('menu-categories__item_selected');
                showProducts("is_breakfast");
            });

            $("#kids-combo").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("kids-combo").classList.add('menu-categories__item_selected');
                showProducts("kids_combo");
            });

            $("#desserts").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("desserts").classList.add('menu-categories__item_selected');
                showProducts("is_dessert");
            });

            $("#other").click(function() {
                document.querySelector(".menu-categories__item_selected").classList.remove('menu-categories__item_selected');
                document.getElementById("other").classList.add('menu-categories__item_selected');
                showProducts("is_other");
            });

            function showProducts(filter) {
                var myData = {
                    category: filter
                }
                $.ajax({
                    type: 'GET',
                    url: '/get_category',
                    data: myData,
                    success: function(data) {
                        var products = data['data'][0]['products']
                        var category = data['data'][1]['category']

                        var html = buildHTML(category, products); // Создание HTML кода на основе полученных данных
                        $('#menu').html(html); // Отображение HTML кода на странице
                        modalsScript();
                    }
                });
            }
        });