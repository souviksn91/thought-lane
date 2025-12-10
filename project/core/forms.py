# project/core/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# search form
class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Search')