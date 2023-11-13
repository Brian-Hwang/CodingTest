#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack2 = []
        final_string = ""
        sub_string = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                count = s[i]
                while s[i + 1].isdigit():
                    i += 1
                    count += s[i]
                stack.append(int(count))

            elif s[i] == "[":
                stack2.append(sub_string)
                sub_string = ""

            elif s[i] == "]":
                sub_string = sub_string * int(stack[-1])
                sub_string = stack2[-1] + sub_string
                stack.pop()
                stack2.pop()

                # empty
                if not stack:
                    final_string += sub_string
                    sub_string = ""

            else:
                sub_string += s[i]

            i += 1

        return final_string + sub_string


# @lc code=end
