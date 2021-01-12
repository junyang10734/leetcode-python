# Letter Combinations of a Phone Number


# runtime: faster than 99.82%
class Solution1:
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


# https://blog.csdn.net/fuxuemingzhu/article/details/79363119
# Backtrack
# running time: faster than 83.36% 
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        self.backtrack(digits, 0, res, '', phone)
        return res

    def backtrack(self, digits, index, res, path, phone):
        if index == len(digits):
            if path != '':
                res.append(path)
            return
        for i in phone[digits[index]]:
            self.backtrack(digits, index+1, res, path+i, phone)


# Circulation
# running time: faster than 58.77% 
class Solution3:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        phones = {'2' : "abc", '3' : "def", '4' : "ghi", '5' : "jkl", '6' : "mno", '7' : "pqrs", '8' : "tuv", '9' : "wxyz"}
        res = ['']
        for d in digits:
            res = [w+c for c in phones[d] for w in res]
        return res