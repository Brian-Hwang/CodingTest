#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#


# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        return Counter(Counter(word1).values()) == Counter(Counter(word2).values())


# @lc code=end
