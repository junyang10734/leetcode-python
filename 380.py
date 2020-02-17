# Insert Delete GetRandom O(1)

# https://blog.csdn.net/fuxuemingzhu/article/details/82732532
# run time: faster than 95.64%
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mylist = []
        self.mydict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.mydict:
            self.mylist.append(val)
            self.mydict[val] = len(self.mylist) - 1
            return True
        return False
   

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.mydict:
            idx, last = self.mydict[val], self.mylist[-1]
            self.mylist[idx] = last
            self.mydict[last] = idx
            self.mylist.pop()
            del self.mydict[val]
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.mylist)-1)
        return self.mylist[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()