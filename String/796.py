# Rotate String

# runtime: faster than 98.60% 
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A is None or B is None or len(A)!=len(B):
            return False
        else:
            s = A + A
            return True if s.find(B)!=-1 else False