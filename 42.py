# 42. Trapping Rain Water
# Math / Stack / Two Pointers

# https://leetcode.com/problems/trapping-rain-water/solution/

# Math
# calculate the area
# runtime: faster than 40.75%
class Solution1:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        n = len(height)
        left, right = [0]*n, [0]*n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(height[i], left[i-1])
        right[n-1] = height[n-1]
        for j in range(n-2, -1, -1):
            right[j] = max(height[j], right[j+1])
        
        res = 0
        for i in range(n):
            res += min(left[i], right[i]) - height[i]
        return res


# Stack
# runtime: faster than 59.96%
class Solution2:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0
        
        res = current = 0
        stack = []
        while current < n:
            while stack and height[current] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                res += distance * bounded_height
            stack.append(current)
            current += 1
        return res



# Two Pointers
# runtime: faster than 80.81%
class Solution3:
        def trap(self, height: List[int]) -> int:
            left, right = 0, len(height) - 1
            l_max, r_max = 0, 0
            res = 0

            while left < right:
                l_max = max(l_max, height[left])
                r_max = max(r_max, height[right])

                if l_max < r_max:
                    res += l_max - height[left]
                    left += 1
                else:
                    res += r_max - height[right]
                    right -= 1
                    
            return res 