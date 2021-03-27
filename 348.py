# 348. Design Tic-Tac-Toe
# Design

# runtime: faster than 83.88%
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows, self.cols = [[0,0] for i in range(n)], [[0,0] for i in range(n)]
        self.diagonal, self.antidiagonal = [0, 0], [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.rows[row][0] == 0:
            self.rows[row] = [player, 1]
        elif self.rows[row][0] == player:
            if self.rows[row][1] == self.n-1:
                return player
            self.rows[row][1] += 1
        elif self.rows[row][0] != -1:
            self.rows[row][0] = -1
        
        if self.cols[col][0] == 0:
            self.cols[col] = [player, 1]
        elif self.cols[col][0] == player:
            if self.cols[col][1] == self.n-1:
                return player
            self.cols[col][1] += 1
        elif self.cols[col][0] != -1:
            self.cols[col][0] = -1
        
        if row == col:
            if self.diagonal[0] == 0:
                self.diagonal = [player, 1]
            elif self.diagonal[0] == player:
                if self.diagonal[1] == self.n-1:
                    return player
                self.diagonal[1] += 1
            elif self.diagonal[0] != -1:
                self.diagonal[0] = -1
        
        if row + col == self.n - 1:
            if self.antidiagonal[0] == 0:
                self.antidiagonal = [player, 1]
            elif self.antidiagonal[0] == player:
                if self.antidiagonal[1] == self.n-1:
                    return player
                self.antidiagonal[1] += 1
            elif self.antidiagonal[0] != -1:
                self.antidiagonal[0] = -1
        
        return 0



# runtime: faster than 94.36%
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows, self.cols = [0]*n, [0]*n
        self.diag, self.atdiag = 0, 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row] += 1 if player == 1 else -1
        if abs(self.rows[row]) == self.n:
            return player
        
        self.cols[col] += 1 if player == 1 else -1
        if abs(self.cols[col]) == self.n:
            return player
        
        if row == col:
            self.diag += 1 if player == 1 else -1
            if abs(self.diag) == self.n:
                return player
            
        if row + col == self.n - 1:
            self.atdiag += 1 if player == 1 else -1
            if abs(self.atdiag) == self.n:
                return player
        
        return 0
        
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)   


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)