# Search a 2D Matrix II

# traversal
# runtime: faster than 18.38%
class Solution1:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        if len(matrix) > 0 and len(matrix[0]) > 0:        
            for i in range(len(matrix)):
                if target == matrix[i][0]:
                    return True
                elif target < matrix[i][0]:
                    return False

                for j in range(len(matrix[0])):
                    if target == matrix[i][j]:
                        return True
                    elif target > matrix[i][j]:
                        continue
        
        return False


# runtime: faster than 80.83% 
class Solution2:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        for x in matrix:
            for y in x:
                if target == y:
                    return True
        
        return False


# binary search
# runtime: faster than 96.95%
class Solution3:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """        
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        i, j = 0, cols-1
        
        while True:
            if i < rows and j >= 0:
                if target == matrix[i][j]:
                    return True
                elif target > matrix[i][j]:
                    i += 1
                else:
                    j -= 1
            else:
                return False
        