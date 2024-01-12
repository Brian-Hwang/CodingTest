#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        minus_inf = float("-inf")
        cur_num, cur_count, dup = minus_inf, 1, 0

        for i, num in enumerate(nums):
            if cur_num != num:
                cur_num = num
                cur_count = 1
            else:
                cur_count += 1

                if cur_count > 2:
                    nums[i] = minus_inf
                    dup += 1
        if dup == 0:
            return len(nums)

        for i, num in enumerate(nums):
            if num != minus_inf:
                minus_one = nums.index(minus_inf)
                if minus_one < i:
                    nums[i], nums[minus_one] = nums[minus_one], nums[i]

        return len(nums) - dup


# @lc code=end
