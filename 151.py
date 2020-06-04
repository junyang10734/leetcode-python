# Reverse Words in a String
# String

# runtime: faster than 92.93%
class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.split(' ')

        res = ''
        for i in range(len(sl)-1, -1, -1):
            if sl[i]:
                res += sl[i]
                res += ' '
        
        return res.strip()