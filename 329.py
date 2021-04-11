# 329. Longest Increasing Path in a Matrix
# Graph

# BFS + Memorize
# runtime: O(mn)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        arr = []
        res = 1
        for i in range(M):
            for j in range(N):
                arr.append([i,j,matrix[i][j]])

        arr.sort(key=lambda x:(-x[2]))
        cache = [[-1]*N for _ in range(M)]
        mx = arr[0][2]
        idx = 0
        while idx < len(arr) and arr[idx][2] == mx:
            cache[arr[idx][0]][arr[idx][1]] = 1
            idx += 1
        
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for idx,t in enumerate(arr[idx:]):
            tmp = -1
            x,y,v = t[0], t[1], t[2]
            for di,dj in dirs:
                new_x, new_y = x + di, y + dj
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]) and matrix[new_x][new_y] > v and cache[new_x][new_y] > 0:
                    tmp = max(tmp, cache[new_x][new_y] + 1)
            
            if tmp == -1:
                tmp = self.getLength(x, y, matrix)

            cache[x][y] = tmp
            res = max(res, tmp)
        
        return res
    
    def getLength(self, i, j, matrix):
        stack = [(i,j,1)]
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        res = 1
        while stack:
            x, y, depth = stack.pop(0)
            for di,dj in dirs:
                new_x, new_y = x + di, y + dj
                if 0 <= new_x < len(matrix) and 0 <= new_y < len(matrix[0]):
                    if matrix[new_x][new_y] > matrix[x][y]:
                        stack.append((new_x, new_y, depth+1))
                        res = max(res, depth + 1)
        return res