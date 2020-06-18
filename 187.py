# Repeated DNA Sequences
# String

# https://blog.csdn.net/fuxuemingzhu/article/details/83017233
# runtime: faster than 85.56% 
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        rep = set()
        for i in range(len(s)):
            cur = s[i: i+10]
            if cur in seen:
                rep.add(cur)
            else:
                seen.add(cur)
        return list(rep)
