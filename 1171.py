# 1711. Count Good Meals

# Array / Hash
# running time: faster than 100.00%
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        nn = []
        for i in range(21):
            nn.append(2**i)

        d = collections.defaultdict(int)
        for i in deliciousness:
            d[i] += 1

        l = {}
        res = 0

        for num in d:
            if num in nn:
                res += ((d[num]*(d[num]-1))//2)
            for n in nn:
                if (n > num) and ((n-num) != num) and ((n-num) in d):
                    if (num, n-num) not in l and (n-num, num) not in l:
                        l[(num, n-num)] = 1
                        l[(n-num, num)] = 1
                        res += (d[num] * d[n-num])

        return res % (10**9 + 7)
