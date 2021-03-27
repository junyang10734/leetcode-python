# 269. Alien Dictionary
# DFS / BFS / Topological Sort

# https://leetcode.com/problems/alien-dictionary/solution/   (amazing article)

# BFS
# runtime: faster than 98.83%
class Solution1:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})
        
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ''
        
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
        
        if len(output) < len(in_degree):
            return ''
        return ''.join(output)


# DFS
# runtime: faster than 58.56%
class Solution2:
    def alienOrder(self, words: List[str]) -> str:
        reverse_adj_list = {c:[] for word in words for c in word}
        
        for first_word, second_word in zip(words, words[1:]):
            for c,d in zip(first_word, second_word):
                if c != d:
                    reverse_adj_list[d].append(c)
                    break
            else:
                if len(second_word) < len(first_word):
                    return ''
        
        seen = {}
        output = []
        def visit(node):
            if node in seen:
                return seen[node]
            seen[node] = False
            for nei in reverse_adj_list[node]:
                result = visit(nei)
                if not result:
                    return False
            seen[node] = True
            output.append(node)
            return True
        
        if not all(visit(node) for node in reverse_adj_list):
            return ''
        return ''.join(output)