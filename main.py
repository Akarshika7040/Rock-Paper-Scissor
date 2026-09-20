# main.py - main program loop

import basic_error
import computer
import rules
import stats

def play_match():
    print("\nStarting Best of 3 match!")
    player_score = 0
    comp_score = 0

    while player_score < 2 and comp_score < 2:
        user_move = basic_error.get_user_move()
        comp_move = computer.get_computer_move()
        print(f"You chose: {user_move} | Computer chose: {comp_move}")

        winner = rules.check_round_winner(user_move, comp_move)

        if winner == "Player":
            player_score += 1
            print("You won this round!")
        elif winner == "Computer":
            comp_score += 1
            print("Computer won this round!")
        else:
            print("It is a tie!")

        print(f"Score -> You: {player_score} | Computer: {comp_score}\n")

    if player_score > comp_score:
        print("Game Over: YOU WON THE MATCH!")
        stats.save_game(player_score, comp_score, "Player Won")
    else:
        print("Game Over: COMPUTER WON THE MATCH!")
        stats.save_game(player_score, comp_score, "Computer Won")

def main():
    while True:
        print("\n=== ROCK PAPER SCISSORS GAME ===")
        print("1. Play Best of 3")
        print("2. View Past History")
        print("3. Reset History")
        print("4. Exit")

        choice = basic_error.get_menu_choice()

        if choice == "1":
            play_match()
        elif choice == "2":
            stats.show_history()
        elif choice == "3":
            stats.reset_history()
        elif choice == "4":
            print("Thanks for playing! Bye.")
            break

if __name__ == "__main__":
    main()
