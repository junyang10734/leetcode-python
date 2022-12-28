# 51. N-Queens
# backtrack

# https://labuladong.github.io/algo/4/31/104/
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]* n for _ in range(n)]
        self.n = n

        def backtrack(board, row):
            if row == self.n:
                format_board = []
                for line in board:
                    print(line)
                    print("".join(line))
                    format_board.append("".join(line))
                res.append(format_board)
            else:
                for col in range(self.n):
                    if not isValid(board, row, col):
                        continue
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'

        def isValid(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            i, j = row - 1, col + 1
            while i >= 0 and j < self.n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            return True

        backtrack(board, 0)
        return res