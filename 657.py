# Robot Return to Origin
# String

# runtime: faster than 67.69% 
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'L':0, 'R':0, 'U':0, 'D':0}
        for i in moves:
            d[i] += 1
        
        if d['L'] == d['R'] and d['U'] == d['D']:
            return True
        else:
            return False