# 1089. Duplicate Zeros
# Array

# runtime: faster than 46.06%
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if not arr:
            return
        i, N = 0, len(arr)
        while i < N:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1