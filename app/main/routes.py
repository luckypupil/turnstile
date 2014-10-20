from flask import render_template, request
from . import main
from ..models import SKU
from app import db

@main.route('/')
def dashboard():
	return render_template("main/dashboard.html",message='hello world!')

@main.route('/list')
def sku_list():
	skus = SKU.query.all()
	return render_template("main/sku_list.html",skus=skus)

@main.route('/stores')
def sku_store():
	return render_template("main/sku_store.html",message='hello world!')

@main.route('/disposition')
def dispo_list():
	return render_template("main/dispo_list.html",message='hello world!')

@main.route('/disposition/<product>')
def dispo_profile(product):
	return render_template("main/dispo_profile.html",message='hello world!')


