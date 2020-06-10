# Shuffle an Array
# Array


# https://blog.csdn.net/fuxuemingzhu/article/details/79391342

# runtime: faster than 76.88%
class Solution1:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle_nums = self.nums[:]
        random.shuffle(shuffle_nums)
        return shuffle_nums


# Fisher–Yates Algorithm
# runtime: faster than 5.13%
class Solution2:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffle_nums = self.nums[:]
        n = len(self.nums)
        
        for i in range(n):
            rand = random.randrange(i, n)
            shuffle_nums[i], shuffle_nums[rand] = shuffle_nums[rand], shuffle_nums[i]
        
        return shuffle_nums
