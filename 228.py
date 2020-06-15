# Summary Ranges
# Array

# runtime: faster than 75.29% 
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        i = 0
        
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] == nums[j+1] - 1:
                j += 1
            if j == i:
                res.append(str(nums[i]))
            else:
                res.append('%s->%s' % (str(nums[i]), str(nums[j])))
            i = j + 1
        
        return res