from User import User
import speech_recognition as sr
import datetime
import sys 
import re
from command import Command

def log(command):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("./data/cmds.log", "a") as log:
        log.write(time + " ----- " + str(command) + "\n")

def getUser():
    return User.getUser()

def process(command):
    command = command.lower()
    if command == "hello" or command == "hi" or command == "hey":
        return "greet"
    return command

def getInput():
    r = sr.Recognizer()
    mic = sr.Microphone()
    output = None
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        output = r.recognize_google(audio)
    return output

def main():
    stopwords = None
    with open("./data/stopwords.txt", "r") as file:
        stopwords = file.read().split("\n")

    # inputs = input()
    inputs = "hey jarvis set an alarm for 10 pm" 
    # inputs = re.sub("%", "", getInput().lower())

    inputs = [q for q in inputs.lower().split(" ") if q not in stopwords]


    command = inputs[0]
    arguments = inputs[1:]
    user = getUser()
    cmd = Command(process(command), arguments, None, user)
    log(cmd)
    print(cmd.execute())

if __name__ == "__main__":
    main()