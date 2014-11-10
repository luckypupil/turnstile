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
    name = db.Column(db.String(32), unique=True)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name


class Segment(db.Model):
    __tablename__ = 'segments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(32))
    last = db.Column(db.String(32))
    email = db.Column(db.String(64), unique=True) #nullable
    password = db.Column(db.String(64))#todo: add password hash#
    phone = db.Column(db.String(10))
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id'))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #toAdds:
    #category_permissions = db.Column(Manyto Many!)
    #category_admin = #
    #list_admin = db.Column(db.Boolean, default=False)
    #is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return self.email

    def __init__(self,first,last,email,password,phone,company_id=None,role_id=None,store_id=None):
        self.first = first
        self.last = last
        self.email = email
        self.password = password
        self.phone = phone
        self.company_id = company_id
        self.role_id = role_id
        self.store_id = store_id

categories = db.Table('cattable',
    db.Column('category_id', db.Integer, db.ForeignKey('categories.id')),
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id')))


class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),) #nullable
    street = db.Column(db.Text())
    city = db.Column(db.String(32))
    state = db.Column(db.String(2))
    zipcd = db.Column(db.Integer)
    segment_id = db.Column(db.Integer, db.ForeignKey('segments.id'))
    stores = db.relationship('Store', lazy='dynamic')
    users = db.relationship('User', lazy='dynamic')
    skus = db.relationship('User', lazy='dynamic')
    categories = db.relationship('Category',secondary=categories, 
        backref=db.backref('companies', lazy='dynamic'))
    #toadd:
    #amazon_credentials =  db.relationships()

    def get_admins(self):
	    pass

    def __repr__(self):
        return self.name

    def __init__(self,name,street,city,state,zip,segment_id=None):
        self.name = name
        self.street =  street
        self.city = city
        self.state = state
        self.zip = zipcd
        self.segment_id = segment_id


class Store(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    store_num = db.Column(db.Integer)#nullable, May need to change to name
    street = db.Column(db.Text())
    city = db.Column(db.String(32))
    state = db.Column(db.String(2))
    zipcd = db.Column(db.Integer)
    lat = db.Column(db.Float(6))
    lng = db.Column(db.Float(6))
    warehouse = db.Column(db.Boolean, default=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    #todo: update coords to postgis
    #geo
    #ship_leads = db.relationships('')
    #managers = db.relationships('')

    def __repr__(self):
        return str(self.store_num)

    def get_metric(self,metric,crrnt_or_optml):
        pass

    def __init__(self,store_num,street,city,state,zipcd,warehouse,lat=None,lng=None,company_id=None):
        self.store_num = store_num
        self.street = street
        self.city = city
        self.state = state
        self.zipcd = zipcd
        self.warehouse = warehouse
        self.lat = lat
        self.lng = lng


class Store_Distribution(db.Model):
    __tablename__ = 'store_distribution'
    id = db.Column(db.Integer, primary_key=True)
    sku_id = db.Column(db.Integer, db.ForeignKey('skus.id')) #nullable
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #nullable
    receipt_dt = db.Column(db.Date)
    units = db.Column(db.Integer)
    crrnt_price = db.Column(db.Integer)
    optml_price= db.Column(db.Integer)
    plan_gm_fc = db.Column(db.Integer)
    crrnt_gm_fc = db.Column(db.Integer)
    optml_gm_fc = db.Column(db.Integer)
    plan_sales_fc = db.Column(db.Integer)
    crrnt_sales_fc = db.Column(db.Integer)
    optml_sales_fc = db.Column(db.Integer)
    plan_sellthru_fc = db.Column(db.Integer)
    crrnt_sellthru_fc = db.Column(db.Integer)
    optml_sellthru_fc = db.Column(db.Integer)
    #Liquidation Considerations#
    lqdt_src = db.Column(db.Boolean, default=False)
    

    def __repr__(self):
        return 'SkuID:{} - StoreID:{} - Units:{} - Shipped:{} - CrrntPrice:{}'.format(self.sku_id,
                                                                                self.store_id,self.units,self.receipt_dt,self.crrnt_price)
    
    def get_perf_list(self):
        pass

    def __init__(self,receipt_dt, units,crrnt_price=None,optml_price=None,plan_gm_fc=None,crrnt_gm_fc=None,optml_gm_fc=None,
                    plan_sales_fc=None,crrnt_sales_fc=None,optml_sales_fc=None,
                    plan_sellthru_fc=None,crrnt_sellthru_fc=None,optml_sellthru_fc=None, lqdt_src=False):
        self.receipt_dt = receipt_dt
        self.units = units
        self.crrnt_price = crrnt_price
        self.optml_price = optml_price
        self.plan_gm_fc = plan_gm_fc
        self.crrnt_gm_fc = crrnt_gm_fc
        self.optml_gm_fc = optml_gm_fc
        self.plan_sales_fc = plan_sales_fc
        self.crrnt_sales_fc = crrnt_sales_fc
        self.optml_sales_fc = optml_sales_fc
        self.plan_sellthru_fc = plan_sellthru_fc
        self.crrnt_sellthru_fc = crrnt_sellthru_fc
        self.optml_sellthru_fc = optml_sellthru_fc
        self.lqdt_src = lqdt_src

class SKU(db.Model):
    __tablename__ = 'skus'
    id = db.Column(db.Integer, primary_key=True)
    sku_num = db.Column(db.String(32), unique=True) #nullable
    prod_nm = db.Column(db.String(64)) #nullable
    brand = db.Column(db.String(64))
    org_price = db.Column(db.Integer) #nullable
    launch_dt = db.Column(db.Date)
    phase_out = db.Column(db.Date)
    unit_cost = db.Column(db.Integer)
    #Liquidation Considerations#
    lqdt_watch = db.Column(db.Boolean, default=False)
    lqdt_rec = db.Column(db.Boolean, default=False)
    on_market = db.Column(db.Boolean, default=False)
    lqdt_price = db.Column(db.Integer)
    units_to_list = db.Column(db.Integer, default=0)
    lqdt_channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'))
    cluster_id = db.Column(db.Integer, db.ForeignKey('clusters.id'))
    
    #shipping dimensions
    #promotions
    #activechannels
    #features
    def __init__(self,sku_num,prod_nm,brand,org_price,launch_dt,phase_out,
                    unit_cost,lqdt_watch,lqdt_rec,on_market,lqdt_price=None,units_to_list=None,
                    lqdt_channel_id=None,cluster_id=None,category_id=None):

        self.sku_num = sku_num
        self.prod_nm = prod_nm
        self.brand = brand
        self.org_price = org_price
        self.launch_dt = launch_dt
        self.phase_out = phase_out
        self.unit_cost = unit_cost
        self.lqdt_watch = lqdt_watch
        self.lqdt_rec = lqdt_rec
        self.on_market = on_market
        self.lqdt_price = lqdt_price
        self.units_to_list = units_to_list
        self.lqdt_channel_id = lqdt_channel_id
        self.cluster_id = cluster_id
        self.category_id = category_id


    
    def lqdt_store(self):
        pass
    
    def avg_price(self):
        pass

    def gm(self,price):
        return ((price - self.unit_cost)/self.unit_cost)

    def price_diff(self):
        """Difference($) between current price and optimal price"""
        return (self.opt_price-self.current_price)
	
    def gm_impact(self):
        return (self.optml_gm_fc-self.crrnt_gm_fc)

    #Data Pulled from Optimization model#
    def get_metric(self,metric='gm',crrnt_or_optml='crrnt'):
        info = _skus['skus'][0]['xo22']['fcs'][metric][crrnt_or_optml]
        return info


    def get_lqdt_stat(self,stat):
        pass


class Cluster(db.Model):
    __tablename__ = 'clusters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) #nullable
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    skus = db.relationship('SKU', lazy='dynamic')

    def __init__(self,name,category_id=None):
        self.name = name
        self.category_id = category_id


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) #nullable
    clusters = db.relationship('Cluster', lazy='dynamic')

    def __init__(self,name):
        self.name = name


class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True) #nullable

    def __init__(self,name):
        self.name = name
#Other Skipped classes: pricing_cluster, features
