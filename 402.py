# Remove K Digits
# stack

# https://blog.csdn.net/fuxuemingzhu/article/details/81034522
# runtime: faster than 59.29%
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        
        stack = []
        for i in num:
            while stack and k and int(stack[-1]) > int(i):
                stack.pop()
                k -= 1
            stack.append(i)
        
        while k:
            stack.pop()
            k -= 1
        
        if not stack:
            return '0'
        
        return str(int(''.join(stack)))
