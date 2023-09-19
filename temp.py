# def urlGen(url, dict):
#     urldata = url + "?"
#     for keys in dict:
#         urldata += f"{keys}={dict[keys]}&"
#     return urldata[0:-1]


# data = {
#     "name": "name",
#     "pass": "pass"
# }
    
# urlGen("https://google.com", data)

# import tkinter as tk
# from tkinter import ttk

# # root window
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')

# root.grid()

# # progressbar
# pb = ttk.Progressbar( root, orient='horizontal', mode='indeterminate', length=280 )
# # place the progressbar
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# # start button
# start_button = ttk.Button( root, text='Start', command=pb.start )
# start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# # stop button
# stop_button = ttk.Button( root, text='Stop', command=pb.stop )
# stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


# root.mainloop()


# Python program to change position
# of cursor in Entry widget

# Import the library tkinter
# from tkinter import *

# # Create a GUI app
# app = Tk()

# # Create a function to move cursor one character
# # left
# def shift_cursor1(event=None):
# 	position = entry_label.index(INSERT)

# 	# Changing position of cursor one character left
# 	entry_label.icursor(position - 1)

# # Create a function to move the cursor one character
# # right
# def shift_cursor2(event=None):
# 	position = entry_label.index(INSERT)

# 	# Changing position of cursor one character right
# 	entry_label.icursor(END)


# # Create and display the button to shift cursor left
# button1 = Button(app, text="Shift cursor left", command=shift_cursor1)
# button1.grid(row=1, column=1, padx=10, pady=10)

# # Create and display the button to shift the cursor right
# button2 = Button(app, text="Shift cursor right", command=shift_cursor2)
# button2.grid(row=1, column=0, padx=10, pady=10)

# # Create and display the textbox
# entry_label = Entry(app)
# entry_label.grid(row=0, column=0, padx=10, pady=10)

# # Set the focus in the textbox
# entry_label.focus()

# # Make the infinite loop for displaying the app
# app.mainloop()

# from tkinter import *
# from tkinter.ttk import *

# def clear():
#     ent.delete("0", END)
# root = Tk()
# root.geometry("300x100")
# ent = Entry(root)
# ent.pack(anchor="center")

# bt = Button(root, text="Clear", command=clear)
# bt.pack(anchor="center")
# root.mainloop()

# import time
# import requests
# def internet_connection():
#     try:
#         requests.get("https://github.com/lkjatinc669", timeout=2)
#         print("getted")
#         return True
#     except requests.ConnectionError:
#         return False    
# while True:
#     if internet_connection():
#         print("The Internet is connected.")
#     else:
#         print("The Internet is not connected.")
#     time.sleep(1)


import time
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

CheckConnPB = ttk.Progressbar( root, orient='horizontal', mode='determinate', length=280 )

def updateLabel():
    return f"Current Progress: {CheckConnPB['value']}%"

def progress():
    if CheckConnPB['value'] < 100:
        CheckConnPB['value'] += 10
        label['text'] = updateLabel()
    else:
        root.destroy()

def stop():
    CheckConnPB.stop()
    label['text'] = updateLabel()

class CheckInternetConnection():
    def __init__(self):
        self.data = 0
        self.window = Tk()
        T1 = threading.Thread(target=updateer)
        T1.start()
        pass

    def gui(self):
        CheckConnPB = ttk.Progressbar( root, orient='horizontal', mode='determinate', length=280 )
        CheckConnPB.grid(10)

    def updateLabel(self):
        return f"Current Progress: {CheckConnPB['value']}%"

    def progress(self):
        if CheckConnPB['value'] < 100:
            CheckConnPB['value'] += 10
            label['text'] = updateLabel()
        else:
            root.destroy()

    def stop(self):
        CheckConnPB.stop()
        label['text'] = updateLabel()
    
    def updateer():
        for x in range(11):
            progress()
            time.sleep(1)
# progressbar
# place the progressbar
CheckConnPB.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
label = ttk.Label(root, text=updateLabel())
label.grid(column=0, row=1, columnspan=2)

def updateer():
    for x in range(11):
        progress()
        time.sleep(1)

    
import threading

T1 = threading.Thread(target=updateer)
T1.start()


# start button
# start_button = ttk.Button( root, text='Progress', command=progress )
# start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

# stop_button = ttk.Button( root, text='Stop', command=stop )
# stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

root.mainloop()