# Lexicographical Numbers
# Math

# https://blog.csdn.net/fuxuemingzhu/article/details/81776094
# runtime: 
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        cur = 1
        ans = []
        
        for i in range(n):
            ans.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10
        return ans