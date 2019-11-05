# Merge Sorted Array

# easier to understand and run faster
class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[len(nums1)-n:] = nums2
        nums1.sort()



class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l = m + n - 1
        m, n = m-1, n-1
        
        while m>=0 and n>=0:
            if nums1[m] > nums2[n]:
                nums1[l] = nums1[m]
                m -= 1
            else:
                nums1[l] = nums2[n]
                n -= 1
            l -= 1
        
        while n >= 0:
            nums1[l] = nums2[n]
            n -= 1
            l -= 1