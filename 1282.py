# 1282. Group the People Given the Group Size They Belong To
# Hash / Array

# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/solutions/446336/java-python-3-9-and-6-liners-group-ids-by-size-w-brief-explanation-and-analysis/?envType=daily-question&envId=2023-09-11
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sizeToGroup = collections.defaultdict(list)
        res = []
        for i,size in enumerate(groupSizes):
            sizeToGroup[size].append(i)
            if len(sizeToGroup[size]) == size:
                res.append(sizeToGroup.pop(size))
        
        return res