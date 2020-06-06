# Queue Reconstruction by Height
# Greedy

# https://blog.csdn.net/fuxuemingzhu/article/details/68486884
# runtime: faster than 36.46% 
class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1],p)
        return res
        