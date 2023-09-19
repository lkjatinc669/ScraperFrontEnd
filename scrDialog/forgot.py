from tkinter import *
from tkinter import messagebox as msgbx
from tkinter.ttk import *
import requests
import json
import hashlib
import re

class ForgotPassword():
    def __init__(self):
        self.Cmail = None
        self.Cotphash = None
        self.Cfptoken = None

        self.window = Tk()
        self.window.title("Forgot Password PythonScraper (By OpenSpaceAPI)")
        self.window.geometry("400x270")
        self.window.resizable(False, False)
        self.BASEURL = "http://localhost:6699/scraper-account/forgot-password/"
        self.gui()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def gui(self):
        Label(self.window, text="Gmail           :").place(x=30, y=10)
        self.mail = Entry(self.window, width=40)
        self.mail.place(x=120, y=10)
        self.sendotpButton = Button(self.window, text="Send OTP", width=26, command=self.sendotp)
        self.sendotpButton.place(x=200, y=40)

        Label(self.window, text="OTP          :").place(x=30, y=80)
        self.otp = Entry(self.window, width=40, state="disabled")
        self.otp.place(x=120, y=80)
        self.verifyotpButton = Button(self.window, text="Verify OTP", width=26, command=self.verifyotp, state="disabled")
        self.verifyotpButton.place(x=200, y=110)
        
        Label(self.window, text="Password    :").place(x=30, y=150)
        self.password = Entry(self.window, width=40, state="disabled", show='*')
        self.password.place(x=120, y=150)
        Label(self.window, text="Type Again :").place(x=30, y=180)
        self.rpassword = Entry(self.window, width=40, state="disabled", show='*')
        self.rpassword.place(x=120, y=180)
        self.showpassword = Checkbutton(self.window, text="Show Password", command=self.passwordToggle, state="disabled",)
        self.showpassword.place(x=120, y=205)
        self.finalizeButton = Button(self.window, text="Update Password", width=26, command=self.updatepassword, state="disabled")
        self.finalizeButton.place(x=200, y=235)


    def sendotp(self):
        mail = self.mail.get()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(not(re.fullmatch(regex, mail))):
            msgbx.showerror("Provide Mail", "Please Provide valid Mail")
        else:
            data = self.fetchdata(base=self.BASEURL+"start/", data={'mail': mail})
            if (data['ERROR']):
                msgbx.showerror("ERROR", f"ERRCODE: {data['ERRCODE']}. \nDescription: {data['DESC']}")
            else :
                self.Cfptoken = data['DATA']['fptoken']
                self.Cmail = mail
                self.mail.config(state="disabled")
                self.sendotpButton.config(state="disabled")
                self.otp.config(state="normal")
                self.verifyotpButton.config(state="normal")
    
    def verifyotp(self):
        otp = self.otp.get()
        otphash = hashlib.md5(otp.encode()).hexdigest()
        data = self.fetchdata(base=self.BASEURL+"verify-fpotp/", data={'mail': self.Cmail,'fptoken': self.Cfptoken, 'otphash': otphash})
        if (data['ERROR']):
            msgbx.showerror("ERROR", f"ERRCODE: {data['ERRCODE']}. \nDescription: {data['DESC']}")
        else :
            self.Cotphash = otphash
            self.otp.config(state="disabled")
            self.password.config(state="normal")
            self.rpassword.config(state="normal")
            self.showpassword.config(state="normal")
            self.finalizeButton.config(state="normal")

    def updatepassword(self):
        paswd = self.password.get()
        rpaswd = self.rpassword.get()
        paswdhash = hashlib.sha256(paswd.encode()).hexdigest()
        rpaswdhash = hashlib.sha256(rpaswd.encode()).hexdigest()
        
        if (paswdhash != rpaswdhash):
            msgbx.showerror("ERROR", f"Password Not Matching")
        else:
            data = self.fetchdata(base=self.BASEURL+"final-step/", data={'mail': self.Cmail,'fptoken': self.Cfptoken, 'otphash': self.Cotphash, 'password': paswdhash})
            if (data['ERROR']):
                msgbx.showerror("ERROR", f"ERRCODE: {data['ERRCODE']}. \nDescription: {data['DESC']}")
            else :
                self.password.config(state="disabled")
                self.rpassword.config(state="disabled")
                self.showpassword.config(state="disabled")
                self.finalizeButton.config(state="disabled")
                msgbx.showinfo("SUCCESS", "Password Updated Successfully")
                self.window.destroy()

    def fetchdata(self, base, data=None):
        link =self.urlGen(base, data)
        data = requests.post(link)
        data = data.json()
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
            self.rpassword['show'] = '*'
        else:
            self.password['show'] = ''
            self.rpassword['show'] = ''

    def on_closing(self):
        if msgbx.askokcancel("Cancel Login", "The data you all remain unsaved and the process will not be restored. Are you Sure?"):
            self.window.destroy()

if __name__ == "__main__":
    print("Cant be run Individually. This is a part of Project"); input("Press any Key to Continue...")