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


# runtime: faster than 92.98%
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key = lambda x:1 if x == 0 else 0)


class Solution4:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0


# Compare with 26, 27
class Solution4:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        for i in range(slow, len(nums)):
            nums[i] = 0
        