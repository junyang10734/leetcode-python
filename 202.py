# Happy Number

# run time: TLE
class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = {}
        
        while True:
            d[n] = True
            sum = 0
            while n>0:
                sum += (n%10)**2
                n /= 10
            if sum == 1:
                return True
            elif sum in d:
                return False
            else:
                n = sum


# https://leetcode.com/problems/happy-number/discuss/56915/My-Python-Solution
# runtime: faster than 25.51% 
class Solution2:
    def isHappy(self, n: int) -> bool:
        happySet = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in happySet:
                return False
            else:
                happySet.add(n)
        return True


# runtime: faster than 99.70% 
# https://blog.csdn.net/coder_orz/article/details/51315486
class Solution3:
    def isHappy(self, n: int) -> bool:
        happySet = set([1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97])

        while n>99:
            n = sum([int(x) * int(x) for x in list(str(n))])
        return n in happySet