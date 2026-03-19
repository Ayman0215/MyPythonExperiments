import json 

with open("DevConfig.json") as logConfig:
    logConfig = json.load(logConfig)

def getLogLevel():
    return logConfig.get("logLevelsNeeded", "INFO")

def isFileLoggingEnabled():
    return logConfig.get("enableFileLogging", False)

def isConsoleLoggingEnabled():
    return logConfig.get("enableConsoleLogging", False)

def getBufferSizeInLines():
    return logConfig.get("bufferSizeInLines", 0)

def getFileName():
    return logConfig.get("fileName", "default_log.txt")

def getMaxCharacters():
    return logConfig.get("maxCharacters", 0)
#-------------------------------------------------------------------#