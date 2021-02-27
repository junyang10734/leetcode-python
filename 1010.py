# 1010. Pairs of Songs With Total Durations Divisible by 60
# Hash + Array

# Brute Force
# TLE
class Solution1:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1
        return res


# Hash
# runtime: faster than 10.57%
class Solution2:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = collections.defaultdict(int)
        arr = []
        for t in time:
            d[t] += 1
            if d[t] == 1:
                arr.append(t)
            
        res = 0
        n = len(arr)

        for i in range(n):
            if (2*arr[i]) % 60 == 0:
                res += d[arr[i]]*(d[arr[i]]-1)//2

            for j in range(i+1, n):
                if (arr[i] + arr[j]) % 60 == 0:
                    res += d[arr[i]] * d[arr[j]]

        return res

# O(n)
# runtime: faster than 74.48%
class Solution3:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int)
        res = 0
        for t in time:
            if t % 60 == 0:
                res += remainders[0]
            else:
                res += remainders[60 - t % 60]
            
            remainders[t % 60] += 1
        return res