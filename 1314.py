# 1314 Matrix Block Sum
# Array / Prefix Sum

# time: O(m * n)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        sumArr = [[0] * n for _ in range(m)]
        
        for i in range(m):
            t = 0
            for j in range(n):
                t += mat[i][j]
                sumArr[i][j] = t
                if i > 0:
                    sumArr[i][j] += sumArr[i-1][j]
            
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                minRow, maxRow = max(0, i-k), min(i+k, m-1)
                minCol, maxCol = max(0, j-k), min(j+k, n-1)
                
                if minRow == 0 and minCol == 0:
                    res[i][j] = sumArr[maxRow][maxCol]
                elif minRow == 0:
                    res[i][j] = sumArr[maxRow][maxCol] - sumArr[maxRow][minCol-1]
                elif minCol == 0:
                    res[i][j] = sumArr[maxRow][maxCol] - sumArr[minRow-1][maxCol]
                else:
                    res[i][j] = sumArr[maxRow][maxCol] - sumArr[minRow-1][maxCol] - sumArr[maxRow][minCol-1] + sumArr[minRow-1][minCol-1]
                
        return res
                    