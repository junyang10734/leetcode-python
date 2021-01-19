# 3Sum Closest
# Array / Two Pointers

# https://leetcode.com/problems/3sum-closest/solution/
# Two Pointers + Sort
# runtime: faster than 76.57%
class Solution1:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                _sum  = nums[i] + nums[lo] + nums[hi]
                if abs(target - _sum) < abs(diff):
                    diff = target - _sum
                if _sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
