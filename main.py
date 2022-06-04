import random 


comp_wins = 0
player_wins = 0
# defining a fuction for the user to make his/her choice

print("Game Starts")
def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: " )
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "r"
    else:
        print("Error, try again")
        Choose_Option()
    return user_choice

# defining a function for computer to make its choice


def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You lose.")
            comp_wins += 1

        elif comp_choice == "s":
            print("You chose rock. The computer choose scissors. You win.")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_wins += 1
        elif comp_choice == "p":
            print("You chose paper.The computre choose paper. You tied")

        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            comp_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You choose scissors. the computer chose rock. You lose. ")
            comp_wins += 1

        elif comp_choice == "p":
            print("You choose scissors. The computer chose paper. You win")
            player_wins += 1
        elif comp_choice == "s":
            print("You chose scisors. The computer chose. You tied.")

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    print("")

    user_choice = input("Dou you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N" "n", "No", "no"]:
       
        break
        
    else:
        print("Game Ends")
        break
   
  
