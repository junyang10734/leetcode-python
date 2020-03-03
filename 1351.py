# 1351. Count Negative Numbers in a Sorted Matrix
# array, binary search


# runtime: faster than 93.15%
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in grid:
            for index,j in enumerate(i):
                if j<0:
                    res += (n-index)
                    break
                    
        return res