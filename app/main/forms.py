from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(FlaskForm):
    username = StringField()
    sex = StringField()
    telnumber = StringField()
    major = StringField()
    submit = SubmitField()
