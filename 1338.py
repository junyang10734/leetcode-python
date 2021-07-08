# 1338. Reduce Array Size to The Half
# Sorting / Hash Table

# runtime: O(nlogn)
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        sorted_cnt = sorted(count.items(), key=lambda x: -x[1])

        res, s, n = 0, 0, len(arr)//2
        for i in range(len(sorted_cnt)):
            s += sorted_cnt[i][1]
            res += 1
            if s >= n:
                return res
