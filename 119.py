# Pascal's Triangle II
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/51348629

# runtime: faster than 51.28%
class Solution1:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [ [1 for j in range(i+1)] for i in range(rowIndex + 1)]
        
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[-1]


# runtime: faster than 51.28%
# space: O(n)
class Solution2:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i-1, 0, -1):
                res[j] += res[j-1]
        return res
