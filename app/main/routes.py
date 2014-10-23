from flask import render_template, request, redirect, flash, url_for
from . import main
from ..models import SKU, Category
from app import db
from .forms import prod_entry, sku_list_search
from pprint import pprint as pp

@main.route('/')
def dashboard():
	return render_template("main/dashboard.html",message='hello world!')

@main.route('/list', methods=["POST","GET"])
def sku_list():
    skus = db.session.query(SKU).all()
    form = sku_list_search()
    if form.validate_on_submit():
        cat_id, sku_num = form.category.data, form.sku.data
        if sku_num:
            skus = db.session.query(SKU).filter(SKU.sku_num == sku_num).all()
        else:
           skus = (skus if not cat_id else db.session.query(SKU).filter(SKU.category == cat_id).all())

    return render_template("main/sku_list.html",skus=skus, form=form)

@main.route('/stores')
def sku_store():
	return render_template("main/sku_store.html",message='hello world!')

@main.route('/disposition')
def dispo_list():
	return render_template("main/dispo_list.html",message='hello world!')

@main.route('/disposition/<product>')
def dispo_profile(product):
	return render_template("main/dispo_profile.html",message='hello world!')


