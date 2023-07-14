# 2462. Total Cost to Hire K Workers
# heap

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head, tail = costs[:candidates], costs[max(candidates, len(costs)-candidates):]
        heapq.heapify(head)
        heapq.heapify(tail)

        ans = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            if not tail or head and head[0] <= tail[0]:
                ans += heapq.heappop(head)
                if next_head <= next_tail:
                    heapq.heappush(head, costs[next_head])
                    next_head += 1
            else:
                ans += heapq.heappop(tail)
                if next_head <= next_tail:
                    heapq.heappush(tail, costs[next_tail])
                    next_tail -= 1

        return ans
