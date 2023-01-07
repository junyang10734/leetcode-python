# 2244. Minimum Rounds to Complete All Tasks
# Counting / Greedy

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = collections.Counter(tasks)

        res = 0
        for k,v in counter.items():
            if v == 1:
                return -1
            if v % 3 == 0:
                res += (v // 3)
            else:
                res += (v // 3 + 1)
        return res