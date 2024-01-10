#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        zigzag = ["" for i in range(numRows)]

        zig = numRows
        zag = numRows - 2
        for i in range(len(s) // (zig + zag) + 1):
            for j in range(zig):
                if i * (zig + zag) + j >= len(s):
                    break
                zigzag[j] += s[i * (zig + zag) + j]
            for j in range(zag):
                if i * (zig + zag) + zig + j >= len(s):
                    break
                zigzag[zag - j] += s[i * (zig + zag) + zig + j]

        result = ""

        for i in range(numRows):
            result += zigzag[i]

        return result


# @lc code=end
