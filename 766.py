# 766. Toeplitz Matrix
# Array

# Set  先遍历左下角对角线，然后从[0,0]开始遍历对角线
# running time: faster than 76.80%
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        h = M - 1
        while h > 0:
            y, x = h, 0
            arr = []
            while 0 <= y < M and 0 <= x < N:
                arr.append(matrix[y][x])
                x += 1
                y += 1
            
            if len(set(arr)) != 1:
                return False
            h -= 1
        
        w = 0
        while w < N:
            x, y = w, 0
            arr = []
            while 0 <= y < M and 0 <= x < N:
                arr.append(matrix[y][x])
                x += 1
                y += 1
            else:
                if len(set(arr)) != 1:
                    return False
            w += 1
        
        return True


# Iterate
# running time: faster than 76.80%
class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        
        return True

# running time: faster than 76.80%
class Solution2:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val for r,row in enumerate(matrix) for c,val in enumerate(row))


# https://blog.csdn.net/fuxuemingzhu/article/details/79127213
# 只要观察到第二行的后面部分 和 第一行的前面部分相等即可。使用切片和一个for循环就能解决问题。
# running time: faster than 52.03%
class Solution3:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[row+1][1:] == matrix[row][:-1] for row in range(len(matrix)-1))
