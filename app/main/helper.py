#!/usr/bin/env python
from . import main
from ..models import SKU, Category
from app import db

def get_categories():
    cat_list = []
    for cat in db.session.query(Category).all():
	    cat_list.append((cat.id,cat.category))
    return cat_list
