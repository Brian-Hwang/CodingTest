#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#


# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        before = 0
        max_alt = 0
        for i in gain:
            before = i + before
            max_alt = max(max_alt, before)

        return max_alt


# @lc code=end
