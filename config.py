import psycopg2
import os

def connect():
    try:
        conn = psycopg2.connect("dbname='kijidata' user='postgres' host='localhost' password='{}'".format(os.environ['POSTGRES_IN']))
        return conn
    except:
        print ("I am unable to connect to the database")