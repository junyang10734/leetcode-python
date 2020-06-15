# Keyboard Row
# Hash Table

# runtime: faster than 46.17%
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d = {}
        
        for i in "qwertyuiopQWERTYUIOP":
            d[i] = 1
        for i in "asdfghjklASDFGHJKL":
            d[i] = 2
        for i in "zxcvbnmZXCVBNM":
            d[i] = 3
        
        res = []
        for w in words:
            if len(set(d[i] for i in w)) == 1:
                res.append(w)
        return res