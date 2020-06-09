# Battleships in a Board
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/79403172
# runtime: faster than 6.40% 
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        
        if m == 0 or n == 0:
            return 0
        
        res = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    res += 1
        
        return res
