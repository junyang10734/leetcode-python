# Rotate Image
# Array

# https://leetcode.com/problems/rotate-image/solution/


# Rotate Groups of Four Cells
# runtime: faster than 84.10%
class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range((n+1)//2):
            for j in range(n//2):
                tmp = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = matrix[i][j]
                matrix[i][j] = tmp


# Reverse on Diagonal and then Reverse Left to Right
# runtime: faster than 99.10%
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]