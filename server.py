from flask import Flask
import dht_operations as dht

app = Flask(__name__)

@app.route("/")
def home():
    t, h, time, human_time = dht.get_live_data(4)
    return render_template("index.html", human_time, t, h)
