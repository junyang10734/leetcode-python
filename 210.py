# 210. Course Schedule II
# DFS

# https://blog.csdn.net/fuxuemingzhu/article/details/83302328
# running time: faster than 84.44% 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i, path):
                return []
        return path
        
    
    def dfs(self, graph, visited, i, path):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, path):
                return False
        visited[i] = 2
        path.append(i)
        return True