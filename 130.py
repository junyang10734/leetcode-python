# Surrounded Regions
# Array

# https://blog.csdn.net/danspace1/article/details/88010210
# BFS
# runtime: faster than 78.53% 
class Solution1:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        row, col = len(board), len(board[0])
        q = collections.deque()
        
        for r in range(row):
            for c in range(col):
                if r in [0, row-1] or c in [0, col-1] and board[r][c] == 'O':
                    q.append((r,c))
        
        while q:
            x, y = q.popleft()
            if 0 <= x < row and 0 <= y < col and board[x][y] == 'O':
                board[x][y] = 'D'
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    q.append((x+dx, y+dy))
        
        for r in range(row):
            for c in range(col):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'D':
                    board[r][c] = 'O'


# https://zhenyu0519.github.io/2020/03/07/lc130/
# DFS
# runtime: faster than 94.85%
class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        M, N = len(board), len(board[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = [[False]* N for _ in range(M)]
        
        def dfs(m,n):
            for dx,dy in dirs:
                x,y = m+dx, n+dy
                if 0 <= x < M and 0 <= y < N and board[x][y] == 'O' and not visited[x][y]:
                    visited[x][y] = True
                    board[x][y] = 'G'
                    dfs(x,y)
        
        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M-1 or j == 0 or j== N-1) and board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'G'
                    visited[i][j] = True
                    dfs(i,j)

        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'G':
                    board[i][j] = 'O'