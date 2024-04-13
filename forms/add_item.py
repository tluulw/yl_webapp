from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddItemForm(FlaskForm):

    title = StringField('Название', validators=[DataRequired()])
    type = StringField('Тип', validators=[DataRequired()])
    size = StringField('Размер', validators=[DataRequired()])
    about = StringField('Краткая информация', validators=[DataRequired()])
    src = StringField('Ссылка на картинку', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])

    is_popular = BooleanField('Популярно', default=False)
    is_new = BooleanField('Новое', default=False)
    is_cafe = BooleanField('Кафе', default=False)
    is_snack = BooleanField('Картофель, стартер, салат', default=False)
    is_dessert = BooleanField('Десерт', default=False)
    is_drink = BooleanField('Напиток', default=False)
    is_breakfast = BooleanField('Завтрак', default=False)
    is_other = BooleanField('Другое', default=False)
    is_burger = BooleanField('Бургер или ролл', default=False)

    add = SubmitField('Добавить')