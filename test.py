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

# import numpy as np
# c = np.array([
#     [ [ 1, 2, 3], [1, 2, 3] ],
#     [ [-1, 1, 4], [-1, 1, 5]]
#     ])
# print(np.linalg.norm(c, axis=0))
# print(np.linalg.norm(c, axis=1))
# print(np.linalg.norm(c, axis=2))
