from Exceptions import UnsupportedOperatingSystem
from osd import OS 
import sys

sys.path.insert(0, './modules/Win-Interfaces/')
# sys.path.insert(0, '../Linux-Interfaces/')
# sys.path.insert(0, '../Mac-Interfaces/')


from audio_win import Audio as winA
# from audio_lin import Audio as linA
# from audio_mac import Audio as macA

WIN = "Windows"
LIN = "Linux"
MAC = "Darwin"

class Audio:
    __current_volume = None

    @staticmethod
    def current_volume():
        if OS == WIN:
            winA.current_volume()
        # elif OS == LIN:
        #     linB.current_volume()
        # elif OS == MAC:
        #     macB.current_volume()
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def __set_current_volume(volume):
        if OS == WIN:
            winA.__set_current_volume(volume)
        # elif OS == LIN:
        #     linB.__set_current_volume(volume)
        # elif OS == MAC:
        #     macB.__set_current_volume(volume)
        else:
            raise UnsupportedOperatingSystem("")


    @staticmethod
    def __track():
        if OS == WIN:
            winA.__track()
        # elif OS == LIN:
        #     linB.__track()
        # elif OS == MAC:
        #     macB.__track()
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def up():
        if OS == WIN:
            winA.up()
        # elif OS == LIN:
        #     linB.up()
        # elif OS == MAC:
        #     macB.up()
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def down():
        if OS == WIN:
            winA.down()
        # elif OS == LIN:
        #     linB.down()
        # elif OS == MAC:
        #     macB.down()
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def set(amount):
        if OS == WIN:
            winA.set(amount)
        # elif OS == LIN:
        #     linB.set(amount)
        # elif OS == MAC:
        #     macB.set(amount)
        else:
            raise UnsupportedOperatingSystem("")

    @staticmethod
    def min():
        Audio.set(0)

    @staticmethod
    def max():
        Audio.set(100)