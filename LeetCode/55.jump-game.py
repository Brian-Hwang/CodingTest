#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = nums[0]
        if max_len == 0:
            return True if len(nums) == 1 else False

        for j in range(1, len(nums) - 1):
            max_len -= 1
            max_len = max(max_len, nums[j])

            if max_len == 0:
                return False

        return True


# @lc code=end
