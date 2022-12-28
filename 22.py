# Generate Parentheses
# backtrack

# Backtracking 模板
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ''
        self.backtrack(n, n, path, res)
        return res
    
    def backtrack(self, left, right, path, res):
        if left > right or left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            res.append(path)
            return
        
        path += '('
        self.backtrack(left-1, right, path, res)
        path = path[:-1]

        path += ')'
        self.backtrack(left, right-1, path, res)
        path = path[:-1]
        

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