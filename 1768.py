# 1768. Merge Strings Alternately
# Two pointor / String

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        n1, n2 = len(word1), len(word2)
        k = min(n1, n2)
        for i in range(min(n1, n2)):
            res += word1[i] + word2[i]
        
        if n1 < n2:
            return res + word2[k:]
        elif n1 > n2:
            return res + word1[k:]
        else:
            return res