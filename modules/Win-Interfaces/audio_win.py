from keyboard_win import Keyboard

class Audio:
    __current_volume = None

    @staticmethod
    def current_volume():
        """
        Current volume getter
        :return: int
        """
        if Audio.__current_volume is None:
            return 0
        else:
            return Audio.__current_volume

    @staticmethod
    def __set_current_volume(volume):
        """
        Current volumne setter
        prevents numbers higher than 100 and numbers lower than 0
        :return: void
        """
        if volume > 100:
            Audio.__current_volume = 100
        elif volume < 0:
            Audio.__current_volume = 0
        else:
            Audio.__current_volume = volume


    # The Audio is not muted by default, better tracking should be made
    __is_muted = False

    @staticmethod
    def is_muted():
        """
        Is muted getter
        :return: boolean
        """
        return Audio.__is_muted

    @staticmethod
    def __track():
        """
        Start tracking the Audio and mute settings
        :return: void
        """
        if Audio.__current_volume == None:
            Audio.__current_volume = 0
            for i in range(0, 50):
                Audio.up()

    @staticmethod
    def mute():
        """
        Mute or un-mute the system Audios
        Done by triggering a fake VK_VOLUME_MUTE key event
        :return: void
        """
        Audio.__track()
        Audio.__is_muted = (not Audio.__is_muted)
        Keyboard.key(Keyboard.VK_VOLUME_MUTE)

    @staticmethod
    def up():
        """
        Increase system volume
        Done by triggering a fake VK_VOLUME_UP key event
        :return: void
        """
        Audio.__track()
        Audio.__set_current_volume(Audio.current_volume() + 2)
        Keyboard.key(Keyboard.VK_VOLUME_UP)

    @staticmethod
    def down():
        """
        Decrease system volume
        Done by triggering a fake VK_VOLUME_DOWN key event
        :return: void
        """
        Audio.__track()
        Audio.__set_current_volume(Audio.current_volume() - 2)
        Keyboard.key(Keyboard.VK_VOLUME_DOWN)


    @staticmethod
    def set(amount):
        """
        Set the volume to a specific volume, limited to even numbers.
        This is due to the fact that a VK_VOLUME_UP/VK_VOLUME_DOWN event increases
        or decreases the volume by two every single time.
        :return: void
        """
        Audio.__track()

        if Audio.current_volume() > amount:
            for i in range(0, int((Audio.current_volume() - amount) / 2)):
                Audio.down()
        else:
            for i in range(0, int((amount - Audio.current_volume()) / 2)):
                Audio.up()

    @staticmethod
    def min():
        Audio.set(0)

    @staticmethod
    def max():
        Audio.set(100)