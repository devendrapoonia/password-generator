from tkinter import *
from tkinter.ttk import *
import string
import random
import webbrowser

root = Tk()

root.title("Strong password generator")

root.geometry("350x300+463+200")

lbl1 = Label(root,text="Strong password generator in python")
lbl1.place(x="12", y="12")

url = "https://www.github.com/devendrapoonia"
new = 1

def web():
    webbrowser.open(url, new)

button1 = Button(root, text="Follow me on GitHub", command=web)
button1.place(x="220", y="12")

def generatepass():
    s1 = string.ascii_lowercase
    s2 = string.punctuation
    s3 = string.ascii_uppercase
    s4 = string.digits
    s5 = string.punctuation
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))
    random.shuffle(s)
    plenint= int(plen.get())
    result = "".join(s[0:plenint])
    if(password == ''):
        password.insert(0, result)
        password.focus()
    else:
        password.delete(0, plenint)
        password.insert(0, result)
        password.focus()
        
        

length = Label(text="Enter the length of password:")
length.place(x="12", y="45")

plen = Entry(root)
plen.place(x="12", y="70", width=325)

generatebtn = Button(root, text="Generate password", command=generatepass)
generatebtn.place(x="110", y="110")

genlbl = Label(root, text="Generated password:")
genlbl.place(x="12", y="145")

password = Entry(root)
password.place(x="12", y="170", width=325)

def copypass():
    password.clipboard_clear()
    password.clipboard_append(password.get())
    password.focus()

copybtn = Button(root, text="Copy", command=copypass)
copybtn.place(x="70", y="210")


exit = Button(root, text="Exit", command=root.destroy)
exit.place(x="170", y="210")

root.mainloop()


"""
More softwares on github

visit https://www.github.com/devendrapoonia

"""
