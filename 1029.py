# Two City Scheduling
# Greedy

# https://blog.csdn.net/CSerwangjun/article/details/89500371
# runtime: faster than 50.31%
class Solution1:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        N = len(costs)
        diff = [ c[0] - c[1] for c in costs]
        idx = sorted(range(0,N), key = lambda k:diff[k])

        for i in range(N//2):
            res += costs[idx[i]][0]
            res += costs[idx[N-i-1]][1]

        return res


# https://leetcode.com/problems/two-city-scheduling/discuss/667781/Python-3-Lines-O(n-log-n)-with-sort-explained
# runtime: faster than 73.29%
class Solution2:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        first_city = [i for i,j in costs]   
        diff = [j-i for i,j in costs]
        res = sum(first_city) + sum(sorted(diff)[:len(costs)//2])
        return res