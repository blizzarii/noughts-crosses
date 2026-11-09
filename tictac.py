import time
# these need to be global variables

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
selection = ["O","X"]
current_player = "X"
turns = 0
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]}\n-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}\n-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")
print_board()

while turns != 9:
    print(f"\n1it is {current_player}'s turn!")
    time.sleep(1)
    choice = int(input("select a number on the grid:"))
    choice -= 1
    if board[choice] in selection:
        print("this isnt an empty tile!")
    else:
        board[choice] = str(current_player)
        turns += 1
        print_board()

    if board[0] == board[1] == board[2] == current_player or board[3] == board[4] == board[5] == current_player or board[6] == board[7] == board[8] == current_player or board[0] == board[3] == board[6] == current_player or board[1] == board[4] == board[7] == current_player or board[2] == board[5] == board[8] == current_player or board[0] == board[4] == board[8] == current_player or board[2] == board[4] == board[6] == current_player:
        print(f"player {current_player} wins!")
        break
# here i tried using a "conditional expression" (same line if statement)
    current_player = "O" if current_player == "X" else "X"




