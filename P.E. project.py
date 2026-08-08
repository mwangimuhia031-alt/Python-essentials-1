import random

def display_board(board):
    """
    Renders the 3x3 Tic-Tac-Toe grid in the console.
    Uses ASCII characters (+, -, |) to create a structured visual box.
    """
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("| " * 3, "|", sep="")
        for col in range(3):
            print("| " + str(board[row][col]) + " ", end="")
        print("|")
        print("| " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    """
    Prompts the human player to make a move.
    Validates the input to ensure it is a valid, unoccupied number between 1 and 9.
    """
    while True:
        move = input("Enter your move (1-9): ")
        
        # Validation: Check if input is a digit and falls between 1 and 9
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        # Convert user input (1-9) to 0-indexed matrix coordinates (row, col)
        move = int(move) - 1
        row, col = move // 3, move % 3
        
        # Validation: Check if the selected square is already taken
        if board[row][col] in ['X', 'O']:
            print("That square is already occupied!")
            continue
            
        # Place the user's mark ('O') on the validated spot
        board[row][col] = 'O'
        break

def make_list_of_free_fields(board):
    """
    Scans the board and gathers all available squares.
    Returns a list of tuples containing (row, col) coordinates.
    """
    free = []
    for row in range(3):
        for col in range(3):
            # If the spot contains a number instead of 'X' or 'O', it is free
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))
    return free

def victory_for(board, sign):
    """
    Evaluates the board to check if the given sign ('X' or 'O') has won.
    Checks all 3 rows, all 3 columns, and both primary diagonals.
    """
    for i in range(3):
        # Check rows (all 3 items in a horizontal line match the sign)
        # Check columns (all 3 items in a vertical line match the sign)
        if all(board[i][j] == sign for j in range(3)) or \
           all(board[j][i] == sign for j in range(3)):
            return True
            
    # Check top-left to bottom-right diagonal, and top-right to bottom-left diagonal
    if all(board[i][i] == sign for i in range(3)) or \
       all(board[i][2 - i] == sign for i in range(3)):
        return True
        
    return False

def draw_move(board):
    """
    Executes the computer's turn by randomly selecting an open square.
    Places an 'X' on the selected position.
    """
    free = make_list_of_free_fields(board)
    if free:
        # Pick a random coordinate pair from the available open squares
        row, col = random.choice(free)
        board[row][col] = 'X'

# ==========================================
# GAME INITIALIZATION AND MAIN LOOP
# ==========================================

# Create a 3x3 list comprehension matrix filled with numbers 1 to 9
board = [[3 * j + i + 1 for i in range(1, 4)] for j in range(3)]

# Rule constraint: The computer always claims the center spot (square 5) first
board[1][1] = 'X'
display_board(board)

# Start the continuous loop of alternating turns
while True:
    # 1. Human Turn
    enter_move(board)
    display_board(board)
    
    # Check if the human player just won
    if victory_for(board, 'O'):
        print("You won!")
        break
        
    # Check if the board is completely full after the human move
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
        
    # 2. Computer Turn
    draw_move(board)
    print("Computer's move:")
    display_board(board)
    
    # Check if the computer just won
    if victory_for(board, 'X'):
        print("The computer won!")
        break
        
    # Check if the board is completely full after the computer move
    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
