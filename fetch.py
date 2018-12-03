import psycopg2
import config as config
import sys
import argparse

def fetch(conn, tableName):
	cursor = conn.cursor()
	##cursor.execute("SELECT id, name, address, city, date FROM kijisearch_programs")
	cursor.execute("SELECT * FROM {}".format(tableName))
	print (cursor.fetchall())
	res = cursor.fetchall()
	cursor.close()
	return res

def fetchCamps(conn):
	return fetch(conn, 'kijisearch_camps')

def fetchPrograms(conn):
	return fetch(conn, 'kijisearch_programs')


if __name__ == '__main__':

	conn = config.connect()
	if len(sys.argv) == 1:
		fetch(conn, 'kijisearch_camps')
		print("\nDefaulted to fetch kijisearch_camps")
	elif len(sys.argv) == 2:
		fetch(conn, sys.argv[1])

	conn.close()
