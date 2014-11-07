from flask import Blueprint
from flask.ext.restful import Resource, Api

main = Blueprint('main',__name__)
main_api = Api(main)

_skus =  {
			'skus': [
				{101:
					{'forecasts': {
						'gm': {
							'crrnt': 15,
							'optml': 18
							},
						'sales': {
							'crrnt': 35,
							'optml': 40
							},
			            'sellthrough': {
							'crrnt': .8,
							'optml': .85
							}
					},
					'liquidation': {
						'recommended': True,
						'watchlist': True,
						'list_price': 43,
						'channel': 'Amazon',
						'units': 17,
						'stores': ['321','322','345']
					}}
				}
			]}

_sku_clusters = {
			'clusters': [
				{201:
					{'forecasts': {
					'gm': {
						'crrnt': 112,
						'optml': 125
						},
					'sales': {
						'crrnt': 200,
						'optml': 222
						},
		            'sellthrough': {
						'crrnt': .8,
						'optml': .85
						}
					}}},
				{203:
					{'forecasts': {
					'gm': {
						'crrnt': 56,
						'optml': 65
						},
					'sales': {
						'crrnt': 150,
						'optml': 165
						},
		            'sellthrough': {
						'crrnt': .70,
						'optml': .77
						}
					}}},
				{204:
				{'forecasts': {
				'gm': {
					'crrnt': 88,
					'optml': 93
					},
				'sales': {
					'crrnt': 163,
					'optml': 188
					},
	            'sellthrough': {
					'crrnt': .68,
					'optml': .75
					}
				}}},]
			}

_stores = {
			'stores': [
				{301: {
					'gm': {
						'crrnt': 88,
						'optml': 93
					},
					'sales': {
						'crrnt': 163,
						'optml': 188
					},
	            	'sellthrough': {
						'crrnt': .68,
						'optml': .75
					}
				}}
			]
		}
_categories = {
				'categories': {
					401: {
					'gm': {
						'crrnt': 88,
						'optml': 93,
						'plan': 90
					},
					'sales': {
						'crrnt': 163,
						'optml': 188,
						'plan': 180
					},
	            	'sellthrough': {
						'crrnt': .68,
						'optml': .75,
						'plan': 1.0
					},
					'rolling':[
						{'sales': {
							'crrnt': [1,2,3 ],
							'prioryr': [3,4,5],
							'plan': [6,7,8]
						}},
						{'gm': {
							'crrnt': [1,2,3 ],
							'prioryr': [3,4,5],
							'plan': [6,7,8]
						}}
					],
					'actions': 6
					}}
			}

_store_distro = {
			'stores': [
				{322: {
					'clusters': [
						{'total': {
							'gm': {
							'crrnt': 88,
							'optml': 93,
							'plan': 87
							},
							'sales': {
							'crrnt': 163,
							'optml': 188,
							'plan': 166
							},
			            	'sellthrough': {
							'crrnt': .68,
							'optml': .75,
							'plan': 1
							},
						}},
						{202: {
							'gm': {
							'crrnt': 88,
							'optml': 93,
							'plan': 87
							},
							'sales': {
							'crrnt': 163,
							'optml': 188,
							'plan': 166
							},
			            	'sellthrough': {
							'crrnt': .68,
							'optml': .75,
							'plan': 1
							}
						}}
					]
				}},	
			],
			'lists': {
				'top_perf': [101,106,108,110,112,120,121,130,133,140],
				'bottom_perf': [99,102,111,115,125,126,131,135,136,137]
				}
		}


# main_api.add_resource(_skus,'/api/skus')
# main_api.add_resource(_sku_clusters,'/api/clusters')
# main_api.add_resource(_stores,'/api/stores')
# main_api.add_resource(_store_distro,'/api/distro')

from . import routes, helper, forms