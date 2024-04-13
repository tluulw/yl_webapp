import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Item(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'items'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # id
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # название позиции

    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # тип позиции:
    # напитки: горячие напитки, прохладительные напитки, соки, молочные коктейли
    # снеки: картофель, стартеры, салаты
    # кафе: десерты и выпечка, напитки
    # завтрак: маффины и тосты, роллы и омлеты, разное, топпинги
    # десерты: десерты, мороженое
    # бургеры и роллы: говядина, курица, морепродукты, роллы
    # соусы и другое

    size = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # размер (двойной, маленький, средний, большой, обычный)

    is_popular = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # популярно или нет
    is_new = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # новинка или нет
    is_cafe = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # из кафе или нет
    is_snack = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # снек или нет
    is_dessert = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # десерт или нет
    is_drink = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # напиток или нет
    is_breakfast = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # завтрак или нет
    is_other = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # другое или нет
    is_burger = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # бургер или ролл или нет

    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # описание
    src = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # ссылка на картинку
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # цена
