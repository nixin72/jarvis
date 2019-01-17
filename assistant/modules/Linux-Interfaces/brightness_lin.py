import os

class Brightness:
    """
    Class Brightness
    :author: Paradoxis <luke@paradoxis.nl>
    :description:

    Allows you control the Windows volume
    The first time a sound method is called, the system volume is fully reset.
    This triggers sound and mute tracking.
    """

    # Current volume, we will set this to 100 once initialized
    __current_brightness = None

    @staticmethod
    def current_brightness():
        """
        Current brightness getter
        :return: int
        """
        if Brightness.__current_brightness is None:
            return 0
        else:
            return Brightness.__current_brightness

    @staticmethod
    def __set_current_brightness(brightness):
        """
        Current brightness setter
        prevents numbers higher than 100 and numbers lower than 0
        :return: void
        """
        if brightness > 100:
            Brightness.__current_brightness = 100
        elif brightness < 0:
            Brightness.__current_brightness = 0
        else:
            Brightness.__current_brightness = brightness


    @staticmethod
    def __track():
        """
        Start tracking the sound and mute settings
        :return: void
        """
        if Brightness.__current_brightness == None:
            Brightness.set(100)

    @staticmethod
    def up():
        Brightness.__track()
        Brightness.set(Brightness.__current_brightness + 10)

    @staticmethod
    def down():
        Brightness.__track()
        Brightness.set(Brightness.__current_brightness - 10)

    @staticmethod
    def set(amount):
        os.system("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + str(amount) + ")")

    @staticmethod
    def min():
        Brightness.set(0)

    @staticmethod
    def max():
        Brightness.set(100)