# 953. Verifying an Alien Dictionary
# Hash Table

# runtime: faster than 9.04%
class Solution1:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for w1,w2 in zip(words, words[1:]):
            if w1 == w2:
                continue
            n1, n2 = len(w1), len(w2)
            if n2 < n1 and w1[:n2] == w2:
                return False
            for s1,s2 in zip(w1, w2):
                if s1 == s2:
                    continue
                if s1 not in d:
                    t1 = order.find(s1)
                    d[s1] = t1
                if s2 not in d:
                    t2 = order.find(s2)
                    d[s2] = t2
                if d[s1] > d[s2]:
                    return False
                elif d[s1] < d[s2]:
                    break
        
        return True
                    

# https://leetcode.com/problems/verifying-an-alien-dictionary/solution/
# runtime: faster than 18.63%
class Solution2:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i,o in enumerate(order):
            d[o] = i
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if d[words[i][j]] > d[words[i+1][j]]:
                        return False
                    break
        
        return True


# https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order
# runtime: faster than 18.63%
class Solution3:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))