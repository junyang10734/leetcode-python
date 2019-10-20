# Minimum Cost Tree From Leaf Values
# 该方法虽然可以计算出正确结果，但是Time Limit Exceeded
# 请参考贪心算法
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def dp(i,j):
            if j <= i:
                return 0
            else:
                return min(dp(i,k-1) + dp(k,j) + max(arr[i:k])*max(arr[k:j+1]) for k in range(i+1,j+1))
        return dp(0,len(arr)-1)