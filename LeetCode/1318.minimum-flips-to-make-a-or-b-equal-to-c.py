#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#


# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        bin_a, bin_b, bin_c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        length = max(len(bin_a), len(bin_b), len(bin_c))

        for i in range(1, length + 1):
            temp_a = bin_a[-i] if len(bin_a) >= i else "0"
            temp_b = bin_b[-i] if len(bin_b) >= i else "0"
            temp_c = bin_c[-i] if len(bin_c) >= i else "0"

            if temp_c == "1":
                if temp_a == "0" and temp_b == "0":
                    flips += 1
            else:
                if temp_a == "1":
                    flips += 1
                if temp_b == "1":
                    flips += 1

        return flips


# @lc code=end
