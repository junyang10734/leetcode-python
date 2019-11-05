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