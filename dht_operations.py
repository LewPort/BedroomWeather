#Libraries
import Adafruit_DHT as dht
import time

#Set DATA pin
DHT_PIN = 4

def get_live_data(pin):
    h,t = dht.read_retry(dht.DHT22, pin)
    time_logged = int(time.time())
    human_time = time.ctime(time_logged)
    h = round(h, 2)
    t = round(t, 2)
    return (t, h, time_logged, human_time)
