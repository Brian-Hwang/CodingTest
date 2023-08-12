#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        temp = 1
        for i, num in enumerate(nums):
            ans[i] = temp
            temp *= num

        temp = 1
        for i, num in enumerate(reversed(nums)):
            ans[len(nums) - i - 1] *= temp
            temp *= num

        return ans

        # Used Division...
        # product = 1
        # is_zero = -1
        # for i,num in enumerate(nums):
        #     if num == 0:
        #         if is_zero != -1:
        #             return [0] * len(nums)
        #         is_zero = i
        #     else:
        #         product *= num
        # if is_zero != -1:
        #     return [0] * is_zero + [product] + [0] * (len(nums) - is_zero - 1)
        # return [(product // num) for num in nums]


# @lc code=end
