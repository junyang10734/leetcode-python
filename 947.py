# 947. Most Stones Removed with Same Row or Column

# Union Find
# https://blog.csdn.net/fuxuemingzhu/article/details/84500642

# 两重循环
# running time: faster than 12.91%
class Solution1:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        self.map = [-1] * N
        
        for i in range(N):
            for j in range(i+1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    self.union(i, j)
        
        res = N

        for i in range(N):
            if self.map[i] == -1:
                res -= 1
        
        return res
    
    
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.map[fx] = fy
    
    def find(self, x):
        return x if self.map[x] == -1 else self.find(self.map[x])


# 一重循环
# running time: faster than 45.84%
class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        self.map = [-1] * 20000
        
        for x,y in stones:
            self.union(x, y+10000)
        
        return N - len({self.find(x) for x,y in stones})
    
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.map[fx] = fy
    
    def find(self, x):
        return x if self.map[x] == -1 else self.find(self.map[x])
