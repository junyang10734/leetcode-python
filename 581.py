# Shortest Unsorted Continuous Subarray
# Array


# https://blog.csdn.net/fuxuemingzhu/article/details/79254454
# Sort
# runtime: faster than 87.30%
class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        if new_nums == nums:
            return 0
        
        diff = [i for i in range(len(nums)) if nums[i] != new_nums[i]]
        if diff:
            l = diff[0]
            r = diff[-1]
            return r - l + 1
        else:
            return 0


# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
# Stack
# running time:faster than 38.17% 
class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        N = len(nums)
        if N == 1:
            return 0
        l, r = N, 0
        
        for i in range(N):
            while stack and nums[i] < nums[stack[-1]]:
                l = min(l, stack.pop())
            stack.append(i)
        
        stack = []
        for i in range(N-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                r = max(r, stack.pop())
            stack.append(i)
        
        return r - l + 1 if r > l else 0
