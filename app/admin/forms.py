from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, FileField, StringField, IntegerField, validators, SelectField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import Required, InputRequired, Length, Email
from ..main.helper import get_categories

class prod_entry(Form):
    sku_num = StringField('SKU',validators= [Required(),Length(max=32)])
    product_name = StringField('Product',validators= [Required(),Length(max=64)])
    brand = StringField('Brand',validators= [Length(max=64)])
    category = SelectField('Category', choices=get_categories(),coerce=int)
    org_price = FloatField('MSRP')
    current_price = FloatField('Current Price')
    opt_price = FloatField('Optimal Price')
    unit_cost = FloatField('Unit Cost')
    release = DateField('Release Date')
    phase_out = DateField('Phase Out')