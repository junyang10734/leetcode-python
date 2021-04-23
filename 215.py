# 215. Kth Largest Element in an Array

# Sort
# runtime: faster than 97.75% 
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# heapq 大根堆
# runtime: faster than 99.13% 
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# QuickSort
# runtime: O(n)
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left, right, index):
            pivot = nums[index]
            
            nums[index], nums[right] = nums[right], nums[index]
            tmp = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[tmp], nums[i] = nums[i], nums[tmp]
                    tmp += 1
                    
            nums[right], nums[tmp] = nums[tmp], nums[right]
            return tmp
        
        def select(left, right, k):
            if left == right:
                return nums[left]
            index = random.randint(left, right)
            index = partition(left, right, index)
            if k == index:
                return nums[index]
            elif k < index:
                return select(left, index-1, k)
            else:
                return select(index+1, right, k)
        
        return select(0, len(nums)-1, len(nums)-k)