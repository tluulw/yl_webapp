import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from data import db_session
from data.items import Item
from forms.add_item import AddItemForm

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/catalog', methods=['GET'])
def popular():
    return render_template('catalog.html', title='Каталог')


@app.route('/add/item', methods=['GET', 'POST'])
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
    return render_template('add_item.html', title='Adding an item', form=form)


@app.route('/get_products', methods=['GET'])
def get_products():
    db_sess = db_session.create_session()

    filter = request.args.items().__next__()[0]

    products = []

    if filter == 'is_popular':
        products = db_sess.query(Item).filter(Item.is_popular == 1).all()
        products = [item.to_dict() for item in products]

    return jsonify({'products': products})


def main():
    db_session.global_init('db/database.db')
    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()
