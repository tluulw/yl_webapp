from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddComboForm(FlaskForm):

    title = StringField('Название', validators=[DataRequired()])
    size = StringField('Тип', validators=[DataRequired()])
    about = StringField('Краткая информация', validators=[DataRequired()])
    src = StringField('Ссылка на картинку', validators=[DataRequired()])
    price = IntegerField('Цена', validators=[DataRequired()])
    is_breakfast = BooleanField('Завтрак', default=False)
    main_item = IntegerField('Основная позиция', validators=[DataRequired()])

    add = SubmitField('Добавить')