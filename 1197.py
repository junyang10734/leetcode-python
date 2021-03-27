# 1197. Minimum Knight Moves
# Graph

# https://zhenyu0519.github.io/2020/07/21/lc1197/
# runtime: faster than 51.71%
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x == 1 and y == 1:
            return 2
        
        directions = [(-1, -2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1), (1, 2), (2, 1)]
        seen = set((0, 0))
        q = collections.deque([(0, 0, 0)])
        while q:
            i, j, v = q.popleft()
            if i == x and j == y:
                return v
            for dx, dy in directions:
                if 0 <= dx+i <= 300 and 0 <= dy+j <= 300 and (dx+i, dy+j) not in seen:
                    q.append((i+dx, j+dy, v+1))
                    seen.add((i+dx, j+dy))
        