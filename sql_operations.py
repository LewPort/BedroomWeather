#Libraries
import dht_operations as dht
import weather_api_operations as outdoor
import sqlite3
import time

#Set DATA pin
DHT_PIN = 4

con = sqlite3.connect("/home/lewis/bedroomweather/bedroomweather.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS bedroomweather(time INT, readable TEXT, temp REAL, humd REAL)")
cur.execute("""CREATE TABLE IF NOT EXISTS outdoorweather(time INT, readable_time TEXT, temp REAL, humd INTEGER, 
            pressure INTEGER, wind_spd REAL, wind_dir INTEGER)""")

def return_list_from_db(db, days = 7):
    current_time = time.time()
    sql_select_statement = """SELECT * 
    FROM %s
    WHERE time > %s""" % (db, current_time - 60*60*24*days)
    cur.execute(sql_select_statement)
    data = cur.fetchall()
    return data

def log_dht_reading_to_db():
    t, h, time_logged, human_time = dht.get_live_data(DHT_PIN)
    if (t or h) != None:
        sql_insert_statement= "INSERT INTO bedroomweather VALUES (%i, \'%s\', %f, %f)" % (time_logged, human_time, t, h)
        cur.execute(sql_insert_statement)
        con.commit()

def log_outdoor_reading_to_db():
    readable_time, temp, humd, press, wind_spd, wind_dir = outdoor.return_current_weather()
    sql_insert_statement= ("INSERT INTO outdoorweather VALUES (%i, \'%s\', %f, %d, %d, %f, %i)"
                           % (time.time(), readable_time, temp, humd, press, wind_spd, wind_dir))
    cur.execute(sql_insert_statement)
    con.commit()

log_dht_reading_to_db()
log_outdoor_reading_to_db()
