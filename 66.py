# Plus One
# Array

# runtime: O(n)
# sapce: O(1)
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        tmp = 1
        for i in range(n):
            if digits[n-1-i] + tmp < 10:
                digits[n-1-i] += tmp
                return digits
            else:
                tmp, digits[n-1-i] = divmod(digits[n-1-i] + tmp, 10)
        return [tmp] + digits if tmp > 0 else digits


# runtime: O(n)
# space: O(n)
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