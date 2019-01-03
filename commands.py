import datetime
import sys

sys.path.insert(0, './lib/Win-Audio/')
from sound import Sound
from brightness import Brightness

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

def setter(arguments, user):
    print(arguments)
    obj = arguments[0]
    setting = arguments[1]
    if obj == "volume":
        if setting == "up":
            Sound.volume_up()
        elif setting == "down":
            Sound.volume_down()
        elif setting == "full":
            Sound.volume_max()
        elif setting == "mute" or setting == "off":
            Sound.mute()
        elif setting == "unmute":
            Sound.mute()
        else: 
            Sound.set(int(setting))
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

    return "Volume set to " + str(Sound.current_volume())