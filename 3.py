# Longest Substring Without Repeating Characters

# runtime: faster than 20.85% 
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        maxlen = start = 0
        for i,item in enumerate(s):
            if item in dict:
                start = dict[item] + 1
                dict[item] = i
                delList = []
                for key in dict.keys():
                    if dict[key] < start:
                        delList.append(key)
                for val in delList:
                    del dict[val]
            else:
                dict[item] = i
                num = len(dict)
                if maxlen < num:
                    maxlen = num
        return maxlen


# https://www.youtube.com/watch?v=COVvQ9I7XyI
# runtime: faster than 85.79%
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlen = 0
        d = {}
        
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
                d[s[i]] = i
            else:
                d[s[i]] = i
                maxlen = max(i-start + 1, maxlen)
        return maxlen


# two points
# run time: faster than 31.48%
# https://blog.csdn.net/fuxuemingzhu/article/details/82022530
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        c = set()
        res = 0
        
        while left < len(s) and right < len(s):
            if s[right] in c:
                if s[left] in c:
                    c.remove(s[left])
                left += 1
            else:
                c.add(s[right])
                right += 1
                res = max(res, len(c))
        
        return res


# hash table
# run time: faster than 85.03%
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