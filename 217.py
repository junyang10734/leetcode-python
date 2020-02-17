# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        else:
            newNums = set(nums)

            if len(newNums) == len(nums):
                return False
            else:
                return True