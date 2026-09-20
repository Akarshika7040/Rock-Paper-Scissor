# the game history saving in a list named 'history'  

history = []

#saving game history in 'history' list
def save_game(player_score, comp_score, outcome):
    record = f"Result: {outcome} | Score: {player_score}-{comp_score}"
    history.append(record)

# printing history
def show_history():
    print("\n--- MATCH HISTORY ---")
    if len(history) == 0:
        print("No matches played yet.")
    else:
        count = 1
        for match in history:
            print("Match", count, ":", match)
            count = count + 1
            
#clearing history
def reset_history():
    history.clear()
    print("Match history cleared!")
