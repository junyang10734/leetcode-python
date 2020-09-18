# Majority Element

# Sort
# 先对数组进行排序，因为多数元素一定存在，且个数超过总个数的一半，那么排序后最中间的那个元素一定是多数元素
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]


# 分治
# 每次将数组分成左右两半，在两半中分别找出现次数最多的元素
# 若找到的两个元素相同则此元素即为所求
# 否则在整个数组中分别计算这两个元素出现的次数，取较大的那个
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        return self.dac(nums, 0, len(nums)-1)

    def dac(self, nums, left, right):
        if left == right:
            return nums[left]
        else:
            mid = int((left+right)/2)
            majl = self.dac(nums, left, mid)
            majr = self.dac(nums, mid+1, right)

            if majl == majr:
                return majl
            else:
                return majl if nums[left:right+1].count(majl) > nums[left:right+1].count(majr) else majr



# HashMap
# faster than 62.71%
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


# 摩尔投票法 Moore Voting
# faster than 62.71%
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        m = cm = 0
        for num in nums:
            if m == num:
                cm += 1
            elif cm == 0:
                m = num
                cm = 1
            else:
                cm -= 1
        
        return m
