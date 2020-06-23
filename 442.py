# Find All Duplicates in an Array
# Array

# hash table
# runtime: faster than 70.15% 
class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1
        
        ans = []
        for i in d:
            if d[i] != 1:
                ans.append(i)
        
        return ans


# https://blog.csdn.net/fuxuemingzhu/article/details/79275549
# space: O(1)
# runtime: faster than 70.15% 
class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                ans.append(abs(n))
            nums[abs(n)-1] *= -1
        return ans
