import psycopg2
import config as config

def clear(conn tableName):
    cursor = conn.cursor()
	##cursor.execute("SELECT id, name, address, city, date FROM kijisearch_programs")
	cursor.execute("DELETE FROM {}".format(tableName))
    print('{} is clear'.format(tableName))
	cursor.close()
    retunr

def clearPrograms(conn):
    pass

def clearCamps(conn):
    pass

if __name__ == '__main__':
	conn = config.connect()
	if len(sys.argv) == 1:
		clear(conn, 'kijisearch_camps')
		print("\nDefaulted to clear kijisearch_camps")
	elif len(sys.argv) == 2:
		clear(conn, sys.argv[1])

	conn.close()
