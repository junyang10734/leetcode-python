# 2439. Minimize Maximum of Array
# Array / Prefix Sum

# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706521/java-c-python-prefix-sum-average-o-n/?orderBy=most_votes
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = 0
        res = 0
        for i,num in enumerate(nums):
            total += num
            res = max(res, (total+i) // (i+1))
        
        return res
