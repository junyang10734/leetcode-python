# 1754. Largest Merge Of Two Strings

# String
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = ''
        
        while word1 and word2:
            idx = self.findDiff(word1, word2)
            if len(word1) >= len(word2):
                if word1[idx] >= word2[idx]:
                    res += word1[0]
                    word1 = word1[1:]      
                else:
                    res += word2[0]
                    word2 = word2[1:]
            else: 
                if word1[idx] > word2[idx]:
                    res += word1[0]
                    word1 = word1[1:]      
                else:
                    res += word2[0]
                    word2 = word2[1:]
        
        res += word1 if word1 else word2
        return res
    
    def findDiff(self, w1, w2):
        n = len(w1) if len(w1) <= len(w2) else len(w2)
        for i in range(n):
            if w1[i] != w2[i]:
                return i
        return n-1