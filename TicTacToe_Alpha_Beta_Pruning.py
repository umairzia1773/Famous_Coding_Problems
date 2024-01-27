import random
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n----------")

def is_game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':  #row win ~ check
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':  #column win ~ check
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':      #diagonal win ~ check
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':      # draw ~ check
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def evaluate_board(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return -1
            elif board[i][0] == 'O':
                return 1
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return -1
            elif board[0][i] == 'O':
                return 1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return -1
        elif board[0][0] == 'O':
            return 1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return -1
        elif board[0][2] == 'O':
            return 1
    return 0

def A_B_pruning(board, depth, is_maximizing, alpha, beta):
    if is_game_over(board) or depth == 0:
        return evaluate_board(board)

    if is_maximizing:                #for computer's turn
        max_eval = -float('inf')     #-ve infinity value
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = A_B_pruning(board, depth - 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:                              #for human turn
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = A_B_pruning(board, depth - 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def make_computer_move(board):
    best_move = None
    best_eval = -float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                eval = A_B_pruning(board, 5, False, -float('inf'), float('inf'))
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("TIC-TAC-TOE GAME")
    print("================")
    print()

    for turn in range(9):
        if turn % 2 == 0:
            print_board(board)
            while True:
                try:
                    player_move = int(input("Enter your move (0-8): "))
                    if 0 <= player_move < 9 and board[player_move // 3][player_move % 3] == ' ':
                        board[player_move // 3][player_move % 3] = 'X'
                        break
                    else:
                        print("Invalid Move...TRY AGAIN.")
                except ValueError:
                    print("Invalid Input...Please Enter a Number between 0 and 8.")

            if is_game_over(board):
                break
        else:
            computer_move = make_computer_move(board)
            board[computer_move[0]][computer_move[1]] = 'O'
            if is_game_over(board):
                break

    print_board(board)
    result = evaluate_board(board)
    if result == 1:
        print("Computer wins!")
    elif result == -1:
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
