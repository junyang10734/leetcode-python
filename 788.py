# 788. Rotated Digits
# String

# running time: faster than 60.08%
class Solution1:
    def rotatedDigits(self, N: int) -> int:
        valid = ['2', '5', '6', '9']
        invalid = ['3', '4', '7']          
        def isGood(num):
            num = str(num)
            flag = False
            for n in num:
                if n in invalid:
                    return False
                if n in valid:
                    flag = True
            return flag
            
        res = 0
        for num in range(1, N+1):
            if(isGood(num)):
                res += 1
            
        return res


# https://blog.csdn.net/fuxuemingzhu/article/details/79378135

# running time: faster than 23.98%
class Solution2:
    def rotatedDigits(self, N: int) -> int:
        valid = [2, 5, 6, 9]
        nonValid = [3, 4, 7]
        def isGood(num):
            for y in nonValid:
                if str(y) in str(num):
                    return False
            return any(str(x) in str(num) for x in valid)
        return sum(map(int, [isGood(n) for n in range(1, N + 1)]))


# running time: faster than 22.79%
class Solution3:
    def rotatedDigits(self, N: int) -> int:        
        res = 0
        for num in range(1, N+1):
            if any(x in str(num) for x in ["3","4","7"]):
                continue
            if any(x in str(num) for x in ["2","5","6","9"]):
                res += 1
        return res