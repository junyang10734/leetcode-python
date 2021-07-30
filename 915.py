# 915. Partition Array into Disjoint Intervals
# Array / Prefix

# https://leetcode.com/problems/partition-array-into-disjoint-intervals/solution/
# runtime: O(n)
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        maxLeft = [None] * N
        minRight = [None] * N
        
        tmp = nums[0]
        for i in range(N):
            tmp = max(tmp, nums[i])
            maxLeft[i] = tmp
        
        tmp = nums[-1]
        for i in range(N-1, -1, -1):
            tmp = min(tmp, nums[i])
            minRight[i] = tmp
        
        for i in range(1, N):
            if maxLeft[i-1] <= minRight[i]:
                return i