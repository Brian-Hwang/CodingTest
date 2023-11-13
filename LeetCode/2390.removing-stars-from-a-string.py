#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#


# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        while "*" in s:
            star_index = s.find("*")
            s = s[: star_index - 1] + s[star_index + 1 :]
            # print(s)

        return s


# @lc code=end
