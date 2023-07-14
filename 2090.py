# 2090. K Radius Subarray Averages
# Array / Sliding window

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n < 2 * k:
            return [-1] * n

        window = collections.deque(nums[:2*k])
        total = sum(window)
        res = [-1] * k

        for i in range(k, n-k):
            total += nums[i+k]
            window.append(nums[i+k])
            res.append(total // (2 * k + 1))
            total -= window.popleft()
            
        for i in range(n-k, n):
            res.append(-1)

        return res
