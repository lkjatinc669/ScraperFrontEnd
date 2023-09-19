from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msgbx 
import time
import threading

class CheckInternetConnection():
    def __init__(self):
        self.data = 0
        self.window = Tk()
        self.window.geometry("300x100")
        self.gui()
        self.T1 = threading.Thread(target=self.updateer)
        self.T1.start()
        self.window.mainloop()
        pass

    def gui(self):
        self.CheckConnPB = Progressbar( self.window, orient='horizontal', mode='determinate', length=280 )
        self.CheckConnPB.place(x=0, y=30)
        self.label = Label(self.window, text=self.updateLabel())
        self.label.place(x=0, y=0)

    def updateLabel(self):
        return f"Current Progress: {self.CheckConnPB['value']}"

    def progress(self):
        if self.CheckConnPB['value'] < 100:
            self.CheckConnPB['value'] += 10
            self.label['text'] =self.updateLabel()
        else:
            self.window.destroy()

    
            
    
    def updateer(self):
        for x in range(11):
            self.progress()
            time.sleep(1)
        self.T1.join()

CheckInternetConnection()