from flask import Flask
from flask import render_template
import dht_operations as dht
import sql_operations as sql
from plotter import outdoor_data

app = Flask(__name__)

@app.route("/")
def home():
    indoor_temp, indoor_humid, time, indoor_human_time = dht.get_live_data(4)
    outdoor_data = sql.return_list_from_db('outdoorweather', 1)[-1]
    outdoor_time, outdoor_human_time, outdoor_temp, outdoor_humid, outdoor_pressure, outdoor_wind_speed, outdoor_wind_dir = outdoor_data
    return render_template("index.html",
                           human_time=indoor_human_time,
                           indoor_temp=indoor_temp,
                           indoor_humid=indoor_humid,
                           outdoor_temp=outdoor_temp,
                           outdoor_humid=outdoor_humid,
                           outdoor_pressure=outdoor_pressure,
                           outdoor_wind_speed=outdoor_wind_speed,
                           outdoor_wind_dir=outdoor_wind_dir)
