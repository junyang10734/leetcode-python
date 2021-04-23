# 582. Kill Process
# Queue / BFS

# https://leetcode.com/problems/kill-process/discuss/914266/Python-3-greater-99.85-faster-using-dictionary
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = collections.defaultdict(list)
        for i,p in enumerate(ppid):
            d[p].append(pid[i])

        res = []
        q = collections.deque([kill])
        while q:
            kill = q.popleft()
            res.append(kill)
            if kill in d:
                for c in d[kill]:
                    q.append(c)
        return res
