# 227. Basic Calculator II
# 224 / 772
# Stack

# 模板
class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            num = 0  #345  num = 3*10 + 4 = 34
            
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

