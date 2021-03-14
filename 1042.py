# 1042. Flower Planting With No Adjacent
# Graph / Graph Coloring

# https://blog.csdn.net/fuxuemingzhu/article/details/91357466
# runtime: faster than 94.97%
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0]*(n+1)
        graph = defaultdict(list)
        for a,b in paths:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1, n+1):
            nei_color = []
            for nei in graph[i]:
                nei_color.append(res[nei])
            for color in range(1, 5):
                if color not in nei_color:
                    res[i] = color
                    break
                    
        return res[1:]