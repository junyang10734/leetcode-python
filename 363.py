# 363. Max Sum of Rectangle No Larger Than K
# Array / Ordered Set / Binary Search / Prefix

# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/1312722/Python-Two-solutions-explained
# runtime: O(m^2*n log n)
class Solution1:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        from sortedcontainers import SortedSet
        def maxSum(arr):
            ans = -inf
            total = 0
            s = SortedSet([0])
            for n in arr:
                total += n
                idx = bisect_left(s, total - k)
                if idx != len(s):
                    ans = max(total - s[idx], ans)
                s.add(total)
            return ans
        
    
        res = -inf
        m, n = len(matrix), len(matrix[0])
        for i, j in product(range(1, m), range(n)):
            matrix[i][j] += matrix[i-1][j]
        matrix = [[0]*n] + matrix
        for r1,r2 in combinations(range(m+1), 2):
            rowSum = [j - i for i,j in zip(matrix[r1], matrix[r2])]
            res = max(maxSum(rowSum), res)
            if res == k:
                return res
                
        return res


# https://blog.csdn.net/fuxuemingzhu/article/details/83014580
# runtime: O(m^2*n log n)  优化了时间
class Solution2:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        
        M = max(m, n)
        N = min(m, n)
        ans = -inf
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                slist, num = [], 0
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k:
                        ans = max(ans, num)
                    i = bisect.bisect_left(slist, num - k)
                    if i != len(slist):
                        ans = max(ans, num - slist[i])
                    bisect.insort(slist, num)
        return ans
