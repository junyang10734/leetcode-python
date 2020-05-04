# Backspace String Compare
# Two Points / Stack

# https://blog.csdn.net/fuxuemingzhu/article/details/80643408
# runtime: faster than 42.42%
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        res1, res2 = [], []
        
        for i in S:
            if i != '#':
                res1.append(i)
            elif res1:
                res1.pop()
        
        for j in T:
            if j != '#':
                res2.append(j)
            elif res2:
                res2.pop()
            
        return res1 == res2