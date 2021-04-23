# 1228. Missing Number In Arithmetic Progression
# Math

# runtime: O(n)
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1] - arr[0]) // len(arr)
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != diff:
                return arr[i] + diff
        return arr[0]