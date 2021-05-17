# 1197. Minimum Knight Moves
# Graph

# https://leetcode.com/problems/minimum-knight-moves/solution/
# runtime: O((max(∣x∣,∣y∣)^2) 
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        visited = set()
        queue = collections.deque([(0, 0)])
        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                curx, cury = queue.popleft()
                if x == curx and y == cury:
                    return steps
                for dx, dy in dirs:
                    nx, ny = curx+dx, cury+dy
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            steps += 1      