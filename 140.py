# 140. Word Break II
# Recursive / Backtrack

# https://blog.csdn.net/fuxuemingzhu/article/details/85089275
# runtime: faster than 38.87%
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        d = {}
        return self.dfs(s, res, wordDict, d)
    
    def dfs(self, s, res, wordDict, d):
        if s in d:
            return d[s]
        if not s:
            return ['']
        
        res = []
        for word in wordDict:
            if s[:len(word)] != word:
                continue
            for r in self.dfs(s[len(word):], res, wordDict, d):
                res.append(word + ('' if not r else ' ' + r))
        d[s] = res
        return res
