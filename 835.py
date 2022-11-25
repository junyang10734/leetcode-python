# 835 Image Overlap
# Array / Matrix

# https://leetcode.com/problems/image-overlap/discuss/150504/Python-Easy-Logic
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a, b = [], []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    a.append((i, j))
                if img2[i][j] == 1:
                    b.append((i, j))
        
        d = collections.defaultdict(int)
        res = 0
        for t1 in a:
            for t2 in b:
                t3 = (t2[0]-t1[0], t2[1]-t1[1])
                d[t3] += 1
                res = max(res, d[t3])
        return res