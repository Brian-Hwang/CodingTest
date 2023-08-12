#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#


# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_char = chars[0]

        # cur_index = index in chars, cur_count_index = how many times cur_char is counted
        cur_index, cur_count_index = 0, 1
        index = 1
        while index < len(chars):
            # New char
            if chars[index] != cur_char:
                chars[cur_index] = cur_char
                cur_index += 1

                if cur_count_index != 1:
                    for count_index in range(len(str(cur_count_index))):
                        chars[cur_index] = str(cur_count_index)[count_index]
                        cur_index += 1

                cur_char = chars[index]
                cur_count_index = 1
            # Same char
            else:
                cur_count_index += 1

            index += 1

        chars[cur_index] = cur_char
        cur_index += 1

        if cur_count_index != 1:
            for count_index in range(len(str(cur_count_index))):
                chars[cur_index] = str(cur_count_index)[count_index]
                cur_index += 1

        return cur_index


# @lc code=end
