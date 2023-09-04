#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#


# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        final_max = current_max = index = taken = zero_index = 0
        zeros = []
        while index < len(nums):
            # if 1
            if nums[index] == 1:
                current_max += 1
            # if 0
            else:
                if taken == k:
                    zeros.append(index)
                    final_max = max(final_max, current_max)
                    current_max = index - (zeros[zero_index] + 1) + 1
                    zero_index += 1
                else:
                    while index < len(nums) and nums[index] == 0 and taken < k:
                        zeros.append(index)
                        current_max += 1
                        index += 1
                        taken += 1
                    index -= 1
            index += 1

        return max(final_max, current_max)


# @lc code=end
