# 1059. All Paths from Source Lead to Destination
# DFS

# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/discuss/310527/Python-or-DFS
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(set)
        visited = {}
        for a,b in edges:
            graph[a].add(b)
        
        def dfs(node):
            if len(graph[node]) == 0:
                return node == destination
            
            if node in visited:
                if visited[node] == 1:
                    return True
                elif visited[node] == -1:
                    return False
            else:
                visited[node] = -1
                for nxt in graph[node]:
                    if not dfs(nxt):
                        return False
                visited[node] = 1
                return True
        
        return dfs(source)
