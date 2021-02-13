# 414. Third Maximum Number
# Array

# runtime: faster than 44.58%
class Solution1:
    def thirdMax(self, nums: List[int]) -> int:    
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for n in nums:
            if n > max1:
                max1, max2, max3 = n, max1, max2
            elif max1 > n > max2:
                max2, max3 = n, max2
            elif max2 > n > max3:
                max3 = n

        return max3 if max3 > float('-inf') else max1


# runtime: faster than 89.11%
# converting to list takes O(n) time where n is the number of unique integers in nums
# sorting for set takes worst case O(n), and then we simply index the required max
class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        return arr[-3] if len(arr) >= 3 else arr[-1]