# 529. Minesweeper
# DFS / Array

# https://blog.csdn.net/fuxuemingzhu/article/details/79462285
# running time: faster than 75.52% 
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = click[0], click[1]
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == 'M':
                board[row][col] = 'X'
            elif board[row][col] == 'E':
                n = sum([board[row+r][col+c] == 'M' for r,c in dirs if 0<=row+r<len(board) and 0<=col+c<len(board[0])])
                board[row][col] = str(n) if n else 'B'
                if not n:
                    for r,c in dirs:
                        self.updateBoard(board,[row+r,col+c])
        
        return board