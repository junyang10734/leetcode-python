# Find All Anagrams in a String
# Hash / Slide Window
# same as 567

# https://blog.csdn.net/fuxuemingzhu/article/details/79184109
# runtime: faster than 39.11%
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        m, n = len(s), len(p)
        
        if m < n:
            return ans
        
        pc = Counter(p)
        ps = Counter(s[:n-1])
        
        for idx in range(n-1, m):
            ps[s[idx]] += 1
            if ps == pc:
                ans.append(idx-n+1)
            ps[s[idx-n+1]] -= 1
            if ps[s[idx-n+1]] == 0:
                del ps[s[idx-n+1]]
        
        return ans