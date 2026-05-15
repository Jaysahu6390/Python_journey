import random

# This function will get the choices of the player and the computer
def get_choices():
    user_choice = input("Enter your choice (rock,paper,scissor): ").lower()
    option = ["rock","paper","scissors"]
    computer_choice = random.choice(option)
    choices = {"player": user_choice, "computer": computer_choice}
    return choices

# This function will determine the winner of the game
def get_result(player,computer):
    if player not in ["rock", "paper", "scissors"]:
            return "Invalid choice. Please choose rock, paper, or scissors."
    else:
        print(f"Player chose: {player}, Computer chose: {computer}")
        if player == computer:
            return "It is a tie..."
    
        elif player == "rock":
            if computer == "scissors":
                return "Rock smashes scissors! Player Wins!"
            else:
                return "Paper covers rock. Computer Wins."
        
        elif player == "paper":
            if computer == "scissors":
                return "Scissors cuts the paper. Computer Wins!"
            else:
                return "Paper covers rock! Player Wins!"
        
        elif player == "scissors":
            if computer == "paper":
                return "Scissors cuts the paper ! Player Wins!"
            else:
                return "Rock smashes Paper. Computer Wins."

# Main function to run the game
if __name__ == "__main__": 
    choices = get_choices()
    result = get_result(choices["player"], choices["computer"])
    print(result)