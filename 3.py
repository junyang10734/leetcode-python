# 3. Longest Substring Without Repeating Characters

# hash table / sliding window
# https://blog.csdn.net/fuxuemingzhu/article/details/82022530
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        d = {}
        res = 0
        
        while right<len(s):
            if s[right] in d:
                left = max(left,d[s[right]] + 1)
            
            d[s[right]] = right
            res = max(res, right-left+1)
            right += 1
        
        return res