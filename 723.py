# 723. Candy Crush
# Array

# https://leetcode.com/problems/candy-crush/solution/
# runtime: faster than 49.63%
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        M, N = len(board), len(board[0])
        todo = False
        
        for i in range(M):
            for j in range(N-2):
                if abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]) != 0:
                    board[i][j] = board[i][j+1] = board[i][j+2] = -abs(board[i][j])
                    todo = True
        
        for i in range(M-2):
            for j in range(N):
                if abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]) != 0:
                    board[i][j] = board[i+1][j] = board[i+2][j] = -abs(board[i][j])
                    todo = True
        

        for j in range(N):
            wi = M - 1
            for i in range(M-1, -1, -1):
                if board[i][j] > 0:
                    board[wi][j] = board[i][j]
                    wi -= 1
            for i in range(wi, -1, -1):
                board[i][j] = 0
        
        return board if not todo else self.candyCrush(board)