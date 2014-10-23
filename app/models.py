import random
#todo: Remove once opt model complete
from datetime import date
from app import db

class User_Role(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32), unique=True)

    def __init__(self,role):
        self.role = role

    def __repr__(self):
        return self.role


class Segment(db.Model):
    __tablename__ = 'segments'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32), unique=True)
    

    def __init__(self,type):
        self.type = type

    def __repr__(self):
        return self.type


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64))#todo: add password hash#
    company = db.Column(db.Integer, db.ForeignKey('companies.id'))
    role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    phone = db.Column(db.String(10))
    #category_permissions = db.Column(Manyto Many!)
    #category_admin = #
    list_admin = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    store = db.Column(db.Integer, db.ForeignKey('stores.id'))

    def __repr__(self):
        return self.email


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
	#categories = db.Column(ManytoMany!)
    segment = db.Column(db.Integer, db.ForeignKey('segments.id'))
    stores = db.relationship('Store', lazy='dynamic')
    users = db.relationship('User', lazy='dynamic')
    skus = db.relationship('User', lazy='dynamic')
    street = db.Column(db.Text())
    city = db.Column(db.String(32))
    state = db.Column(db.String(2))
    zip = db.Column(db.Integer)
    #amazon_credentials =  db.relationships()

    def get_admins(self):
	    pass

    def __repr__(self):
        return self.name


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    store_num = db.Column(db.Integer, nullable=False)#May need to change to name
    street = db.Column(db.Text())
    city = db.Column(db.String(32))
    state = db.Column(db.String(2))
    zip = db.Column(db.Integer)
    #todo: update coords to postgis
    lat = db.Column(db.Float(6))
    lng = db.Column(db.Float(6))
    #geo
    warehouse = db.Column(db.Boolean, default=False)
    #ship_leads = db.relationships('')
    #managers = db.relationships('')

    def __repr__(self):
        return str(self.store_num)

    def get_sales(self):
        pass

    def get_sss(self):
        pass


# class Store_Distribution(db.Model):
#     __tablename__ = 'store_distribution'
#     id = db.Column(db.Integer, primary_key=True)
#     sku = db.Column(db.Integer, db.ForeignKey('skus.id'), nullable=False)
#     store_num = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
#     ship_to_date = db.Column(db.Date)
#     units = db.Column(db.Integer)

#     def __repr__(self):
#         return 'Sku:{} - Store:{} - Units:{} - Shipped:{}'.format(self.sku,self.store_num,self.units,self.ship_to_date)


class SKU(db.Model):
    __tablename__ = 'skus'
    id = db.Column(db.Integer, primary_key=True)
    sku_num = db.Column(db.String(32), nullable=False, unique=True)
    product_name = db.Column(db.String(64), nullable=False)
    brand = db.Column(db.String(64))
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    org_price = db.Column(db.Integer, nullable=False)
    current_price = db.Column(db.Integer, nullable=False)
    opt_price= db.Column(db.Integer)
    release = db.Column(db.Date)
    phase_out = db.Column(db.Date)
    unit_cost = db.Column(db.Integer)
    crrnt_gm_forecast = db.Column(db.Integer)
    optml_gm_forecast = db.Column(db.Integer)

    #shipping dimensions
    #promotions
    #activechannels
    #features
    
    def gm(self,price):
        return ((price - self.unit_cost)/self.unit_cost)

    def price_diff(self):
        """Difference($) between current price and optimal price"""
        return (self.opt_price-self.current_price)
	
    def gm_impact(self):
        return (self.optml_gm_forecast-self.crrnt_gm_forecast)

    def days_past(self):
        return 12
    
    #Data Pulled from Optimization model#

    def get_opt_price(self):
        new_opt_price = self.current_price*.9
        #todo: update from optmization model
        self.opt_price = new_opt_price

    def get_gm(self,which_price="optimal"):
        if which_price == "optimal":
            self.optml_gm_forecast = self.crrnt_gm_forecast*1.1
        else:
            self.optml_gm_forecast = self.crrnt_gm_forecast

    def get_salethrough(self,which_price="optimal"):
        return (date(2015,4,15) if "optimal" else date(2015,5,15))

    def get_lqdt_score(self):
        return (random.randint(0,10))


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(64), nullable=False)
    skus = db.relationship('SKU', lazy='dynamic')


# class SKU_Group(db.Model):
# 	__tablename__ = 'skus'
#     id = db.Column(db.Integer, primary_key=True)
#     name
#     skus(backref)
#     category()


#Other Skipped classes: pricing_cluster, features
