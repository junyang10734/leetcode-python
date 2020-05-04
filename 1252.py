# Cells with Odd Values in a Matrix
# Array

# runtime: faster than 0
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        l = [[0]*m for i in range(n)]
        
        for x in range(n):
            for y in range(m):
                for item in indices:
                    if item[0] == x:
                        l[x][y] += 1
                    if item[1] == y:
                        l[x][y] += 1

        res = 0
        for x in range(n):
            for y in range(m):
                if l[x][y]%2 != 0:
                   res += 1
        return res