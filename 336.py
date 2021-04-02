# 336. Palindrome Pairs
# String

# https://leetcode.com/problems/palindrome-pairs/solution/

# runtime: faster than 68.81%
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def prefix(word):
            prefix = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    prefix.append(word[:i])
            return prefix
        
        def suffix(word):
            suffix = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    suffix.append(word[i+1:])
            return suffix
        
        d = {word : i for i,word in enumerate(words)}
        res = []
        
        for idx,word in enumerate(words):
            reversed_word = word[::-1]
            if reversed_word in d and idx != d[reversed_word]:
                res.append([idx, d[reversed_word]])
        
            for pre in prefix(word):
                reversed_pre = pre[::-1]
                if reversed_pre in d and idx != d[reversed_pre]:
                    res.append([idx, d[reversed_pre]])
            
            for suf in suffix(word):
                reversed_suf = suf[::-1]
                if reversed_suf in d and idx != d[reversed_suf]:
                    res.append([d[reversed_suf], idx])
        
        return res
        