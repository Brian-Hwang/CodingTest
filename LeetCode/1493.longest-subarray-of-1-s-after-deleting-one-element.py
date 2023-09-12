#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        local_max = global_max = 0
        last_zero = -1
        for i in range(len(nums)):
            # is 1
            if nums[i] == 1:
                local_max += 1
            # is 0
            else:
                global_max = max(global_max, local_max)
                if last_zero != -1:
                    local_max = i - last_zero - 1
                last_zero = i

        global_max = max(global_max, local_max)
        # No zero exists
        if last_zero == -1:
            global_max -= 1

        return global_max


# @lc code=end
