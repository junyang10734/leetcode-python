# 74. Search a 2D Matrix
# Binary Search


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = bisect.bisect_left([matrix[i][-1] for i in range(m)], target)
        if row < m:
            col = bisect.bisect_left(matrix[row], target)
            if col >= 0:
                if matrix[row][col] == target:
                    return True

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            idx = (left + right) // 2
            item = matrix[idx // n][idx % n]
            if target == item:
                return True
            elif target < item:
                right = idx - 1
            elif target > item:
                left = idx + 1

        return False