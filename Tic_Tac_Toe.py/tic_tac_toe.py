board= [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# This function will create the board
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

print_board(board)

def quit(user_quit):
    if user_input.lower() == "q":
        print("Thanks for playing")
        return True
    else:
        return False
 
# Check if its a user input a number
def check_input(user_input):
    if not isnum(user_input): return False
    user_input = int(user_input)
    # Checking if its 1 - 9
    if not bounds(user_input): return False
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else: return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "_":
        print("This position is already taken")
        return True
    else: return False

def coordinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row,col)
    

while True:
    print_board(board)
    user_input = input("Please enter a position 1 through 9 or enter \'q'\ to quit:")
    if quit(user_input): break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input = int(user_input) -1
    coords = coordinates(user_input)
    board[0][0] = "x"
    if istaken(coords, board):
        print("Please try again.")
        continue 


