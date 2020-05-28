# Partition Equal Subset Sum
# DP

# acwing.com/solution/LeetCode/content/8588/
# 0 - 1 backpack problem
# runtime: faster than 30.52%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_sum = sum(nums)
        if all_sum % 2 == 1:
            return False
        
        all_sum = all_sum//2
        n = len(nums)
        dp = [0]*(all_sum+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(all_sum, 0, -1):
                if j - nums[i-1] >= 0 and dp[j - nums[i-1]]:
                    dp[j] = 1
        
        return dp[-1]
