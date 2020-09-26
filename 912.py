# Sort an Array
# (all sort algorithms)
# https://www.runoob.com/w3cnote/ten-sorting-algorithm.html

# sort() function
# faster than 92.29%
class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


# bubble sort 冒泡排序  O(n^2)
# Time Limit Exceeded
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            for j in range(0, len(nums)-i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums


# selection sort 选择排序  O(n^2)
# Time Limit Exceeded
class Solution3:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            minIndex = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            if i != minIndex:
                nums[i], nums[minIndex] = nums[minIndex], nums[i]
        
        return nums


# insertion sort 插入排序  O(n^2)
# Time Limit Exceeded
class Solution4:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            
            nums[j+1] = key
        
        return nums


# shell sort 希尔排序  O(nlogn)
# faster than 13.76%
class Solution5:
    def sortArray(self, nums: List[int]) -> List[int]:
        gap = len(nums) // 2
        while gap > 0:
            for i in range(gap, len(nums)):
                j = i
                while j >= gap and nums[j] < nums[j-gap]:
                    nums[j], nums[j-gap] = nums[j-gap], nums[j]
                    j -= gap
            gap = gap //2
            
        return nums


# merge sort 归并排序  O(nlogn)
# faster than 42.80%
class Solution6:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
        
    def merge(self, left, right):
        res = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res += left[i:]
        res += right[j:]
        return res


# quick sort 快速排序  O(nlogn)
# faster than 71.49% 
class Solution7:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) <= 1:
            return nums
        
        self.quickSort(nums, 0, len(nums)-1)
        return nums
        
    def quickSort(self, nums, low, high):
        if low >= high:
            return
        
        i, j = low, high
        p = nums[(i+j) // 2]
        
        while i <= j:
            while i <= j and nums[i] < p:
                i += 1
            while i <= j and nums[j] > p:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        self.quickSort(nums, low, j)
        self.quickSort(nums, i, high)

# https://blog.csdn.net/Orientliu96/article/details/103333716
# faster than 76.58%
class Solution7:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) <= 1:
            return nums
        
        p = random.choice(nums)
        left, mid, right = [], [], []
        
        for i in nums:
            if i < p:
                left.append(i)
            elif i > p:
                right.append(i)
            else:
                mid.append(i)
        
        return self.sortArray(left) + mid + self.sortArray(right)


# heap sort 堆排序  O(nlogn)
# faster than 13.53%
class Solution8:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(nums, n, i)
        
        for i in range(n-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        return nums
    
    def heapify(self, nums, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and nums[i] < nums[l]:
            largest = l
        if r < n and nums[largest] < nums[r]:
            largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)

  
# counting sort 计数排序  O(n+k)
# faster than 82.58%
class Solution9:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_num, max_num = nums[0], nums[0]
        for n in nums:
            if n < min_num:
                min_num = n
            elif n > max_num:
                max_num = n
        
        count = max_num - min_num + 1
        arr = [0] * count
        for n in nums:
            arr[n-min_num] += 1
            
        res = []
        for i in range(count):
            while arr[i] > 0:
                res.append(min_num + i)
                arr[i] -= 1
        return res


# bucket sort 桶排序  O(n+k)
# faster than 82.72% 
# https://blog.csdn.net/fuxuemingzhu/article/details/100888707
class Solution10:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = [0] * 100010
        for n in nums:
            count[n + 50000] += 1
        
        res = []
        for c in range(100010):
            while count[c] > 0:
                res.append(c - 50000)
                count[c] -= 1
        
        return res
