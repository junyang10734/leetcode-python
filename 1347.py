# 1347. Minimum Number of Steps to Make Two Strings Anagram
# String

# Counter
# runtime: faster than 91.58%
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1, cnt2 = collections.Counter(s), collections.Counter(t)
        common = 0
        for k,v in cnt1.items():
            if k in cnt2:
                common += min(v, cnt2[k])
        return len(s) - common