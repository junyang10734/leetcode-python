# 1151. Minimum Swaps to Group All 1's Together
# Array / Sliding Window

# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/solution/
# sliding window + two pointers
# runtime: O(n)
class Solution1:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        cnt_one = max_one = 0
        left = right = 0
        while right < len(data):
            cnt_one += data[right]
            right += 1
            if right - left > ones:
                cnt_one -= data[left]
                left += 1
            max_one = max(max_one, cnt_one)
        return ones - max_one


# sliding window + one pointer
# runtime: O(n)
class Solution2:
    def minSwaps(self, data: List[int]) -> int:
        count = sum(data)
        if count <= 1:
            return 0
        
        n = sum(data[:count])
        cur = n
        i = 1
        while i <= len(data)-count:
            cur = cur - data[i-1] + data[i+count-1]
            n = max(n, cur)
            i += 1
        return count - n