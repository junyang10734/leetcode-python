# Random Pick with Weight
# Binary Search

# https://blog.csdn.net/fuxuemingzhu/article/details/81807215
# runtime: faster than 45.87%
class Solution:

    def __init__(self, w: List[int]):
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i-1] + w[i]
        

    def pickIndex(self) -> int:
        total = self.preSum[-1]
        rand = random.randint(0, total-1)
        left, right = 0, len(self.preSum) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if rand >= self.preSum[mid]:
                left = mid
            else:
                right = mid
        if rand < self.preSum[left]:
            return left
        return right
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
