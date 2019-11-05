# Rotate Array
# list operation, faster than 21.35%
class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k>0:
            a = nums[-1]
            nums.pop()
            nums.insert(0,a)
            k -= 1


# faster than 66.76%
# k may larger than len(nums)
# when k > len(nums), we only need to considerate k = k % len(nums)
# because when we rotate len(nums) steps, the array is the same as original array
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return 

        k %= len(nums)
        
        nums[:k], nums[k:] = nums[len(nums) - k:], nums[: len(nums) - k]