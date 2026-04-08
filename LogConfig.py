import json 

with open("DevConfig.json") as logConfig:
    logConfig = json.load(logConfig)

def getLogLevel():
    if type(logConfig.get("logLevelsNeeded")) != int:
        print("Set To Default, INFO")
    return logConfig.get("logLevelsNeeded", "INFO")

def isFileLoggingEnabled():
    if type(logConfig.get("enableFileLogging", False)) != bool:
        print("Set To Default, False")
    return logConfig.get("enableFileLogging", False)

def isConsoleLoggingEnabled():
    if type(logConfig.get("enableConsoleLogging", False)) != bool:
        print("Set To Default, False")
    return logConfig.get("enableConsoleLogging", False) 

def getBufferSizeInLines():
    if type(logConfig.get("bufferSizeInLines", 3)) != int:    
        print("Set To Default, 3")
    return logConfig.get("bufferSizeInLines", 3) 

def getFileName():
    if type(logConfig.get("fileName", "log.txt")) != str:
        print("Set To Default, log.txt")
    return logConfig.get("fileName", "log.txt")
def getMaxCharacters():
    if type(logConfig.get("maxCharacters", 0)) != int:
        print("Set To Default, 0")
    return logConfig.get("maxCharacters", 0)  
#-------------------------------------------------------------------#