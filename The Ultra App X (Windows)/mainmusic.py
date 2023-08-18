# importing required libraries and files
import os
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askdirectory
from pygame import mixer

# creating a function to open this app from the main app
def main2():
    print("\n------------------------------------------------")
    print("            Music Player 10.0         ")
    print("------------------------------------------------")
    print("\nSelect The Playlist Folder ")
    print("Enjoy The Music")

    # creating commands for buttons
    def playsong():
        print("\nNow Playing : - ")
        currentsong = playlist.get(ACTIVE)
        print(currentsong)
        mixer.music.load(currentsong)
        songstatus.set("Playing")
        mixer.music.play()

    def pausesong():
        songstatus.set("Paused")
        mixer.music.pause()

    def resumesong():
        songstatus.set("Resuming")
        mixer.music.unpause()

    def exitplayer():
        songstatus.set("Stopped")
        mixer.music.stop()
        screen.destroy()
        print("\nThank You For Using The Music Player....")

    # for asking the directory of the music playlist folder
    path = askdirectory(title='Select Folder')

    # creating the GUI (Tkinter Window)
    screen = tk.Tk()
    screen.title('Music player 10.0')
    screen.iconbitmap(r'musicicon.ico')
    screen.geometry("800x600")
    screen.configure(bg='sky blue')

    # to initialize the pygame module for  loading and playing sounds
    mixer.init()
    songstatus = StringVar()
    songstatus.set("choosing")

    # creating a list box for displaying the songs in the folder
    playlist = Listbox(screen, selectmode=SINGLE, bg="blue violet", fg="white", font=('Trebuchet MS', 22), width=150,
                       height=20)
    playlist.grid(columnspan=4, rowspan=4)

    # displaying the songs playlist in the list box and to choose which song to play
    os.chdir(path)
    songs = os.listdir()
    for s in songs:
        playlist.insert(END, s)

    # creating buttons with unique colours and commands
    playbtn = Button(screen, text="Play", command=playsong)
    playbtn.config(font=('Trebuchet MS', 20), highlightbackground="#F70611", bg="white", fg="black", padx=7, pady=7)
    playbtn.place(x=50, y=546)

    pausebtn = Button(screen, text="Pause", command=pausesong)
    pausebtn.config(font=('Trebuchet MS', 20), highlightbackground="#F70611", bg="white", fg="black", padx=7, pady=7)
    pausebtn.place(x=250, y=546)

    Resumebtn = Button(screen, text="Resume", command=resumesong)
    Resumebtn.config(font=('Trebuchet MS', 20), highlightbackground="#F70611", bg="white", fg="black", padx=7, pady=7)
    Resumebtn.place(x=450, y=546)

    Exitbtn = Button(screen, text="Exit", command=exitplayer)
    Exitbtn.config(font=('Trebuchet MS', 20), highlightbackground="#F70611", bg="white", fg="black", padx=7, pady=7)
    Exitbtn.place(x=650, y=546)

    screen.mainloop()

    quit()
