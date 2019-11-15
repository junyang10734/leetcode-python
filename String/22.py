# Generate Parentheses

# Brute Force
# runtime: faster than 5.20%
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    res.append(''.join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()
                
        def valid(A):
            bal = 0
            for c in A:
                if c == '(': 
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
        
        res = []
        generate()
        return res


# Backtracking
# runtime: faster than 99.97%
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2*n:
                res.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
                
        backtrack()
        return res