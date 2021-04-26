# 224. Basic Calculator
# Stack / Math

# https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
class Solution:
    def calculate(self, s: str) -> int:
        res, current, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                current = current * 10 + int(c)
            elif c == '-' or c == '+':
                res += sign * current
                current = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * current
                res *= stack.pop()
                res += stack.pop()
                current = 0
        return res + sign * current