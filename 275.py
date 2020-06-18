# H-Index II
# Array

# runtime: faster than 60.72% 
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n-1
        h = 0
        
        while l <= r:
            mid = l + (r - l) // 2
            h = max(h, min(citations[mid], n-mid))
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid - 1
        return h