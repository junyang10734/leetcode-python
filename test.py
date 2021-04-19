# total = int(input())
# for t in range(total):
#     n, b = map(int, input().split())
#     A = list(map(int, input().split()))
#     res = 0
#     A.sort()

#     for i in A:
#         if b >= i:
#             b -= i
#             res += 1
#         else:
#             break
#     print("Case #{}: {}".format((t+1), res), flush = True)


from typing import List
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        start_times = []
        processing_times = {}
        for i,task in enumerate(tasks):
            start_times.append((i,task[0]))
            processing_times[(i,task[0])] = (i, task[1])
        
        start_times.sort(key=lambda x:(x[1], x[0]))
        start = start_times[0][1]
        res = []
        
        def helper(start):
            available = []
            for i in range(len(start_times)):
                if start >= start_times[i][1]:
                    available.append(processing_times[start_times[i]])
                else:
                    break
                    
            if available:
                available.sort(key=lambda x:(x[1], x[0]))
                start += available[0][1]
                idx = available[0][0]
                res.append(idx)
                start_times.remove((idx, tasks[idx][0]))
            else:
                start += 1
            
            if len(start_times) > 0:
                helper(start)
                
        
        helper(start)
        return res

s = Solution()
tasks = [[1,2],[2,4],[3,2],[4,1]]
print(s.getOrder(tasks))