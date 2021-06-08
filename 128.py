# 128. Longest Consecutive Sequence
# Hash Set

# https://leetcode.com/problems/longest-consecutive-sequence/solution/
# runtime: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                cur_num = num
                cur_length = 1
                
                while cur_num + 1 in nums:
                    cur_num += 1
                    cur_length += 1
                
                res = max(res, cur_length)
        return res