# 890. Find and Replace Pattern
# String

# runtime: O(NK)  N: length of words list, K: length of pattern string
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isPattern(w1, w2):
            cnt1, cnt2 = {}, {}
            for l1, l2 in zip(w1, w2):
                if l1 in cnt1 and l2 in cnt2:
                    if cnt1[l1] == l2 and cnt2[l2] == l1:
                        continue
                    else:
                        return False
                elif l1 not in cnt1 and l2 not in cnt2:
                    cnt1[l1] = l2
                    cnt2[l2] = l1
                else:
                    return False
            return True
                
        res = []
        for word in words:
            if isPattern(word, pattern):
                res.append(word)
        return res