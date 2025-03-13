import Adafruit_DHT as dht
import json
import time

DHT_PIN = 4

def get_live_data(pin):
    h,t = dht.read_retry(dht.DHT22, pin) #Get Humidity and Temperature
    time_logged = int(time.time()) #Get Time Logged
    human_time = time.ctime(time_logged) #Create a human-readable version of time_logged
    h = round(h, 2) #Round them to 2 decimal places
    t = round(t, 2)
    return (t, h, time_logged, human_time) #return all that info as tuple

def write_to_json(dht_object):
    t, h, time_logged, human_time = dht_object
    with open('./json/dht.json', 'w') as f:
        data = {'temp': t,
                'humd': h,
                'unix': time_logged,
                'time': human_time
                }
        json.dumps(data, f, indent=4)

write_to_json(get_live_data(DHT_PIN))
