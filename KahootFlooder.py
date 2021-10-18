import tkinter
from tkinter import Label, StringVar
from tkinter.constants import DISABLED
from kahoot import client
import random
import threading
import time

bgcolor = '#46178f'
version = 1.0

app = tkinter.Tk()
app.config(bg=bgcolor)
app.geometry('1000x700')
app.title(f'Kahoot Flooder v{version}')
app.resizable(False, False)

canvas = tkinter.Canvas(app, width=1000, height=700, bg=bgcolor)
canvas.place(x=0, y=0)

square = canvas.create_rectangle(0, 150, 250, 50, fill='pink')

titlelbl = tkinter.Label(app, text = f'Kahoot Flooder v{version}', bg=bgcolor, font='Arial 40 bold', fg='white')
titlelbl.pack(pady=40)

gamepinlbl = tkinter.Label(app, text = 'Game Pin:', font='Arial 20 bold', fg='white', bg=bgcolor)
gamepinlbl.pack()

gamepinentr = tkinter.Entry(app, font = 'Arial 15 bold', bd=0)
gamepinentr.pack(pady=20)

namelbl = tkinter.Label(app, text = 'Name:', font='Arial 20 bold', fg='white', bg=bgcolor)
namelbl.pack(pady=20)

nameentr = tkinter.Entry(app, font = 'Arial 15 bold', bd=0)
nameentr.pack()

threadslbl = tkinter.Label(app, font='Arial 15 bold', text='Threads:', fg='white', bg=bgcolor)
threadslbl.place(x=20, y=20)

threadsentr = tkinter.Entry(app, font='Arial 25 bold', bg='white')
threadsentr.place(x=32, y=55, width=60, height=40)

Bot = client()

toggle=0
def floodtoggle():
    global toggle
    toggle = toggle + 1

floodthread = 1

namevar = StringVar()

def flood():
    while True:
        while toggle==1:
            gamepinentr.config(state=DISABLED)
            nameentr.config(state=DISABLED)
            threadsentr.config(state=DISABLED)
            def joingame():
                botname = nameentr.get()
                pin = gamepinentr.get()
                while toggle==1:
                    num = random.randint(0, 1000)
                    Bot.join((pin), f'{botname}{num}')
                    namevar.set(f'{botname}{num}')
            global floodthread
            while floodthread==1:
                for i in range(int(threadsentr.get())):
                    game = threading.Thread(target=joingame)
                    game.start()
                floodthread = 0



floodactivate = threading.Thread(target=flood)
floodactivate.start()

floodbtntext = StringVar()

floodbtn = tkinter.Button(app, textvariable=floodbtntext, font='Arial 15 bold', bd=0, bg='white', command=floodtoggle)
floodbtn.pack(pady=20)

def floodtextchange():
    while True:
        if toggle == 0:
            floodbtntext.set('Flood')
        if toggle == 1:
            floodbtntext.set('Stop')
        time.sleep(1)
        if toggle == 2:
            floodbtntext.set('Flood')
            floodbtn.config(bg='gray', activebackground='gray')

floodtextthread = threading.Thread(target=floodtextchange)
floodtextthread.start()

botnamelbl = tkinter.Label(app, textvariable=namevar, font='Monsterrat 25 bold', bg='#25076c', fg='white')
botnamelbl.pack(pady=20)

app.mainloop()