# 952. Largest Component Size by Common Factor
# Graph / Union-Find

# https://blog.csdn.net/fuxuemingzhu/article/details/85015411
# runtime: faster than 58.21%
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        maxa = max(A)
        n = len(A)
        m = list(range(maxa+1))
        
        for a in A:
            for k in range(2, int(math.sqrt(a))+1):
                if a % k == 0:
                    self.union(m, a, k)
                    self.union(m, a, a//k)
                    
        cnt = collections.defaultdict(int)
        for a in A:
            cnt[self.find(m, a)] += 1
        return max(cnt.values())
        
    def find(self, m, a):
        while a != m[a]:
            m[a] = m[m[a]]
            a = m[a]
        return a
    
    def union(self, m, a, b):
        if m[a] == m[b]:
            return
        pa, pb = self.find(m, a), self.find(m, b)
        m[pa] = pb
