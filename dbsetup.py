#!/usr/bin/env python
import psycopg2

Models = {
		'categories': ['name'],
		'companies': ['name','street','city','state','zip'],
		'segments': ['type'],
		'channels': ['name'],
		

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
    cur.execute(copyit)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
	popdb('categories','companies')