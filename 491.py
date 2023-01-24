# 491. Non-decreasing Subsequences
# backtrack

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subarr = []
        res = set()

        def backtrack(index):
            if index == len(nums):
                if len(subarr) > 1:
                    res.add(tuple(subarr))
                return
            
            if not subarr or subarr[-1] <= nums[index]:
                subarr.append(nums[index])
                backtrack(index+1)
                subarr.pop()
            
            backtrack(index+1)
        
        backtrack(0)
        return list(res)
