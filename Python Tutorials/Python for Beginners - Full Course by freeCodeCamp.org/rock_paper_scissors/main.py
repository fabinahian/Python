import random


def get_choices():
    player_pick = input("Would you pick 'rock', 'paper' or 'scissors'? -")

    options = ["rock", "paper", "scissors"]
    computer_pick = random.choice(options)

    choices = {"player": player_pick, "computer": computer_pick}

    return choices


def check_win(player_pick, computer_pick):

    print(f"You picked {player_pick} and the computer picked {computer_pick}.")

    if player_pick == computer_pick:
        return "It's a tie!"

    elif player_pick == "rock":
        if computer_pick == "paper":
            return "Paper beats rock. You lose."
        else:
            return "Rock smashes scissors. You win!"

    elif player_pick == "paper":
        if computer_pick == "rock":
            return "Paper beats rock. You win!"
        else:
            return "Rock smashes scissors. You lose."

    elif player_pick == "scissors":
        if computer_pick == "rock":
            return "Rock beats scissors. You lose."
        else:
            return "Scissors cut papers. You win!"

    else:
        return "Unrecognized inputs!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
