#doesnt go in print_board() -> needs to be a global variable
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]}\n-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}\n-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")
print_board()

choice_1 = int(input("select a number on the grid:"))
choice_1 -= 1
board[choice_1] = "X"
print_board()