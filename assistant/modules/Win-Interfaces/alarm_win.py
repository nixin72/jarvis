import json
import os

class Alarm:
    PATH = r"C:\Users\\" + os.getenv('username') + "\AppData\Local\Packages\Microsoft.WindowsAlarms_8wekyb3d8bbwe\LocalState\Alarms\Alarms.json"
    alarms = None

    @staticmethod
    def set(time):
        if Alarm.alarms == None:
            with open(Alarm.PATH, "r") as data:
                Alarm.alarms = json.load(data)
            print(Alarm.alarms)

