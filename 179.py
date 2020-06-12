# Largest Number
# Array

# https://blog.csdn.net/AIpush/article/details/103809256?utm_medium=distribute.pc_relevant.none-task-blog-baidujs-2
# runtime: faster than 5.73% 
class Solution1:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if self.compare(nums[j+1], nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        res = ''.join(map(str, nums))
        return '0' if res[0] == '0' else res
    
    def compare(self, a, b):
        return str(a) + str(b) > str(b) + str(a)


# runtime: faster than 80.64% 
class LargerNumKey(str):
    def __lt__(x,y):
        return x+y > y+x

class Solution2:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str,nums), key=LargerNumKey))
        
        return '0' if largest_num[0] == '0' else largest_num