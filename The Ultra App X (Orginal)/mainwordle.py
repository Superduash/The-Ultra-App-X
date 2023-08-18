# importing required libraries and files
import tkinter as tk
from tkinter import *
import words
import sys
from tkinter import messagebox

guessnum: int = 1
wd = words.get_word()

# creating a function to open this app from the main app
def main4():
    # creating a function for the guess button
    def getguess():
        global wd
        guess = wordinput.get()
        global guessnum
        guessnum += 1
        # to show error if the user's guess is not a word
        if guess.isalpha():
            # to stop after the number of chances is over
            if guessnum <= chances:
                # to show error if the guess has less than or more than 5 characters
                if len(guess) == 5:
                    if wd == guess:
                        messagebox.showinfo("You Won!!", f"The Word Was {wd.title()} ... You Won!! ⧹(⦁ᴗ⦁)⧸")
                        print("\nHope You Enjoyed The Game.. See You Soon (ツ)")
                        screen.destroy()
                        sys.exit()
                    else:
                        for i, letter in enumerate(guess):
                            label = Label(screen, text=letter.upper())
                            label.grid(row=guessnum, column=i, padx=10, pady=10)
                            if letter == wd[i]:
                                label.config(bg=Green, fg=Black)
                            if letter in wd and not letter == wd[i]:
                                label.config(bg=Yellow, fg=Black)
                            if letter not in wd:
                                label.config(bg=Black, fg=White)
                else:
                    messagebox.showerror("Error!", "Please Use 5 Characters In Your Guess.. Try Again... (▱˘︹˘▱)")
            else:
                messagebox.showinfo("You Lost!!", f"You Lost!! The Word Was {wd.title()} ... (▱˘︹˘▱) ")
                print("\nHope You Enjoyed The Game.. See You Soon (ツ)")
                screen.destroy()
                sys.exit()

        else:
            messagebox.showerror("Error!", "Only Letters Are Allowed.. Try Again... (▱˘︹˘▱) ")

    print("\n-----------------------------------------------------------------")
    print("          (ツ)   Wordle 5.0 (The Word Guessing Game)   (ツ)         ")
    print("-------------------------------------------------------------------")
    print(f"Enjoy The Game!! Hope You Win!! ⧹(⦁ᴗ⦁)⧸")
    while True:
        # asking the difficulty; more hard the difficulty, least the chances to guess the word
        difficulty = input("\nEnter The Difficulty (Very Easy(v)/ Easy(e)/ Medium(m)/ Hard(h)): -  ").title()
        if difficulty == "Very easy" or difficulty == "V" or difficulty == "Very Easy":
            d = "Very Easy"
            chances = 17
        elif difficulty == "Easy" or difficulty == "E":
            d = 'Easy'
            chances = 10
        elif difficulty == "Medium" or difficulty == "M":
            d = 'Medium'
            chances = 8
        elif difficulty == "Hard" or difficulty == "H":
            d = 'Hard'
            chances = 6
        else:
            print('\nInvalid Option...Please Try Again (▱˘︹˘▱)')
            continue

        # instructions for the game
        print("\nInstructions : - ")
        print(f"1) You Have Chosen ({d}) Difficulty.. So You Have ({chances}) Chances")
        print("2) Enter The Words In The Box And Click The Guess Button ")
        print("3) Green Highlight Indicates That The Letter Is In The Word And Also In The Correct Place ")
        print("4) Yellow Highlight Indicates That The Letter Is In The Word But Not In the Correct Place")
        print("5) No Highlight Indicates That The Letter Is Not In The Word")
        print("6) Ready!! Set!! Guess!! ⧹(⦁ᴗ⦁)⧸")

        # creating the GUI (Tkinter Window)
        Green = "green2"
        Yellow = "yellow2"
        White = "snow"
        Black = "black"
        screen = tk.Tk()
        screen.config(bg=Black)
        screen.title('Wordle 5.0')
        screen.iconbitmap(r'wordleicon.ico')
        wordinput = Entry(screen)
        wordinput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

        # creating the guess button
        guessbtn = Button(screen, text="Guess", command=getguess)
        guessbtn.config(font=('Trebuchet MS', 20), highlightbackground="#02EFFE", bg="white", fg="black")
        guessbtn.grid(row=999, column=3, columnspan=2)

        screen.mainloop()
