# 27. Remove Element
# Compare with 26, 283

# Array / Two pointers
# runtime: faster than 88.15%
# https://blog.csdn.net/fuxuemingzhu/article/details/51303161
class Solution1:
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


# Two Pointers
# runtime: faster than 88.15%
# https://labuladong.github.io/algo/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E5%8E%9F%E5%9C%B0%E4%BF%AE%E6%94%B9%E6%95%B0%E7%BB%84.html
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow