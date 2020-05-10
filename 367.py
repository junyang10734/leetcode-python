# Valid Perfect Square &bigstar
# Math / Binary Search

# https://blog.csdn.net/fuxuemingzhu/article/details/71159714

# runtime: faster than 6.14%
# 完全平方式性质
class Solution1:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while num>0:
            num -= i
            i += 2
        return num == 0


# Time Limit Exceeded
# 暴力遍历
class Solution2:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(num//2+2):
                    if i*i == num:
                        return True
                return False


# runtime: faster than 9.50%
# binary search
class Solution3:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num+1
        while l<r:
            mid = l + (r-l)//2
            
            if mid*mid == num:
                return True
            elif mid*mid < num:
                l = mid + 1
            else:
                r = mid
        return False