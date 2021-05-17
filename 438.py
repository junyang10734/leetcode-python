# Find All Anagrams in a String
# Hash / Slide Window
# same as 567

# Sliding Window + Hash 计数
# https://leetcode.com/problems/find-all-anagrams-in-a-string/solution/
# runtime: O(ns + np)
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []
        
        p_count = collections.Counter(p)
        s_count = collections.Counter()
        res = []
        for i in range(ns):
            s_count[s[i]] += 1
            if i >= np:
                if s_count[s[i - np]] == 1:
                    del s_count[s[i - np]]
                else:
                    s_count[s[i - np]] -= 1
            
            if p_count == s_count:
                res.append(i - np + 1)
                
        return res


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