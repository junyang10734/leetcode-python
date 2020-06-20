# Permutation Sequence
# Math

# https://blog.csdn.net/fuxuemingzhu/article/details/80658810
# runtime: faster than 59.88% 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ''
        f = [1]*n
        num = [str(i) for i in range(1, 10)]
        
        for i in range(1, n):
            f[i] = f[i-1] * i
        
        k -= 1
        for i in range(n, 0, -1):
            a = k // f[i-1]
            k %= f[i-1]
            ans += num[a]
            num.pop(a)
        
        return ans