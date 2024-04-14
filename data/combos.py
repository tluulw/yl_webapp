import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Combo(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'combos'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)  # id

    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # название комбо

    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # тип комбо (обычный или кидз)

    is_breakfast = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True, default=False)  # завтрак или нет

    main_item = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('items.id'),
                                  nullable=True)  # основной товар в комбо

    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # описание

    src = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # ссылка на картинку

    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)  # цена

    item = orm.relationship('Item')