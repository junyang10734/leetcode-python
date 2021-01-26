# Intersection of Two Arrays II

# faster than 25.19%
class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        minl = nums1 if len(nums1) <= len(nums2) else nums2
        maxl = nums1 if len(nums1) > len(nums2) else nums2
        res = []
        for item in minl:
            if item in maxl:
                res.append(item)
                maxl.remove(item)
        return res


# hash table
# faster than 80.16%
class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        d = {}
        
        for i in nums1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for j in nums2:
            if j in d and d[j] > 0:
                res.append(j)
                d[j] -= 1
        return res


# hash table / Counter
class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d1 = collections.Counter(nums1)
        d2 = collections.Counter(nums2)
        
        for k,v in d1.items():
            if k in d2:
                res += [k] * (min(v, d2[k]))
        
        return res



# sort and two points
# faster than 58.11%
class Solution4(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        
        i,j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res