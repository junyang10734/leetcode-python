# Flood Fill
# Depth-First Search

# DFS + recursion
# runtime: faster than 86.08%
class Solution1:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image
        
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r-1, c)
                if r + 1 < R:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r,c-1)
                if c+1 < C:
                    dfs(r, c+1)
        
        dfs(sr,sc)
        return image


# DFS + stack
# runtime: faster than 99.06%
class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]
        color = image[sr][sc]
        while stack:
            r, c = stack.pop()
            if image[r][c] == color and (r, c) not in visited:
                image[r][c] = newColor
                visited.add((r, c))
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == color and (nr, nc) not in visited:
                        stack.append((nr, nc))
        
        return image