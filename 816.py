# 816. Ambiguous Coordinates
# String

# https://leetcode.com/problems/ambiguous-coordinates/discuss/1205982/Python-product-solution-with-correct-complexity-explained
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(s):
            ans = []
            if s == '0' or s[0] != '0':
                ans.append(s)
            for i in range(1, len(s)):
                if (s[:i] == '0' or s[0] != '0') and s[-1] != '0':
                    ans.append(s[:i] + '.' + s[i:])
            return ans
        
        n, ans = len(s), []
        for i in range(2, n-1):
            left, right = make(s[1:i]), make(s[i:-1])
            for l, r in product(left, right):
                ans.append('(' + l + ', ' + r + ')')
        return ans