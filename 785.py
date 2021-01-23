# 785. Is Graph Bipartite?


# DFS + 染色
# http://bookshadow.com/weblog/2018/02/18/leetcode-is-graph-bipartite/
# runtime: faster than 35.53%
class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        d = collections.defaultdict(list)
        for i,items in enumerate(graph):
            for n in items:
                d[i].append(n)
        
        colors = {}
        
        def dfs(k, c):
            new_c = 1 - c
            for p in d[k]:
                if p not in colors:
                    colors[p] = new_c
                    if not dfs(p, new_c):
                        return False
                elif colors[p] != new_c:
                    return False
            return True
            
        for k in d:
            if k in colors:
                continue
            colors[k] = 0
            if not dfs(k,0):
                return False
        
        return True



# BFS + 染色
# https://blog.csdn.net/fuxuemingzhu/article/details/82788401
# runtime: faster than 79.35%
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)  # 0: not visited, 1 - blue, 2 - red
        
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                visited[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    v = q.popleft()
                    for e in graph[v]:
                        if visited[e] != 0:
                            if visited[e] == visited[v]:
                                return False
                        else:
                            visited[e] = 3 - visited[v]
                            q.append(e)
        
        return True
        