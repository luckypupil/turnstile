from flask import render_template, request, redirect, flash, url_for, make_response
from . import main
from ..models import SKU, Category, Store, Cluster, Channel
from app import db
from .forms import cluster_anal, sku_store_search, cat_select
from pprint import pprint as pp
from random import randint
from .helper import get_clusters


@main.route('/', methods=["POST","GET"])
def dashboard():

    form = cat_select()
    
    if form.validate_on_submit():
        cat_id = form.categories.data
        print (cat_id)
        # category = Category.query.get(cat_id) # Need to populate data for cats for this to work
        category = Category.query.get(7)
    else:
        category = Category.query.get(7)
    
    clusters = get_clusters(7)
    graphs = category.graphs()

    return render_template("main/dashboard.html",message='hello world!',graphs=graphs,clusters=clusters,category=category,randint=randint, form=form)

@main.route('/analysis', methods=["POST","GET"])
def analysis():
    category = Category.query.get(7)
    clusters = category.clusters.all()
    clusters = list(filter(lambda x: x.metric() > 0, clusters))
    graphs = category.graphs()

    skus = db.session.query(SKU).all()
    form = cat_select()
    formanal = cluster_anal()
    if form.validate_on_submit():
        cat_id, sku_num = form.category.data, form.sku.data
        if sku_num:
            skus = db.session.query(SKU).filter(SKU.sku_num == sku_num).all()
        else:
           skus = (skus if not cat_id else db.session.query(SKU).filter(SKU.category == cat_id).all())

    return render_template("main/analysis.html",skus=skus, form=form, formanal=formanal,results=len(skus),graphs=graphs)


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
    listskus = SKU.query.filter(SKU.lqdt_rec == True)
    watchskus = SKU.query.filter(SKU.lqdt_watch == True)
    return render_template("main/dispositions.html",listskus=listskus,watchskus=watchskus)

@main.route('/disposition/profile/<int:id>')
def dispo_profile(id=21):
    sku = SKU.query.get_or_404(id)
    
    return render_template("main/dispo_profile.html",sku=sku)





