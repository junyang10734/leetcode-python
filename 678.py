# Valid Parenthesis String
# String / Greedy

# runtime: faster than 91.85%
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for i in s:
            if i == '(':
                lo += 1
            else:
                lo -= 1
            
            if i != ')':
                hi += 1
            else:
                hi -= 1
            
            if hi < 0:
                break
            lo = max(lo,0)
        
        return lo == 0
