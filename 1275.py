# Find Winner on a Tic Tac Toe Game
# Array

# runtime: faster than 98.33%
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return 'Pending'
        else:
            grid = [[-1 for i in range(3)] for j in range(3)]
            for i, item in enumerate(moves):
                x = item[0]
                y = item[1]
                grid[x][y] = 'X' if i%2==0 else 'O'
                temp = grid[x][y]

                if grid[x][0] == temp and grid[x][1] == temp and grid[x][2] == temp:
                    return 'A' if temp == 'X' else 'B'
                elif grid[0][y] == temp and grid[1][y] == temp and grid[2][y] == temp:
                    return 'A' if temp == 'X' else 'B'
                elif grid[0][0] == temp and grid[1][1] == temp and grid[2][2] == temp:
                    return 'A' if temp == 'X' else 'B'
                elif grid[0][2] == temp and grid[1][1] == temp and grid[2][0] == temp:
                    return 'A' if temp == 'X' else 'B'
                else:
                    continue
            if len(moves) < 9:
                return 'Pending'
            return 'Draw'