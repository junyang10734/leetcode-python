# 84. Largest Rectangle in Histogram
# Stack / DaC


# https://leetcode.com/problems/largest-rectangle-in-histogram/solution/


# Better Brute Force
# runtime: O(n**2)
# TLE
class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area

# DaC
# runtime: O(nlogn)
# TLE
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def helper(heights, start, end):
            if start > end:
                return 0
            minIdx = start
            for i in range(start, end+1):
                if heights[minIdx] > heights[i]:
                    minIdx = i
            return max(heights[minIdx]*(end-start+1), helper(heights, start, minIdx-1), helper(heights, minIdx+1, end))
        
        return helper(heights, 0, len(heights)-1)


# Stack
# runtime: O(n)
class Solution3:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        mx = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                mx = max(mx, curr_height*curr_width)
            stack.append(i)
        
        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            mx = max(mx, curr_height*curr_width)
        return mx