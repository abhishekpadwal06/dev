import random

def get_choices():
    player_choice = input("Enter a choice (rock / paper / scissors): ")
    options = ["rock", "paper", "scissors"]     # List
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}    # Dictionaries

    return choices

def check_win(player, computer):
    print("You chose " + player + ", Computer chose " + computer) # String concatenation  
    #   OR  print(f"You chose {player}, Computer chose {computer}")
    
    if player == computer:
        return "It's a tie!" 

    elif player == "rock":                   # Player is rock
        if computer == "paper": 
            return "Uh-oh! You've lost."

        if computer == "scissors": 
            return "Yay! You win!"
    
    elif player == "paper":                  # Player is paper
        if computer == "scissors": 
            return "Uh-oh! You've lost."

        if computer == "rock": 
            return "Yay! You win!"

    elif player == "scissors":               # Player is scissors
        if computer == "rock":
            return "Uh-oh! You've lost."

        if computer == "paper": 
            return "Yay! You win!"   


response = get_choices()
result = check_win(response["player"], response["computer"])

print(result)