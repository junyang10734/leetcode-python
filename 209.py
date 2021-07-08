# 209. Minimum Size Subarray Sum
# Two Pointers

# runtime: O(n)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cnt = inf
        i, j = 0, 0
        s = 0
        while j < len(nums):
            s += nums[j]
            while s >= target:
                cnt = min(cnt, j-i+1)
                s -= nums[i]
                i += 1
            j += 1

        return cnt if cnt < inf else 0