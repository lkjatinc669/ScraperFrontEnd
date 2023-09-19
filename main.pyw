import json
import time
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as msgbx
import requests
from scrDialog import login, signup, forgot
import threading
import multiprocessing

class Main():
    def __init__(self):
        self.isScreenOpened = False
        self.isLogSinScreenLoaded = False
        self.isLogOutScreenLoaded = False
        self.win = Tk()
        self.win.title("OpenSpaceApi - PythonScraper")
        self.win.geometry("670x300")
        
        self.logoutFrame = Frame(self.win, width=230, height=300)
        self.logsinFrame = Frame(self.win, width=230, height=300)

        self.checkConnThread = threading.Thread(target=self.loadInit, daemon=True)
        self.checkConnThread.start()
        self.win.protocol("WM_DELETE_WINDOW", self.setWindowProtocols)
        self.win.mainloop()

    def loadInit(self):
        error = False
        if self.check_Internet():
            if self.check_Server():
                self.gui()
                self.getScreen()
                self.updateLogs()
            else :
                msgbx.showerror("ServerError", f"Unable to Connect To the Server")
                error = True
        else :
            msgbx.showerror("InternetError", f"Unable to Connect To the Internet")
            error = True
        
        if error:
            self.win.destroy()
        try:
            self.checkConnThread.join()
        except RuntimeError:
            pass

    def logsinScreenLoad(self):
        self.ig_a = Label(self.logsinFrame, text="        Already Have a Account   ", width=28)
        self.ig_b = Button(self.logsinFrame, text="Login", command=self.Login, width=28)
        self.ig_c = Label(self.logsinFrame, text="           ---------OR---------    ", width=28)
        self.ig_d = Label(self.logsinFrame, text="          Don't have a account?      ", width=28)
        self.ig_e = Button(self.logsinFrame, text="Signup", command=self.Signup, width=28)
        self.ig_f = Label(self.logsinFrame, text="           ---------OR---------    ", width=28)
        self.ig_g = Label(self.logsinFrame, text=" Don't remember your account?      ", width=28)
        self.ig_h = Button(self.logsinFrame, text="Forgot Password", command=self.ForgotPassword, width=28)
        yz = 30
        self.ig_a.place(x=30, y=yz+0)
        self.ig_b.place(x=30, y=yz+20)
        self.ig_c.place(x=30, y=yz+60)
        self.ig_d.place(x=30, y=yz+90) 
        self.ig_e.place(x=30, y=yz+110)
        self.ig_f.place(x=30, y=yz+150)
        self.ig_g.place(x=30, y=yz+180) 
        self.ig_h.place(x=30, y=yz+200)

    def logoutScreenLoad(self):
        data = self.ReadJson()
        self.ib_a = Button(self.logoutFrame, text="Logout", command=self.Logout, width=33)
        self.ib_b = Separator(self.logoutFrame, orient='horizontal')
        self.ib_c = Label(self.logoutFrame, text="            Scraper", width=18, font=("Arial", 16))
        self.ib_d = Label(self.logoutFrame, text="Name : ")
        self.ib_e = Entry(self.logoutFrame, width=34)
        self.ib_f = Label(self.logoutFrame, text="Mail : ")
        self.ib_g = Entry(self.logoutFrame, width=34)
        self.ib_h = Label(self.logoutFrame, text="Token : ")
        self.ib_i = Entry(self.logoutFrame, width=34)
        self.ib_j = Button(self.logoutFrame, text="Config", width=15, command=self.updateLogs)
        self.ib_k = Button(self.logoutFrame, text="Start", width=15)

        yz = 10
        self.ib_a.place(x=15, y=yz)
        self.ib_b.place(x=10, y=yz+40, relwidth=1)
        self.ib_c.place(x=15, y=yz+50)
        self.ib_d.place(x=15, y=yz+90)
        self.ib_e.place(x=15, y=yz+110)
        self.ib_f.place(x=15, y=yz+140)
        self.ib_g.place(x=15, y=yz+160)
        self.ib_h.place(x=15, y=yz+190)
        self.ib_i.place(x=15, y=yz+210)
        self.ib_j.place(x=15, y=yz+240)
        self.ib_k.place(x=125, y=yz+240)

        self.ib_e.insert("0", data['name'])
        self.ib_g.insert("0", data['mail'])
        self.ib_i.insert("0", data['token'])
        self.ib_e.config(state="disabled")
        self.ib_g.config(state="disabled")
        self.ib_i.config(state="disabled")

    def setWindowProtocols(self):
        if self.isScreenOpened:
            pass
        else:
            self.win.destroy()

    def screenload(self, screen):
        if screen=="login":
            x = login.Login()

    def Login(self):
        self.isScreenOpened = True
        screen = login.Login()
        if screen.isWindowDestroyed():

        self.isScreenOpened = False
        self.getScreen()

    def Signup(self):
        self.isScreenOpened = True
        signup.Signup()
        self.isScreenOpened = False
        self.getScreen()
    
    def ForgotPassword(self):
        self.isScreenOpened = True
        forgot.ForgotPassword()
        self.isScreenOpened = False
        self.getScreen()
    
    def get_data(self, data):
        try:
            while True:
                with open("Scraper.log", "r") as file:
                    text = file.readlines()
                text = text[-15:]
                self.logs.config(state="normal")
                self.logs.delete("1.0", END)
                self.logs.config(state="disabled")
                for x in text:
                    self.logs.config(state="normal")
                    self.logs.insert(END, x)
                    self.logs.config(state="disabled")
                time.sleep(1)
        except RuntimeError:
            pass
    
    def updateLogs(self):
        t1 = threading.Thread(target=self.get_data, args=("",))
        t1.start()

    def Logout(self):
        data = self.ReadJson()
        data['name'] = None
        data['mail'] = None
        data['token'] = None
        data['update'] = None
        data['screen'] = "logsin"
        data = self.sortDict(data)
        json_object = json.dumps(data, indent=4)

        with open("CONSTS.json", "w") as outfile:
            outfile.write(json_object)
        self.getScreen()

    def sortDict(self, dict):
        keys = list(dict.keys())
        keys.sort()
        return {i: dict[i] for i in keys}
    
    def getScreen(self):
        data = self.ReadJson()
        print(data['screen'])
        if data['screen'] == "logsin":
            self.logoutFrame.pack_forget()
            self.logoutFrame.place_forget()
            self.logsinFrame.pack(fill='none')
            self.logsinFrame.place(x=0, y=0)
            self.logsinScreenLoad()
        elif data['screen'] == "logout":
            self.logsinFrame.pack_forget()
            self.logsinFrame.place_forget()
            self.logoutFrame.pack(fill='none')
            self.logoutFrame.place(x=0, y=0)
            self.logoutScreenLoad()

    def ReadJson(self):
        with open('CONSTS.json', 'r') as openfile:
            data = json.load(openfile)
        return data
    
    def gui(self):
        separator = Separator(self.win, orient='vertical')
        separator.place(x=238, y=10, relheight=0.93)
        Label(self.win, text="Logs (Only Last 15 Logs will be Displayed here. For more Check Scraper.log): ").place(x=250, y=5)
        self.logs = Text(self.win, height=16, width=50, state="disabled")
        self.logs.place(x=250, y=28)
    
    def check_Internet(self):
        try:
            requests.get("https://github.com/lkjatinc669", timeout=5)
            return True
        except requests.ConnectionError:
            return False  
    
    def check_Server(self):
        BASE_URL = "http://localhost:6699/"
        try:
            requests.get(BASE_URL, timeout=5)
            return True
        except requests.ConnectionError:
            return False

a = Main()