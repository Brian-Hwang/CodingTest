#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = float("inf")
        second_min = float("inf")

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False
        # biggest, middle, i = 0, 1, len(nums) - 1

        # while i >= 0:
        #     print("BEFORE", biggest, middle, nums[i], i)
        #     if i == len(nums) - 1 or nums[i] >= biggest:
        #         biggest = nums[i]
        #         middle = nums[i - 1]
        #         i -= 1
        #         while biggest <= middle:
        #             biggest = nums[i]
        #             middle = nums[i - 1]
        #             i -= 1
        #             if i < 1:
        #                 return False
        #     elif nums[i] >= middle:
        #         middle = nums[i]
        #     else:
        #         return True
        #     print("AFTER", biggest, middle, i)

        #     i -= 1

        # return False


# @lc code=end
