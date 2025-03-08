import sql_operations
from datetime import datetime as dt
import time
import sys
from matplotlib import pyplot as plt

HUMD_COLOUR = 'powderblue'
TEMP_COLOUR = 'lightcoral'
OTHER_COLOUR = 'gainsboro'

bedroom_data = sql_operations.return_list_from_db('bedroomweather', 3)
outdoor_data = sql_operations.return_list_from_db('outdoorweather', 3)

plt.style.use('dark_background')



def generate_chart_image(data, title):
    x_axis = [dt.fromtimestamp(row[0]) for row in data]
    temp = [row[2] for row in data]
    humd = [row[3] for row in data]

    fig, temp_axis = plt.subplots()
    humd_axis = temp_axis.twinx()
    temp_axis.set_ylim(-30, 30)
    humd_axis.set_ylim(0,100)
    temp_axis.tick_params(axis='x', rotation=45, color=OTHER_COLOUR)
    temp_axis.set_ylabel("Temp ºc", color=TEMP_COLOUR)
    humd_axis.set_ylabel("Humidity %", color=HUMD_COLOUR)

    temp_axis.plot(x_axis, temp, color=TEMP_COLOUR)
    humd_axis.plot(x_axis, humd, color=HUMD_COLOUR)
    plt.title("%s - Generated %s" % (title, time.strftime('%a %H:%M')), color=OTHER_COLOUR)
    fig.tight_layout(pad=1)
    plt.savefig("/home/lewis/bedroomweather/static/%s.png" % title.lower(), format='png', transparent=True)
    plt.close(fig)

generate_chart_image(bedroom_data, 'Bedroom')
generate_chart_image(outdoor_data, 'Outdoor')
sys.exit()
