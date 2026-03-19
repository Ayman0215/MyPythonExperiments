import json
from datetime import datetime
from LogConfig import *

def logWithWrapping(logMessage):
    print(logMessage)

def logToFile(logMessage):
    buffer = ""
    counter = 0
    fileName = getFileName()
    bufferSize = getBufferSizeInLines()
    if counter < bufferSize:
        buffer = buffer + logMessage + "\n"
        counter += 1
    else:
        with open(fileName, "a") as file:
           file.write(buffer)
        counter = 0
        buffer = ""

def log(log_level, user_info):
    if log_level >= getLogLevel():
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        logMessage = f"{time}" + f"{user_info}" + f"{log_level}"
        logWithWrapping(logMessage)
        logToFile(logMessage)

        