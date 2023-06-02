# 2101. Detonate the Maximum Bombs
# DFS

# Depth-First Search, Recursive
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            for nxt in graph[node]:
                if nxt not in visited:
                    dfs(nxt, visited)
            return len(visited)
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i, set()))
        return res


# Depth-First Search, Iterative
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)
        
        def dfs(i):
            stack = [i]
            visited = set([i])
            while stack:
                cur = stack.pop()
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)
            return len(visited)
        
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
        return res


# BFS
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)
        
        def bfs(i):
            queue = collections.deque([i])
            visited = set([i])
            while queue:
                cur = queue.popleft()
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            return len(visited)
        
        res = 0
        for i in range(n):
            res = max(res, bfs(i))
        return res