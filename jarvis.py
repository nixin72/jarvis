from commands import greet, shutdown, invalid, setter
from User import User
import speech_recognition as sr
import datetime
import sys 
import re

def log(command, arguments, user):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("./data/cmds.log", "a") as log:
        log.write(time + " ----- " + user.getName() + ": " + command + " " + " ".join(arguments) + "\n")

def execute(command, arguments, user):
    commands = {
        "greet": greet,
        "shutdown": shutdown,
        "set": setter
    }
    return commands.get(command, invalid)(arguments, user)

def getUser():
    return User.getUser()

def narrow(command):
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
    # inputs = "hey jarvis set my volume to 50 percent" 
    inputs = re.sub("%", "", getInput().lower())
    inputs = [q for q in inputs.lower().split(" ") if q not in stopwords]
    print(inputs)
    # exit()
    command = inputs[0]
    arguments = inputs[1:]
    user = getUser()
    log(command, arguments, user)
    print(execute(narrow(command), arguments, user))

if __name__ == "__main__":
    main()