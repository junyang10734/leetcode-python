# 841. Keys and Rooms
# DFS

# https://blog.csdn.net/fuxuemingzhu/article/details/80476862
# DFS
# running time: faster than 91.69%
class Solution1:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        self.dfs(rooms, 0, visited)
        return sum(visited) == len(rooms)
    
    def dfs(self, rooms, index, visited):
        visited[index] = 1
        for item in rooms[index]:
            if not visited[item]:
                self.dfs(rooms, item, visited)


# https://leetcode.com/problems/keys-and-rooms/solution/
# DFS with stack
# running time: faster than 76.38%
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]
        
        while stack:
            node = stack.pop()
            for i in rooms[node]:
                if not visited[i]:
                    visited[i] = True
                    stack.append(i)
        
        return all(visited)
