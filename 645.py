# 645. Set Mismatch
# Array / Hash Table

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = -1

        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                dup = abs(nums[i])
            else:
                nums[idx] *= -1
        
        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        
        return [dup, missing]



class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        dup = -1

        for num in nums:
            if num in s:
                dup = num
                break
            else:
                s.add(num)

        n = len(nums)
        total = (1 + n) * n // 2
        missing = dup + (total - sum(nums))

        return [dup, missing]