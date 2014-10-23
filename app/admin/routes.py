from flask import render_template, request, redirect, flash, url_for
from . import admin
from ..models import SKU
from app import db
from .forms import prod_entry
from pprint import pprint as pp


@admin.route('/add', methods=['GET','POST'])
def add_prod():
    print('got to add page')
    form = prod_entry()
    
    if form.validate_on_submit():
        if not db.session.query(SKU).filter(SKU.sku_num == form.data['sku_num']).first():
            try:
	            u = SKU(
	                sku_num=form.data['sku_num'],
	                product_name=form.data['product_name'],
	                brand=form.data['brand'],
	                category=form.data['category'],
	                org_price = form.data['org_price'],
	                current_price = form.data['current_price'],
	                opt_price = form.data['opt_price'],
	                release = form.data['release'],
	                phase_out = form.data['phase_out'],
	                unit_cost = form.data['unit_cost']
	                )
	            #db.session.add(u)
	            #db.session.commit()
	            flash('Thanks for your submission!')
	            return(redirect(url_for('main.sku_list')))
            except:
                flash('Something didnt submit')
        else:
            flash('Looks like we already have that SKU')
    else:
    	for error in form.errors.items():
    		flash('{} field, error :{}\n'.format(error[0],error[1][0]))
    return render_template("main/prod_add.html",form=form)