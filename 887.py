# 887. Super Egg Drop
# DP

# labuladong
# DP + Dictionary
# TLE, easy to understand
class Solution1:
    def superEggDrop(self, K: int, N: int) -> int:
        d = {}
        
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
        
            if (K,N) in d:
                return d[(K,N)]
            
            res = float('inf')
            for i in range(1, N+1):
                res = min(res, max(dp(K-1, i-1), dp(K, N-i)) + 1)
            d[(K,N)] = res
            return res

        return dp(K, N)


# labuladong
# DP + Dictionary + Binary Search
# runtime: faster than 9.60%
class Solution2:
    def superEggDrop(self, K: int, N: int) -> int:
        d = {}
        
        def dp(K, N):
            if K == 1:
                return N
            if N == 0:
                return 0
        
            if (K,N) in d:
                return d[(K,N)]
            
            res = float('inf')
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            
            d[(K,N)] = res
            return res

        return dp(K, N)


# labuladong
# runtime: faster than 77.06%
# dp[k][m] = n
# 当前有 k 个鸡蛋，可以尝试扔 m 次鸡蛋
# 这个状态下，最坏情况下最多能确切测试一栋 n 层的楼
# 比如说 dp[1][7] = 7 表示：
# 现在有 1 个鸡蛋，允许你扔 7 次;
# 这个状态下最多给你 7 层楼，
# 使得你可以确定楼层 F 使得鸡蛋恰好摔不碎
# （一层一层线性探查嘛）
# dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1
# dp[k][m - 1]就是楼上的楼层数，因为鸡蛋个数k不变，也就是鸡蛋没碎，扔鸡蛋次数m减一；
# dp[k - 1][m - 1]就是楼下的楼层数，因为鸡蛋个数k减一，也就是鸡蛋碎了，同时扔鸡蛋次数m减一。
class Solution3:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0]*(N+1) for _ in range(K+1)]
        cnt = 0
        while dp[K][cnt] < N:
            cnt += 1
            for k in range(1, K+1):
                dp[k][cnt] = dp[k][cnt - 1] + dp[k-1][cnt - 1] + 1
        return cnt
