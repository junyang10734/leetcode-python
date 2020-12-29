# 524. Longest Word in Dictionary through Deleting
# String / Array

# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/solution/
# running time: faster than 38.21%
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        max_str = ''
        
        for i in d:
            if(self.isSubstr(i, s)):
                if len(i) > len(max_str) or (len(i) == len(max_str) and i < max_str):
                    max_str = i
        
        return max_str
    
    
    def isSubstr(self, x, y):
        i, j = 0, 0
        while (i < len(x) and j < len(y)):
            if x[i] == y[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(x)
