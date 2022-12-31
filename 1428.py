# 1428. Leftmost Column with at Least a One
# binary search 


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# binary search
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        res = cols
        for row in range(rows):
            left, right = 0, cols-1
            while left < right:
                mid = (left + right) // 2
                if binaryMatrix.get(row, mid) == 0:
                    left = mid + 1
                else:
                    right = mid

            if binaryMatrix.get(row, left) == 1:
                res = min(res, left)

        return -1 if res == cols else res


# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/solutions/590040/leftmost-column-with-a-at-least-a-one/
# faster than 1st solution
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        i, j = 0, n-1
        while i < m and j >= 0:
            if binaryMatrix.get(i,j) == 0:
                i += 1
            else:
                j -= 1
        return j + 1 if j != n - 1 else -1

  
  