#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output_word = ""
        longer = word1 if len(word1) >= len(word2) else word2
        shorter_len = len(word1) if len(word1) <= len(word2) else len(word2)
        for i in range(shorter_len):
            output_word += word1[i] + word2[i]
        output_word += longer[shorter_len:]
        return output_word


# AI Solution
# class Solution:
# def mergeAlternately(self, word1: str, word2: str) -> str:
# output = "".join(a + b for a, b in zip(word1, word2))
# return output + word1[len(output) // 2 :] + word2[len(output) // 2 :]


# @lc code=end
