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

# https://labuladong.github.io/algo/di-san-zha-24031/shu-xue-yu-659f1/tan-tan-yo-b4bb5/#%E6%B4%97%E7%89%8C%E7%AE%97%E6%B3%95
# Fisher–Yates Algorithm
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def reset(self) -> List[int]:
        return self.nums
        
    def shuffle(self) -> List[int]:
        n = len(self.nums)
        copy = self.nums.copy()
        for i in range(n):
            r = i + random.randint(0, n-i-1)
            copy[i], copy[r] = copy[r], copy[i]
        return copy


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()