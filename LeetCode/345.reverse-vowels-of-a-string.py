#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        string_list = list(s)
        i = 0
        j = len(string_list) - 1
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        while True:
            while i <= j and string_list[i] not in vowel:
                i += 1
            while i <= j and string_list[j] not in vowel:
                j -= 1

            if i >= j:
                break

            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1
        return "".join(string_list)


# @lc code=end
