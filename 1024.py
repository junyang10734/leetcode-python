# 1024. Video Stitching
# Greedy

# https://labuladong.github.io/algo/di-er-zhan-a01c6/tan-xin-le-9bedf/jian-shi-p-4302c/
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0:
            return 0

        # 按起点升序排列，起点相同的降序排列
        clips.sort(key=lambda x:(x[0], -x[1])) 
        # 记录选择的短视频个数
        res = 0
        curEnd, nextEnd = 0, 0
        i = 0
        n = len(clips)
        while i < n and clips[i][0] <= curEnd:
            # 在第 res 个视频的区间内贪心选择下一个视频
            while i < n and clips[i][0] <= curEnd:
                nextEnd = max(nextEnd, clips[i][1])
                i += 1
            # 找到下一个视频，更新 curEnd
            res += 1
            curEnd = nextEnd
            if curEnd >= time:
                # 已经可以拼出区间 [0, T]
                return res
        # 无法连续拼出区间 [0, T]
        return -1