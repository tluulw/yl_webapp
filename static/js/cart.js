var tg = window.Telegram.WebApp;
var MainButton = tg.MainButton;
var BackButton = tg.BackButton;


function showButton () {
    MainButton.setParams({color: '#264f36', is_visible: true, text: 'В корзину'});
}
BackButton.show();

MainButton.onClick(function() {
//    myData = {print: 'ok'}
//    $.ajax({
//        type: 'GET',
//        url: '/get_invoice_url',
//        data: myData,
//        success: function(data) {
//            tg.openInvoice(data);
//        }
//    });
    tg.openInvoice('https://t.me/$NMnOiAYmGUnXBgAANSSkXuBgXiY');
});


BackButton.onClick(function() {
  WebApp.showAlert("Нет пути назад!");

  BackButton.hide();
});