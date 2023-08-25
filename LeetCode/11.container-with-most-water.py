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
        max_water = 0
        while left < right:
            max_water = max(
                max_water, (right - left) * min(height[left], height[right])
            )
            if height[left] < height[right]:
                for i in range(right - left):
                    if height[left] < height[left + 1]:
                        left += 1
                        break
                    left += 1
            else:
                for i in range(right - left):
                    if height[right] < height[right - 1]:
                        right -= 1
                        break
                    right -= 1
        return max_water


# @lc code=end
