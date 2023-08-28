#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#


# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = maxs = 0
        vowel = set("aeiou")
        isFirstVowel = s[0] in vowel
        for i in range(k):
            if s[i] in vowel:
                maxs += 1
        count = maxs

        for i in range(1, len(s) - k + 1):
            if isFirstVowel:
                count -= 1
            isFirstVowel = s[i] in vowel
            if s[i + k - 1] in vowel:
                count += 1
                maxs = max(maxs, count)

        return maxs


# @lc code=end
