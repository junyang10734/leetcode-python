# 566. Reshape the Matrix
# Array

# runtime: O(r*c)
# space: O(r*c)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        
        flatted = []
        for i in range(m):
            for j in range(n):
                flatted.append(mat[i][j])

        res = []
        idx = 0
        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(flatted[idx])
                idx += 1
            res.append(tmp)
        return res

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flattened = [x for row in mat for x in row]
        if len(flattened) == r*c:
            return [flattened[i*c: (i+1)*c] for i in range(r)]
        else:
            return mat