from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col, board):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # Check upper left diagonal
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            # Check upper right diagonal
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False

            return True

        def backtrack(row, board):
            if row == n:
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_safe(row, col, board):
                    board[row][col] = 'Q'
                    backtrack(row+1, board)
                    board[row][col] = '.'

        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        backtrack(0, board)
        return result

# Example usage:
solution = Solution()
n = 4
print(solution.solveNQueens(n))
