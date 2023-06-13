# 1351. Count Negative Numbers in a Sorted Matrix
# array, binary search


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for line in grid:
            for i,num in enumerate(line):
                if num < 0:
                    res += (n - i)
                    break
        return res
    

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        m, n = len(grid)-1, len(grid[0])-1
        col = 0
        while m >= 0:
            for j in range(n, col-1, -1):
                if grid[m][j] < 0:
                    cnt += 1
                else:
                    col = j
                    break
            m -= 1
        return cnt