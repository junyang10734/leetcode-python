# Sqrt(x)

# easy to understand, but time limit exceeded
class Solution1:
    def mySqrt(self, x: int) -> int:
        dic = {0:0,1:1,2:1,3:1,4:2}
        if x<5:
            return dic[x]
        
        i = 0
        flag = 0
        while i <= x//2 + 1:
            if i*i > x:
                flag = i -1
                break
            elif i*i == x:
                flag = i
                break
            else:
                i += 1
        
        return flag


# Binary Search
class Solution2:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = (left+right)//2
            if mid*mid <= x:
                left = mid + 1
            else:
                right = mid - 1
        
        return int(left-1)