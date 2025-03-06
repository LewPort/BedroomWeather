from flask import Flask
import dht_operations as dht

app = Flask(__name__)

@app.route("/")
def home():
    t, h, time, human_time = dht.get_live_data(4)
    webshite = '''
    <center>
    <title>Bedroom Weather</title>
    <body style="background-color:#024063; color:#c1e2f5; font-family: Tahoma, sans-serif;">
    <h1>Bedroom Weather</h1>
    <p>%s</p>
    <p>%s°c</p>
    <p>%s%%</p>
    <img src=\"static/graph.jpg\">
    </center>''' % (human_time, t, h)
    return webshite
