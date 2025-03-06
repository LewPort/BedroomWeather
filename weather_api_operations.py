import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

API_KEY = os.environ("API_KEY")
LAT, LON = 43.2334, -79.9496
MODE = 'xml'
LANG = 'en'
UNITS = 'metric'

def API_call(lat, lon):
    # Generate openweathermap.org api request with the options I want (the ones in the constants)
    API_CALL = ('https://api.openweathermap.org/data/2.5/weather?lat=%f&lon=%f&appid=%s&mode=%s&lang=%s&units=%s'
            % (lat,lon,API_KEY,MODE,LANG,UNITS))
    return API_CALL

def return_current_weather():
    #Get data (temperature etc) from the XML file returned by the API_Call above, and return it as tuple
    r = requests.get(API_call(LAT, LON)) #get the xml data
    XML_result = r.text #convert to a string
    soup = BeautifulSoup(XML_result, 'xml') #parse the data with beautiful soup

    #store data in variables
    time = soup.lastupdate.get("value") #time of report
    temp = soup.temperature.get("value") #ºc
    humd = soup.humidity.get("value") #%
    press = soup.pressure.get("value") #HPa
    wind_spd = soup.wind.speed.get("value") #m/s
    wind_dir = soup.wind.direction.get("value") #degs

    return (time, temp, humd, press, wind_spd, wind_dir)

