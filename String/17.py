# Letter Combinations of a Phone Number


# runtime: faster than 99.82%
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:   
        res1 = []
        res2 = []
        length = len(digits)
        for i in range(length):
            if len(res1) <= len(res2):
                res1 = self.combine(res2, digits[i])
            else:
                res2 = self.combine(res1, digits[i])
        
        return res1 if len(res1) >= len(res2) else res2
    
    
    def combine(self, l, d):
        letter = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        if len(l) == 0:
            return letter[d]
        else:
            r = []
            for item in l:
                for i in letter[d]:
                    newl = [item, i]
                    s = ''.join(newl)  # .join() is much faster than str+str
                    r.append(s)
            return r