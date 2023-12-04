import psycopg2
conn = psycopg2.connect(
   database="proyectocurso", user='postgres', password='vordank', host='127.0.0.1', port= '5432'
)
cur = conn.cursor()

sentencia = "INSERT INTO producto (nombre, descripcion, precio, stock) VALUES (%s,%s,%s,%s)"
recs = [('MotherBoard', 'Una motherboard', 8700000,10)] 
cur.executemany(sentencia, recs) 
conn.commit() 
conn.close()