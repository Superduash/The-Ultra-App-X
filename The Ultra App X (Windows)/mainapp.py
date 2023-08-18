"""
Libraries To Import (Use In Terminal Or Command Prompt) : -
python.exe -m pip install tk
python.exe -m pip install pygame
python.exe -m pip install Pillow
"""
#A.ASHWIN,S.VIVEK,S.SRINATH
#11-B
#6205,6233,6238

#COMPUTER SCIENCE PROJECT

# importing required libraries and files
import tkinter
import tkinter as tk
from tkinter import *
import sys
from tkinter import messagebox
import maincalc, mainmusic, mainrps, mainwordle
from PIL import Image, ImageTk

print("\n---------------------------------------------------------------")
print("           The Ultra App X      ")
print("---------------------------------------------------------------")
print("Available Apps: -")
print("1) Calculator ++")
print("2) Music Player 10.0")
print("3) Rock Papers Scissors Game (RPS)")
print("4) Wordle")

# defining functions and commands for buttons to open apps and other things
def calc():
    maincalc.main1()
def music():
    mainmusic.main2()
def rps():
    mainrps.main3()
def wordle():
    mainwordle.main4()
def exit():
    if messagebox.askokcancel("Exit", "Do You Want To Quit? :"):
        screen.destroy()
        print("\nThank You For Using The Ultra App X .... ")
        sys.exit()
def credit():
    lines = ['Team Superduash : - ', ' ★ A.Ashwin - Wordle, Music Plyr', ' ★ S.Srinath - RPS, GUI', ' ★ S.Vivek - Calculator, GUI', ' ★ IDE Used - Pycharm And IDLE', ' ★ Reference From Internet']
    tkinter.messagebox.showinfo('Credits!', "\n".join(lines))
def info():
    lines = ['Version - 2.0.1 ', ' ★ Fixed Minor Bugs And Glitches', ' ★ Performance Improvements', ' ★ GUI And Design Improvement', '★ Features And Emojis Added', ' ★ Some Problems To Be Fixed In The Future']
    tkinter.messagebox.showinfo('Info!', "\n".join(lines))
def title():
    var = None

# creating the GUI (Tkinter Window)
screen = tk.Tk()
screen.title('The Ultra App X')
screen.iconbitmap(r'xicon.ico')
screen.geometry("900x400")
screen.iconbitmap(r'xicon.ico')
screen.configure(bg="black")

# creating images for apps
frame = Frame(screen, width=140, height=140)
frame.pack()
frame.place(x=80, y=80)
img = ImageTk.PhotoImage(Image.open("Calc.jpeg"))
label1 = Label(frame, image=img)
label1.pack()

frame2 = Frame(screen, width=140, height=140)
frame2.pack()
frame2.place(x=288, y=80)
img2 = ImageTk.PhotoImage(Image.open("musicplay.png"))
label2 = Label(frame2, image=img2)
label2.pack()

frame3 = Frame(screen, width=140, height=140)
frame3.pack()
frame3.place(x=510, y=80)
img3 = ImageTk.PhotoImage(Image.open("rps.png"))
label3 = Label(frame3, image=img3)
label3.pack()

frame4 = Frame(screen, width=140, height=140)
frame4.pack()
frame4.place(x=710, y=80)
img4 = ImageTk.PhotoImage(Image.open("wordle.png"))
label4 = Label(frame4, image=img4)
label4.pack()

# creating buttons with unique colours and commands
calculator = Button(screen, text="Calculator", command=calc)
calculator.config(font=('Trebuchet MS', 20), highlightbackground="#FE0221", bg="white", fg="black", padx=7, pady=7)
calculator.place(x=80, y=250)

musicplayer = Button(screen, text="Music Player", command=music)
musicplayer.config(font=('Trebuchet MS', 20), highlightbackground="#FAFE02", bg="white", fg="black", padx=7, pady=7)
musicplayer.place(x=280, y=250)

rpsbtn = Button(screen, text="RPS", command=rps)
rpsbtn.config(font=('Trebuchet MS', 20), highlightbackground="#1DFE02", bg="white", fg="black", padx=7, pady=7)
rpsbtn.place(x=538, y=250)

wordlebtn = Button(screen, text="Wordle", command=wordle)
wordlebtn.config(font=('Trebuchet MS', 20), highlightbackground="#DF02FE", bg="white", fg="black", padx=7, pady=7)
wordlebtn.place(x=725, y=250)

Exitbtn = Button(screen, text="Exit", command=exit)
Exitbtn.config(font=('Trebuchet MS', 20), highlightbackground="#02FEFA", bg="white", fg="black", padx=7, pady=7)
Exitbtn.place(x=410, y=336)

creditbtn = Button(screen, text="Credits", command=credit)
creditbtn.config(font=('Trebuchet MS', 20), highlightbackground="#3402FE", bg="white", fg="black", padx=7, pady=7)
creditbtn.place(x=728, y=336)

infobtn = Button(screen, text="Info", command=info)
infobtn.config(font=('Trebuchet MS', 20), highlightbackground="#FE7502", bg="white", fg="black", padx=7, pady=7)
infobtn.place(x=70, y=336)

titlebtn = Button(screen, text=" The Ultra App X ", command=title)
titlebtn.config(font=('Trebuchet MS', 20), highlightbackground="#FE7502", bg="white", fg="black", padx=7, pady=7)
titlebtn.place(x=330, y=10)

screen.mainloop()
