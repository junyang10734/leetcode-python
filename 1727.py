# 1727. Largest Submatrix With Rearrangements
# Array / Greedy

# https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020708/Python-9-lines-or-Easy-to-understand-explanation-with-pictures-or-Faster-than-100
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0 and matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
            curr = sorted(matrix[i], reverse=True)
            for k in range(len(matrix[0])):
                res = max(res, curr[k]*(k+1))
        
        return res
