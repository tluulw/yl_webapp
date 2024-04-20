var tg = window.Telegram.WebApp;

var MainButton = tg.MainButton;

var cart = ''

function showButton () {
    MainButton.setParams({color: '#264f36', is_visible: true, text: 'В корзину'});
}

function hideButton () {
    MainButton.hide();
}

function addItem (item) {
    if (cart != '') {
        cart += ' ' + item;
    } else {
        cart += item;
    }
}

MainButton.onClick(function() {
    var cartModal = document.getElementById('cart-modal');
    if (cartModal.classList.contains('open')) {
        var myData = {items: cart};
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
        cartModal.classList.add('open');
        MainButton.setParams({color: '#264f36', is_visible: true, text: 'Оплатить'});
        cartModal.addEventListener('click', function (e) {
                if (!e.target.closest('.modal__box')) {
                    popupClose(document.querySelector('.modal.open'));
                }
            });
    }
});