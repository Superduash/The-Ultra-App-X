# importing the random module (No GUI Used)
import random

# creating a function to open this app from the main app
def main3():
    print("\n-----------------------------------------------------------------")
    print("             Rock! Paper! And Scissors! Shoot!!            ")
    print("-------------------------------------------------------------------")
    while True:
        options = ['Rock', 'Paper', 'Scissor']
        # input from user asking some details (No Of Rounds and Name)
        username = input("Enter your name : - ")
        name = username.title()
        while True:
            rounds = input("Enter The Number Of Rounds (min 2): - ")
            # to show error if the user's input is not a number
            if rounds == '1':
                print("There Should Be Minimum 2 Rounds... Please Try Again\n")
                continue
            elif rounds.isdigit():
                num = int(rounds)
                CompScore = 0
                PlayerScore = 0
                NumberOfRounds: int = 1
                gameOn = True
                print(f"\nWelcome ( {name} ) !! Enjoy The Game!! Hope You Win!!")
                while NumberOfRounds < num:
                    while True:
                        print("------------------------------------------------------")
                        print(f"Round No: - {NumberOfRounds}")
                        user_action = input("\nEnter Rock(r)/ Paper(p)/ Scissor(s) : - ").title()
                        # confirming the user action
                        if user_action == "R" or user_action == "Rock":
                            ua = 'Rock'
                            NumberOfRounds += 1
                        elif user_action == "P" or user_action == "Paper":
                            ua = 'Paper'
                            NumberOfRounds += 1
                        elif user_action == "S" or user_action == "Scissor" or user_action == "Scissors":
                            ua = 'Scissor'
                            NumberOfRounds += 1
                        else:
                            print('Invalid Option...Please Try Again')
                            continue
                        # deciding the computer action using the random module
                        computer_action = random.choice(options)
                        # comparing the user and computer action to see who won the round
                        print('\nYou Chose (', ua, ') , And The Computer Chose (', computer_action, ')')
                        if ua == computer_action:
                            print(f"Both Players Selected {ua}.So, It's A Tie!")
                        elif ua == "Rock" and computer_action == "Scissor":
                            print("Rock Crushes Scissor... U Win")
                            PlayerScore += 1
                        elif ua == "Scissor" and computer_action == "Rock":
                            print("Rock Smashes Scissor... U Lose")
                            CompScore += 1
                        elif ua == "Paper" and computer_action == "Rock":
                            print("Paper Covers Rock... U Win")
                            PlayerScore += 1
                        elif ua == 'Rock' and computer_action == 'Paper':
                            print('Paper Covers Rock... U Lose')
                            CompScore += 1
                        elif ua == 'Scissor' and computer_action == "Paper":
                            print("Scissor Cuts Paper... U Win")
                            PlayerScore += 1
                        elif ua == 'Paper' and computer_action == "Scissor":
                            print("Scissor Cuts Paper... U Lose")
                            CompScore += 1
                        # to end the game after the given No. of Rounds
                        if NumberOfRounds == num + 1:
                            gameOn = False
                            break
                # to display the winner (who won the most rounds).. or draw match if it's a tie
                if PlayerScore == CompScore:
                    print("\nDraw Match!! -_-")
                elif PlayerScore > CompScore:
                    print(f"\nCongrats {name}, You won the game !!")
                else:
                    print(f"\nOops Computer won the game!! Better luck next time {name}!")

                # Play Again Option
                play_again = input("\nPlay again? (y/n): ")
                if play_again.lower() != "y":
                    print("\nHope You Enjoyed The Game.. See You Soon")
                    return
            else:
                print("Invalid Option.. Please Try Again\n")
                continue
