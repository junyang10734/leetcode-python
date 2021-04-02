# 999. Available Captures for Rook
# Array

# runtime: faster than 86.82%
class Solution1:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m, n = 0, 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    m, n = i, j
                    break
        
        res = 0
        for i,j in [(-1,0), (0,-1), (0,1), (1,0)]:
            x, y = m + i, n + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    res += 1
                    break
                if board[x][y] == 'B':
                    break
                x, y = x + i, y + j
        return res
