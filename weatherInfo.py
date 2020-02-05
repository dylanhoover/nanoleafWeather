import requests 
import json
from variables import *

url = 'http://api.openweathermap.org/data/2.5/weather?q=Santa%20Clara,us&units=imperial&APPID=' + api_key

json_data = requests.get(url).json()

class getWeatherData():

    
    def currentConditions(self):
        self.conditions = json_data['weather'][0]['main']
        #print(self.conditions)
        return self.conditions
    
    def currentTemp(self):
        tempurature = json_data['main']['temp']
        #print(tempurature)
        return tempurature
    

test = getWeatherData()

test.currentTemp()
