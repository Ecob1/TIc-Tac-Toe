board= [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# To check when it's true refering to "x", otherwise will be "o"
user = True


# This function will create the board
def main(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

main(board)

# If user want to quit the game
def user_quit(user_quit):
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
# To check if user will enter a number only
def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else: return True

# This will check if user will enter a number between 1 to 9
def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else: return True

# this function will check if row and col hasn't been check
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

def addToBoard(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user


def current_user(user):
    if user: return "x"
    else: return "o"

def isWing(user, board):
    if check_row(user, board): return True

def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False   

while True:
    active_user = current_user(user)
    main(board)
    user_input = input('Please enter a position 1 through 9 or enter \"q"\ to quit: ')
    if user_quit(user_input): break
    if not check_input(user_input):
        print("Please try again")
        continue
    user_input = int(user_input) -1
    coords = coordinates(user_input)
    # board[0][0] = "x"
    if istaken(coords, board):
        print("Please try again.")
        continue 
    addToBoard(coords, board, active_user)
    if isWing(active_user, board):
        print(f"{active_user.upper()} won!")
        break

    user = not user

if __name__ == "__main__":
    main()


