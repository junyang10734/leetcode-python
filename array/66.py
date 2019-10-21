# Plus One
class Solution:
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