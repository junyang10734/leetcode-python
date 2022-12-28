# Course Schedule
# compare: 210, 802
# Graph

# https://blog.csdn.net/fuxuemingzhu/article/details/82951771

# BFS - labuladong
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        for i,j in prerequisites:
            graph[i].append(j)
            indegrees[j] += 1
        
        queue = collections.deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nx in graph[node]:
                indegrees[nx] -= 1
                if indegrees[nx] == 0:
                    queue.append(nx)
        
        return count == numCourses


# DFS
# runtime: faster than 97.15%
# visited[i] == 0，还没判断这个点；
# visited[i] == 1，当前的循环正在判断这个点；
# visited[i] == 2，已经判断过这个点，含义是从这个点往后的所有路径都没有环，认为这个点是安全的
class Solution2:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        
        for i,j in prerequisites:
            graph[i].append(j)
        
        visited = [0] * numCourses
        
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    
    def dfs(self, graph, visited, i):
        if visited[i] == 1:
            return False
        if visited[i] == 2:
            return True
        visited[i] = 1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 2
        
        return True