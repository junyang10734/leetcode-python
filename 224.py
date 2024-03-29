# 224. Basic Calculator
# 227 / 772
# Stack / Math

# 模板
class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0
            
            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = helper(s)
                
                if (not c.isdigit() and c != ' ') or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] *= num
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / float(num))
                    num = 0
                    sign = c
                
                if c == ')':
                    break
                    
            return sum(stack)
        
        return helper(collections.deque(s))
                    

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