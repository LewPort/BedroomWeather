#Libraries
import dht_operations as dht
import sqlite3
import time

#Set DATA pin
DHT_PIN = 4

con = sqlite3.connect("/home/lewis/bedroomweather/bedroomweather.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS bedroomweather(time INT, readable TEXT, temp REAL, humd REAL)")

def list_from_all_data():
    cur.execute("SELECT * FROM bedroomweather")
    data = cur.fetchall()
    return data

def log_reading_to_db():
    t, h, time_logged, human_time = dht.get_live_data(DHT_PIN)
    if (t or h) != None:
        sql_insert_statement= "INSERT INTO bedroomweather VALUES (%i, \'%s\', %f, %f)" % (time_logged, human_time, t, h)
        cur.execute(sql_insert_statement)
        con.commit()

log_reading_to_db()
