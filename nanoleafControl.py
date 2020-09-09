from nanoleafapi import Nanoleaf
from nanoleafapi import RED, ORANGE,YELLOW,BLUE,GREEN,WHITE,LIGHT_BLUE,PINK,PURPLE
from variables import ip, authtoken

nl = Nanoleaf(ip,authtoken)

def powerOff():
    nl.power_off()
    return

class weatherControl():

    @staticmethod
    def thunderStorm():
        nl.set_effect("Thunder")
        return

    @staticmethod
    def rain():
        nl.set_effect("Rain")
        return
    
    @staticmethod
    def sunshine():
        nl.set_effect("Sunlight")
        return
    
    @staticmethod
    def clouds():
        nl.set_effect("Clouds")
        return

    @staticmethod
    def smoke():
        nl.set_effect("Smoke")
        return

class tempControl():

    def hotOutside(self):
        nl.set_color(RED)
        return
    
    def niceOutside(self):
        nl.set_color(YELLOW)
        return

    def coldOutside(self):
        nl.set_color(BLUE)
        return

