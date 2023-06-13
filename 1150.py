# 1150. Check If a Number Is Majority Element in a Sorted Array
# Array / Sort

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = 0
        for idx,num in enumerate(nums):
            if num == target:
                cnt += 1
            if cnt > 0 and num != target:
                break
        
        return cnt > len(nums) / 2