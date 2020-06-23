# Additive Number
# String

# https://blog.csdn.net/fuxuemingzhu/article/details/80661715
# BackTracking
# runtime: faster than 92.90%
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.dfs(num, [])
    
    def dfs(self, num, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num and len(path) >= 3:
            return True
        
        for i in range(len(num)):
            curr = num[:i+1]
            if (curr[0] == '0' and len(curr) != 1):
                continue
            if self.dfs(num[i+1:], path + [int(curr)]):
                return True
        
        return False
