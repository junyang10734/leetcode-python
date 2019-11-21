# K Closest Points to Origin

# sort
# run time: faster than 98.59% 
class Solution1:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda p:p[0]**2 + p[1]**2)
        return points[:K]


# heapq
# run time: faster than 75.95%
# https://blog.csdn.net/fuxuemingzhu/article/details/86425412
class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = []
        for p in points:
            d = p[0]**2 + p[1]**2
            dis.append((d,p))
        heapq.heapify(dis)
        
        res = [d[1] for d in heapq.nsmallest(K, dis)]
        return res