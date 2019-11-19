# Unique Paths

# runtime: faster than 96.36%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            res[i][0] = 1
        for j in range(m):
            res[0][j] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        
        return res[n-1][m-1]