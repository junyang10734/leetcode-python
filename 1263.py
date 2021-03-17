# 1263. Minimum Moves to Move a Box to Their Target Location
# Graph / BFS

# runtime: faster than 30.43%
# https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/discuss/431071/Python-Straightforward-2-stage-BFS-Explained
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'T':
                    target = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'S':
                    player = (i, j)
                    
        def canGet(b, p, t):
            # b: current box, p: current player, t: target
            seen, cur = set([p]), set([p])
            while cur:
                tmp = []
                for loc in cur:
                    for x, y in dirs:
                        if 0 <= loc[0]+x < m and 0 <= loc[1]+y < n and (loc[0]+x, loc[1]+y) != b and grid[loc[0]+x][loc[1]+y] != '#' and (loc[0]+x, loc[1]+y) not in seen:
                            tmp += [(loc[0]+x, loc[1]+y)]
                cur = set(tmp)
                seen |= cur
                if t in seen:
                    return True
            return False
            
        
        seen, cur, res = set([(box, player)]), set([(box, player)]), 0
        while cur:
            tmp = []
            res += 1
            for b, p in cur:
                for x,y in dirs:
                    if 0 <= b[0]+x < m and 0 <= b[1]+y < n and grid[b[0]+x][b[1]+y] != '#' and ((b[0]+x, b[1]+y), b) not in seen and canGet(b, p, (b[0]-x, b[1]-y)):
                        tmp += [((b[0]+x, b[1]+y), b)]
            cur = set(tmp)
            seen |= cur
            for x,y in dirs:
                if (target, (target[0]+x, target[1]+y)) in seen:
                    return res
        return -1
                    