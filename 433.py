# Minimum Genetic Mutation
# String

# https://blog.csdn.net/fuxuemingzhu/article/details/82903720
# BFS
# runtime: faster than 96.27% 
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bfs = collections.deque()
        bfs.append((start, 0))
        bankset = set(bank)
        
        while bfs:
            gene, step = bfs.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for x in 'AGCT':
                    newGene = gene[:i] + x + gene[i+1:]
                    if newGene in bank and newGene != gene:
                        bfs.append((newGene, step+1))
                        bank.remove(newGene)
        return -1