# Rotate Image

# Flip up and down first, then flip along the diagonal line from the top left to the bottom right (mirror operation).
# https://blog.csdn.net/fuxuemingzhu/article/details/79451733
# runtime: faster than 89.72%
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            rows, cols = len(matrix), len(matrix[0])
            for i in range(int(rows/2)):
                for j in range(cols):
                    matrix[i][j], matrix[rows-i-1][j] = matrix[rows-i-1][j], matrix[i][j]
            
            for i in range(rows):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]