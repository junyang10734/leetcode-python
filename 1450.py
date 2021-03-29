# 1405. Longest Happy String
# Greedy


# https://leetcode.com/problems/longest-happy-string/discuss/564248/Python-HEAP-solution-with-explanation
# runtime: faster than 58.91%
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:
            heappush(heap, (-a, 'a'))
        if b != 0:
            heappush(heap, (-b, 'b'))
        if c != 0:
            heappush(heap, (-c, 'c'))
        
        s = ''
        while heap:
            num1, char1 = heappop(heap)
            if len(s) >= 2 and s[-1] == s[-2] == char1:
                if not heap:
                    return s
                num2, char2 = heappop(heap)
                s += char2
                num2 += 1
                if num2 != 0:
                    heappush(heap, (num2, char2))
                heappush(heap, (num1, char1))
            else:
                s += char1
                num1 += 1
                if num1 != 0:
                    heappush(heap, (num1, char1))
        
        return s
