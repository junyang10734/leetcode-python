# 490. The Maze
# BFS

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * n for _ in range(m)]

        q = collections.deque()
        q.append(start)
        visited[start[0]][start[1]] = True
        while q:
            x, y = q.popleft()
            for d in dirs:
                nx, ny = x, y
                while 0 <= nx < m and 0 <= ny < n and not maze[nx][ny]:
                    nx += d[0]
                    ny += d[1]
                nx -= d[0]
                ny -= d[1]

                if nx == destination[0] and ny == destination[1]:
                    return True
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
        
        return False

