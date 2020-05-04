# Ransom Note
# String

# runtime: faster than 49.28%
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = collections.defaultdict(int)
        for i in magazine:
            d[i] += 1
        
        for j in ransomNote:
            if j not in d or d[j] < 1:
                return False
            else:
                d[j] -= 1
        
        return True