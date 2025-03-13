import os
from dotenv import load_dotenv
import json
from urllib.request import urlopen

load_dotenv()

DHT_URL = os.getenv("DHT_URL")

def get_dht_json():
    with urlopen(DHT_URL) as response:
        source = response.read()
    data = json.loads(source)
    return data