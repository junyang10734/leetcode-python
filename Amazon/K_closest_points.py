# leetcode 973: K Closest Points to Origin

# sort
# faster than 98.59%
class Solution1:
    def kClosest(points, K):
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]


# heapq
# faster than 75.95%
import heapq
class Solution2:
    def kClosest(points, K):
        dis = []
        for p in points:
            d = p[0] ** 2 + p[1] ** 2
            dis.append((d, p))
        heapq.heapify(dis)

        res = [d[1] for d in heapq.nsmallest(K, dis)]
        return res


if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    k = 1
    res1 = Solution1.kClosest(points, k)
    res2 = Solution2.kClosest(points, k)
    print(res1)
    print(res2)
