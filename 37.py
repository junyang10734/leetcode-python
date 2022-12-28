# 37. Sudoku Solver
# backtrack

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board, 0, 0)

    def backtrack(self, board, r, c):
        # 穷举到最后一列的话就换到下一行重新开始
        if c == 9:
            return self.backtrack(board, r+1, 0)
        # 找到一个可行解，触发 base case
        if r == 9:
            return True
            
        # 如果该位置是预设的数字，不用我们操心
        if board[r][c] != ".":
            return self.backtrack(board, r, c+1)

        for num in range(1, 10):
            # 如果遇到不合法的数字，就跳过
            if not self.isValid(board, r, c, str(num)):
                continue
            board[r][c] = str(num)
            if self.backtrack(board, r, c+1):
                return True
            board[r][c] = '.' 
            
        return False


    def isValid(self, board, r, c, num):
        for i in range(9):
            if board[r][i] == num:
                return False
            if board[i][c] == num:
                return False
            if board[(r//3)*3 + i//3][(c//3)*3 + i%3] == num:
                return False
        return True