from tkinter import *
from random import randint

root = Tk()
root.title('Countries & caps')
root.geometry('600x600')
root.configure(background = 'snow')

caps = {'India': 'Delhi', 'Netherland': 'Rotterdam', 'Italy': 'Milan'}

entCou = Entry(root)
entCou.place(relx = 0.5, rely = 0.1, anchor = CENTER)
entCap = Entry(root)
entCap.place(relx = 0.5, rely = 0.2, anchor = CENTER)

lblAllCou = Label(root, text = 'All Countrys: ', background = 'light blue')
lblAllCou.place(relx = 0.5, rely = 0.4, anchor = CENTER)
lblAllCap = Label(root, text = 'All Capitals: ', background = 'light blue')
lblAllCap.place(relx = 0.5, rely = 0.5, anchor = CENTER)

lblRandCou = Label(root, text = 'Random Country: ', background = 'light blue')
lblRandCou.place(relx = 0.5, rely = 0.7, anchor = CENTER)
lblRandCap = Label(root, text = 'Random Capital: ', background = 'light blue')
lblRandCap.place(relx = 0.5, rely = 0.8, anchor = CENTER)

def addCap(cou, cap):
    caps[cou] = cap
    lblAllCou['text'] = 'All Countries: ' + str(list(caps.keys()))
    lblAllCap['text'] = 'All Capitals: ' + str(list(caps.values()))

def randCap():
    randNum = randint(0, len(caps) - 1)
    keys = list(caps.keys())
    lblRandCou['text'] = 'Random Country: ' + str(keys[randNum])
    lblRandCap['text'] = 'Random Capital: ' + str(caps[keys[randNum]])

btnAddCap = Button(root, text = 'Add Capital', command = lambda: addCap(entCou.get(), entCap.get()))
btnAddCap.place(relx = 0.5, rely = 0.3, anchor = CENTER)
btnRandCap = Button(root, text = 'Get Random Capital', command = lambda: randCap())
btnRandCap.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()