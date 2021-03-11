# Course Schedule
# compare: 210, 802
# Graph

# https://blog.csdn.net/fuxuemingzhu/article/details/82951771

# BFS
# runtime: faster than 20.27%
class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegrees = collections.defaultdict(int)
        
        for i,j in prerequisites:
            graph[j].append(i)
            indegrees[i] += 1
        
        for m in range(numCourses):
            zeroDegree = False
            
            for n in range(numCourses):
                if indegrees[n] == 0:
                    zeroDegree = True
                    break
            
            if not zeroDegree:
                return False
            indegrees[n] = -1
            for node in graph[n]:
                indegrees[node] -= 1
        
        return True


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