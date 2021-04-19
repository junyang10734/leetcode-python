# 1539. Kth Missing Positive Number
# Array

# runtime: O(n)
class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        for a in arr:
            if a-num == k:
                return a-1
            elif a-num < k:
                k -= a - num
                num = a + 1
            else:
                return num + k - 1
        
        return arr[-1] + k

class Solution1:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k <= arr[0] - 1:
            return k
        k -= arr[0] - 1
        for i in range(len(arr)-1):
            curr_missing = arr[i+1] - arr[i] - 1
            if k <= curr_missing:
                return arr[i] + k
            k -= curr_missing
        return arr[-1] + k


# https://leetcode.com/problems/kth-missing-positive-number/solution/
# runtime: O(nlogn)
class Solution2:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k