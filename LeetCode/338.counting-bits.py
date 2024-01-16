#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i)[2:].count("1") for i in range(n + 1)]


# @lc code=end
