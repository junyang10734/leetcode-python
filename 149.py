# 149. Max Points on a Line
# Hash Table / Math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        
        res = 2
        for i in range(n):
            cnt = collections.defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                if points[j][0] == points[i][0]:
                    k = math.inf
                else:
                    k = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                cnt[k] += 1
            res = max(res, max(cnt.values())+1)

        return res
