# Tic Tac Toe Game
import random

# Function to print the board
def print_board(board):
    print("╔═════════╗")
    for i in range(0, len(board), 3):
        print(" " + board[i] + " | " + board[i + 1] + " | " + board[i + 2])
        if i == len(board) - 3:
            print("╚═════════╝")
        else:
            print("----------")

            

# Function to check if the board is full
def is_full(board):
    for i in range(9):
        if board[i] == " ":
            return False
    return True

# Function to check if the game is over
def is_game_over(board):
    if board[0] == board[1] == board[2] != " ":
        return True
    elif board[3] == board[4] == board[5] != " ":
        return True
    elif board[6] == board[7] == board[8] != " ":
        return True
    elif board[0] == board[3] == board[6] != " ":
        return True
    elif board[1] == board[4] == board[7] != " ":
        return True
    elif board[2] == board[5] == board[8] != " ":
        return True
    elif board[0] == board[4] == board[8] != " ":
        return True
    elif board[2] == board[4] == board[6] != " ":
        return True
    else:
        return False

# Function to check if the player|computer has won
def wins(board, target):
    if board[0] == board[1] == board[2] == target:
        return True
    elif board[3] == board[4] == board[5] == target:
        return True
    elif board[6] == board[7] == board[8] == target:
        return True
    elif board[0] == board[3] == board[6] == target:
        return True
    elif board[1] == board[4] == board[7] == target:
        return True
    elif board[2] == board[5] == board[8] == target:
        return True
    elif board[0] == board[4] == board[8] == target:
        return True
    elif board[2] == board[4] == board[6] == target:
        return True
    else:
        return False

# Function to check if the move is valid
def is_valid_move(board, move):
    if board[move] == " ":
        return True
    else:
        return False

# Function to get the player's move
def get_player_move(board):
    while True:
        move_index = int(input("Enter your move (1-9): ")) - 1
        if is_valid_move(board, move_index):
            return move_index
        else:
            print("Invalid move! Try again....")

# Function to get the computer's move
def get_computer_move(board):
    while True:
        move = random.randint(0, 8)
        if is_valid_move(board, move):
            return move

# Function to play the game
def play_game():
    board = [" "]*9
    player = "X"
    computer = "O"
    print_board(board)

    while not is_full(board):
        move = get_player_move(board)
        board[move] = player
        print_board(board)
        if is_game_over(board):
            if wins(board, player):
                print("Player wins!")
            else:
                print("Computer wins!")
            return
        if is_full(board):
            print("It's a tie!")
            return
        move = get_computer_move(board)
        board[move] = computer
        print_board(board)
        if is_game_over(board):
            if wins(board, player):
                print("Player wins!")
            else:
                print("Computer wins!")
            return
        if is_full(board):
            print("It's a tie!")
            return

# Main function


def main():
    play_game()


# Call the main function
if __name__ == "__main__":
    main()
