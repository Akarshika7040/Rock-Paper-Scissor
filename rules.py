# game rules and winner logic

def check_round_winner(player, computer):
    if player == computer:
        return "Tie"
    if player == "Rock" and computer == "Scissors":
        return "Player"
    elif player == "Scissors" and computer == "Paper":
        return "Player"
    elif player == "Paper" and computer == "Rock":
        return "Player"
    else:
        return "Computer"
