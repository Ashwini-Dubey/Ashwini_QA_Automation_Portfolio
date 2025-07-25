import random

def get_choices():
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors):").lower()
        if player_choice in ["rock","paper","scissors"]:
            options = ["rock", "paper", "scissors"]
            computer_choice = random.choice(options)
            choices = {"player" : player_choice , "computer" : computer_choice}
            return choices
        else:
            print("Enter valid choice!!")

def check_win(player , computer):
    print(f"You chose: {player}, Computer Chose: {computer}.")

    if player == computer:
        return "Its a tie!!"

    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!!"
        else:
            return "Paper covers rock! You lose!!"

    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper! You lose!!"
        else:
            return "Paper covers rock! You win!!"

    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!!"
        else:
            return "Rock smashes scissors! You lose!!"

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)