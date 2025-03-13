from flask import Flask
from flask import render_template
import bedroom_api_operations
import sql_operations as sql

app = Flask(__name__)

@app.route("/")
def home():
    indoor_temp, indoor_humid, time, indoor_human_time = bedroom_api_operations.get_dht_json()
    outdoor_data = sql.return_list_from_db('outdoorweather', 1)[-1]
    outdoor_time, outdoor_human_time, outdoor_temp, outdoor_humid, outdoor_pressure, outdoor_wind_speed, outdoor_wind_dir = outdoor_data
    return render_template("index.html",
                           human_time=indoor_human_time,
                           indoor_temp=indoor_temp,
                           indoor_humid=indoor_humid,
                           outdoor_temp=round(outdoor_temp, 1),
                           outdoor_humid=outdoor_humid,
                           outdoor_pressure=outdoor_pressure,
                           outdoor_wind_speed=round(outdoor_wind_speed,1),
                           outdoor_wind_dir=outdoor_wind_dir)

#butts