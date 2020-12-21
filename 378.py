# 378. Kth Smallest Element in a Sorted Matrix
# http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/

# stack / heap
# running time: faster than 39.51% 
class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = 0
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i+1 < m:
                heapq.heappush(q,(matrix[i+1][j], i+1, j))
            if j+1 < n:
                heapq.heappush(q,(matrix[i][j+1], i, j+1))
        
        return ans


# binary search
# running time: faster than 89.49% 
class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, h = matrix[0][0], matrix[-1][-1]
        while l <= h:
            mid = l + (h - l)//2
            loc = sum(bisect.bisect_right(m,mid) for m in matrix)
            if loc >= k:
                h = mid - 1
            else:
                l = mid + 1
        return l