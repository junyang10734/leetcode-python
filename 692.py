# 692. Top K Frequent Words

# Hash / Heap
# https://blog.csdn.net/fuxuemingzhu/article/details/79559691

# Hash
# running time: faster than 95.14%
class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        candidates = list(cnt.keys())
        candidates.sort(key=lambda w: (-cnt[w], w))
        return candidates[:k]

class Solution1:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        a = sorted(cnt.items(), key=lambda x:(-x[1], x[0]))
        return [a[i][0] for i in range(k)]


# Heap
# running time: faster than 5.19% 
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        heap = [(-t, w) for w,t in cnt.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
