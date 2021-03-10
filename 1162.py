# 1162. As Far from Land as Possible
# DFS / BFS

# runtime: faster than 83.98%
# https://leetcode-cn.com/problems/as-far-from-land-as-possible/solution/python-tu-jie-chao-jian-dan-de-bfs1162-di-tu-fen-x/
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        steps = -1
        q = deque([(i, j) for i in range(N) for j in range(N) if grid[i][j] == 1])
        if len(q) == 0 or len(q) == N ** 2:
            return steps
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while len(q) > 0:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        grid[nx][ny] = -1
            steps += 1

        return steps