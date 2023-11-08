#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#


# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums) - nums[0]
        left_sum = 0
        for i in range(len(nums) - 1):
            if right_sum == left_sum:
                return i
            right_sum -= nums[i + 1]
            left_sum += nums[i]

        if left_sum == 0:
            return len(nums) - 1
        else:
            return -1


# @lc code=end
