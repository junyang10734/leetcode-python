# Reconstruct Itinerary
# Graph / DFS


# https://leetcode.com/problems/reconstruct-itinerary/solution/
# runtime: O(vlogv)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for f, t in tickets:
            graph[f].append(t)

        for f, t in graph.items():
            t.sort(reverse=True)

        res = []
        self.dfs(graph, "JFK", res)
        return res[::-1]
        
    def dfs(self, graph, source, res):
        while graph[source]:
            v = graph[source].pop()
            self.dfs(graph, v, res)
        res.append(source)