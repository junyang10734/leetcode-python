# ZigZag Conversion
# String

# runtime: faster than 79.34% 
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        mul = 2 * numRows - 2
        res = [[] for _ in range(numRows)]
        
        for i in range(len(s)):
            x = i % mul
            y = x if x < numRows else (mul - x)
            res[y].append(s[i])
        
        ans = ''
        for i in res:
            ans += ''.join(i)
        
        return ans