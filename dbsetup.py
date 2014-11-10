#!/usr/bin/env python
import psycopg2
from app.models import SKU, Store, Store_Distribution
from app import db
from random import randint

Models = {
		'categories': ['name'],
		'companies': ['name','street','city','state','zipcd'],
		'segments': ['name'],
		'channels': ['name'],
		'skus': ['sku_num','prod_nm','brand','org_price','launch_dt','phase_out',
				'unit_cost','lqdt_watch','lqdt_rec','on_market','lqdt_price'],
		'stores': ['store_num','street','city','state',	'zipcd','warehouse'],
		'clusters':['name'],
		'user_roles':['name'],
		'users':['first','last','email','password','phone'],
		'store_distribution':['sku_id','store_id','receipt_dt','units','crrnt_price','optml_price','plan_gm_fc','crrnt_gm_fc','optml_gm_fc','plan_sales_fc',
			'crrnt_sales_fc','optml_sales_fc','plan_sellthru_fc','crrnt_sellthru_fc','optml_sellthru_fc','lqdt_src']
		} 


def popdb(*tables):	
     
    conn = psycopg2.connect("dbname=devturnstile user=blakeadams")
    cur = conn.cursor()
    copyit = "BEGIN;"
    for table in tables:
    	copyit+= 'COPY {} ('.format(table)
    	for column in Models[table]:
    		copyit+= column+','
    	copyit = copyit[:-1]
    	copyit+=") FROM '/Users/blakeadams/Dev/turnstile/dbs/csv/{}.csv' DELIMITER ',' CSV;".format(table)

    copyit+= "COMMIT;"		
    #print (copyit)
    cur.execute(copyit)
    conn.commit()
    cur.close()
    conn.close()

def store_distro():
	skus = SKU.query.all()
	stores = Store.query.all()
	for sku in skus:
		for store in stores:
			units = randint(50,225)
			crrnt_price = int(sku.org_price*randint(85,100)/100)
			optml_price = int(crrnt_price*randint(90,100)/100)
			plan_gm_fc = int(units*crrnt_price*.25)
			crrnt_gm_fc = int(plan_gm_fc*randint(90,105)/100)
			optml_gm_fc = int(crrnt_gm_fc*randint(100,115)/100)
			plan_sales_fc = int(units*crrnt_price*.95)
			crrnt_sales_fc = int(plan_sales_fc*randint(90,105)/100)
			optml_sales_fc = int(crrnt_sales_fc*randint(100,115)/100)
			plan_sellthru_fc = randint(80,100)
			crrnt_sellthru_fc = plan_sellthru_fc - randint(1,9)
			optml_sellthru_fc = crrnt_sellthru_fc + randint(1,12)
			sku_store = Store_Distribution(sku.launch_dt,units,crrnt_price,optml_price,
				plan_gm_fc,crrnt_gm_fc,optml_gm_fc,plan_sales_fc,crrnt_sales_fc,optml_sales_fc,
				plan_sellthru_fc,crrnt_sellthru_fc,optml_sellthru_fc)    
			sku_store.sku_id, sku_store.store_id = sku.id, store.id
			# print (sku_store)
			db.session.add(sku_store)
			db.session.commit()


if __name__ == '__main__':
	#popdb('categories','companies','segments','channels','skus','stores','clusters','user_roles','users')
	store_distro()