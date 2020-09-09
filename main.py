######################################################################
# Created by: Dylan Hoover                                           #
# Main file for nanoleaf weather                                     #
# File requires nanoLeafControl.py and weatherInfo.py to function    #




from weatherInfo import getWeatherData
from nanoleafControl import weatherControl
from nanoleafControl import tempControl
from nanoleafControl import powerOff

data = getWeatherData()
condition = data.currentConditions()
temp = data.currentTemp()

def main():
    
    weather = displayWeatherConditions()
    temp = displayTemperature()

    while True:
        selection = int(input("Select 0 for weather\nSelect 1 for Temperature\nSelect 2 to power off\nSelect 3 to exit\nSelection: "))
        if(selection == 0):
            weather.switcher()
        elif(selection == 1):
            temp.switcher()
        elif(selection == 2):
            powerOff()
        elif(selection == 3):
            break
        else:
            print("Not an option\n")
    
    return
    
    

class displayWeatherConditions():

    ctrl = weatherControl()

    def clear(self):
        self.ctrl.sunshine()
        return
    
    def clouds(self):
        self.ctrl.clouds()
        return
    
    def thunder(self):
        self.ctrl.thunderStorm()
        return
    
    def rain(self):
        self.ctrl.rain()
        return
    
    def smoke(self):
        self.ctrl.smoke()
        return

    def switcher(self):
        if(condition == "Clear"):
            self.clear()
        elif(condition == "Clouds"):
            self.clouds()
        elif(condition == "Thunder Storm"):
            self.thunder()
        elif(condition == "Rain"):
            self.rain()
        elif(condition == "Smoke"):
            self.smoke()
        else:
            pass
        return
    


class displayTemperature():

    ctrl = tempControl()

    def hot(self):
        self.ctrl.hotOutside()
        return
    
    def nice(self):
        self.ctrl.niceOutside()
        return
    
    def cold(self):
        self.ctrl.coldOutside()
        return
    
    def switcher(self):
        if(temp >= 85):
            self.hot()
        elif(temp >= 60 and temp < 85):
            self.nice()
        elif(temp < 60):
            self.cold()
        else:
            pass
        return
    
    

main()