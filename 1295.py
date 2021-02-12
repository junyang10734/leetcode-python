# 1295. Find Numbers with Even Number of Digits
# Array

# runtime: faster than 97.76%
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        if not nums:
            return res
        
        for n in nums:
            if len(str(n)) % 2 == 0:
                res += 1
        return res