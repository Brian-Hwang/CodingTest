#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        for word in reversed(s.split(" ")):
            if word == " " or word == "":
                continue
            ans.append(word)

        return " ".join(ans)


# @lc code=end
