# 1533. Find the Index of the Large Integer
# Binary Search

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


# https://leetcode.com/problems/find-the-index-of-the-large-integer/solutions/2885830/find-the-index-of-the-large-integer/
class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left = 0
        length = reader.length()
        while length > 1:
            length //= 2
            cmp = reader.compareSub(left, left + length - 1, left + length, left + 2*length - 1)
            if cmp == 0:
                return left + 2 * length
            if cmp == -1:
                left += length
        return left


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length()-1
        while left < right:
            halfLength = (right - left + 1) // 2
            cmp = reader.compareSub(left, left + halfLength - 1, left + halfLength, left + 2 * halfLength - 1)
            if cmp == 0:
                return right
            elif cmp == -1:
                left += halfLength
            elif cmp == 1:
                right = left + halfLength - 1
        return left