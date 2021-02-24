# 120. Triangle
# DP

# https://blog.csdn.net/fuxuemingzhu/article/details/82883187
# runtime: faster than 86.10%
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[-1]
        for k in range(n-2, -1, -1):
            for i in range(k+1):
                dp[i] = min(dp[i], dp[i+1]) + triangle[k][i]
        return dp[0]


# modify in place
# runtime: faster than 68.43%
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        
        return min(triangle[-1])

        