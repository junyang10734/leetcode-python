# 773. Sliding Puzzle
# BFS

# https://labuladong.github.io/algo/4/31/111/
# 题意即置换0和其相邻的cell
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        start = ''
        for i in range(2):
            for j in range(3):
                start += str(board[i][j])
        
        # index of neighbor
        # eg: the neighbor of index 0 is the cell of index 1 and index 3
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        queue = collections.deque([start])
        visited = set()
        visited.add(start)
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur == target:
                    return step
                
                index = cur.index('0')
                for nx in neighbors[index]:
                    arr = list(cur).copy()
                    arr[index], arr[nx] = arr[nx], arr[index]
                    newS = ''.join(arr)
                    if newS not in visited:
                        queue.append(newS)
                        visited.add(newS)
            step += 1
        
        return -1