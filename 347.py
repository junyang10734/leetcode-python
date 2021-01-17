# Top K Frequent Elements

# heapq
# runtime: faster than 70.59% 
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get) 


# Counter
# running time: less than 73.96%
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums).most_common(k)        
        return [i[0] for i in d]