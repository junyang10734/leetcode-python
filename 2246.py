# 2246. Longest Path With Different Adjacent Characters
# DFS

# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/2889382/longest-path-with-different-adjacent-characters/?orderBy=most_votes
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = collections.defaultdict(list)
        for i,j in enumerate(parent):
            children[j].append(i)
        
        res = 1

        def dfs(node):
            nonlocal res
            if node not in children:
                return 1
            longestChain = 0
            secondLongestChain = 0
            for child in children[node]:
                longestChainStartingFromChild = dfs(child)
                if s[node] == s[child]:
                    continue
                
                if longestChainStartingFromChild > longestChain:
                    secondLongestChain = longestChain
                    longestChain = longestChainStartingFromChild
                elif longestChainStartingFromChild > secondLongestChain:
                    secondLongestChain = longestChainStartingFromChild

            res = max(res, longestChain + secondLongestChain + 1)
            return longestChain + 1

        dfs(0)
        return res


# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/1955433/java-c-python-dfs-on-tree/?orderBy=most_votes
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = collections.defaultdict(list)
        for i,j in enumerate(parent):
            if j >= 0:
                children[j].append(i)
        
        res = 0

        def dfs(node):
            nonlocal res
            candidates = [0]
            for child in children[node]:
                cur = dfs(child)
                if s[child] != s[node]:
                    candidates.append(cur)

            candidates = heapq.nlargest(2, candidates)
            res = max(res, sum(candidates) + 1)

            return max(candidates) + 1

        dfs(0)
        return res