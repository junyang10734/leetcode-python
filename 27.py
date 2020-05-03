# Remove Element

# Array / Two pointers
# runtime: faster than 88.15%
# https://blog.csdn.net/fuxuemingzhu/article/details/51303161
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] == val:
                nums[l] = nums[r]
                r -= 1
            else:
                l += 1
        
        return l