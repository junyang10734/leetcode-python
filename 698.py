# 698. Partition to K Equal Sum Subsets
# 此题应为 hard 难度
# backtrack

# https://labuladong.github.io/algo/4/31/105/
# 必须用带memo的优化方法才能pass
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        numsSum = sum(nums)
        if numsSum % k != 0:
            return False
        target = numsSum // k
        used = 0  # 使用位图技巧
        memo = {}

        def backtrack(index, bucket, nums, start, used, target):
            # base case
            if index == 0:
                # 所有桶都被装满了，而且 nums 一定全部用完了
                return True
            
            if bucket == target:
                # 装满了当前桶，递归穷举下一个桶的选择
                # 让下一个桶从 nums[0] 开始选数字
                res = backtrack(index-1, 0, nums, 0, used, target)
                # 缓存结果
                memo[used] = res
                return res
            
            # 避免冗余计算
            if used in memo:
                return memo[used]

            for i in range(start, len(nums)):
                # 剪枝
                
                if (used >> i & 1) == 1: # 判断第 i 位是否是 1
                    # nums[i] 已经被装入别的桶中
                    continue
                if nums[i] + bucket > target:
                    continue
                
                # 做选择
                used |= 1 << i # 将第 i 位置为 1
                bucket += nums[i]
                # 递归穷举下一个数字是否装入当前桶
                if backtrack(index, bucket, nums, i+1, used, target):
                    return True
                
                # 撤销选择
                used ^= 1 << i  # 使用异或运算将第 i 位恢复 0
                bucket -= nums[i]
            
            return False
        
        # k 号桶初始什么都没装，从 nums[0] 开始做选择
        return backtrack(k, 0, nums, 0, used, target)