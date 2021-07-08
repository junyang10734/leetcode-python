# 658. Find K Closest Elements
# Array / Binary Search / Sliding Window / Sorting / Heap

# https://leetcode.com/problems/find-k-closest-elements/solution/

# Sorting
# runtime: O(nlogn+klogk)
class Solution1:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key=lambda n: abs(x-n))[:k])

# Binary Search + Heap
class Solution2:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        heap = []
        left_idx = bisect.bisect_left(arr, x)
        right_idx = bisect.bisect_right(arr, x)
        k -= right_idx - left_idx
        for i in range(k):
            idx = left_idx - i - 1
            if idx >= 0:
                heapq.heappush(heap, (x - arr[idx], arr[idx]))
            
            idx = right_idx + i
            if idx <= len(arr)-1:
                heapq.heappush(heap, (arr[idx] - x, arr[idx]))
        
        for i in range(k):
            if len(heap) > 0:
                res.append(heapq.heappop(heap)[1])
            else:
                break
        for i in range(left_idx, right_idx):
            res.append(arr[i])
        return sorted(res)


# Binary Search + Slding Window
# runtime: O(logn+k)
class Solution3:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        
        left = bisect_left(arr, x) - 1
        right = left + 1
        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left+1: right]