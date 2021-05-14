# 665. Non-decreasing Array

# https://leetcode.com/problems/non-decreasing-array/solution/
# runtime: O(n)
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        found = False

        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if found:
                    return False
                found = True
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]

        return True