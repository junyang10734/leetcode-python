# Unique Binary Search Trees
# Tree / DP


# https://blog.csdn.net/fuxuemingzhu/article/details/79367789

# recursive
# runtime: faster than 9.04%
class Solution1:
    def __init__(self):  # use this dictionary to reduce excute time
        self.dp = {}
        
    def numTrees(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n == 0 or n == 1:
            return 1
        
        ans = 0
        for i in range(1, n+1):
            ans += self.numTrees(i-1) * self.numTrees(n - i)
        self.dp[n] = ans
        
        return ans

# DP
# runtime: faster than 7.80%
class Solution2:
    def numTrees(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            count = 0
            for j in range(i):
                count += dp[j] * dp[i-j-1]
            dp.append(count)
        return dp[-1]