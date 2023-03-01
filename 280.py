# 280. Wiggle Sort
# Sorting / Greedy

# https://leetcode.com/problems/wiggle-sort/solutions/2961467/wiggle-sort/


# Sorting
# time: O(nlogn)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]


# Greedy
# time: O(n)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if ((i % 2 == 0) and (nums[i] > nums[i+1])) or ((i % 2 == 1) and (nums[i] < nums[i+1])):
                nums[i], nums[i+1] = nums[i+1], nums[i]