import random

choices=["rock","paper", "scissor"]

play_game = input("Do you want to play Rock, Paper, Scissors? (yes/no): ").lower()

if play_game != "yes":
    print("Maybe next time. Goodbye!")
else:    
    while True:
        user_input=input("Enter weapon :  or 'quit' to exit ").lower()

        if user_input=="quit":
            print("the game has quit")
            break

        if user_input not in choices:
            print("invalid input")
            continue

        computer_input=random.choice(choices)

        print(f"The user have choosen : {user_input}")
        print(f"The computer have chosen : {computer_input}")

            

        if user_input==computer_input:
            print("It's a tie")
        elif (user_input=="rock" and computer_input=="scissor") or (user_input=="scissor" and computer_input=="paper") or (user_input=="paper" and computer_input=="rock"):
            print("You won")
        else:
            print("You lost")

