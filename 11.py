# Container With Most Water

# two pointers
# runtime: faster than 47.39% 
# https://blog.csdn.net/fuxuemingzhu/article/details/82822939
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        area = 0
        while l < r:
            area = max(area, min(height[l], height[r])*(r-l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return area