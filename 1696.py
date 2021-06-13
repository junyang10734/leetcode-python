# 1696. Jump Game VI
# DP / Deque

# https://leetcode.com/problems/jump-game-vi/solution/
# runtime: O(n)
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        q = collections.deque([0])
        
        for i in range(1, n):
            while q and q[0] < i-k:
                q.popleft()
            dp[i] = dp[q[0]] + nums[i]
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            q.append(i)
            
        return dp[-1]        
