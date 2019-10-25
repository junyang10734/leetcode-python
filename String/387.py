# First Unique Character in a String

# easy to understand, but time limit exceeded
class Solution1(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1


# collections
# faster than 36.34%
class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for i,item in enumerate(s):
            if count[item] == 1:
                return i
        return -1


# hash table
# faster than 82.04%
class Solution3(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for i,item in enumerate(s):
            if d[item] == 1:
                return i
        return -1