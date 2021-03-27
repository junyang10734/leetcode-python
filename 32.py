# 32. Longest Valid Parentheses
# String / Stack

# https://leetcode.com/problems/longest-valid-parentheses/discuss/514247/eight-lines-python-no-dp-needed
# runtime: faster than 47.92%
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [(')', -1)]
        res = 0
        for i in range(len(s)):
            if s[i] == ')' and stack[-1][0] == '(':
                stack.pop()
                res = max(res, i-stack[-1][1])
            else:
                stack.append((s[i], i))
        return res
