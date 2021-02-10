# 567. Permutation in String
# Hash / Slide Window
# same as 438

# runtime: faster than 68.29%
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ans = []
        m, n = len(s2), len(s1)
        
        if m < n:
            return False
        
        s1c = Counter(s1)
        s2c = Counter(s2[:n-1])
        
        for i in range(n-1, m):
            s2c[s2[i]] += 1
            if s1c == s2c:
                return True
            
            s2c[s2[i-n+1]] -= 1
            if s2c[s2[i-n+1]] == 0:
                del s2c[s2[i-n+1]]
            
        return False


# Sliding Window 
# 模板写法
# runtime: faster than 63.31%
class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs, window = collections.defaultdict(int), collections.defaultdict(int)
        for i in s1:
            needs[i] += 1
        
        left, right = 0, 0
        valid = 0
        
        while right < len(s2):
            c = s2[right]
            right += 1
            
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid += 1
            
            while right - left >= len(s1):
                if valid == len(needs):
                    return True
                d = s2[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        
        return False