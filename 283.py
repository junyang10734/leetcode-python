# Move Zeroes

# faster than 19.29%
class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i>=0:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            i -= 1
        

# faster than 88.23%
class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[k] == 0:
                nums.append(0)
                del nums[k]
                k -= 1
            k += 1     