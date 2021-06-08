# 752. Open the Lock
# BFS

# https://leetcode.com/problems/open-the-lock/solution/
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = collections.deque([('0000', 0)])
        visited = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            if node in deadends:
                continue

            for i in range(4):
                for d in [1, -1]:
                    nei = node[:i] + str((int(node[i]) + d) % 10) + node[i+1:]
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, depth+1))
        
        return -1
