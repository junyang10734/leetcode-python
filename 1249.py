# 1249. Minimum Remove to Make Valid Parentheses
# Stack

# runtime: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0
        for i in s:
            if i == '(':
                count += 1
                stack.append(i)
            elif i == ')':
                if count > 0:
                    count -= 1
                    stack.append(i)
            else:
                stack.append(i)
        
        if count == 0:
            return ''.join(stack)
        else:
            res = ''
            for i in stack[::-1]:
                if i == '(' and count > 0:
                    count -= 1
                else:
                    res = i + res
            return res