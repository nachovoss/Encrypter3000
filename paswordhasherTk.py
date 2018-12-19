import hashlib
from tkinter import *
import os
import time



window = Tk()
window.title('Encrypter 3000')
filename = PhotoImage(file = "D:\\YourPath\\passwordhasher\\lock.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.geometry("300x300")
window.maxsize(width=300, height=300)
window.minsize(width=300, height=300)
window.iconbitmap(r'D:\\YourPath\\passwordhasher\\Lock.ico')
m=hashlib.sha256()

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def Hashing():
    wtohash = entry_1.get()
    m.update(wtohash.encode('utf-8'))
    addToClipBoard(m.hexdigest())
    label_3=Label(window,text='Encripted password copied to clipboard')
    label_3.place(x=54, y=160)
    time.sleep(1)
    entry_1.delete(0, END)
    time.sleep(1)
    exit()  

label_1=Label(window,text='Please enter what you wish to hash:',fg='blue')
entry_1 = Entry(window)
button_1=Button(window,text='Click me to encrypt',command=Hashing)

label_1.place(x=54, y=220)
entry_1.place(x=3, y=240, width=294)
button_1.place(x=93, y=260)
 
window.mainloop()
