import sql_operations
from datetime import datetime as dt
import time
import sys
from matplotlib import pyplot as plt

data = sql_operations.list_from_all_data()

x_axis = [dt.fromtimestamp(row[0]) for row in data]
temp = [row[2] for row in data]
humd = [row[3] for row in data]

fig, temp_axis = plt.subplots()
humd_axis = temp_axis.twinx()
temp_axis.set_ylim(0, 30)
humd_axis.set_ylim(20,80)
temp_axis.tick_params(axis='x', rotation=45)
temp_axis.set_ylabel("Temp ºc", color='r')
humd_axis.set_ylabel("Humidity %", color='b')

temp_axis.plot(x_axis, temp, 'r')
humd_axis.plot(x_axis, humd, 'b')
#plt.locator_params(axis='x', nbins=12)
plt.title("Temperature & Humidity - Generated %s" % time.strftime('%a %H:%M'))
fig.tight_layout(pad=1)
plt.savefig("/home/lewis/bedroomweather/static/graph.jpg")
plt.close(fig)
sys.exit()
