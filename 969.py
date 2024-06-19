# 969. Pancake Sorting
# Array


# https://leetcode.com/problems/pancake-sorting/solutions/214213/java-c-python-straight-forward/
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i+1, x])
            arr = arr[i+1:][::-1] + arr[:i]
        return res