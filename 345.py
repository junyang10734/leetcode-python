# Reverse Vowels of a String
# String

# https://blog.csdn.net/fuxuemingzhu/article/details/51291677

# stack
# runtime: faster than 88.56%
class Solution1:
    def reverseVowels(self, s: str) -> str:
        l = []
        v = 'aeiouAEIOU'
        
        for i in s:
            if i in v:
                l.append(i)
        
        res = []
        for i in s:
            if i in v:
                res.append(l.pop())
            else:
                res.append(i)
        
        return ''.join(res)


# two pointers
# runtime: faster than 98.65% 
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        v = 'aeiouAEIOU'
        res = list(s)
        l, r = 0, n - 1
        while l < r:
            while r >= 0 and res[r] not in v:
                r -= 1
            while l < r and res[l] not in v:
                l += 1
            if l < r:
                res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        return ''.join(res)
