# 1136. Parallel Courses
# Graph
# https://leetcode.com/problems/parallel-courses/solution/


# BFS
# runtime: faster than 98.62%
class Solution1:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n+1)}
        in_degree = {i:0 for i in range(1, n+1)}
        
        for a,b in relations:
            graph[a].append(b)
            in_degree[b] += 1
        
        queue = []
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
                
        res = 0
        studied = 0
        while queue:
            res += 1
            next_queue = []
            for node in queue:
                studied += 1
                end_nodes = graph[node]
                for node in end_nodes:
                    in_degree[node] -= 1
                    if in_degree[node] == 0:
                        next_queue.append(node)
            queue = next_queue
        
        return res if studied == n else -1


# DFS
# runtime: faster than 21.40% 
class Solution2:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n+1)}
        for a,b in relations:
            graph[a].append(b)
            
            
        visited = {}
        def checkCycle(node):
            if node in visited:
                return visited[node]
            else:
                visited[node] = -1
            for end_node in graph[node]:
                if checkCycle(end_node):
                    return True
            visited[node] = False
            return False
        
        for node in range(1, n+1):
            if checkCycle(node):
                return -1
        
        visited_length = {}
        def maxPath(node):
            if node in visited_length:
                return visited_length[node]
            max_length = 1
            for end_node in graph[node]:
                length = maxPath(end_node)
                max_length = max(length+1, max_length)
            visited_length[node] = max_length
            return max_length
        
        return max(maxPath(node) for node in range(1, n+1))
                    