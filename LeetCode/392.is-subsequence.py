#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_t = 0
        for char_s in s:
            while index_t < len(t) and char_s != t[index_t]:
                index_t += 1
            if index_t >= len(t):
                return False
            index_t += 1

        return True


# @lc code=end
