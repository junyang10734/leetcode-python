# 916. Word Subsets
# String

# https://leetcode.com/problems/word-subsets/solution/
# runtime: faster than 21.66%
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0]*26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans
        
        bmax = [0]*26
        for b in B:
            for i,c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)
        
        res = []
        for a in A:
            if all(x>=y for x,y in zip(count(a), bmax)):
                res.append(a)
        return res