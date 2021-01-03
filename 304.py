# 304. Range Sum Query 2D - Immutable
# DP
# https://blog.csdn.net/fuxuemingzhu/article/details/83537572

# running time: faster than 56.02%
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            m, n = 0, 0
        else:
            m, n = len(matrix), len(matrix[0])
        self.area = [[0]*(n+1) for _ in range(m+1)]
          
        for i in range(m):
            for j in range(n):
                self.area[i+1][j+1] = matrix[i][j] + self.area[i][j+1] + self.area[i+1][j] - self.area[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.area[row2+1][col2+1] - self.area[row2+1][col1] - self.area[row1][col2+1] + self.area[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)