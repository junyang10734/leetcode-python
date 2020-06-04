# Add Digits
# Math


# runtime: faster than 95.59% 
class Solution1:
    def addDigits(self, num: int) -> int:
        res = 0
        
        while num > 0:
            res += num % 10
            num = num // 10
            
            if num == 0 and res > 9:
                num = res
                res = 0
        
        return res


# runtime: faster than 84.39% 
class Solution2:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


# runtime: faster than 59.71% 
class Solution3:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0