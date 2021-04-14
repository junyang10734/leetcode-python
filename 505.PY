# 505. The Maze II
# DFS / BFS

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        M, N = len(maze), len(maze[0])
        q = [(0, start[0], start[1])]
        d = {(start[0], start[1]): 0}
        
        while q:
            path, r, c = heapq.heappop(q)
            if [r, c] == destination:
                return path
            
            for i,j in [(-1,0), (0,-1), (0,1), (1,0)]:
                dis = 0
                nr, nc = r, c
                while 0<=nr+i<M and 0 <= nc+j < N and maze[nr+i][nc+j] == 0:
                    dis += 1
                    nr += i
                    nc += j
                if (nr, nc) not in d or dis + path < d[(nr, nc)]:
                    d[(nr,nc)] = dis + path
                    heapq.heappush(q, (dis+path, nr, nc))
        return -1
                    