import hashlib
from tkinter import *
import os
import time



window = Tk()
window.title('Encrypter 3000')
C = Canvas(window, bg="blue", height=500, width=800)
filename = PhotoImage(file = "D:\\PythonProjects\\passwordhasher\\lock.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.geometry("300x200")
window.iconbitmap(r'D:\\PythonProjects\\passwordhasher\\Lock.ico')
m=hashlib.sha256()

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def Hashing():
    wtohash = entry_1.get()
    m.update(wtohash.encode('utf-8'))
    addToClipBoard(m.hexdigest())
    label_3=Label(window,text='Encripted password copied to clipboard')
    label_3.grid(row=2,column=1)
    
    entry_1.delete(0, END)
    time.sleep(2)
    exit()
    

label_1=Label(window,text='Please enter what you wish to hash:',fg='blue')
entry_1 = Entry(window)
button_1=Button(window,text='Click me to encrypt',command=Hashing)



label_1.place(x=60, y=20)
entry_1.place(x=80, y=140)
button_1.place(x=90, y=170)




    
window.mainloop()
