from Exceptions import UnsupportedOperatingSystem
from osd import OS 
import sys


sys.path.insert(0, '../Win-Interfaces/')
# sys.path.insert(0, '../Linux-Interfaces/')
# sys.path.insert(0, '../Mac-Interfaces/')

from brightness_win import Brightness as winB
# from brightness_lin import Brightness as linB
# from brightness_mac import Brightness as macB

WIN = "Windows"
LIN = "Linux"
MAC = "Darwin"

class Brightness:
    __current_brightness = None

    @staticmethod
    def current_brightness():
        if OS == WIN:
            winB.current_brightness()
        # elif OS == LIN:
        #     linB.current_brightness()
        # elif OS == MAC:
        #     macB.current_brightness()
        else:
            raise UnsupportedOperatingSystem("")



    @staticmethod
    def __set_current_brightness(brightness):
        if OS == WIN:
            winB.__set_current_brightness(brightness)
        # elif OS == LIN:
        #     linB.__set_current_brightness(brightness)
        # elif OS == MAC:
        #     macB.__set_current_brightness(brightness)
        else:
            raise UnsupportedOperatingSystem("")


    @staticmethod
    def __track():
        if OS == WIN:
            winB.__track()
        # elif OS == LIN:
        #     linB.__track()
        # elif OS == MAC:
        #     macB.__track()
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def up():
        if OS == WIN:
            winB.up()
        # elif OS == LIN:
        #     linB.up()
        # elif OS == MAC:
        #     macB.up()
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def down():
        if OS == WIN:
            winB.down()
        # elif OS == LIN:
        #     linB.down()
        # elif OS == MAC:
        #     macB.down()
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def set(amount):
        if OS == WIN:
            winB.set(amount)
        # elif OS == LIN:
        #     linB.set(amount)
        # elif OS == MAC:
        #     macB.set(amount)
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def min():
        Brightness.set(0)

    @staticmethod
    def max():
        Brightness.set(100)