from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, FileField, StringField, IntegerField, validators, SelectField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, InputRequired, Length, Email
from .helper import get_states, get_categories, get_clusters_select


class cluster_anal(Form):
    test_price = StringField('Price')
    aggresiveness = StringField('Aggresiveness')
    demand_index = StringField('Demand_Index')

class sku_store_search(Form):
    state = SelectField('State', choices=get_states())
    store_num = StringField('Store#')
    categories = SelectField('Categories', choices=get_categories(),coerce=int)
    
class cat_clu_select(Form):
    categories = SelectField('Categories', choices=get_categories(),coerce=int)
    clusters = SelectField('Cluster', choices=get_clusters_select(),coerce=int)