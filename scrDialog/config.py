from tkinter import *
from tkinter import messagebox as msgbx
from tkinter.ttk import *
import time
import json
import hashlib
import re
import os

class Config:
    def __init__(self) -> None:
        
        self.options = ["None", "Crawler", "Extractor"]

        self.window = Tk()
        self.window.title("Config PythonScraper (By OpenSpaceAPI)")
        self.window.geometry("400x250")
        self.window.resizable(False, False)
        self.BASEURL = "http://localhost:6699/scraper-account/join/"
        self.functionVar = StringVar()
        self.gui()

        self.extractorFrame = Frame(self.window, width=333, height=170)
        self.crawlerFrame = Frame(self.window, width=333, height=170)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()
    
    def crawlerScreenLoad(self):
        self.text = Text(self.crawlerFrame, height=10, width=41)
        self.text.place(x=0, y=5)
        self.text.insert(END, "# Type your Topics to be crawled below \n# Write each topic on new line")

    def extractorScreenLoad(self):
        Label(self.extractorFrame, text="No Config To Show").place(x=125, y=70)
        
    def callback(self, event):
        print(event)
        if (self.functionVar.get() == "Crawler"):
            print("CW")
            self.extractorFrame.pack_forget()
            self.extractorFrame.place_forget()
            self.crawlerFrame.pack(fill='none')
            self.crawlerFrame.place(x=30, y=35)
            self.crawlerScreenLoad()
        elif (self.functionVar.get() == "Extractor"):
            print("EX")
            self.crawlerFrame.pack_forget()
            self.crawlerFrame.place_forget()
            self.extractorFrame.pack(fill='none')
            self.extractorFrame.place(x=30, y=35)
            self.extractorScreenLoad()
            
    def gui(self):
        self.functionLabel = Label(self.window, text="Function")
        self.function = OptionMenu( self.window , self.functionVar ,*self.options, command=self.callback)


        self.saveButton = Button(self.window, text="Save", width=10, command=self.getData)
        self.cancelButton = Button(self.window, text="Cancel", width=10)

        yz= 10
        self.functionLabel.place(x=30, y=yz)
        self.function.place(x=120, y=yz, width=245)

        self.saveButton.place(x=215, y=yz+200)
        self.cancelButton.place(x=295, y=yz+200)


        
        self.functionVar.set("None")

    def getData(self):
        textData = self.text.get("1.0",'end-1c')
        textData = textData.split("\n")
        for line in textData:
            if line.split(" ")[0] == "#":
                pass
            else:
                with open("crawler.topics", "a") as topicsFile:
                    topicsFile.write(line + "\n")

    def on_closing(self):
        if msgbx.askokcancel("Cancel Login", "The data you all remain unsaved and the process will not be restored. Are you Sure?"):
            self.window.destroy()


# d = {"SThread":["IsFree", "TimeSpend", "Operation", "On"],
#      1: ["True", 00, "NONE", "NONE"],
#      2: ["True", 00, "NONE", "NONE"],
#      3: ["True", 00, "NONE", "NONE"],
#      4: ["True", 00, "NONE", "NONE"],
#      5: ["True", 00, "NONE", "NONE"],
#      6: ["True", 00, "NONE", "NONE"],
#      7: ["True", 00, "NONE", "NONE"],
#      8: ["True", 00, "NONE", "NONE"]
# }
# for k, v in d.items():
#     lang, perc, change, on= v
#     print ("{:<8} {:<7} {:<10} {:<10} {:<35}".format(k, lang, perc, change, on))
# input(">")
