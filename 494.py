# Target Sum
# DP 背包问题

# https://blog.csdn.net/fuxuemingzhu/article/details/80484450
# runtime: faster than 79.06%
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = [ collections.defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        
        for k, v in enumerate(nums):
            for s,cnt in dp[k].items():
                dp[k+1][s+v] += cnt
                dp[k+1][s-v] += cnt
        
        return dp[len(nums)][S]


# DP 转化为背包问题
# https://labuladong.github.io/algo/di-er-zhan-a01c6/bei-bao-le-34bd4/dong-tai-g-35341/
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < abs(target) or (total + target) % 2 == 1:
            return 0
        
        # 计算 nums 中有几个子集的和为total
        total = (total + target) // 2
        n = len(nums)
        dp = [[0] * (total + 1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(total+1):
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]


# backtrack
# TLE
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0

        def backtrack(nums, i, remain):
            nonlocal res
            if i == len(nums):
                if remain == 0:
                    res += 1
                return

            # "-" for nums[i]
            remain += nums[i]
            backtrack(nums, i+1, remain)
            remain -= nums[i]

            # "+" for nums[i]
            remain -= nums[i]
            backtrack(nums, i+1, remain)
            remain -= nums[i]
        
        backtrack(nums, 0, target)
        return res
