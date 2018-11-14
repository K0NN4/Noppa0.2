#test GUI 
from tkinter import * 
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import time
from multiprocessing import Process

#create the window
root = Tk() 

# Event object used to send signals from one thread to another
stop_event = Event()

#dice animation
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

#photos
photo_1 = PhotoImage(file="1.png")
photo_2 = PhotoImage(file="2.png")
photo_3 = PhotoImage(file="3.png")
photo_4 = PhotoImage(file="4.png")
photo_5 = PhotoImage(file="5.png")
photo_6 = PhotoImage(file="6.png")
ilabel = ImageLabel(root)

#funciton for gif loading
def load_gif ():
    ilabel.load('11scaled.gif')

#rolling sequence
import random
def dice_roll (): 
    x = random.randint(1,6)
    if x == 1:
        label1 = Label(root, image=photo_1)
        label1.place(x=115, y=100)
    elif x == 2:
        label2 = Label(root, image=photo_2)
        label2.place(x=115, y=100)
    elif x == 3:
        label3 = Label(root, image=photo_3)
        label3.place(x=115, y=100)
    elif x == 4:  
        label4 = Label(root, image=photo_4)
        label4.place(x=115, y=100)
    elif x == 5:
        label5 = Label(root, image=photo_5)
        label5.place(x=115, y=100)
    elif x == 6:
        label6 = Label(root, image=photo_6)
        label6.place(x=115, y=100)

#button functions
def button_press ():
    count = 0
    while count < 1:
        load_gif ()
        time.sleep (2)
        count + 1
    else:
        dice_roll ()

 #modify root window
root.geometry("300x300") 
root.title("Digital Dice 6000") 
thelabel = Label(root, text="Welcome to Digital Dice 6000!")
button_roll = Button(root, text="Roll", fg="red", height="2", width="4", activebackground="gray", command=button_press)

thelabel.pack()
ilabel.place(x=100, y=100)
button_roll.place(x=135, y=35)
 #kick off the event loop
root.mainloop()