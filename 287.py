# Find the Duplicate Number
# Array


# sort
# runtime: faster than 83.88% 
class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]


# set
# runtime: faster than 94.11%
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


# two pointers
# runtime: faster than 46.77%
class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        t = h = nums[0]
        
        while True:
            t = nums[t]
            h = nums[nums[h]]
            if t == h:
                break
        
        t = nums[0]
        while t != h:
            t = nums[t]
            h = nums[h]
        
        return h