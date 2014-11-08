import random
from flask import url_for
#todo: Remove once opt model complete
from datetime import date
from app import db
from .main import _skus, _stores, _sku_clusters, _store_distro, _categories
import requests

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
    email = db.Column(db.String(64), unique=True) #nullable
    password = db.Column(db.String(64))#todo: add password hash#
    company = db.Column(db.Integer, db.ForeignKey('companies.id'))
    role = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    phone = db.Column(db.String(10))
    store = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #toAdds:
    #category_permissions = db.Column(Manyto Many!)
    #category_admin = #
    #list_admin = db.Column(db.Boolean, default=False)
    #is_admin = db.Column(db.Boolean, default=False)
    

    def __repr__(self):
        return self.email

categories = db.Table('cattable',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id')))


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),) #nullable
    categories = db.relationship('Category',secondary=categories, 
        backref=db.backref('companies', lazy='dynamic'))
    segment = db.Column(db.Integer, db.ForeignKey('segments.id'))
    stores = db.relationship('Store', lazy='dynamic')
    users = db.relationship('User', lazy='dynamic')
    skus = db.relationship('User', lazy='dynamic')
    street = db.Column(db.Text())
    city = db.Column(db.String(32))
    state = db.Column(db.String(2))
    zip = db.Column(db.Integer)
    #toadd:
    #amazon_credentials =  db.relationships()

    def get_admins(self):
	    pass

    def __repr__(self):
        return self.name


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.Integer, db.ForeignKey('companies.id')) #nullable
    store_num = db.Column(db.Integer)#nullable, May need to change to name
    street = db.Column(db.Text())
    city = db.Column(db.String(32))
    state = db.Column(db.String(2))
    zip = db.Column(db.Integer)
    lat = db.Column(db.Float(6))
    lng = db.Column(db.Float(6))
    warehouse = db.Column(db.Boolean, default=False)
    crrnt_gm_forecast = db.Column(db.Integer)
    optml_gm_forecast = db.Column(db.Integer)
    crrnt_sales_forecast = db.Column(db.Integer)
    optml_sales_forecast = db.Column(db.Integer)
    crrnt_sellthru_forecast = db.Column(db.Integer)
    optml_sellthru_forecast = db.Column(db.Integer)
    #todo: update coords to postgis
    #geo
    #ship_leads = db.relationships('')
    #managers = db.relationships('')

    def __repr__(self):
        return str(self.store_num)

    def get_metric(self,metric,crrnt_or_optml):
        pass

class Store_Distribution(db.Model):
    __tablename__ = 'store_distribution'
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, db.ForeignKey('skus.id')) #nullable
    store_num = db.Column(db.Integer, db.ForeignKey('stores.id')) #nullable
    ship_to_date = db.Column(db.Date)
    units = db.Column(db.Integer)

    def __repr__(self):
        return 'Sku:{} - Store:{} - Units:{} - Shipped:{}'.format(self.sku,self.store_num,self.units,self.ship_to_date)
    
    def get_perf_list(self):
        pass

class SKU(db.Model):
    __tablename__ = 'skus'
    id = db.Column(db.Integer, primary_key=True)
    sku_num = db.Column(db.String(32), unique=True) #nullable
    prod_name = db.Column(db.String(64)) #nullable
    brand = db.Column(db.String(64))
    cluster = db.Column(db.Integer, db.ForeignKey('clusters.id'))
    subcategory = db.Column(db.Integer, db.ForeignKey('subcats.id'))
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    org_price = db.Column(db.Integer) #nullable
    current_price = db.Column(db.Integer) #nullable
    launch_dt = db.Column(db.Date)
    phase_out = db.Column(db.Date)
    unit_cost = db.Column(db.Integer)
    opt_price= db.Column(db.Integer)
    crrnt_gm_forecast = db.Column(db.Integer)
    optml_gm_forecast = db.Column(db.Integer)
    crrnt_sales_forecast = db.Column(db.Integer)
    optml_sales_forecast = db.Column(db.Integer)
    crrnt_sellthru_forecast = db.Column(db.Integer)
    optml_sellthru_forecast = db.Column(db.Integer)
    lqdt_recommended = db.Column(db.Boolean, default=False)
    on_market = db.Column(db.Boolean, default=False)
    lqdt_price = db.Column(db.Integer)
    lqdt_channel = db.Column(db.Integer, db.ForeignKey('channels.id'))
    units_to_list = db.Column(db.Integer)
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

    #Data Pulled from Optimization model#
    def get_metric(self,metric='gm',crrnt_or_optml='crrnt'):
        info = _skus['skus'][0]['xo22']['forecasts'][metric][crrnt_or_optml]
        return info


    def get_lqdt_stat(self,stat):
        pass


class Cluster(db.Model):
    __tablename__ = 'clusters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) #nullable
    skus = db.relationship('SKU', lazy='dynamic')


class Subcategory(db.Model):
    __tablename__ = 'subcats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) #nullable
    skus = db.relationship('SKU', lazy='dynamic')


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) #nullable
    skus = db.relationship('SKU', lazy='dynamic')


class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) #nullable
#Other Skipped classes: pricing_cluster, features
