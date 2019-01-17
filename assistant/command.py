from commands import greet, shutdown, invalid, setter

class Command:
    def __init__(self, command, arguments, time, user):
        self.command = command
        self.arguments = arguments
        self.time = time
        self.user = user 

    def execute(self):
        commands = {
            "greet": greet,
            "shutdown": shutdown,
            "set": setter
        }

        if self.time == None:
            return commands.get(self.command, invalid)(self.arguments, self.user)
        
    def __str__(self):
        return self.getUser().getName() + ": " + self.command + " " + " ".join(self.arguments)

    ## Accessors 
    def getCommand(self):
        return self.command
    def getArguments(self):
        return self.arguments
    def getTime(self):
        return self.time
    def getUser(self):
        return self.user

    ## Mutators
    def setCommand(self, command):
        self.command = command
    def setArguments(self, arguments):
        self.arguments = arguments
    def setTime(self, time):
        self.time = time
    def setUser(self, user):
        self.user = user