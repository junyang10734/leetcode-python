# 480. Sliding Window Median
# Array / Heap

# https://leetcode.com/problems/sliding-window-median/discuss/394302/Python-clean-solution-(easy-to-understand)
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or not k:
            return []
        
        lo, hi = [], []
        for i in range(k):
            if len(lo) == len(hi):
                heapq.heappush(lo, -nums[i])
                tmp = -heapq.heappop(lo)
                heapq.heappush(hi, tmp)
            else:
                heapq.heappush(hi, nums[i])
                tmp = heapq.heappop(hi)
                heapq.heappush(lo, -tmp)
        
        
        res = [hi[0]] if k % 2 == 1 else [(hi[0] - lo[0]) / 2.0]
        to_remove = collections.defaultdict(int)
        for i in range(k, len(nums)):
            heapq.heappush(hi, nums[i])
            tmp = heapq.heappop(hi)
            heapq.heappush(lo, -tmp)
            out_num = nums[i-k]
            if out_num > -lo[0]:
                tmp = -heapq.heappop(lo)
                heapq.heappush(hi, tmp)
            to_remove[out_num] += 1
            while lo and to_remove[-lo[0]]:
                to_remove[-lo[0]] -= 1
                heapq.heappop(lo)
            while to_remove[hi[0]]:
                to_remove[hi[0]] -= 1
                heapq.heappop(hi)
            if k % 2:
                res.append(hi[0])
            else:
                res.append((hi[0] - lo[0]) / 2.0)
                
        return res
