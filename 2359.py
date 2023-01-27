# 2359. Find Closest Node to Given Two Nodes
# DFS / BFS

# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/solutions/2864716/find-closest-node-to-given-two-nodes/?orderBy=most_votes

# DFS
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dis1, dis2 = [math.inf] * n, [math.inf] * n
        dis1[node1] = 0
        dis2[node2] = 0
        visited1, visited2 = set(), set()


        def dfs(node, edges, dis, visited):
            visited.add(node)
            nx = edges[node]
            if nx != -1 and nx not in visited:
                dis[nx] = dis[node] + 1
                dfs(nx, edges, dis, visited)


        dfs(node1, edges, dis1, visited1)
        dfs(node2, edges, dis2, visited2)

        idx, minD = -1, math.inf
        for i in range(n):
            if max(dis1[i], dis2[i]) < minD:
                minD = max(dis1[i], dis2[i])
                idx = i
        
        return idx

# BFS
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dis1, dis2 = [math.inf] * n, [math.inf] * n

        def bfs(start, edges, dis):
            visited = set()
            queue = collections.deque()
            queue.append(start)
            dis[start] = 0

            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                nx = edges[node]
                if nx != -1 and nx not in visited:
                    dis[nx] = dis[node] + 1
                    queue.append(nx)


        bfs(node1, edges, dis1)
        bfs(node2, edges, dis2)

        idx, minD = -1, math.inf
        for i in range(n):
            if max(dis1[i], dis2[i]) < minD:
                minD = max(dis1[i], dis2[i])
                idx = i
        
        return idx