# 562. Longest Line of Consecutive One in Matrix
# Array

# runtime: O(mn)  m=len(M),n=len(M[0])
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        
        res = 0
        R, C = len(M), len(M[0])
        
        def getN(arr):
            arr = [str(a) for a in arr]
            s = ''.join(arr)
            arr = s.split('0')
            n = 0
            for a in arr:
                n = max(n, len(a))
            return n
        
        for i in range(R):
            arr = M[i]
            res = max(res, getN(arr))
            
        for j in range(C):
            arr = []
            for i in range(R):
                arr.append(M[i][j])
            res = max(res, getN(arr))
        
        for j in range(C):
            i = 0
            arr = []
            while i < R and j >= 0:
                arr.append(M[i][j])
                i += 1
                j -= 1
            res = max(res, getN(arr))
                   
        for i in range(1, R):
            j = C - 1
            arr = []
            while i < R and j >= 0:
                arr.append(M[i][j])
                i += 1
                j -= 1
            res = max(res, getN(arr))
        
        for j in range(C):
            i = 0
            arr = []
            while i < R and j < C:
                arr.append(M[i][j])
                i += 1
                j += 1
            res = max(res, getN(arr))
        
        for i in range(1, R):
            j = 0
            arr = []
            while i < R and j < C:
                arr.append(M[i][j])
                i += 1
                j += 1
            res = max(res, getN(arr))
           
        return res
            

# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/discuss/102275/Python-Simple-with-Explanation
class Solution2:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        
        def score(arr):
            ans = count = 0
            for a in arr:
                if a:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
            return ans
        
        groups = collections.defaultdict(list)
        for i,row in enumerate(M):
            for j,v in enumerate(row):
                groups[0, i] += [v]
                groups[1, j] += [v]
                groups[2, i+j] += [v]
                groups[3, i-j] += [v]

        return max(map(score, groups.values()))
        