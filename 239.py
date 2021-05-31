# 239. Sliding Window Maximum

# https://leetcode.com/problems/sliding-window-maximum/solution/

# Sliding Window
# runtime: O(n)
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            if q and q[0] == i - k:
                q.popleft()
            
            while q and nums[i] > nums[q[-1]]:
                q.pop()
        
        
        q = collections.deque()
        max_id = 0
        for i in range(k):
            clean_deque(i)
            q.append(i)
            if nums[i] > nums[max_id]:
                max_id = i
        output = [nums[max_id]]
        
        for i in range(k, n):
            clean_deque(i)
            q.append(i)
            output.append(nums[q[0]])
        return output


# DP
# runtime: O(n)
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums
        
        left, right = [0] * n, [0] * n
        left[0], right[n-1] = nums[0], nums[n-1]
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(nums[i], left[i-1])
            
            j = n - 1 - i
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(nums[j], right[j+1])
        
        output = []
        for i in range(n - k + 1):
            output.append(max(left[i+k-1], right[i]))
        return output