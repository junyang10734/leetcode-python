# Partition Equal Subset Sum
# DP

# acwing.com/solution/LeetCode/content/8588/
# 0 - 1 backpack problem
# runtime: faster than 30.52%
class Solution1:
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


# https://blog.csdn.net/fuxuemingzhu/article/details/79787425
# runtime: TLE
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        div, mod = divmod(_sum, 2)
        if mod or max(nums) > div:
            return False
        nums.sort(reverse=True)
        target = [div] * 2
        return self.dfs(nums, 0, target)
    
    def dfs(self, nums, index, target):
        for i in range(2):
            if target[i] >= nums[index]:
                target[i] -= nums[index]
                if target[i] == 0 or self.dfs(nums, index+1, target):
                    return True
                target[i] += nums[index]
        return False
