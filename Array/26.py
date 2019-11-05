# Remove Duplicates from Sorted Array
# note: do not allocate extra space for another array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        a = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[a]:
                a += 1
                nums[a] = nums[i]
        
        return a+1