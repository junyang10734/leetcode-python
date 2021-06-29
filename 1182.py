# 1182. Shortest Distance to Target Color
# Binary Search

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for i, c in enumerate(colors):
            d[c].append(i)

        res = []
        for i, c in queries:
            if colors[i] == c:
                res.append(0)
            elif len(d[c]) == 0:
                res.append(-1)
            else:
                right = bisect_left(d[c], i)
                if right > len(d[c]) - 1:
                    distance = abs(i - d[c][-1])
                elif right == 0:
                    distance = abs(i - d[c][0])
                else:
                    left = right - 1
                    distance = abs(i - d[c][right]) if abs(i - d[c][right]) <= abs(d[c][left] - i) else abs(d[c][left] - i)
                res.append(distance)
        return res
