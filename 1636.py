# 1636. Sort Array by Increasing Frequency
# Array / Sort

# runtime: faster than 92.70%
class Solution1:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        l = sorted(count.items(), key=lambda x:(x[1], -x[0]))
        res = []
        for i in l:
            res += [i[0]]*i[1]
        return res


# https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/917795/C%2B%2BPython-Sort
# runtime: faster than 79.67%
class Solution2:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return sorted(nums, key=lambda x:(count[x], -x))