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


# class Solution:
#     def maxFrequency(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         count = collections.Counter(nums)
#         d = [nums[i]-nums[i-1] for i in range(1, len(nums))]
#         res = sorted(count.items(), key=lambda x:(-x[1], x[0]))[0][1]
        
#         while k > 0:
#             if sum(d) == 0:
#                 return res
#             minD, idx = inf, -1
#             for i,n in enumerate(d):
#                 if n > 0 and n < minD:
#                     minD, idx = n, i
#             d[idx-1] += 1
#             d[idx] -= 1
#             count[nums[idx]] -= 1
#             nums[idx] += 1
#             count[nums[idx]] += 1
#             res = max(res, count[nums[idx]])
#             k -= 1
        
#         return res 

# s = Solution()
# nums = [1, 2, 4]
# k = 5
# print(s.maxFrequency(nums, k))


# from typing import List
# class Solution:
#     def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
#         dp = [i for i in range(n)]
#         for i,h in restrictions:
#             dp[i-1] = min(h, i-1)
        
#         for i in range(1, n):
#             if i == n-1:
#                 dp[i] = min(dp[i], dp[i-1]+1)
#             else:
#                 dp[i] = min(dp[i], dp[i-1]+1, dp[i+1]+1)
        
#         return max(dp)

# s = Solution()
# n = 5
# restrictions = [[2,1],[4,1]]
# print(s.maxBuilding(n, restrictions))
