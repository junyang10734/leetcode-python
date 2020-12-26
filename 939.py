# 939. Minimum Area Rectangle
# hash table
# https://leetcode.com/problems/minimum-area-rectangle/solution/

# running time: faster than 76.43%
# 遍历，先找x值相同的两个值，然后找是否有矩阵
class Solution1:
    def minAreaRect(self, points: List[List[int]]) -> int:
        cols = collections.defaultdict(list)
        for x,y in points:
            cols[x].append(y)
        
        lastx = {}
        ans = float('inf')

        for x in sorted(cols):
            col = cols[x]
            col.sort()

            for i,y1 in enumerate(col):
                for j in range(i):
                    y2 = col[j]
                    if (y2, y1) in lastx:
                        ans = min(ans, (x-lastx[y2,y1])*(y1-y2))
                    lastx[y2,y1] = x

        return ans if ans < float('inf') else 0


# running time: faster than 22.27%
# 遍历，先确定对角线两个点，然后查找矩形的另外两个点是否存在
class Solution2:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = float('inf')
        S = set(map(tuple, points))
        
        for i,p1 in enumerate(points):
            for j in range(i):
                p2 = points[j]

                if(p1[0] != p2[0] and p1[1] != p2[1] and (p1[0],p2[1]) in S and (p2[0],p1[1]) in S):
                    ans = min(ans, abs(p1[0]-p2[0])*abs(p1[1]-p2[1]))

        return ans if ans < float('inf') else 0