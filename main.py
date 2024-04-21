import requests
from flask import Flask, render_template, request, jsonify, redirect

from data import db_session
from data.combos import Combo
from data.items import Item
from forms.add_combo import AddComboForm
from forms.add_item import AddItemForm

from config import SECRET_KEY, PROVIDER_TOKEN, BOT_TOKEN

db_session.global_init('db/database.db')
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

BOT_TOKEN = BOT_TOKEN
PROVIDER_TOKEN = PROVIDER_TOKEN

ITEMS_CATEGORY_FILTERS = {
    'is_popular': Item.is_popular,
    'is_snack': Item.is_snack,
    'is_new': Item.is_new,
    'is_cafe': Item.is_cafe,
    'is_dessert': Item.is_dessert,
    'is_drink': Item.is_drink,
    'is_breakfast': Item.is_breakfast,
    'is_other': Item.is_other,
    'is_burger': Item.is_burger
}

COMBOS_CATEGORY_FILTERS = {
    'combo': 'Обычный',
    'kids_combo': 'Кидз'
}


@app.route('/menu', methods=['GET'])
def popular():
    return render_template('menu.html', title='Меню')


@app.route('/item/add', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        item = Item(
            title=form.title.data,
            type=form.type.data,
            size=form.size.data,
            is_popular=form.is_popular.data,
            is_new=form.is_new.data,
            is_cafe=form.is_cafe.data,
            is_snack=form.is_snack.data,
            is_dessert=form.is_dessert.data,
            is_drink=form.is_drink.data,
            is_breakfast=form.is_breakfast.data,
            is_other=form.is_other.data,
            is_burger=form.is_burger.data,
            about=form.about.data,
            src=form.src.data,
            price=form.price.data,
        )
        db_sess.add(item)
        db_sess.commit()
        return 'Item was added'
    return render_template('add_item.html', title='Adding an item', form=form, h='Добавить позицию')


@app.route('/combo/add', methods=['GET', 'POST'])
def add_combo():
    form = AddComboForm()

    if form.validate_on_submit():
        db_sess = db_session.create_session()
        combo = Combo(
            title=form.title.data,
            size=form.size.data,
            is_breakfast=form.is_breakfast.data,
            about=form.about.data,
            src=form.src.data,
            price=form.price.data,
            main_item=form.main_item.data
        )
        db_sess.add(combo)
        db_sess.commit()
        return 'Combo was added'
    return render_template('add_combo.html', title='Adding a combo', form=form, h='Добавить комбо')


@app.route('/combo/delete/<int:id>', methods=['GET'])
def delete_combo(id):
    db_sess = db_session.create_session()

    db_sess.delete(db_sess.query(Combo).filter(Combo.id == id).first())
    db_sess.commit()

    if db_sess.query(Combo).filter(Combo.id > id).first():
        for el in db_sess.query(Combo).filter(Combo.id > id).all():
            el.id -= 1
            db_sess.commit()

    return 'Combo was deleted'


@app.route('/item/delete/<int:id>', methods=['GET'])
def delete_item(id):
    db_sess = db_session.create_session()

    db_sess.delete(db_sess.query(Item).filter(Item.id == id).first())
    db_sess.commit()

    if db_sess.query(Item).filter(Item.id > id).first():
        for el in db_sess.query(Item).filter(Item.id > id).all():
            el.id -= 1
            db_sess.commit()

    return 'Item was deleted'


@app.route('/item/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    db_sess = db_session.create_session()

    item = db_sess.query(Item).filter(Item.id == id).first()

    form = AddItemForm()

    if form.validate_on_submit():
        item.title = form.title.data
        item.type = form.type.data
        item.size = form.size.data
        item.is_popular = form.is_popular.data
        item.is_new = form.is_new.data
        item.is_cafe = form.is_cafe.data
        item.is_snack = form.is_snack.data
        item.is_dessert = form.is_dessert.data
        item.is_drink = form.is_drink.data
        item.is_breakfast = form.is_breakfast.data
        item.is_other = form.is_other.data
        item.is_burger = form.is_burger.data
        item.about = form.about.data
        item.src = form.src.data
        item.price = form.price.data

        db_sess.commit()

        return redirect(f'/item/edit/{id + 1}')

    form.title.data = item.title
    form.type.data = item.type
    form.size.data = item.size
    form.is_popular.data = item.is_popular
    form.is_new.data = item.is_new
    form.is_cafe.data = item.is_cafe
    form.is_snack.data = item.is_snack
    form.is_dessert.data = item.is_dessert
    form.is_drink.data = item.is_drink
    form.is_breakfast.data = item.is_breakfast
    form.is_other.data = item.is_other
    form.is_burger.data = item.is_burger
    form.about.data = item.about
    form.src.data = item.src
    form.price.data = item.price

    return render_template('add_item.html', title='Editing an item', form=form, h='Редактировать позицию')


@app.route('/get_category', methods=['GET'])
def get_category():
    db_sess = db_session.create_session()

    category = request.args.get('category')  # парсинг запроса (получение нужной категории)

    if category in ITEMS_CATEGORY_FILTERS:  # получение продуктов, исходя из нужной категории
        return jsonify(
            {'data': [{
                'products': [item.to_dict() for item in
                             sorted(db_sess.query(Item).filter(ITEMS_CATEGORY_FILTERS[category] == 1).all(),
                                    key=lambda x: x.title)]},
                {'category': category}]})

    return jsonify(
        {'data': [{
            'products': [item.to_dict() for item in
                         sorted(db_sess.query(Combo).filter(Combo.size == COMBOS_CATEGORY_FILTERS[category]).all())]},
            {'category': category}]})


@app.route('/get_invoice_url', methods=['GET'])
def get_invoice():
    db_sess = db_session.create_session()

    cart = request.args.get('items')

    params = {'title': 'Заказ', 'description': 'Оплатить заказ', 'payload': 'true',
              'photo_url': 'https://free-png.ru/wp-content/uploads/2022/06/free-png.ru-443.png',
              'provider_token': PROVIDER_TOKEN, 'currency': 'rub'}

    prices = []

    for el in cart.split(' '):

        item_id = el.split('__')[0]
        category = el.split('__')[1]

        if category not in ['combo', 'kids_combo']:
            item = db_sess.query(Item).filter(Item.id == item_id).first()
        else:
            item = db_sess.query(Combo).filter(Combo.id == item_id).first()

        dct = {'label': f'{item.title} {item.size} x 1', 'amount': item.price * 100}
        labels = [el['label'][:-4] for el in prices]

        if dct['label'][:-4] not in labels:
            prices.append(dct)
        else:
            i = labels.index(dct['label'][:-4])
            prices[i]['label'] = f'{item.title} {item.size} x {int(prices[i]["label"][-1]) + 1}'
            prices[i]['amount'] += item.price * 100

    params['prices'] = prices

    req = requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/createInvoiceLink', json=params).json()
    print(req)

    return req


@app.route('/get_items', methods=['GET'])
def get_items():
    db_sess = db_session.create_session()

    cart = request.args.get('items')

    response = {}

    for el in cart.split(' '):

        item_id = el.split('__')[0]
        category = el.split('__')[1]

        if category not in ['combo', 'kids_combo']:
            item = db_sess.query(Item).filter(Item.id == item_id).first()

        else:
            item = db_sess.query(Combo).filter(Combo.id == item_id).first()

        if item.title not in response:
            response[item.title] = {'title': item.title,
                                 'size': item.size,
                                 'src': item.src,
                                 'price': item.price,
                                 'count': 1,
                                 'id': item_id}
        else:
            response[item.title]['count'] = cart.count(item_id)

    return response


@app.route('/reviews', methods=['GET'])
def reviews():
    return render_template('reviews.html')


def main():
    db_session.global_init('db/database.db')

    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()
