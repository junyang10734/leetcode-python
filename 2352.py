# 2352. Equal Row and Column Pairs
# Hash Table

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowDict, colDict = collections.defaultdict(int), collections.defaultdict(int)
        n = len(grid)
        for i in range(n):
            row = tuple(grid[i])
            col = [grid[c][i] for c in range(n)]
            rowDict[row] += 1
            colDict[tuple(col)] += 1
        
        res = 0
        for item,count in rowDict.items():
            if item in colDict:
                res += count * colDict[item]
        return res