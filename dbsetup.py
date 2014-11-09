#!/usr/bin/env python
import psycopg2

Models = {
		'categories': ['name'],
		'companies': ['name','street','city','state','zip'],
		'segments': ['type'],
		'channels': ['name'],
		'skus': ['sku_num','prod_name','brand','cluster_id','subcategory_id','category_id','org_price','current_price','launch_dt',
			'phase_out','unit_cost','opt_price','plan_gm_forecast','crrnt_gm_forecast','optml_gm_forecast','plan_sales_forecast',
			'crrnt_sales_forecast','optml_sales_forecast','plan_sellthru_forecast','crrnt_sellthru_forecast','optml_sellthru_forecast',
			'lqdt_recommended','on_market','lqdt_price','units_to_list'],
		'stores': ['store_num','street','city','state',	'zip','warehouse','crrnt_gm_forecast','optml_gm_forecast',
			'crrnt_sales_forecast','optml_sales_forecast','crrnt_sellthru_forecast','optml_sellthru_forecast'],
		'subcats': ['name'],
		'clusters':['name', 'category_id'],
		'user_roles':['role'],
		'users':['first_name','last_name','email','password','phone']
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

if __name__ == '__main__':
	popdb('categories','companies','segments','channels','skus','stores','subcats','clusters','user_roles','users')