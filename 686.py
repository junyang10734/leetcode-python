# 686. Repeated String Match
# String

# https://blog.csdn.net/fuxuemingzhu/article/details/79574835
# running time: faster than 5.10% 
class Solution1:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na, nb = len(a), len(b)
        times = 2 * math.ceil(nb / na) + 2

        for i in range(1, times):
            if b in a*i:
                return i
        return -1


# https://leetcode.com/problems/repeated-string-match/discuss/918623/Python-Solution..-Beat-99.54
# running time: faster than 96.10%
class Solution2:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0
        if set([ch for ch in b]) - set([ch for ch in a]):
            return -1
        
        for i in range(len(a)):
            match = True
            repeat = 1
            ai = i
            for bi in range(len(b)):
                if ai >= len(a):
                    ai -= len(a)
                    repeat += 1
                if a[ai] != b[bi]:
                    match = False
                    break
                ai += 1
            if match:
                return repeat
        
        return -1


# combine solution1 and solution2
# running time: faster than 96.10%
class Solution3:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not b:
            return 0
        if set([ch for ch in b]) - set([ch for ch in a]):
            return -1
        
        na, nb = len(a), len(b)
        times = 2 * math.ceil(nb / na) + 2

        for i in range(1, times):
            if b in a*i:
                return i
        return -1