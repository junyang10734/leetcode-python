# 76. Minimum Window Substring
# Sliding Window

# https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/shou-ba-shou-shua-shu-zu-ti-mu/hua-dong-chuang-kou-ji-qiao-jin-jie
# runtime: faster than 98.98%
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs, window = collections.defaultdict(int), collections.defaultdict(int)
        for i in t:
            needs[i] += 1
        
        left, right = 0, 0
        valid = 0
        start = 0
        num = 100001
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1
            while valid == len(needs):
                if right - left < num:
                    start = left
                    num = right - left
                
                d = s[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        
        return '' if num == 100001 else s[start:start+num]