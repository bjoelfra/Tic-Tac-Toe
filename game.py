board = [' ' for _ in range(9)]  


def display_board():
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_tie():
    return ' ' not in board


def play_game():
    current_player = 'X'
    while True:
        display_board()
        print(f"Player {current_player}'s turn.")
        
        
        try:
            move = int(input("Enter a number between 1 and 9 to place your mark: ")) - 1
            if board[move] != ' ':
                print("That spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        
        
        board[move] = current_player
        
        
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        
        
        if check_tie():
            display_board()
            print("It's a tie!")
            break
        
        
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()