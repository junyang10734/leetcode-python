# Find Minimum in Rotated Sorted Array II

# Dac
# https://zxi.mytechroad.com/blog/divide-and-conquer/leetcode-154-find-minimum-in-rotated-sorted-array-ii/
# faster than 98.91% 
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        def dac(nums, l, r):
            if r - l <= 1:
                return min(nums[l], nums[r])
            if nums[l] < nums[r]:
                return nums[l]
            
            mid = l + (r - l) // 2
            return min(dac(nums, l, mid), dac(nums, mid+1, r))
        
        return dac(nums, 0, len(nums)-1)


# Search
# https://blog.csdn.net/fuxuemingzhu/article/details/79536203
# faster than 65.65% 
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        def minInOrder(nums, l, r):
            n = nums[l]
            for i in range(l+1, r):
                if nums[i] < n:
                    return nums[i]
            return n
        
        l, r = 0, len(nums) - 1
        mid = l
        
        while nums[l] >= nums[r]:
            if r - l == 1:
                mid = r
                break
            mid = (l + r) // 2
            if nums[mid] == nums[l] and nums[mid] == nums[r]:
                return minInOrder(nums, l, r)
            if nums[mid] >= nums[l]:
                l = mid
            elif nums[mid] <= nums[r]:
                r = mid
            
        return nums[mid]
