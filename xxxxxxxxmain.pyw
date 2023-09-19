import json
from tkinter import *
from tkinter.ttk import *
from scrDialog import login, signup

class Main():
    def __init__(self):
        self.isLogSinScreenLoaded = False
        self.isLogOutScreenLoaded = False
        self.win = Tk()
        self.win.title("OpenSpaceApi - PythonScraper")
        self.win.geometry("670x300")

        self.gui()
        self.getScreen()
        # Button(self.win, text="On", command=self.loadScreenLogsin).place(x=120, y=10)
        # Button(self.win, text="On", command=self.loadScreenLogout).place(x=120, y=50)

        self.win.mainloop()


    def logsinScreenLoad(self):
        self.logsinFrame = Frame(self.win)
        self.ig_a = Label(self.win, text="        Already Have a Account   ", width=28)
        self.ig_b = Button(self.win, text="Login", command=self.LoadLoginDialog, width=28)
        self.ig_c = Label(self.win, text="           ---------OR---------    ", width=28)
        self.ig_d = Label(self.win, text="          Don't have a account?      ", width=28)
        self.ig_e = Button(self.win, text="Signup", command=signup.Signup, width=28)
        self.ig_f = Label(self.win, text="           ---------OR---------    ", width=28)
        self.ig_g = Label(self.win, text=" Don't remember your account?      ", width=28)
        self.ig_h = Button(self.win, text="Forgot Password", command=signup.Signup, width=28)
        yz = 30
        self.ig_a.place(x=30, y=yz+0)
        self.ig_b.place(x=30, y=yz+20)
        self.ig_c.place(x=30, y=yz+60)
        self.ig_d.place(x=30, y=yz+90) 
        self.ig_e.place(x=30, y=yz+110)
        self.ig_f.place(x=30, y=yz+150)
        self.ig_g.place(x=30, y=yz+180) 
        self.ig_h.place(x=30, y=yz+200)
    
    def logsinScreenDestroy(self):
        self.ig_a.destroy()
        self.ig_b.destroy()
        self.ig_c.destroy()
        self.ig_d.destroy()
        self.ig_e.destroy()
        self.ig_f.destroy()
        self.ig_g.destroy()
        self.ig_h.destroy()

    def logoutScreenLoad(self):
        self.logoutFrame = Frame(self.win)
        data = self.ReadJson()
        self.ib_a = Button(self.win, text="Logout", command=self.Logout, width=33)
        self.ib_b = Separator(self.win, orient='horizontal')
        self.ib_c = Label(self.win, text="            Scraper", width=18, font=("Arial", 16))
        self.ib_d = Label(self.win, text="Name : ")
        self.ib_e = Entry(self.win, width=34)
        self.ib_f = Label(self.win, text="Mail : ")
        self.ib_g = Entry(self.win, width=34)
        self.ib_h = Label(self.win, text="Token : ")
        self.ib_i = Entry(self.win, width=34)
        self.ib_j = Button(text="Config", width=15)
        self.ib_k = Button(text="Start", width=15)

        yz = 10
        self.ib_a.place(x=15, y=yz)
        self.ib_b.place(x=10, y=yz+40, relwidth=0.33)
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

    def logoutScreenDestroy(self):
        self.ib_a.destroy()
        self.ib_b.destroy()
        self.ib_c.destroy()
        self.ib_d.destroy()
        self.ib_e.destroy()
        self.ib_f.destroy()
        self.ib_g.destroy()
        self.ib_h.destroy()
        self.ib_i.destroy()
        self.ib_j.destroy()
        self.ib_k.destroy()

    def clearer(self):
        if self.isLogSinScreenLoaded == True:
            self.logsinScreenDestroy()
            self.isLogSinScreenLoaded = False
        if self.isLogOutScreenLoaded == True:
            self.logoutScreenDestroy()
            self.isLogOutScreenLoaded = False
    
    def loadScreenLogsin(self):
        self.clearer()
        self.logsinScreenLoad()
        self.isLogSinScreenLoaded = True
    
    def loadScreenLogout(self):
        self.clearer()
        self.logoutScreenLoad()
        self.isLogOutScreenLoaded = True

    def LoadLoginDialog(self):
        login.Login()
        self.win.update_idletasks()

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

    def sortDict(self, dict):
        keys = list(dict.keys())
        keys.sort()
        return {i: dict[i] for i in keys}
    
    def getScreen(self):
        data = self.ReadJson()
        print(data['screen'])
        if data['screen'] == "logsin":
            self.loadScreenLogsin()
        if data['screen'] == "logout":
            self.loadScreenLogout()

    def ReadJson(self):
        with open('CONSTS.json', 'r') as openfile:
            data = json.load(openfile)
        return data
    
    def updateLogs(self, text="hfksdjalfhkjsafkjsadfsdfjhkaf\n"*3):
        self.logs.insert(text)
    
    def gui(self):
        separator = Separator(self.win, orient='vertical')
        separator.place(x=238, y=10, relheight=0.93)
        Label(self.win, text="Logs : ").place(x=250, y=5)
        self.logs = Text(self.win, height=16, width=50, state="disabled")
        self.logs.place(x=250, y=28)
    



a = Main()