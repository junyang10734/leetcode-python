# 2348. Number of Zero-Filled Subarrays
# Array

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = []
        while left < len(nums) and right < len(nums):
            if nums[left] != 0:
                left += 1
            else:
                right = left
                while right < len(nums) and nums[right] == 0:
                    right += 1
                res.append(right - left)
                left = right + 1
        
        ans = 0
        for n in res:
            ans += (1+n) * n // 2
        return ans


# https://leetcode.com/problems/number-of-zero-filled-subarrays/solutions/2322338/two-pointers/?orderBy=most_votes
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 0:
                j = i + 1
            res += i - j + 1
            i += 1
        return res