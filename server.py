import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from data import db_session
from data.items import Item

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/catalog', methods=['GET'])
def popular():
    return render_template('catalog.html', title='Каталог')


@app.route('/add/item', methods=['GET', 'POST'])
def add_item():
    pass


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
