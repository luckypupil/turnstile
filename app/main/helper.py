#!/usr/bin/env python
from . import main
from ..models import SKU, Category
from app import db
from operator import itemgetter
import numpy as np
import pygal
import random

# def get_categories():
#     cat_list = [(0,' All')]
#     for cat in db.session.query(Category).all():
# 	    cat_list.append((cat.id,cat.name))
#     return sorted(cat_list,key=itemgetter(1))

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

def make_stackedbar(title,plan,forecast,opp):
    # plt.style.use('ggplot')
    plan /= 100000
    forecast /= 100000
    opp /= 100000
    assert title and plan and forecast and opp, "missing params"
    bar_chart = pygal.StackedBar(style=pygal.style.LightColorizedStyle)
    bar_chart.title = title
    bar_chart.x_labels = ['Plan','Forecast']
    bar_chart.add('Plan', [plan, None])
    bar_chart.add('Forecast', [None, forecast])
    bar_chart.add('Oppty', [None, opp])
    return bar_chart.render(is_unicode=True)

def make_wklybar(title,plan,forecast,opp):
    # plt.style.use('ggplot')
    assert title and plan and forecast and opp, "missing params"
    bar_chart = pygal.StackedBar(style=pygal.style.LightColorizedStyle)
    bar_chart.title = title
    bar_chart.x_labels = map(str,range(12))
    bar_chart.add('Actual', [10,12,8,14,12,11,0,0,0,0,0,0])
    bar_chart.add('Forecast', [0,0,0,0,0,0,12,12,11,14,15,13])
    return bar_chart.render(is_unicode=True)