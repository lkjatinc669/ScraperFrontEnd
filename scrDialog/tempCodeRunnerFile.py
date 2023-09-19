import time
from tkinter import *
from tkinter.ttk import *
import threading

def isWindowDestroyed():
    while True:
        time.sleep(1)
        print(root.winfo_exists())
root = Tk()
root.geometry("500x500")

t = threading.Thread(target=isWindowDestroyed)
t.start()

root.mainloop()
