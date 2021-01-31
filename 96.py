# 96. Unique Binary Search Trees
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


# https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247490696&idx=1&sn=798a350fcca16c89572caf65323dbec7&chksm=9bd7e280aca06b961613987e49b59cfc0faa67276b732c2ed664a8bb81daf8487a103ac0d0ce&cur_album_id=1318892385270808576&scene=189#rd
# recursive
# same as solution1, but easy to understand
class Solution2:
    def numTrees(self, n: int) -> int:
        self.dp = [[0] * (n+1) for _ in range(n+1)]
        return self.count(1, n)
    
    def count(self, lo, hi):
        if lo > hi:
            return 1
        
        if self.dp[lo][hi] != 0:
            return self.dp[lo][hi]
        
        res = 0
        for mid in range(lo, hi+1):
            left = self.count(lo, mid-1)
            right = self.count(mid+1, hi)
            res += left * right
        
        self.dp[lo][hi] = res
        
        return res   

# DP
# runtime: faster than 7.80%
class Solution3:
    def numTrees(self, n: int) -> int:
        dp = [1, 1]
        for i in range(2, n+1):
            count = 0
            for j in range(i):
                count += dp[j] * dp[i-j-1]
            dp.append(count)
        return dp[-1]
