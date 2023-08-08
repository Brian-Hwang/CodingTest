#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#


# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Find short /long
        shorter, longer = (str1, str2) if len(str1) <= len(str2) else (str2, str1)

        # Find Pattern
        pattern = ""
        for i in range(1, len(shorter)):
            if shorter[i] == shorter[0]:
                semi_pattern = shorter[0 : i * 2]
                if pattern != "" and not any(
                    dup_pattern != "" for dup_pattern in semi_pattern.split(pattern)
                ):
                    continue
                if shorter[0:i] == shorter[i : i + i]:
                    pattern = shorter[0:i]
        if pattern == "":
            pattern = shorter

        # Find pattern occurance
        shorter_divide = shorter.split(pattern)
        longer_divide = longer.split(pattern)

        # If longer with something else than pattern return ""
        if any(pattern for pattern in longer_divide if pattern != "") or any(
            pattern for pattern in shorter_divide if pattern != ""
        ):
            return ""

        # Find gcd
        gcd = 0
        shorter_divide_len = len(shorter_divide) - 1
        longer_divide_len = len(longer_divide) - 1
        for i in range(1, shorter_divide_len + 1):
            if shorter_divide_len % i == 0 and longer_divide_len % i == 0:
                gcd = i

        # Result = pattern * gcd
        return pattern * gcd


# @lc code=end
