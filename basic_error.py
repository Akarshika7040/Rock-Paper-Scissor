# takes care of user inputs using dictionaries. and return error when terms are out of box

def get_user_move():
    moves = {"r": "Rock", "p": "Paper", "s": "Scissors" }
    
    while True:
        choice = input("Choose (r)ock, (p)aper, or (s)cissors: ").lower().strip()
        if choice in moves:
            return moves[choice]
        else:
            print("Invalid input! Please type only r, p, or s.")

def get_menu_choice():
    valid_choices = {"1", "2", "3", "4"}
    
    while True:
        choice = input("Enter choice (1-4): ").strip()
        if choice in valid_choices:
            return choice
        else:
            print("Invalid option! Please enter 1, 2, 3, or 4.")
