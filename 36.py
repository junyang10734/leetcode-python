# Valid Sudoku
# Array


# https://blog.csdn.net/fuxuemingzhu/article/details/82813653
# runtime: faster than 69.87%
class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidCell(board)
        
    def isValidRow(self, board):
        n = len(board)
        for i in range(n):
            row = [x for x in board[i] if x != '.']
            if len(set(row)) != len(row):
                return False
        return True

    def isValidCol(self, board):
        n = len(board)
        for i in range(n):
            col = [board[r][i] for r in range(n) if board[r][i] != '.']
            if len(set(col)) != len(col):
                return False
        return True
        
    def isValidCell(self, board):
        n = len(board)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                cell = []
                for a in range(3):
                    for b in range(3):
                        num = board[i+a][j+b]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False 
        return True


# https://blog.csdn.net/coder_orz/article/details/51596499
# runtime: faster than 85.67% 
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            if not self.isValidNine(board[i]):
                return False
            col = [c[i] for c in board]
            if not self.isValidNine(col):
                return False
        
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                block = [board[i+a][j+b] for a in range(3) for b in range(3)]
                if not self.isValidNine(block):
                    return False
        
        return True
    
    def isValidNine(self, arr):
        d = {}
        for i in arr:
            if i != '.':
                if i in d:
                    return False
                else:
                    d[i] = True
        return True


# runtime: faster than 12.19%
class Solution3:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = [[False for i in range(n)] for j in range(n)]
        col = [[False for i in range(n)] for j in range(n)]
        block = [[False for i in range(n)] for j in range(n)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i//3*3 + j//3
                    if row[i][num] or col[j][num] or block[k][num]:
                        return False
                    row[i][num] = col[j][num] = block[k][num] = True
        
        return True