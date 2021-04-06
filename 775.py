# 775. Global and Local Inversions
# Array / Math

# https://leetcode.com/problems/global-and-local-inversions/solution/

# Remember Minimum
# runtime: faster than 49.04%
class Solution1:
    def isIdealPermutation(self, A: List[int]) -> bool:
        N = len(A)
        floor = N
        for i in range(N-1, -1, -1):
            floor = min(floor, A[i])
            if i >= 2 and A[i-2] > floor:
                return False
        return True


# Linear Scan
# runtime: faster than 86.59%
class Solution2:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i-x) <= 1 for i,x in enumerate(A))