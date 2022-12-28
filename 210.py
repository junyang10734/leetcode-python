# 210. Course Schedule II
# compare: 207, 802
# DFS

# https://blog.csdn.net/fuxuemingzhu/article/details/83302328


# DFS
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


# BFS - labuladong
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for i,j in prerequisites:
            graph[j].append(i)
            indegrees[i] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        res = [0] * numCourses
        count = 0
        while queue:
            node = queue.popleft()
            res[count] = node
            count += 1
            for nx in graph[node]:
                indegrees[nx] -= 1
                if indegrees[nx] == 0:
                    queue.append(nx)
        
        return res if count == numCourses else []