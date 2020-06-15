# Multiply Strings
# String


# runtime: faster than 97.66% 
class Solution1:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))


# https://blog.csdn.net/fuxuemingzhu/article/details/80681702
# runtime: faster than 22.34%
class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        ans = 0
        for i,m in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j,n in enumerate(num1[::-1]):
                multi = (ord(m) - ord('0')) * (ord(n) - ord('0'))
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10**j)
                pre = first
            
            curr += pre * (10 ** len(num1))
            ans += curr * (10 ** i)
        
        return str(ans)