# Game of Life
# Array


# runtime: faster than 49.89% 
class Solution1:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]
        rows = len(board)
        cols = len(board[0])        
        
        new_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for n in neighbors:
                    r = (row + n[0])
                    c = (col + n[1])
                    
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and (new_board[r][c] == 1):
                        live_neighbors += 1
                
                if new_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                elif new_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1


# runtime: faster than 92.78%
class Solution2:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for n in neighbors:
                    r = (row + n[0])
                    c = (col + n[1])
                    
                    if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                        live_neighbors += 1
                    
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
