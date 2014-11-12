#!/usr/bin/env python
from . import main
from ..models import SKU, Category, Store_Distribution
from app import db
from operator import itemgetter
import numpy as np

import random
from sqlalchemy import func

def get_categories():
    cat_list = [(0,' All')]
    for cat in db.session.query(Category).all():
	    cat_list.append((cat.id,cat.name))
    return sorted(cat_list,key=itemgetter(1))

def get_clusters(cat_id):
    cluster_list = [(0,' All')]
    category = Category.query.get(cat_id)
    for cluster in category.clusters.all():
        cluster_list.append((cluster.id,cluster.name))
    return sorted(cluster_list,key=itemgetter(1))

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def get_states():
    state_list = [('','All')]
    for state in states:
	    state_list.append((state,state))

    return sorted(state_list,key=itemgetter(0))


def get_sku_units(skuid=5):
    units = db.session.query(func.sum(Store_Distribution.units)).filter(Store_Distribution.sku_id == skuid).first()
    return units



def get_clust_met(skus):
    units = 0
    for sku in skus:
        units+=get_sku_units(sku.id)
    return units


