#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        first = 0
        second = nums[0]
        third = nums[1]

        for i in range(2, len(nums)):
            temp_third = nums[i] + max(first, second)
            first, second, third = second, third, temp_third

        return max(second, third)


# @lc code=end
