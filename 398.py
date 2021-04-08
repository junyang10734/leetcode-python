# 398. Random Pick Index
# Design / Hash Table

# runtime: faster than 36%
class Solution:

    def __init__(self, nums: List[int]):
        self.d = collections.defaultdict(list)
        for i,num in enumerate(nums):
            self.d[num].append(i)

    def pick(self, target: int) -> int:
        arr = self.d[target]
        idx = randint(0, len(arr)-1)
        return arr[idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)