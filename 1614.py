# 1614. Maximum Nesting Depth of the Parentheses
# String

# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/discuss/888949/JavaC%2B%2BPython-Parentheses-Problem-Foundation
class Solution:
    def maxDepth(self, s: str) -> int:
        res = cur = 0
        for ch in s:
            if ch == '(':
                cur += 1
                res = max(res, cur)
            elif ch == ')':
                cur -= 1
        return res