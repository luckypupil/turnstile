from flask import render_template, request, redirect, flash, url_for, make_response
from . import main
from ..models import SKU, Category, Store, Cluster
from app import db
from .forms import sku_list_search, sku_store_search
from pprint import pprint as pp
from .helper import make_stackedbar, make_wklybar
from . import _skus, _stores, _sku_clusters, _store_distro, _categories

@main.route('/')
def dashboard():
    # Cat Info
    cat_skus = SKU.query.filter_by(category_id = 7).all()
    salesP = sum(i.plan_sales_forecast for i in cat_skus)
    salesC = sum(i.crrnt_sales_forecast for i in cat_skus)
    salesO = sum(i.optml_sales_forecast for i in cat_skus)-salesC

    gmP = sum(i.plan_gm_forecast for i in cat_skus)
    gmC = sum(i.crrnt_gm_forecast for i in cat_skus)
    gmO = sum(i.optml_gm_forecast for i in cat_skus)-gmC
    # cat_clusters = Cluster.filter_by(category_id = 7).all()
    graphs = {}
    graphs['sales'] = make_stackedbar("Sales($K)",salesP,salesC,salesO)
    graphs['gm'] = make_stackedbar('GM($K)',gmP,gmC,gmO)
    graphs['saleswk'] = make_wklybar("Sales($M)",30,28,5)
    graphs['gmwk'] = make_wklybar('GM($M)',13,12,2.5)
    
    clusters = Cluster.query.filter_by(category_id = 7).limit(10).all()
    #test = mysku.get_metric('gm','crrnt')
    return render_template("main/dashboard.html",message='hello world!', graphs=graphs, clusters=clusters)

@main.route('/analysis', methods=["POST","GET"])
def analysis():
    skus = db.session.query(SKU).all()
    form = sku_list_search()
    if form.validate_on_submit():
        cat_id, sku_num = form.category.data, form.sku.data
        if sku_num:
            skus = db.session.query(SKU).filter(SKU.sku_num == sku_num).all()
        else:
           skus = (skus if not cat_id else db.session.query(SKU).filter(SKU.category == cat_id).all())

    return render_template("main/analysis.html",skus=skus, form=form,results=len(skus))


@main.route('/analysis', methods=["POST", "GET"])
def history():
    return('hellow world!')


@main.route('/stores',methods=["POST","GET"])
def stores():
    stores = db.session.query(Store).all()
    form = sku_store_search()
    if form.validate_on_submit():
        print('validated')
        state, store_num = form.state.data, form.store_num.data
        if store_num:
           stores = db.session.query(SKU).filter(Store.store_num == store_num).all()
        else:
           stores = (stores if not state else db.session.query(Store).filter(Store.state == state).all())
    else: print(form.errors)
    return render_template("main/stores.html",stores=stores, form=form,results=len(stores))

@main.route('/disposition')
def dispositions():
	return render_template("main/dispositions.html",message='hello world!')

@main.route('/disposition/profile')
def dispo_profile():
	return render_template("main/dispo_profile.html",message='hello world!')





