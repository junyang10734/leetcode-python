# Evaluate Reverse Polish Notation

# run time: faster than 99.00% 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1+num2))
            elif i == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1-num2))
            elif i == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1*num2))
            elif i == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1/num2))
            else:
                stack.append(int(i))
        
        return stack[0]