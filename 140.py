# 140. Word Break II
# Recursive / Backtrack

# https://blog.csdn.net/fuxuemingzhu/article/details/85089275
# runtime: faster than 38.87%
class Solution1:
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


# https://zxi.mytechroad.com/blog/leetcode/leetcode-140-word-break-ii/
# runtime: faster than 75.24%
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = {}
        
        def helper(s):
            if s in d:
                return d[s]
            res = []
            if s in wordDict:
                res.append(s)
            for i in range(1, len(s)):
                right = s[i:]
                if right in wordDict:
                    res += [w + ' ' + right for w in helper(s[:i])]
            d[s] = res
            return d[s]
        
        return helper(s)
