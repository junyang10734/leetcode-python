# Uncrossed Lines
# DP

# runtime: faster than 53.05% 
class Solution1:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[ 0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if A[i] == B[j]:
                        dp[i][j] = 1     
                elif i == 0:          
                    if A[i] == B[j]:
                        dp[i][j] = max(dp[i][j-1],1)
                    else:
                        dp[i][j] = dp[i][j-1]
                elif j == 0:
                    if A[i] == B[j]:
                        dp[i][j] = max(dp[i-1][j],1)
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    if A[i] == B[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]



# runtime: faster than 70.19% 
# simplify solution1
class Solution2:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m, n = len(A), len(B)
        dp = [[ 0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]