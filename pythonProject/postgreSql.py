import psycopg2 as pg2
conn = pg2.connect(database='dvdrental',user='postgres',password='nikhil123')
cur = conn.cursor()
cur.execute('select * from payment')
cur.fetchmany(10)
print(cur.fetchmany(10))
conn.close()