import psycopg2
import config as config

def fetch(conn):
	cursor = conn.cursor()
	##cursor.execute("SELECT id, name, address, city, date FROM kijisearch_programs")
	cursor.execute("SELECT %s, %s, %s FROM kijisearch_programs", ('id', 'name', 'date',))
	print (cursor.fetchall())
	return cursor.fetchall()

if __name__ == '__main__':
	conn = config.connect()
	fetch(conn)
