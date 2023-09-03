#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        final_max = current_max = index = 0
        while index < len(nums):
            # if 1
            if nums[index] == 1:
                current_max += 1
            # if 0
            else:
                sub_index = 0
                index += 1
                while index < len(nums) and sub_index <= k:
                    if nums[index] == 1:
                        break
                    elif sub_index == k - 1:
                        final_max = max(final_max, current_max)
                    index += 1
                    sub_index += 1
            index += 1

        return final_max


# @lc code=end
