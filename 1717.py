#  
# Greedy / Stack

# runtime: faster than 53.12%
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        p1, p2 = 'ab', 'ba'
        if x < y:
            p1, p2 = p2, p1
            x, y = y, x
        
        s, res1 = self.remove(s, x, p1)
        s, res2 = self.remove(s, y, p2)
        return res1 + res2
    
    def remove(self, s, x, p):
        stack = []
        res = 0
        for n in s:
            if len(stack) > 0 and n == p[1] and stack[-1] == p[0]:
                    stack.pop()
                    res += x
                    continue
            stack.append(n)
            
        return ''.join(stack), res