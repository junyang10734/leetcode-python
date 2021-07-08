# Gray Code
# Math / Recursive

# https://leetcode.com/problems/gray-code/discuss/29893/One-liner-Python-solution-(with-demo-in-comments)
class Solution1:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x + pow(2, i) for x in reversed(res)]
        return res


# https://blog.csdn.net/fuxuemingzhu/article/details/80664204

# Math
# runtime: faster than 69.15%
class Solution2:
    def grayCode(self, n: int) -> List[int]:
        grays = dict()
        grays[0] = ['0']
        grays[1] = ['0','1']
        
        for i in range(2, n+1):
            n_gray = []
            for pre in grays[i-1]:
                n_gray.append('0'+pre)
            for pre in grays[i-1][::-1]:
                n_gray.append('1'+pre)
            grays[i] = n_gray
        
        return map(lambda x: int(x,2), grays[n])


# Recursive
# runtime: faster than 69.15%
class Solution3:
    def grayCode(self, n: int) -> List[int]:
        return map(lambda x:int(x,2), self.bit_gray(n))

    def bit_gray(self, n):
        ans = None
        if n == 0:
            ans = ['0']
        elif n == 1:
            ans = ['0', '1']
        else:
            pre_gray = self.bit_gray(n-1)
            ans = ['0' + x for x in pre_gray] + ['1' + x for x in pre_gray[::-1]]
        
        return ans