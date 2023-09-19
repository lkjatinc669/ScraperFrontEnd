import json
import time

def loadConstants() -> None:
    f = open('CONSTS.json')
    data = json.load(f)
    print(data)

def addLinks()-> bool:
    return False

def getLinks() -> list:
    return [True, ["Data"]]


def createLog(logs):
    with open("Scraper.log", "a+") as logfile:
        logfile.writelines(logs + "\n")
