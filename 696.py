# 696. Count Binary Substrings
# String

# https://leetcode.com/problems/count-binary-substrings/solution/

# Group By Character
# runtime: O(n)
class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        counts = []
        tmp, idx = s[0], 0
        for i in range(1, len(s)):
            if s[i] != tmp:
                counts.append(i-idx)
                tmp = s[i]
                idx = i
        
        counts.append(len(s)-idx)
        
        res = 0
        for i in range(len(counts)-1):
            res += min(counts[i], counts[i+1])

        return res