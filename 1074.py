# 1074. Number of Submatrices That Sum to Target
# Array / DP / Sliding Window

# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/solution/
# runtime: O(R^2*C), R is the number of rows and C is the number of columns
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        prefix = [[0]*(N+1) for _ in range(M+1)]
        for i in range(1, M+1):
            for j in range(1, N+1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + matrix[i-1][j-1]
        
        count = 0
        for i1 in range(1, M+1):
            for i2 in range(i1, M+1):
                h = collections.defaultdict(int)
                h[0] = 1
                for j in range(1, N+1):
                    curr_sum = prefix[i2][j] - prefix[i1-1][j]
                    count += h[curr_sum - target]
                    h[curr_sum] += 1
        
        return count