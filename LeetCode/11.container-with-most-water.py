#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        lefts = []
        rights = []
        lefts.append(left)
        rights.append(right)

        for left_index in range(1, len(height) - 1, 1):
            if height[left] < height[left_index]:
                left = left_index
                lefts.append(left)

        for right_index in range(len(height) - 2, 1, -1):
            if height[right] < height[right_index]:
                right = right_index
                rights.append(right)

        max_water = 0
        for left in lefts:
            for right in rights:
                max_water = max(
                    max_water, (right - left) * min(height[left], height[right])
                )
                print(left, right, height[left], height[right], max_water)
        return max_water


# @lc code=end
