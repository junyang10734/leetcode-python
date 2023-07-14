# 1493. Longest Subarray of 1's After Deleting One Element
# Sliding window

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        sliding = 0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1
            
            sliding = max(sliding, i - start)

        return sliding