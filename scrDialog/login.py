from tkinter import *
from tkinter import messagebox as msgbx
from tkinter.ttk import *
import requests
import json
import hashlib
import re

class Login():
    def __init__(self):
        self.Cmail = None
        self.Cpassword = None

        self.window = Tk()
        self.window.title("Login PythonScraper (By OpenSpaceAPI)")
        self.window.geometry("400x200")
        self.window.resizable(False, False)
        self.BASEURL = "http://localhost:6699/scraper-account/login/"
        self.gui()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()

    def isWindowDestroyed(self):
        return self.window.winfo_exists()

    def gui(self):
        Label(self.window, text="Gmail           :").place(x=30, y=10)
        self.mail = Entry(self.window, width=40)
        self.mail.place(x=120, y=10)
        Label(self.window, text="Password    :").place(x=30, y=40)
        self.password = Entry(self.window, width=40, show='*')
        self.password.place(x=120, y=40)
        self.showpassword = Checkbutton(self.window, text="Show Password", command=self.passwordToggle)
        self.showpassword.place(x=120, y=65)
        self.sendButton = Button(self.window, text="Verify and Send OTP", width=26, command=self.verifyandsend)
        self.sendButton.place(x=200, y=90)

        Label(self.window, text="OTP          :").place(x=30, y=130)
        self.otp = Entry(self.window, width=40, state="disabled")
        self.otp.place(x=120, y=130)
        self.verifyButton = Button(self.window, text="Verify OTP", width=26, command=self.verifyotp, state="disabled")
        self.verifyButton.place(x=200, y=160)

    def verifyandsend(self):
        mail = self.mail.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(not(re.fullmatch(regex, mail))):
            msgbx.showerror("Provide Mail", "Please Provide valid Mail")
        else:
            paswd = self.password.get()
            paswdhash = hashlib.sha256(paswd.encode()).hexdigest()
            data = self.fetchdata(base=self.BASEURL+"start/", data={'mail': mail, 'password':paswdhash})
            if (data['ERROR']):
                msgbx.showerror("ERROR", f"ERRCODE: {data['ERRCODE']}. \nDescription: {data['DESC']}")
            else :
                self.Cmail = mail
                self.Cpassword = paswdhash
                self.Cltoken = data['DATA']['ltoken']
                self.mail.config(state="disabled")
                self.password.config(state="disabled")
                self.showpassword.config(state="disabled")
                self.sendButton.config(state="disabled")
                self.otp.config(state="normal")
                self.verifyButton.config(state="normal")

    def verifyotp(self):
        otp = self.otp.get()
        otphash = hashlib.md5(otp.encode()).hexdigest()
        data = self.fetchdata(base=self.BASEURL+"verify-lotp/", data={'mail': self.Cmail, 'password':self.Cpassword, 'otphash': otphash, 'ltoken': self.Cltoken})
        if (data['ERROR']):
            pass
        else :
            self.WriteJson(data['DATA']['name'], data['DATA']['mail'], data['DATA']['token'])
            self.otp.config(state="disabled")
            self.verifyButton.config(state="disabled")
            self.window.destroy()

    def ReadJson(self):
        with open('CONSTS.json', 'r') as openfile:
            data = json.load(openfile)
        return data

    def WriteJson(self, name, mail, token):
        data = self.ReadJson()
        data['name'] = name
        data['mail'] = mail
        data['token'] = token
        data['update'] = True
        data['screen'] = "logout"
        print(data)
        data = self.sortDict(data)
        print(data)
        json_object = json.dumps(data, indent=4)

        with open("CONSTS.json", "w") as outfile:
            outfile.write(json_object)
    
    def sortDict(self, dict):
        keys = list(dict.keys())
        keys.sort()
        return {i: dict[i] for i in keys}

    def fetchdata(self, base, data=None):
        link =self.urlGen(base, data)
        data = requests.post(link)
        data = data.json()
        print(link)
        print(data)
        return data
    
    def urlGen(self, url, dict):
        if dict != None:
            urldata = url + "?"
            for keys in dict:
                urldata += f"{keys}={dict[keys]}&"
            return urldata[0:-1]
        else :
            return url
        
    def passwordToggle(self):
        if self.password['show'] == '':
            self.password['show'] = '*'
        else:
            self.password['show'] = ''

    def on_closing(self):
        if msgbx.askokcancel("Cancel Login", "The data you all remain unsaved and the process will not be restored. Are you Sure?"):
            self.window.destroy()