from tkinter import *
import os

def openscript():
    os.system('python paswordhasherTk.py')


window = Tk()

window.maxsize(width=300, height=300)
window.minsize(width=300, height=300)
window.geometry("300x300")
filename = PhotoImage(file = "D:\\PythonProjects\\passwordhasher\\lock.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
window.iconbitmap(r'D:\\PythonProjects\\passwordhasher\\Lock.ico')



window.title('Encrypter 3000 Launcher')


label_1=Label(window,text='Encrypter 3000 Launcher', fg='blue', bg='skyblue')

button_1=Button(window,text='Click me to Lauch', bg='skyblue',command=openscript)

label_1.place(x=82, y=50)

button_1.place(bordermode=OUTSIDE, x=95, y=225,)


window.mainloop()

