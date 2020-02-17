# Missing Number

# hash
# faster than 30.71% 
class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """   
        list = [i for i in range(len(nums)+1)]
        newset = set(list) - set(nums)
        return (newset).pop()


# sort
# runtime: O(n)  faster than 15.78%
class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


# XOR
# runtime: O(n)  faster than 43.05%
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i^num
        return missing


# Gauss' Formula
# faster than 98.29%
class Solution4(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)*(len(nums)+1)/2
        b = sum(nums)
        return a - b