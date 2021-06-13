# # total = int(input())
# # for t in range(total):
# #     n, b = map(int, input().split())
# #     A = list(map(int, input().split()))
# #     res = 0
# #     A.sort()

# #     for i in A:
# #         if b >= i:
# #             b -= i
# #             res += 1
# #         else:
# #             break
# #     print("Case #{}: {}".format((t+1), res), flush = True)


# # class Solution:
# #     def maxFrequency(self, nums: List[int], k: int) -> int:
# #         nums.sort()
# #         count = collections.Counter(nums)
# #         d = [nums[i]-nums[i-1] for i in range(1, len(nums))]
# #         res = sorted(count.items(), key=lambda x:(-x[1], x[0]))[0][1]

# #         while k > 0:
# #             if sum(d) == 0:
# #                 return res
# #             minD, idx = inf, -1
# #             for i,n in enumerate(d):
# #                 if n > 0 and n < minD:
# #                     minD, idx = n, i
# #             d[idx-1] += 1
# #             d[idx] -= 1
# #             count[nums[idx]] -= 1
# #             nums[idx] += 1
# #             count[nums[idx]] += 1
# #             res = max(res, count[nums[idx]])
# #             k -= 1

# #         return res

# # s = Solution()
# # nums = [1, 2, 4]
# # k = 5
# # print(s.maxFrequency(nums, k))


# # from typing import List
# # class Solution:
# #     def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
# #         dp = [i for i in range(n)]
# #         for i,h in restrictions:
# #             dp[i-1] = min(h, i-1)

# #         for i in range(1, n):
# #             if i == n-1:
# #                 dp[i] = min(dp[i], dp[i-1]+1)
# #             else:
# #                 dp[i] = min(dp[i], dp[i-1]+1, dp[i+1]+1)

# #         return max(dp)

# # s = Solution()
# # n = 5
# # restrictions = [[2,1],[4,1]]
# # print(s.maxBuilding(n, restrictions))


# class Filter:
#     def __init__(self):
#         pass

#     def apply(self, file):
#         pass

# class SizeFilter(Filter):
#     def __init__(self, size):
#         self.size = size

#     def apply(self, file):
#         return file.size > self.size

# class ExtensionFilter(Filter):
#     def __init__(self, ext):
#         self.extension = ext
#     def apply(self, file):
#         return file.extension == self.extension

# class File:
#     def __init__(self, name, size):
#         self.name = name
#         self.isDirectory = False if '.' in name else True
#         self.size = size
#         self.extension = name.split(".")[1] if '.' in name else ""
#         self.children = []

#     def __repr__(self):
#         return "{" + self.name + "}"

# class FileSystem:

#     def __init__(self):
#         self.filters = []

#     def addFilter(self, f):
#         # self.filters.append(f)
#         if isinstance(f, Filter):
#             self.filters.append(f)


#     # This implementation is OR implementation of filter.
#     def traverse(self, root):

#         result = []
#         def traverseUtil(root, result):
#             for r in root.children:
#                 if r.isDirectory:
#                     traverseUtil(r, result)
#                 else:

#                     for _f in self.filters:
#                         if _f.apply(r):
#                             print("result:", result)
#                             result.append(r)
#         #return result
#         traverseUtil(root, result)
#         return result

# f1 = File("StarTrek.txt", 5)
# f2 = File("StarWars.xml", 10)
# f3 = File("JusticeLeague.txt", 15)
# f4 = File("IronMan.txt", 9)
# f5 = File("Spock.jpg", 1)
# f6 = File("BigBangTheory.txt", 50)
# f7 = File("MissionImpossible", 10)
# f8 = File("BreakingBad", 11)
# f9 = File("root", 100)

# f9.children = [f7, f8]
# f7.children = [f1, f2, f3]
# f8.children = [f4, f5, f6]

# filter1 = SizeFilter(5)
# filter2 = ExtensionFilter("txt")

# fs = FileSystem()
# fs.addFilter(filter1)
# fs.addFilter(filter2)
# print(fs.traverse(f9))


# class Filter:  # abstract class
#   def apply(self, file):
#     if not isinstance(file, File):  # file validation
#       raise TypeError

# class SizeFilter(Filter):
#   def __init__(self, size, larger=False):
#     self._size = size
#     self._larger = larger

#   def apply(self, file):  # returns true if correct file
#     super().apply(file)

#     if file.size < self._size and not self._larger:
#       return True
#     elif file.size > self._size and self._larger:
#       return True
#     else:
#       return False

# class TypeFilter(Filter):
#   def __init__(self, file_type):
#     self._file_type = file_type

#   def apply(self, file):
#     super().apply(file)

#     if file.file_type == self._file_type:
#       return True
#     return False

# class FindCommand:
#   def find_all(self, curr_dir, filters):
#     all_files = []
#     for file in curr_dir.files:
#       if isinstance(file, Directory):
#         all_files += self.find_all(file, filters)
#       for f in filters:
#         if f.apply(file):
#           all_files.append(file.name)
#     return all_files


def solution(l):
    res = 0

    def backtrack(path, start):
        nonlocal res
        for i in range(start, len(l)):
            s = set(l[i])
            if s & path:
                continue
            else:
                # path |= s
                res = max(res, len(path) + len(s))
                backtrack(path | s, i + 1)

    backtrack(set([]), 0)
    return res

l = ['ab', 'cd', 'bc', 'efg', 'ahyjlo']
print(solution(l))
