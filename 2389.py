# 2389. Longest Subsequence With Limited Sum
# Array / Binary Search

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        res = []
        for query in queries:
            index = bisect.bisect_right(nums, query)
            res.append(index)
            
        return res
