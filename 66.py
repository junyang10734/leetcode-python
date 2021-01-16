# Plus One

# running time: faster than 67.55%
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return 1
        
        for i in range(len(digits)):
            digits[i] = str(digits[i])

        s = ''.join(digits)
        s = int(s)
        s = s + 1
        s = str(s)
        s = list(s)
        return s


# running time: faster than 67.55%
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        a = 1
        for i in range(len(digits)-1, -1, -1):
            if a == 1:
                if digits[i] == 9:
                    res.append(0)
                    a = 1
                else:
                    res.append(digits[i]+1)
                    a = 0
            else:
                res.append(digits[i])
        
        if a == 1:
            res.append(1)
        
        return res[::-1]