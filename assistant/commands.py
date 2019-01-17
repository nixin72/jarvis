import datetime
import sys

sys.path.insert(0, './modules/Callable/')
from audio import Audio
from brightness import Brightness
from alarm import Alarm

def greet(arguments, user):
    aprx_time = datetime.datetime.now().hour
    greet = "Hello"
    if aprx_time >= 0 and aprx_time <= 11:
        greet = "Good morning"
    if aprx_time >= 12 and aprx_time <= 19:
        greet = "Good afternoon"
    if aprx_time >= 20:
        greet = "Good Evening"

    return greet + " " + user.getName()

def invalid(arguments, user):
    return "Invalid command"

def shutdown(arguments, user):
    exit()

def spotify(arguments, user):
    print (arguments)

def fetch(arguments, user):
    print ("Not yet implemented")

def setter(arguments, user):
    print(arguments)
    obj = arguments[0]
    setting = arguments[1]
    curr = None
    if obj == "volume":
        if setting == "up":
            Audio.volume_up()
        elif setting == "down":
            Audio.volume_down()
        elif setting == "full":
            Audio.volume_max()
        elif setting == "mute" or setting == "off":
            Audio.mute()
        elif setting == "unmute":
            Audio.mute()
        else: 
            Audio.set(int(setting))

        curr = Audio.current_volume()
    if obj == "brightness":
        if setting == "up":
            Brightness.up()
        elif setting == "down":
            Brightness.down()
        elif setting == "full" or setting == "max":
            Brightness.max()
        elif setting == "min":
            Brightness.min()
        else: 
            Brightness.set(int(setting))
        curr = Brightness.current_brightness()
    if obj == "alarm":
        Alarm.set(setting)

    return obj + " set to " + str(curr)