# Sort Colors

# two pass
# runtime: faster than 94.62%
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0:0,1:0,2:0}
        for i in nums:
            count[i] += 1
            
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2


# one pass
# runtime: faster than 98.47%
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num0 = nums.count(0)
        num1 = nums.count(1)
        num2 = nums.count(2)
        
        for i in range(len(nums)):
            if i < num0:
                nums[i] = 0
            elif i < num0 + num1:
                nums[i] = 1
            else:
                nums[i] = 2

# two points
# https://leetcode.com/problems/sort-colors/discuss/427732/Pointers-Python3-(99-100)
# runtime: faster than 98.47%
class Solution3:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p, l, r = 0, 0, len(nums)-1
        
        while p <= r:
            if nums[p] == 0:
                nums[p], nums[l] = nums[l], nums[p]
                p += 1
                l += 1
                continue
            if nums[p] == 1:
                p += 1
                continue
            if nums[p] == 2:
                nums[p], nums[r] = nums[r], nums[p]
                r -= 1
                
        return