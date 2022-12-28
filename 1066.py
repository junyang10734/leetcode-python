# 1066. Campus Bikes II
# DP / bit Manipulation（位操作）

# https://leetcode.com/problems/campus-bikes-ii/solutions/303422/python-priority-queue/?orderBy=most_votes
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def distance(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        q = [[0, 0, 0]]
        visited = set()
        while True:
            cost, i, takenState = heapq.heappop(q)
            if (i, takenState) in visited:
                continue

            visited.add((i, takenState))
            if i == len(workers):
                return cost
            
            for j in range(len(bikes)):
                if takenState & (1 << j) == 0:
                    heapq.heappush(q, [cost + distance(i, j), i+1, takenState | (1 << j)])
