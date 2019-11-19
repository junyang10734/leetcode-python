# Coin Change

# runtime: faster than 50.41%
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ (amount+1) for i in range(amount+1)]
        dp[0] = 0
        
        for i in range(1,len(dp)):
            for coin in coins:
                if coin<=i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] <= amount else -1