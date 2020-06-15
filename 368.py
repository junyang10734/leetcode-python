# Largest Divisible Subset
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/83027364
# runtime: faster than 68.72%
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        nums.sort()
        dp = [0] * n
        parent = [0] * n
        mx = 0
        mx_index = -1
        res = []
        
        for i in range(n):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > mx:
                        mx = dp[i]
                        mx_index = i
                        
        for k in range(mx+1):
            res.append(nums[mx_index])
            mx_index = parent[mx_index]
        
        return res[::-1]