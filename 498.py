# 498. Diagonal Traverse
# Array

# https://leetcode.com/problems/diagonal-traverse/solution/

# Diagonal Iteration and Reversal
# running time: faster than 82.92%
class Solution1:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        M, N = len(matrix), len(matrix[0])
        res, inter = [], []
        
        for d in range(M+N-1):
            inter = []
            i = 0 if d < N else d - N + 1
            j = d if d < N else N - 1
            
            while i < M and j > -1:
                inter.append(matrix[i][j])
                i += 1
                j -= 1
            
            if d % 2 == 0:
                res += inter[::-1]
            else:
                res += inter
        
        return res



# Simulation
# running time: faster than 82.92% 
class Solution2:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        M, N = len(matrix), len(matrix[0])
        i, j = 0, 0
        direction = 1
        res = []

        while i < M and j < N:
            res.append(matrix[i][j])
            
            new_i = i + (-1 if direction == 1 else 1)
            new_j = j + (1 if direction else -1)
            
            if new_i < 0 or new_i == M or new_j < 0 or new_j == N:
                if direction == 1:
                    i += (j == N - 1)
                    j += (j < N - 1)
                else:
                    j += (i == M - 1)
                    i += (i < M - 1)
                direction = 1 - direction
            else:
                i = new_i
                j = new_j
        
        return res             