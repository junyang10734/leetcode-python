# Find All Anagrams in a String
# Hash / Slide Window
# same as 567

# Sliding Window + Hash 计数
# https://blog.csdn.net/fuxuemingzhu/article/details/79184109
# runtime: faster than 39.11%
class Solution1:
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


# Sliding Window 模板
# https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/shou-ba-shou-shua-shu-zu-ti-mu/hua-dong-chuang-kou-ji-qiao-jin-jie
# runtime: faster than 74.94%
class Solution2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needs, window = collections.defaultdict(int), collections.defaultdict(int)
        for i in p:
            needs[i] += 1
        
        left, right = 0, 0
        valid = 0
        res = []
        
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in needs:
                window[c] += 1
                if needs[c] == window[c]:
                    valid += 1
            
            while right - left >= len(p):
                if valid == len(needs):
                    res.append(left)
                
                d = s[left]
                left += 1
                
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        
        return res