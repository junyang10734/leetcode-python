# 869. Reordered Power of 2
# Math

# runtime: faster than 16.13%
class Solution1:
    def reorderedPowerOf2(self, N: int) -> bool:
        for num in itertools.permutations(str(N), len(str(N))):
            num = ''.join(num)
            if num[0] != '0':
                num = int(num)
                if (num & (num-1) == 0) and num != 0:
                    return True
        return False


# https://leetcode.com/problems/reordered-power-of-2/solution/
# runtime: faster than 11.29%
class Solution2:
    def reorderedPowerOf2(self, N: int) -> bool:
        for num in itertools.permutations(str(N)):
            num = ''.join(num)
            if num[0] != '0' and bin(int(num)).count('1') == 1:
                return True
        return False


# https://blog.csdn.net/fuxuemingzhu/article/details/82468653
# Counter
# runtime: faster than 81.85%
class Solution3:
    def reorderedPowerOf2(self, N: int) -> bool:
        cnt = collections.Counter(str(N))
        return any(cnt == collections.Counter(str(1 << i)) for i in range(32))

