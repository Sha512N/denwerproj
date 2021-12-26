from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class Search(FlaskForm):
    word = StringField('Введите контекст поиска:', validators=[InputRequired()])
    search = SubmitField('Искать')
