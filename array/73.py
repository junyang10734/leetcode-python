# Set Matrix Zeroes

# Additional Memory Approach
# run time: O(m*n)  faster than 61.63%
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix)
        y = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(x):
            for j in range(y):
                if i in rows or j in cols:
                    matrix[i][j] = 0


# run time: O(m*n)  faster than 94.12%
# spcae: O(1)
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        r = len(matrix)
        c = len(matrix[0])
        
        for i in range(r):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1,c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,r):
            for j in range(1,c):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(1,c):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(r):
                matrix[i][0] = 0