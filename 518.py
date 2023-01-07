# Coin Change 2
# DP 背包问题

# https://blog.csdn.net/fuxuemingzhu/article/details/82845212
class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(1, amount+1):
                if coin <= i:
                    dp[i] += dp[i - coin]
        
        return dp[amount]


# 和solution1思想一样
# dp数组不考虑空间压缩
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][j]: 若只使用 coins 中的前 i 个（i 从 1 开始计数）硬币的面值，若想凑出金额 j，有 dp[i][j] 种凑法
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]
