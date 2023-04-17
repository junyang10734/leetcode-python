# 760. Find Anagram Mappings
# Hash Table

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = collections.defaultdict(list)
        for i,num in enumerate(nums2):
            d[num].append(i)
        
        res = []
        for num in nums1:
            res.append(d[num].pop())
        return res


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        for i,num in enumerate(nums2):
            d[num] = i
        
        return [d[num] for num in nums1]