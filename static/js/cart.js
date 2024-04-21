var tg = window.Telegram.WebApp;

var MainButton = tg.MainButton;

var cart = ''

function showButton () {
    MainButton.setParams({color: '#264f36', is_visible: true, text: 'В корзину', is_active: true});
}

function offButton () {
    MainButton.setParams({is_active: false});
}

function addItem (item) {
    if (cart != '') {
        cart += ' ' + item;
    } else {
        cart = item;
    }
}

function cartHTML (items) {
    var html = "";

    Object.values(items).forEach(function(item) {
        html += `
            <div class="cart-item">
                <div class="cart-item__image">
                      <img src="${item['src']}" alt="">
                </div>
                <div class="cart-item__title">${item['title']}</div>
                <div class="cart-item__quantity">
                    <div class="cart-item__int">${item['count']}шт.</div>
                </div>
                <div class="cart-item__total-price">${item['count'] * item['price']}₽</div>
            </div>`;
    });

    return html;
}

MainButton.onClick(function () {
    var cartModal = document.getElementById('cart-modal');
    var myData = {items: cart};
    if (cartModal.classList.contains('open')) {
        $.ajax({
            type: 'GET',
            url: '/get_invoice_url',
            data: myData,
            success: function(data) {
                tg.openInvoice(data['result']);
            }
        });
    } else {
        bodyLock();
        $.ajax({
            type: 'GET',
            url: '/get_items',
            data: myData,
            success: function(data) {
                var html = cartHTML(data); // Создание HTML кода на основе полученных данных
                var header = `
                    <h2>Корзина</h2>
                    <a class="modal__close-btn close-popup" id="close-modal__item">
                        <svg width="23" height="25" viewBox="0 0 23 25" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M2.09082 0.03125L22.9999 22.0294L20.909 24.2292L-8.73579e-05 2.23106L2.09082 0.03125Z" fill="#333333"></path>
                            <path d="M0 22.0295L20.9091 0.0314368L23 2.23125L2.09091 24.2294L0 22.0295Z" fill="#333333"></path>
                        </svg>
                    </a>`;
                $('#cart-modal__box').html(header + html); // Отображение HTML кода на странице
                modalsScript();
            }
        });
        cartModal.classList.add('open');
        MainButton.setParams({text: 'Оплатить'});
        cartModal.addEventListener('click', function (e) {
            if (!e.target.closest('.modal__box')) {
                popupClose(document.querySelector('.modal.open'));
            }
        });
    }
});

tg.onEvent('invoiceClosed', function(object) {
  if (object.status == 'paid') {
    tg.close();
  } else if (object.status == 'failed') {
    tg.showAlert("Не беспокойтесь. Мы сохраним ваш выбор.");
  }
});