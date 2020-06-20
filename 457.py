# Circular Array Loop
# Array

# https://blog.csdn.net/fuxuemingzhu/article/details/87968610
# runtime: faster than 5.17%
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        self.nums = nums
        for i in range(len(nums)):
            slow = i
            fast = self.nextpos(slow)
            while nums[fast] * nums[i] > 0 and nums[self.nextpos(fast)] * nums[i] > 0:
                if fast == slow:
                    if slow == self.nextpos(slow):
                        break
                    return True
                slow = self.nextpos(slow)
                fast = self.nextpos(self.nextpos(fast))
        return False
    
    def nextpos(self, index):
        n = len(self.nums)
        return (index + self.nums[index] + n) % n