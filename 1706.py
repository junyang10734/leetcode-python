# 1706. Where Will the Ball Fall
# Matrix

# https://leetcode.com/problems/where-will-the-ball-fall/discuss/988576/JavaC%2B%2BPython-Solution-with-Explanation
# time: O(m*n)
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def getDirection(j):
            for i in range(m):
                j2 = j + grid[i][j]
                if j2 < 0 or j2 >= n or grid[i][j] != grid[i][j2]:
                    return -1
                j = j2
            return j
        
        res = []
        for j in range(n):
            res.append(getDirection(j))
        
        return res