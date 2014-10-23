from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, FileField, StringField, IntegerField, validators, SelectField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, InputRequired, Length, Email
from .helper import get_categories, get_states


class sku_list_search(Form):
    category = SelectField('Category', choices=get_categories(),coerce=int)
    sku = StringField('Search')

class sku_store_search(Form):
    state = SelectField('State', choices=get_states())
    store_num = StringField('Store#')