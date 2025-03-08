from flask import Flask
import dht_operations as dht

app = Flask(__name__)

@app.route("/")
def home():
    t, h, time, human_time = dht.get_live_data(4)
    webshite = '''
    <center>
    <title>Bedroom Weather</title>
    <body style="background: url(static/bokeh.jpg); background-size: auto;
    color:#c1e2f5; font-family: arial; font-style: italic; letter-spacing: 3px;">
    <h1>Bedroom Weather</h1>
    <p>%s</p>
    <p>%s°c</p>
    <p>%s%%</p>
    <img src=\"static/bedroom.png\">
    <img src=\"static/outdoor.png\">
    </center>''' % (human_time, t, h)
    return webshite
