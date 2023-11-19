# Define the board size and the symbols for the players
ROWS = 6
COLS = 7
EMPTY = "."
PLAYER1 = "X"
PLAYER2 = "O"

# Create a new board as a list of lists
def create_board():
    board = []
    for i in range(ROWS):
        row = [EMPTY] * COLS
        board.append(row)
    return board

# Print the board in a human-readable format
def print_board(board):
    print("  1 2 3 4 5 6 7")
    print(" +-------------+")
    for i in range(ROWS):
        print("|", end=" ")
        for j in range(COLS):
            print(board[i][j], end=" ")
        print("|")
    print(" +-------------+")

# Check if a column is valid and not full
def is_valid_move(board, col):
    return col >= 0 and col < COLS and board[0][col] == EMPTY

# Drop a piece into a column and return the row it landed on
def drop_piece(board, col, piece):
    for i in range(ROWS-1, -1, -1):
        if board[i][col] == EMPTY:
            board[i][col] = piece
            return i

# Check if a piece at a given location has a four-in-a-row horizontally, vertically or diagonally
def is_winning_move(board, row, col, piece):
    # Check horizontal
    count = 0
    for j in range(COLS):
        if board[row][j] == piece:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    # Check vertical
    count = 0
    for i in range(ROWS):
        if board[i][col] == piece:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    # Check positive diagonal
    count = 0
    i = row - min(row, col)
    j = col - min(row, col)
    while i < ROWS and j < COLS:
        if board[i][j] == piece:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        i += 1
        j += 1
    # Check negative diagonal
    count = 0
    i = row + min(ROWS-1-row, col)
    j = col - min(ROWS-1-row, col)
    while i >= 0 and j < COLS:
        if board[i][j] == piece:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        i -= 1
        j += 1
    # No four-in-a-row found
    return False

# Check if the board is full and the game is a tie
def is_tie(board):
    for j in range(COLS):
        if board[0][j] == EMPTY:
            return False
    return True

# Main game loop
def play_game():
    # Create a new board and print it
    board = create_board()
    print_board(board)
    # Initialize the game state
    game_over = False
    turn = 0
    # Loop until the game is over
    while not game_over:
        # Get the current player and their symbol
        player = (turn % 2) + 1
        if player == 1:
            piece = PLAYER1
        else:
            piece = PLAYER2
        # Prompt the player to enter a valid column
        print(f"Player {player}'s turn ({piece})")
        col = int(input("Enter a column (1-7): ")) - 1
        while not is_valid_move(board, col):
            print("Invalid move. Try again.")
            col = int(input("Enter a column (1-7): ")) - 1
        # Drop the piece into the board and print it
        row = drop_piece(board, col, piece)
        print_board(board)
        # Check if the player has won or the game is a tie
        if is_winning_move(board, row, col, piece):
            print(f"Player {player} wins!")
            game_over = True
        elif is_tie(board):
            print("It's a tie!")
            game_over = True
        # Switch to the next player
        turn += 1

# Start the game
play_game()