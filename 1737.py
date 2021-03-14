# 1737. Change Minimum Characters to Satisfy One of Three Conditions
# String

# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/discuss/1032070/JavaC%2B%2BPython-Clean-Solution
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n  = len(a), len(b)
        cnt1 = Counter(ord(c) - ord('a') for c in a)
        cnt2 = Counter(ord(c) - ord('a') for c in b)
        res = m + n - max((cnt1+cnt2).values())  #condition3
        
        for i in range(25):
            cnt1[i+1] += cnt1[i]
            cnt2[i+1] += cnt2[i]
            res = min(res, m-cnt1[i]+cnt2[i])  # condition1
            res = min(res, n-cnt2[i]+cnt1[i])  # condition2

        return res