# # import tkinter as tk 
# from tkinter import *
# from tkinter import messagebox as msgbx
# from tkinter.ttk import *
# # from tkinter import *
# # from tkinter import ttk 


# root = Tk()
# frame = Frame(root)


# label_pass = Label(frame, text='Password:', font=('verdana',14))
# entry_pass = Entry(frame, font=('verdana',14), show='*')

# def show_and_hide():
#     if entry_pass['show'] == '*':
#         entry_pass['show'] = ''
#     else:
#         entry_pass['show'] = '*'
  
# checkBox_showPassword = Checkbutton(frame, text="show", command=show_and_hide)

# frame.grid(row=0, column=0)

# label_pass.grid(row=0, column=0, padx=(10,0), pady=10, sticky='e')
# entry_pass.grid(row=0, column=1, padx=(0,10), pady=10)
# checkBox_showPassword.grid(row=1, column=1, padx=0, pady=0, sticky='w')


# root.mainloop()

# myDict = {'ravi': 10, 'rajnish': 9,
# 		'sanjeev': 15, 'yash': 2, 'suraj': 32}



# def dictSort(dictc):
#         keys = list(dictc.keys())
#         keys.sort()
#         return {i: dictc[i] for i in keys}

# print(dictSort(myDict))


