import psycopg2 as pg2
secret ='admin'
conn = pg2.connect(database ='dvdrental',user ='postgres',password =secret)
cur = conn.cursor()
cur.execute('SELECT payment_id,customer_id FROM payment')
ROW = cur.fetchmany(10)
for i in ROW:
    print(ROW[0])

conn.close()
